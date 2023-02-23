import pygame
import sys

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
