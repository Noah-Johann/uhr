import pygame, time
from pygame.locals import *
from math import sin, cos, radians

pygame.init()
clock = pygame.time.Clock()

Rot = (255,0,0); Background = (255, 255, 255); UI = (0, 0, 0)

MX = 200; MY = 200; MP = ((MX, MY))

def punkt(A, W):
    w1 = radians(W * 6 - 90); x1 = int(MX + A * cos(w1))
    y1 = int(MY + A * sin(w1))
    return ((x1, y1))

def UI_Draw():
    for i in range(60):
        pygame.draw.circle(Feld, UI, punkt(190, i), 2) 

    for i in range(12):
        pygame.draw.circle(Feld, UI, punkt(190, i*5), 4)

Feld = pygame.display.set_mode((400, 400))
Feld.fill(Background)
UI_Draw()

clock.tick(60) 

mainloop = True
s1 = 0

while mainloop:
    zeit=time.localtime()
    s = zeit.tm_sec; m = zeit.tm_min; h = zeit.tm_hour

    if h > 12:
        h = h - 12

    hm=(h + m / 60.0) * 5
    pygame.draw.circle(Feld, Background, MP, 182)
    pygame.draw.line(Feld, UI, MP, punkt(120, hm), 6)
    pygame.draw.line(Feld, UI, MP, punkt(170, m), 4)

    current_time = time.time()
    seconds = current_time % 60  # Dies gibt auch Dezimalstellen zurück
    seconds_angle = 270 + (seconds * 6)  # 6 Grad pro Sekunde

    seconds_x = MX + 180 * cos(radians(seconds_angle))
    seconds_y = MY + 180 * sin(radians(seconds_angle))

    pygame.draw.line(Feld, Rot, MP, (seconds_x, seconds_y), 2)

    
        
    s1 = pygame.display.update()

    for event in pygame.event.get():

        #Dark Mode
        if event.type == KEYUP and event.key == K_d:
            if Background == (255, 255, 255):
                Background = (0, 0, 0)
                UI = (255, 255, 255)
            else:
                Background = (255, 255, 255) 
                UI = (0, 0, 0)

            Feld.fill(Background)
            UI_Draw()

        #Quit
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            mainloop = False


pygame.quit()
