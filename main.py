import sampleSpace, sensors
import pygame
import sys
from ast import literal_eval
from os import path

def usage():
    print('Correct usage for the program is python [program_name] [image_location] [sensor_range] [sigma_nose_values] [lane_Prescision')
    exit(-1)
def listedFileNotFoundError():
    print('Listed file not found...')
    exit(-1)

def unknownError():
    print('Unknown error detected')
    exit(-1)
try:
    userInput = sys.argv
    if len(userInput)!=4:
        raise IndexError
    if type(userInput[1])!=str:
        raise ValueError
    if type(literal_eval(userInput[2]))!=int or type(literal_eval(userInput[3]))!=tuple:
        raise ValueError
    if not path.isfile(userInput[1]):
        raise FileNotFoundError
except (IndexError,SyntaxError,ValueError):
    usage()
except FileNotFoundError:
    listedFileNotFoundError()
except:
    unknownError()

enviroment = sampleSpace.startSampleSpaceEnv((1200, 600))
enviroment.originalMap = enviroment.map.copy()
laser = sensors.lidarSensor(int(sys.argv[2]), enviroment.originalMap,tuple(literal_eval(sys.argv[3])))
enviroment.map.fill((0, 0, 0))
enviroment.infomap = enviroment.map.copy()
yLanePrecisor = 0
xLanePrecisor = 4
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if yLanePrecisor <= enviroment.imageDimensions[1]:
            for x in range(enviroment.imageDimensions[0]):
                print("Scanning at", x, yLanePrecisor)
                position = (x, yLanePrecisor)
                laser.position = position
                sensors_data = laser.has_sensed()
                enviroment.dataStorage(sensors_data)
                enviroment.show_sensorData()
            yLanePrecisor += enviroment.imageDimensions[1] / xLanePrecisor
        enviroment.map.blit(enviroment.infomap, (0, 0))
        pygame.display.update()
