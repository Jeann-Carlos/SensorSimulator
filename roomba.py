import sys
from ast import literal_eval

from gym_game.envs.sampleSpace import enviroment
import pygame
from enum import Enum
import sensors



class roombaSimulator:
    def __init__(self, xlanePrecisor=4, ylanePrecisor=0, startingPosition=(220,170)):
        self.startingPosition = startingPosition
        self.prescisor = (xlanePrecisor,ylanePrecisor)
        self.roombaImage = pygame.image.load('images/ball.png')
        self.roombaObject = pygame.transform.scale(self.roombaImage, (50, 50))
        self.roomba = pygame.Rect(0,0,50,50)
        self.roomba.x, self.roomba.y = startingPosition
        self.laser= sensors.lidarSensor(int(sys.argv[2]), enviroment.originalMap,literal_eval(sys.argv[3]))
        self.direction = Direction.EAST

    def algorithm(self):
          cur_pos = self.getposition()
          if self.roomba.y <= enviroment.imageDimensions[1]:
                if self.roomba.x<enviroment.imageDimensions[0]:
                    self.roombaDetectColision()
                    print("Scanning at",  cur_pos[0],  cur_pos[1])
                    position = ( cur_pos[0],  cur_pos[1])
                    self.laser.position = position
                    sensors_data = self.laser.has_sensed()
                    enviroment.dataStorage(sensors_data)
                    enviroment.show_sensorData()
                if self.direction == Direction.NORTH:
                    self.roomba.y -= 1
                if self.direction == Direction.SOUTH:
                    self.roomba.y += 1
                if self.direction == Direction.EAST:
                    self.roomba.x += 1
                if self.direction == Direction.WEST:
                    self.roomba.x -= 1
          self.roombaUpdate()


    def getposition(self):
        return (self.roomba.x, self.roomba.y)

    def roombaUpdate(self):
        enviroment.map.blit(self.roombaObject, (self.roomba.x, self.roomba.y))

    def roombaDetectColision(self):
        print(self.direction)
        if enviroment.infomap.get_at((self.roomba.x+60,self.roomba.y))!=(255,255,255,255):
            print('front')
            self.direction=Direction.NORTH
        if enviroment.infomap.get_at((self.roomba.x-60,self.roomba.y))!=(255,255,255,255):
            self.direction=Direction.NORTH
            print('back')
        if enviroment.infomap.get_at((self.roomba.x,self.roomba.y+60))!=(255,255,255,255):
            self.direction=Direction.EAST
            print('down')
        if enviroment.infomap.get_at((self.roomba.x,self.roomba.y-60))!=(255,255,255,255):
            self.direction=Direction.EAST
            print('up')

        if self.direction == Direction.NORTH:
            print(self.direction)
            print("en4")



class Direction(Enum):
        NORTH = 1
        SOUTH = 2
        EAST = 3
        WEST = 4