import math, pygame, sys

class startSampleSpaceEnv:
    def __init__(self, imageDimensions):
        pygame.init()
        self.imageDimensions = imageDimensions
        self.pointcloud = []
        self.originalMap = []
        self.externalMap = pygame.image.load(sys.argv[1])
        self.mapw, self.maph = self.imageDimensions
        self.gameWindowName = '2D lidar path sensor planning'
        pygame.display.set_caption(self.gameWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))

    def AD2pos(self, distance, angle, position):
        x = distance * math.cos(angle) + position[0]
        y = -distance * math.sin(angle) + position[1]
        return (int(x), int(y))

    def dataStorage(self, data):
        if type(data) != bool:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointcloud:
                    self.pointcloud.append(point)

    def show_sensorData(self):
        self.infomap = self.externalMap.copy()
        for point in self.pointcloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))


enviroment = startSampleSpaceEnv((1200, 600))
enviroment.originalMap = enviroment.map.copy()
enviroment.map.fill((0, 0, 0))
enviroment.infomap = enviroment.map.copy()