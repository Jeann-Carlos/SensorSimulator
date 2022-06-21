from gym_game.envs.sampleSpace import enviroment
from roomba import roombaSimulator
from ast import literal_eval
from os import path
import sys,pygame


def usage():
    print('Correct usage for the program is python [program_name] [image_location] [sensor_range] [sigma_nose_values] [lane_Prescision]')
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
    if type(literal_eval(userInput[2]))!=int or type(literal_eval(userInput[3]))!=int or type(userInput[1])!=str:
        raise ValueError
    if not path.isfile(userInput[1]):
        raise FileNotFoundError
except (IndexError,SyntaxError,ValueError):
    usage()
except FileNotFoundError:
    listedFileNotFoundError()
except:
    unknownError()

roomba = roombaSimulator()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        enviroment.map.blit(enviroment.infomap, (0, 0))
        roomba.algorithm()
        pygame.display.update()

