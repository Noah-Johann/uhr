import pygame, time
from pygame.locals import *
from math import sin, cos, radians

pygame.init()

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
    pygame.draw.line(Feld, Rot, MP, punkt(180, s), 2)

    
        
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
