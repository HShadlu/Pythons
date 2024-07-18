import pygame,sys
from pygame.locals import *
import time
import math
from math import *
import tkinter
from tkinter import *
Screen = pygame.display.set_mode((824,824))
pygame.init()
Screen.fill((255,255,255))
pygame.display.set_caption(" my clock")
mypic = pygame.image.load('d:\\clock.png')
Screen.blit(mypic, (0, 0))



#######################3
x0=412
y0=412
xm=412
ym=190
xh=200
yh=412
x=0
y=0
r=200
minute=0
second=0
deg=360
degm=85
degh=180
###########################
pygame.draw.line(Screen,(0,0,0), (x0,y0), (xm,ym),4)
pygame.draw.line(Screen,(0,0,0), (x0,y0), (xh,yh),8)
##########################

while True:
       for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #pygame.display.update()






       if deg!=360:
            pygame.draw.line(Screen,(255, 255, 255), (x0, y0), (x, y),1)


       z=radians(deg)

       x=r*cos(z)+x0
       y=r*sin(z)-y0
       y=abs(y)

       pygame.draw.line(Screen, (255, 0, 0), (x0,y0), (x,y), 1)

       deg=deg-6
       pygame.display.update()
       time.sleep(1)
       second = second + 1

       if second % 60 == 0:

           pygame.draw.line(Screen, (255, 255, 255), (x0, y0), (xm, ym), 4)
           zm = radians(degm)

           xm = r * cos(zm) + x0
           ym = r * sin(zm) - y0
           ym = abs(ym)

           pygame.draw.line(Screen, (0, 0, 0), (x0, y0), (xm, ym), 4)
           degm = degm - 6
           pygame.display.update()
           minute=minute+1
           if minute%60==0:
               pygame.draw.line(Screen, (255, 255, 255), (x0, y0), (xh, yh), 8)
               degh = degh - 30
               zh = radians(degh)

               xh = r * cos(zh) + x0
               yh = r * sin(zh) - y0
               yh = abs(yh)

               pygame.draw.line(Screen, (0, 0, 0), (x0, y0), (xh, yh), 8)

               pygame.display.update()







#while True: # main game loop

