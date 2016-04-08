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

DISPLAYSURF.fill(BLACK)
pygame.draw.rect(DISPLAYSURF, PURPLE, (100, 150, 200 , 300))
pygame.draw.rect(DISPLAYSURF, BLUE, (150, 200, 50, 100))
pygame.draw.polygon(DISPLAYSURF, GREEN, ((200, 400), (200, 300), (200, 400))
pygame.draw.rect(DISPLAYSURF, WHITE, (200, 50, 100, 150))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()