import pygame
import sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Drawing stuff")

#Palette of colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
PURPLE= (160,  32, 240)
RANDOM= (210, 254,  17)

DISPLAYSURF.fill(RANDOM)
pygame.draw.line(DISPLAYSURF, WHITE, (100, 28), (300, 200), 4)
pygame.draw.line(DISPLAYSURF, BLACK, (0,0), (400, 300), 4)
pygame.draw.line(DISPLAYSURF, BLACK, (0,300), (400,0), 4)
pygame.draw.polygon(DISPLAYSURF, RED, ((200,0),(250, 50),(225,100),(175,100),(150,50)))
pygame.draw.circle(DISPLAYSURF, BLUE, (275, 140), 48, 0)
pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, 200, 100), 0)
pygame.draw.ellipse(DISPLAYSURF, GREEN, (0, 0, 200, 100), 0)

#draw a blue 120x100 rectangle in the bottom right corner 

#draw a black hexagon each side 25 anywhere

#OCTAGON
pygame.draw.polygon(DISPLAYSURF, BLACK, ((200,100),(225,100),(242.67,117.67),(242.67,142.67),(225,160.34),(200,160.34),(182.33,142.67),(182.33,117.67)),5)
pygame.draw.polygon(DISPLAYSURF, WHITE, ((200,100),(225,100),(242.67,117.67),(242.67,142.67),(225,160.34),(200,160.34),(182.33,142.67),(182.33,117.67)))


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()