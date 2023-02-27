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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                engine.dir("n")
            if event.key == pygame.K_s:
                engine.dir("s")
            if event.key == pygame.K_d:
                engine.dir("e")
            if event.key == pygame.K_a:
                engine.dir("w")

    engine.render(screen)
    pygame.display.flip()
    clock.tick(8) #! ФПС(скорость движения змейки)