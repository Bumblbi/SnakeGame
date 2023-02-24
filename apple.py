import random

class Apple():
    cells = [(x, y) for y in range(30) for x in range(30)] #! список клеток

    def __init__(self, pos):
        self.pos = pos

    def spawn(self, Snake):
        allowed = [cell for cell in self.cells if cell not on snake.pos] #! проверка на нахождения змеи в клетке, что бы яблоко не появилось в змее
        self.pos = random.choice(allowed) #! выбор одной случайной клетки на которой появится яблоко