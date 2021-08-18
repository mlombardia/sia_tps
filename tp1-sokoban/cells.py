from tokens import *

class Cell():
    token = None
    symbol= ""

    def __init__(self):
        self.symbol = " "

    def update(self, inserted):
        self.token = inserted
        self.symbol = inserted.symbol

class ObjectiveCell(Cell):
    def __init__(self, x, y):
        super().__init__()
        self.symbol = "."
        self.x=x
        self.y=y

    def isCompleted(self):
        return isinstance(self.token, Box)

class Wall(Cell):
    def __init__(self):
        super().__init__()
        self.symbol = "#"

    def update(self, inserted):
        return False

