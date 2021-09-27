import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((556, 787))

rect(screen, (255, 255, 255), (0, 0, 556, 787))
rect(screen, (225, 225, 225), (0, 0, 556, 352))
circle(screen, (225, 225, 225), (174, 454), 132)
circle(screen, (0, 0, 0), (174, 454), 132, 2)
rect(screen, (255, 255, 255), (42, 454, 264, 132))
line(screen, (0, 0, 0), (42, 454), (306, 454))
line(screen, (0, 0, 0), (54, 398), (292, 398))
line(screen, (0, 0, 0), (79, 362), (267, 362))
line(screen, (0, 0, 0), (118, 335), (230, 335))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
