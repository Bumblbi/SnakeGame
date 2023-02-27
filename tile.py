import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, id): #! id - tile id, идентификатор каждой плитки
        super().__init__()
        self.id = id
        self.color = (0, 0, 0)

        self.surf = pygame.Surface((20, 20)) #! создание поверхности
        self.surf.fill(self.color) #! заливка поверхности
        self.rect = self.surf.get_rect(topleft = (self.id[0] * 20 - 3, self.id[1] * 20 - 3))
    
    def set_color(self, color): #! метод color для перекраски плиток
        self.color = color
        self.surf.fill(color)
