from Map import Map
from cells import Cell

class AI:
    stateList = []
    mentalMap = None
    moves = ["up", "down", "left", "right"]

    def __init__(self, mapa):
        self.mentalMap = mapa
        self.stateList = self.stateList.append(State(self.mentalMap))

    def moveUp(self):
        if self.mentalMap.movePlayer("up"):
            self.stateList.append(State(self.mentalMap))

    def moveDown(self):
        if self.mentalMap.movePlayer("down"):
            self.stateList.append(State(self.mentalMap))

    def moveLeft(self):
        if self.mentalMap.movePlayer("left"):
            self.stateList.append(State(self.mentalMap))

    def moveRight(self):
        if self.mentalMap.movePlayer("right"):
            self.stateList.append(State(self.mentalMap))

    def DFS(self):
        for move in self.moves:




class State:
    playerRow = 0
    playerCol = 0
    boxRow = 0
    boxCol = 0

    def __init__(self, map):
        x = 0
        for row in map.cellMap:
            y = 0
            for col in row:
                if col == "$":
                    self.boxCol = y
                    self.boxRow = x
                elif col == "@":
                    self.playerRow = x
                    self.playerCol = y
                y += 1
            x += 1
