import sampleSpace,sensors
import pygame

enviroment = sampleSpace.startSampleSpaceEnv((600,1200))
enviroment.originalMap = enviroment.map.copy()
laser = sensors.lidarSensor(200,enviroment.originalMap,(0.5,0.01))
enviroment.map.fill((0,0,0))
enviroment.infomap = enviroment.map.copy()
yDimPrecisor=0
lanePrescision = 4

running = True

while running:
    sensorsON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorsON= True
        elif not pygame.mouse.get_focused():
            sensorsON = False
    if sensorsON:

        while yDimPrecisor< enviroment.imageDimensions[0]:

            for x in range(enviroment.imageDimensions[1]):
                print("Scanning at",x,yDimPrecisor)
                position = (x,yDimPrecisor)
                laser.position = position
                sensors_data = laser.has_sensed()
                enviroment.dataStorage(sensors_data)
                enviroment.show_sensorData()
            yDimPrecisor += enviroment.imageDimensions[0] / lanePrescision
    enviroment.map.blit(enviroment.infomap,(0,0))
    pygame.display.update()