import sys
import pygame

class Snake():
    movement = {"n": (0, -1), "s": (0, 1), "e": (1, 0), "w": (-1, 0)} #! север, юг, запад, восток

    def __init__(self, dir, pos):
        self.dir = dir #! текущее направление движения змеи
        self.pos = pos #! клетки являющиеся частью змеи
    
    def move(self, apple): #! метод для движения змеии
        head = (self.pos[0][0] + self.movement[self.dir][0], self.pos[0][1] + self.movement[self.dir][1]) #! добавление или вычитание пиксель головы в соответствии с направлением движения

        if head == apple.pos:
            self.pos = [head] + self.pos
            return True
        
        else:
            self.pos.remove(self.pos[::-1][0]) #! добавление новой позиции головы змеи к остельной части и отрезание последней клетки хвоста
            self.pos = [head] + self.pos
            return False
