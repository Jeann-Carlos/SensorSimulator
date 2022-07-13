import math
import sys
import time
from ast import literal_eval

import numpy as np
import pygame


class SampleSpaceEnv:
    def __init__(self, image_dimensions):
        pygame.init()
        self.known_pos = []
        self.running = True
        self.imageDimensions = image_dimensions
        self.originalMap = []
        self.externalMap = pygame.image.load(sys.argv[1])
        self.mapw, self.maph = self.imageDimensions
        self.gameWindowName = '2D lidar path sensor planning'
        pygame.display.set_caption(self.gameWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))
        self.originalMap = self.map.copy()
        self.roomba = RoombaSimulator(original_map=self.originalMap)
        self.map.fill((255, 255, 255))
        self.infomap = self.map.copy()
        self.reward = 0
        self.time = time.time()
        self.objective = False


    def show_sensor_data(self):
        self.infomap = self.externalMap.copy()
        for point in self.roomba.get_roomba_point_cloud():
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))

    def action(self, action):
        self.roomba.roomba_update(action)

    def get_roomba_pos(self):
        return self.roomba.roomba_pos()

    def draw_radar(self):
        roombaposx, roombaposy = self.get_roomba_pos()
        for pos, dist, cos, sin in self.roomba.get_roomba_radars():
            if dist < 40:
                pygame.draw.line(self.map, (255, 0, 0), (roombaposx + (cos * 20), roombaposy + (sin * 20)), pos, 2)
                pygame.draw.circle(self.map, (255, 0, 0), pos, 5)
            else:
                pygame.draw.line(self.map, (0, 0, 0), (roombaposx + (cos * 20), roombaposy + (sin * 20)), pos, 2)
                pygame.draw.circle(self.map, (0, 0, 0), pos, 5)

    def observe(self):
        # return state
        ret = self.get_roomba_pos()
        return tuple(ret)

    def view(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        roombaposx, roombaposy = self.get_roomba_pos()
        self.map.blit(self.roomba.roombaObject, (roombaposx, roombaposy))
        self.show_sensor_data()
        self.map.blit(self.infomap, (0, 0))
        self.set_objective()
        self.map.blit(self.roomba.roombaObject, (roombaposx - 25, roombaposy - 25))
        self.draw_radar()

        pygame.display.update()
        return self.running

    def objective(self):
        start_time = self.time
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.objective = True

        return elapsed_time


    def evaluate(self):
        roomba_pos = self.get_roomba_pos()
        if roomba_pos not in self.known_pos:
            self.known_pos.append(roomba_pos)
            return 1
        else:
            return 0
    def prev_evaluate(self):
        reward = 0
        if self.previous_radar is None:
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

    def set_objective(self):
        pygame.draw.circle(self.map, (0,0,128), (860, 500), 5)


class RoombaSimulator:
    class Spot:
        def __init__(self, i, j):
            self.x, self.y = i, j
            self.neighbors = []
            self.prev = None
            self.wall = False
            self.visited = False



    def __init__(self, starting_pos=(400, 230), original_map=None):
        self.pointcloud = []
        self.originalMap = original_map
        self.startingPosition = starting_pos
        self.roombaImage = pygame.image.load('images/ball.png')
        self.roombaObject = pygame.transform.scale(self.roombaImage, (50, 50))
        self.roomba = pygame.Rect(0, 0, 50, 50)
        self.roomba.x, self.roomba.y = starting_pos
        self.laser = LidarSensor(int(sys.argv[2]), original_map, literal_eval(sys.argv[3]))
        self.radars = []
        self.npGrid = None


    def check_radar(self, degree):
        length = 15
        cos = math.cos(math.radians(360 - degree))
        sin = math.sin(math.radians(360 - degree))
        x = int(self.roomba.x + cos * length)
        y = int(self.roomba.y + sin * length)

        while (self.originalMap.get_at((x, y)) == (255, 255, 255, 255) or self.originalMap.get_at((x, y)) == (0, 0, 0, 0)) and length < 80:
            length = length + 1
            x = int(self.roomba.x + cos * length)
            y = int(self.roomba.y + sin * length)

        dist = int(math.sqrt(math.pow(x - self.roomba.x, 2) + math.pow(y - self.roomba.y, 2)))
        self.radars.append([(x, y), dist, cos, sin])



    def roomba_update(self, action):
        self.move_roomba(action)
        self.laser.laser_update(self.roomba_pos())
        sensors_data = self.laser.has_sensed()
        self.data_storage(sensors_data)
        self.radars.clear()
        for degree in (90, 270, 180, 0):
            self.check_radar(degree)

    def data_storage(self, data):
        if type(data) != bool:
            for element in data:
                point = self.ad2_pos(element[0], element[1], element[2])
                if point not in self.pointcloud:
                    self.pointcloud.append(point)

    def roomba_pos(self):
        return self.roomba.x, self.roomba.y

    @staticmethod
    def ad2_pos(distance, angle, position):
        x = distance * math.cos(angle) + position[0]
        y = -distance * math.sin(angle) + position[1]
        return int(x), int(y)

    def get_roomba_point_cloud(self):
        return self.pointcloud

    def move_roomba(self, action):
        if len(self.radars)!=0:
            if action == 0 and self.radars[0][1]>20:
                self.roomba.y -= 1
            elif action == 1 and self.radars[1][1]>20:
                self.roomba.y += 1
            elif action == 2 and self.radars[3][1]>20:
                self.roomba.x += 1
            elif action == 3 and self.radars[2][1]>20:
                self.roomba.x -= 1
            else:
                pass
    def get_roomba_radars(self):
        return self.radars


class LidarSensor:

    def __init__(self, sensor_range, sensor_map, distortion):
        self.position = (0, 0)
        self._range = sensor_range
        self._speed = 4
        self._sigma = np.array([distortion, 0])
        self._map = sensor_map
        self._w, self.h = pygame.display.get_surface().get_size()
        self._beingSensed = []
        self._distance = None

    def laser_distance(self, obstacle_pos):
        px = (obstacle_pos[0] - self.position[0]) ** 2
        py = (obstacle_pos[1] - self.position[1]) ** 2
        return math.sqrt(px + py)

    def laser_update(self, position):
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
                        self._distance = self.laser_distance((x, y))
                        output = self.sensor_noise(angle)
                        output.append(self.position)
                        data.append(output)
                        break
        if len(data) > 0:
            return data
        else:
            return False

    def sensor_noise(self, angle):
        mean = np.array([self._distance, angle])
        covariance = np.diag(self._sigma ** 2)
        distance, angle = np.random.multivariate_normal(mean, covariance)
        distance = max(distance, 0)
        angle = max(angle, 0)
        return [distance, angle]

