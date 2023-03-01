import pygame
from snake import Snake
from tile import Tile
from apple import Apple

class Engine():
    def __init__(self):
        self.snake = Snake("n", [(15, 15), (16, 15), (17, 15)]) #! инициализация змейки с начальными точками и направлением
        self.apple = Apple((5, 5)) #! создание яблока с нач. координатами

        self.tiles = [Tile((x, y)) for y in range(30) for x in range(30)] #! генерация списка с плитками

    def dir(self, direction): #! метод для смены направления движения змейки
        if self.snake.alternate != []: #! очередь смены направления
            new_dir = self.snake.alternate[::-1][0]
        else:
            new_dir = self.snake.dir
        
        if (new_dir == "n" or new_dir == "s") and (direction == "n" or direction == "s"): #! змея не сможет развернуться в себя же
            return False
        if (new_dir == "e" or new_dir == "w") and (direction == "e" or direction == "w"):
            return False

        if len(self.snake.alternate) < 2: #! запись кнопок в очередь
            self.snake.alternate.append(direction)
        
    def update(self):
        if self.snake.move(self.apple):
            self.apple.spawn(self.apple)

        for tile in self.tiles: #! проверка для наличия плитки в списки змеи(строка 5)
            if tile.id in self.snake.pos:
                if tile.id == self.snake.pos[0]:
                    tile.set_color((51, 204, 0))
                else:
                    tile.set_color((0, 153, 0))

            elif tile.id == self.apple.pos:
                tile.set_color((255, 0, 0))
            else:
                if tile.color != (0, 0, 0):
                    tile.set_color((0, 0, 0))
        
    def render(self, screen): #! метод для отрисовки всего на экран
        self.update()

        for tile in self.tiles:
            screen.blit(tile.surf, tile.rect)