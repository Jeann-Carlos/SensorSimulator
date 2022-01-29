import sampleSpace,sensors
import pygame

enviroment = sampleSpace.startSampleSpaceEnv((600,1200))
enviroment.originalMap = enviroment.map.copy()
laser = sensors.lidarSensor(200,enviroment.originalMap,(0.5,0.01))
enviroment.map.fill((0,0,0))
enviroment.infomap = enviroment.map.copy()

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
        for x,y in enviroment.
        position =
        laser.position = position
        sensors_data = laser.has_sensed()
        enviroment.dataStorage(sensors_data)
        enviroment.show_sensorData()
    enviroment.map.blit(enviroment.infomap,(0,0))
    pygame.display.update()