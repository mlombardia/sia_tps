from cells import Wall, ObjectiveCell, Cell
from tokens import Box, Player, Token


class Map():
    cellMap = []
    playerFila = 0
    playerColumna = 0
    cantFilas = 0
    cantColumnas = 0
    objectiveList = []
    caja = Box()
    pared = Wall()


    def __init__(self, asciiMap, cantFilas, cantColumnas):
        self.cantColumnas = cantColumnas
        self.cantFilas = cantFilas
        # for x in range(cantFilas):
        x = 0
        for j in asciiMap:
            y = 0
            aux = []
            for k in j:
                auxCell = Cell()
                if (k == "#"):
                    aux.append(Wall())
                elif (k == " "):
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
                    auxObj = ObjectiveCell()
                    aux.append(auxObj)
                    self.objectiveList.append(auxObj)
                y += 1
            x += 1
            self.cellMap.append(aux)

    '''
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
    '''

    '''
    def isThing(self, row, col, element):
        if isinstance(element, Cell):
            print("cosa 1")
            return isinstance(self.cellMap[row][col], element)
        elif isinstance(element, Token):
            print("cosa 2")
            return isinstance(self.cellMap[row][col].token, element)

        if isinstance(self.caja, Token):
            print("box es token")
        
        #print("error in isThing")
    '''

    def checkIfWin(self):
        for cell in self.objectiveList:
            if not cell.isCompleted():
                return False
        print("\nsos un capo de la vida")
        exit()
        return True

    def checkIfLoose(self):
        row = 0
        for x in self.cellMap:
            col = 0
            for y in x:
                # if isinstance(x[y], Box)
                if isinstance((self.cellMap[row])[col].token, Box):  # si la caja está en una esquina
                    if ((isinstance((self.cellMap[row + 1])[col], Wall) and isinstance((self.cellMap[row])[col + 1],
                                                                                       Wall)) or
                            (isinstance((self.cellMap[row + 1])[col], Wall) and isinstance((self.cellMap[row])[col + 1],
                                                                                           Wall)) or
                            (isinstance((self.cellMap[row + 1])[col], Wall) and isinstance((self.cellMap[row])[col + 1],
                                                                                           Wall)) or
                            (isinstance((self.cellMap[row + 1])[col], Wall) and isinstance((self.cellMap[row])[col + 1],
                                                                                           Wall))):
                        print("perdiste")
                        return True
                col += 1
            row += 1
        return False

    def movePlayer(self, direction):
        if direction == 'up':
            if isinstance((self.cellMap[self.playerFila - 1])[self.playerColumna], Wall):
                return False
            elif isinstance((self.cellMap[self.playerFila - 1])[self.playerColumna].token, Box):
                if isinstance((self.cellMap[self.playerFila - 2])[self.playerColumna].token, Box) or isinstance(
                        (self.cellMap[self.playerFila - 2])[self.playerColumna], Wall):
                    return False
                else:
                    (self.cellMap[self.playerFila - 2])[self.playerColumna].update(Box())

            (self.cellMap[self.playerFila - 1])[self.playerColumna].update(Player())
            (self.cellMap[self.playerFila])[self.playerColumna].token = None
            (self.cellMap[self.playerFila])[self.playerColumna].symbol = " "
            self.playerFila = self.playerFila - 1

        elif direction == 'down':
            if isinstance((self.cellMap[self.playerFila + 1])[self.playerColumna], Wall):
                return False
            elif isinstance((self.cellMap[self.playerFila + 1])[self.playerColumna].token, Box):
                if isinstance((self.cellMap[self.playerFila + 2])[self.playerColumna].token, Box) or isinstance(
                        (self.cellMap[self.playerFila + 2])[self.playerColumna], Wall):
                    return False
                else:
                    (self.cellMap[self.playerFila + 2])[self.playerColumna].update(Box())

            (self.cellMap[self.playerFila + 1])[self.playerColumna].update(Player())
            (self.cellMap[self.playerFila])[self.playerColumna].token = None
            (self.cellMap[self.playerFila])[self.playerColumna].symbol = " "
            self.playerFila = self.playerFila + 1

        elif direction == 'left':
            if isinstance((self.cellMap[self.playerFila])[self.playerColumna - 1], Wall):
                return False
            elif isinstance((self.cellMap[self.playerFila])[self.playerColumna - 1].token, Box):
                if isinstance((self.cellMap[self.playerFila])[self.playerColumna - 2].token, Box) or isinstance(
                        (self.cellMap[self.playerFila])[self.playerColumna - 2], Wall):
                    return False
                else:
                    (self.cellMap[self.playerFila])[self.playerColumna - 2].update(Box())

            (self.cellMap[self.playerFila])[self.playerColumna - 1].update(Player())
            (self.cellMap[self.playerFila])[self.playerColumna].token = None
            (self.cellMap[self.playerFila])[self.playerColumna].symbol = " "
            self.playerColumna = self.playerColumna - 1

        elif direction == 'right':
            if isinstance((self.cellMap[self.playerFila])[self.playerColumna + 1], Wall):
                return False
            elif isinstance((self.cellMap[self.playerFila])[self.playerColumna + 1].token, Box):
                if isinstance((self.cellMap[self.playerFila])[self.playerColumna + 2].token, Box) or isinstance(
                        (self.cellMap[self.playerFila])[self.playerColumna + 2], Wall):
                    return False
                else:
                    (self.cellMap[self.playerFila])[self.playerColumna + 2].update(Box())

            (self.cellMap[self.playerFila])[self.playerColumna + 1].update(Player())
            (self.cellMap[self.playerFila])[self.playerColumna].token = None
            (self.cellMap[self.playerFila])[self.playerColumna].symbol = " "
            self.playerColumna = self.playerColumna + 1

        return True  # move successfull

    def printBoard(self):
        for i in self.cellMap:
            print()
            for j in i:
                print(j.symbol, end="")

        self.checkIfWin()
        self.checkIfLoose()


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
