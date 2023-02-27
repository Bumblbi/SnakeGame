import pygame
import sys
from engine import Engine

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

engine = Engine()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.render(screen)
    pygame.display.flip()
    clock.tick(7) #! ФПС(скорость движения змейки)
