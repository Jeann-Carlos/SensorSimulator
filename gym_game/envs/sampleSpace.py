import sys
from ast import literal_eval
from enum import Enum
import pygame
import math
import numpy as np


class startSampleSpaceEnv:
    def __init__(self, imageDimensions):

        self.previous_radar = None
        pygame.init()
        self.running = True
        self.imageDimensions = imageDimensions
        self.pointcloud = []
        self.originalMap = []
        self.externalMap = pygame.image.load(sys.argv[1])
        self.mapw, self.maph = self.imageDimensions
        self.gameWindowName = '2D lidar path sensor planning'
        pygame.display.set_caption(self.gameWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))
        self.originalMap = self.map.copy()
        self.roomba = roombaSimulator(originalMap=self.originalMap)
        self.map.fill((255, 255, 255))
        self.infomap = self.map.copy()
        self.reward = 0
        self.radars = []

    def show_sensorData(self):
        self.infomap = self.externalMap.copy()
        for point in self.roomba.getRoombaPointCloud():
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))

    def action(self, action):
        if action == 0:
            self.roomba.roomba.y -= 2
        if action == 1:
            self.roomba.roomba.y += 1
        if action == 2:
            self.roomba.roomba.x += 1
        if action == 3:
            self.roomba.roomba.x -= 1
        self.roomba.roombaUpate()

    def getroombaposition(self):
        return self.roomba.roombaPosition()

    def draw_radar(self):
        roombaposx, roombaposy = self.getroombaposition()
        for pos, dist, cos, sin in self.roomba.radars:
            if dist < 40:
                pygame.draw.line(self.map, (255, 0, 0), (roombaposx + (cos * 20), roombaposy + (sin * 20)), pos, 2)
                pygame.draw.circle(self.map, (255, 0, 0), pos, 5)
            else:
                pygame.draw.line(self.map, (0, 0, 0), (roombaposx + (cos * 20), roombaposy + (sin * 20)), pos, 2)
                pygame.draw.circle(self.map, (0, 0, 0), pos, 5)

    def roombaViewUpdate(self):
        self.map.blit(self.roomba.roombaObject, (self.roomba.roomba.x, self.roomba.roomba.y))

    def observe(self):
        # return state
        ret = self.getroombaposition()
        return tuple(ret)

    def view(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.roombaViewUpdate()
        self.show_sensorData()
        self.map.blit(self.infomap, (0, 0))
        rombax, rombay = self.getroombaposition()
        self.map.blit(self.roomba.roombaObject, (rombax - 25, rombay - 25))
        self.draw_radar()
        pygame.display.update()
        return self.running

    def evaluate(self):
        reward = 0
        if self.previous_radar == None:
            self.previous_radar = self.roomba.radars.copy()
        for i, distance in enumerate(self.roomba.radars):
            if distance[1] > self.previous_radar[i][1]:
                reward += 1
            elif distance[1] == self.previous_radar[i][1]:
                reward += 0
            elif distance[1] >= 70:
                reward += 1
            else:
                reward -= 1
        self.previous_radar = self.roomba.radars.copy()
        return reward

    def is_done(self):
        done = False
        for xy, dist, cos, sin in self.roomba.radars:
            if dist < 10:
                done = True
        return done


class roombaSimulator:
    def __init__(self, xlanePrecisor=4, ylanePrecisor=0, startingPosition=(400, 230), originalMap=None):
        self.pointcloud = []
        self.angle = 0
        self.originalMap = originalMap
        self.startingPosition = startingPosition
        self.prescisor = (xlanePrecisor, ylanePrecisor)
        self.roombaImage = pygame.image.load('images/ball.png')
        self.roombaObject = pygame.transform.scale(self.roombaImage, (50, 50))
        self.roomba = pygame.Rect(0, 0, 50, 50)
        self.roomba.x, self.roomba.y = startingPosition
        self.laser = lidarSensor(int(sys.argv[2]), originalMap, literal_eval(sys.argv[3]))
        self.radars = []

    def check_radar(self, degree):
        len = 0
        cos = math.cos(math.radians(360 - (degree)))
        sin = math.sin(math.radians(360 - (degree)))
        x = int(self.roomba.x + cos * len)
        y = int(self.roomba.y + sin * len)

        while self.originalMap.get_at((x, y)) == (255, 255, 255, 255) and len < 80:
            len = len + 1
            x = int(self.roomba.x + cos * len)
            y = int(self.roomba.y + sin * len)

        dist = int(math.sqrt(math.pow(x - self.roomba.x, 2) + math.pow(y - self.roomba.y, 2)))
        self.radars.append([(x, y), dist, cos, sin])

    def roombaUpate(self):
        self.laser.laserUpdate(self.roombaPosition())
        sensors_data = self.laser.has_sensed()
        self.dataStorage(sensors_data)
        self.radars.clear()
        for degree in (90, 270, 180, 0):
            self.check_radar(degree)

    def dataStorage(self, data):
        if type(data) != bool:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointcloud:
                    self.pointcloud.append(point)

    def roombaPosition(self):
        return (self.roomba.x, self.roomba.y)

    def AD2pos(self, distance, angle, position):
        x = distance * math.cos(angle) + position[0]
        y = -distance * math.sin(angle) + position[1]
        return (int(x), int(y))

    def getRoombaPointCloud(self):
        return self.pointcloud


class lidarSensor():

    def __init__(self, range, map, distortion):
        self.position = (0, 0)
        self._range = range
        self._speed = 4
        self._sigma = np.array([distortion, 0])
        self._map = map
        self._w, self.h = pygame.display.get_surface().get_size()
        self._beingSensed = []
        self._distance = None

    def laser_distance(self, obstaclePosition):
        px = (obstaclePosition[0] - self.position[0]) ** 2
        py = (obstaclePosition[1] - self.position[1]) ** 2
        return math.sqrt(px + py)

    def laserUpdate(self, position):
        self.position = position

    def has_sensed(self):
        data = []
        x1, y1 = self.position[0], self.position[1]
        for angle in np.linspace(0, 2 * math.pi, 60, False):
            x2, y2 = (x1 + self._range * math.cos(angle), y1 - self._range * math.sin(angle))
            for i in range(100):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self._w and 0 < y < self.h:
                    color = self._map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (0, 0, 0):
                        self.distance = self.laser_distance((x, y))
                        output = self.sensorNoise(angle)
                        output.append(self.position)
                        data.append(output)
                        break
        if len(data) > 0:
            return data
        else:
            return False

    def sensorNoise(self, angle):
        mean = np.array([self.distance, angle])
        covariance = np.diag(self._sigma ** 2)
        distance, angle = np.random.multivariate_normal(mean, covariance)
        distance = max(distance, 0)
        angle = max(angle, 0)
        return [distance, angle]
