import pygame
import sys
from engine import Engine

pygame.init()

width, height = 600, 600

screen = pygame.display.set_mode((width, height))

ARIAL = pygame.font.SysFont("arial", 50)

fps = 8
clock = pygame.time.Clock()

engine = Engine()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                engine.dir("n")
            if event.key == pygame.K_s:
                engine.dir("s")
            if event.key == pygame.K_d:
                engine.dir("e")
            if event.key == pygame.K_a:
                engine.dir("w")
            if event.key == pygame.K_LSHIFT:
                fps = 18

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                fps = 8

    engine.render(screen)
    pygame.display.flip()
    clock.tick(fps) #! ФПС(скорость движения змейки)