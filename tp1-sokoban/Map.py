from cells import Wall, ObjectiveCell, Cell
from tokens import Box, Player

class Map():
    cellMap = []
    playerFila = 0
    playerColumna = 0
    cantFilas = 0
    cantColumnas = 0

    def __init__(self, asciiMap, cantFilas, cantColumnas):
        self.cantColumnas = cantColumnas
        self.cantFilas = cantFilas
        #for x in range(cantFilas):
        x = 0
        for j in asciiMap:
            y = 0
            aux = []
            auxCell = Cell()
            for k in j:
                if(k == "#"):
                    aux.append(Wall())
                elif(k == " "):
                    aux.append(auxCell)
                elif (k == "$"):
                    auxCell.update(Box())
                    aux.append(auxCell)
                elif (k == "@"):
                    auxCell.update(Player())
                    aux.append(auxCell)
                    self.playerFila = x
                    self.playerColumna = y
                elif (k == "."):
                    aux.append(ObjectiveCell())
                y += 1
            x += 1
            self.cellMap.append(aux)

    def update(self, coordinates, element, move):
            if(move == 'up'):
                if not isinstance(element, Box):
                    self.cellMap[coordinates[0]][coordinates[1]] = Cell()
                    self.cellMap[coordinates[0] - 1][coordinates[1]] = element
                else:
                    if isinstance(self.cellMap[coordinates[0] - 1][coordinates[1]], ObjectiveCell):
                        self.cellMap[coordinates[0] - 1][coordinates[1]].isCompleted = True
            if(move == 'down'):
                if not isinstance(element, Box):
                    self.cellMap[coordinates[0]][coordinates[1]] = Cell()
                self.cellMap[coordinates[0] + 1][coordinates[1]] = element
            if (move == 'left'):
                if not isinstance(element, Box):
                    self.cellMap[coordinates[0]][coordinates[1]] = Cell()
                    self.cellMap[coordinates[0]][coordinates[1] - 1] = element
            if(move == 'right'):
                if not isinstance(element, Box):
                    self.cellMap[coordinates[0]][coordinates[1]] = Cell()
                self.cellMap[coordinates[0]][coordinates[1] + 1] = element

    def movePlayer(self, direction):
            if direction == 'up':
                if isinstance((self.cellMap[self.playerFila-1])[self.playerColumna], Wall):
                    print("no1")
                    return False
                elif isinstance((self.cellMap[self.playerFila-1])[self.playerColumna].Token, Box):
                    if isinstance((self.cellMap[self.playerFila-2])[self.playerColumna].Token, Box) or isinstance((self.cellMap[self.playerFila-2])[self.playerColumna], Wall):
                        print("no2")
                        return False
                    else:
                        print("si")
                        (self.cellMap[self.playerFila - 2])[self.playerColumna].update(Box())
                else:
                    print("raios")

                print("si devuelta")
                (self.cellMap[self.playerFila - 1])[self.playerColumna].update(Player())
                (self.cellMap[self.playerFila])[self.playerColumna].Token = None
                (self.cellMap[self.playerFila])[self.playerColumna].symbol = " "
                self.playerFila = self.playerFila - 1


    def printBoard(self):
        for i in self.cellMap:
            print()
            for j in i:
                print(j.symbol, end="")
'''
            case 'down':
                self.playerFila = self.playerFila + 1
            case 'left':
                self.cellMap[x][y] = Cell()
                self.cellMap[x][y].update(Box(x, y))
            case 'right':
                self.cellMap[x][y] = Cell()
                self.cellMap[x][y].update(Player(x, y))
'''
