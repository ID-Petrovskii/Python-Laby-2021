import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

rect(screen, (200, 200, 200), (0, 0, 600, 600))
circle(screen, (255, 255, 0), (300, 300), 150)
circle(screen, (0, 0, 0), (300, 300), 150, 1)
rect(screen, (0, 0, 0), (225, 360, 150, 25))
circle(screen, (255, 0, 0), (225, 250), 30)
circle(screen, (0, 0, 0), (225, 250), 30, 1)
circle(screen, (0, 0, 0), (225, 250), 12)
circle(screen, (255, 0, 0), (375, 250), 25)
circle(screen, (0, 0, 0), (375, 250), 25, 1)
circle(screen, (0, 0, 0), (375, 250), 12)
line(screen, (0, 0, 0), (150, 171), (270, 231), 18)
line(screen, (0, 0, 0), (435, 190), (330, 235), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
