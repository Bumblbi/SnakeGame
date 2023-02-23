class Tile(pygame.sprite.Sprite):
    def __init__(self, id): #! id - tile id, идентификатор каждой плитки
        super().init()
        self.id = id
        self.color = color

        self.surf = pygame.Surface((20, 20)) #! создание поверхности
        self.surf.fill(color) #! заливка поверхности
        self.rect = self.surf.get_rect(topleft = (self.id[0] * 20, self.id[1] * 20))
    
    def set_color(self, color): #! метод color для перекраски плиток
        self.color = color
        self.surf.fill(color)
