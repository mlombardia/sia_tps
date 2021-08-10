from tokens import *

class Cell():
    Token = None
    symbol= ""

    def __init__(self):
        self.symbol = " "

    def update(self, inserted):
        self.token = inserted
        self.symbol = inserted.symbol

class ObjectiveCell(Cell):
    def __init__(self):
        super().__init__()
        self.symbol = "."

    def isCompleted(self):
        return isinstance(self.Token, Box)

class Wall(Cell):
    def __init__(self):
        super().__init__()
        self.symbol = "#"

    def update(self, inserted):
        return False

