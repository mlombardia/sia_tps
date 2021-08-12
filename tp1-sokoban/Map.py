from cells import Wall, ObjectiveCell, Cell
from tokens import Box, Player, Token
from node import Node
from quadrant import Quadrant


class Map():
    cellMap = []
    playerFila = 0
    playerColumna = 0
    cantFilas = 0
    cantColumnas = 0
    objectiveList = []
    caja = Box()
    pared = Wall()
    coordinates = []

    def __init__(self, asciiMap, cantFilas, cantColumnas):
        self.cantColumnas = cantColumnas
        self.cantFilas = cantFilas
        self.objectives = []
        self.boxes = []
        self.walls = []
        # for x in range(cantFilas):
        x = 0
        for j in asciiMap:
            y = 0
            aux = []
            aux_coordinates = []
            for k in j:
                auxCell = Cell()
                if k == "#":
                    aux_coordinates.append(Quadrant('wall', [x, y], True))
                    aux.append(Wall())
                    self.walls.append([x, y])
                elif k == " ":
                    aux_coordinates.append(Quadrant('blank', [x, y]))
                    aux.append(auxCell)
                elif k == "$":
                    self.boxes.append([x, y])
                    aux_coordinates.append(Quadrant('box', [x, y]))
                    auxCell.update(Box())
                    aux.append(auxCell)
                elif k == "@":
                    aux_coordinates.append(Quadrant('player', [x, y]))
                    auxCell.update(Player())
                    aux.append(auxCell)
                    self.playerFila = x
                    self.playerColumna = y
                elif k == ".":
                    self.objectives.append([x, y])
                    aux_coordinates.append(Quadrant('objective', [x, y], True))
                    auxObj = ObjectiveCell()
                    aux.append(auxObj)
                    self.objectiveList.append(auxObj)
                y += 1
            x += 1
            self.coordinates.append(aux_coordinates)
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

    def can_move_box(self, direction, position, boxes, new_boxes):
        if direction == 'up':
            if ([position[0]-1, position[1]] not in self.walls) and ([position[0]-1, position[1]] not in boxes):
                new_boxes.append([position[0]-1, position[1]])
                return True
            else:
                return False

        elif direction == 'down':
            if ([position[0]+1, position[1]] not in self.walls) and ([position[0]+1, position[1]] not in boxes):
                new_boxes.append([position[0]+1, position[1]])
                return True
            else:
                return False
        elif direction =='left':
            if([position[0], position[1]-1] not in self.walls) and ([position[0], position[1]-1] not in boxes):
                new_boxes.append([position[0], position[1]-1])
                return True
            else:
                return False

        elif direction == 'right':
            if([position[0], position[1]+1] not in self.walls) and ([position[0], position[1]+1] not in boxes):
                new_boxes.append([position[0], position[1]+1])
                return True
            else:
                return False

    def can_move(self, direction, position, boxes, new_boxes):  # chequeo todo el tema de instancias para ver si se puede mover
        if direction == 'up':
            if [position[0] - 1, position[1]] not in self.walls:
                if [position[0] - 1, position[1]] in boxes:
                    if self.can_move_box( 'up', [position[0]-1, position[1]], boxes, new_boxes):
                        #if existe una caja en la lista con esas coordenadas
                        new_boxes.remove([position[0]-1, position[1]])
                        return True
                else:
                    return True
            else:
                return False
            if direction == 'down':
                if self.coordinates[position[0] + 1][position[1]].element != 'wall':
                    if self.coordinates[position[0] + 1][position[1]].element == 'box':
                        if self.can_move_box('down', [position[0] + 1, position[1]], boxes, new_boxes):
                            # if existe una caja en la lista con esas coordenadas
                            new_boxes.remove([position[0] + 1, position[1]])
                            return True
                else:
                    return False
                if direction == 'left':
                    if self.coordinates[position[0]][position[1] + 1].element != 'wall':
                        if self.coordinates[position[0]][position[1] + 1].element == 'box':
                            if self.can_move_box('left', [position[0], position[1] + 1], boxes, new_boxes):
                                # if existe una caja en la lista con esas coordenadas
                                new_boxes.remove([position[0], position[1] + 1])
                                return True
                    else:
                        return False
                    if direction == 'right':
                        if self.coordinates[position[0]][position[1] - 1].element != 'wall':
                            if self.coordinates[position[0]][position[1] - 1].element == 'box':
                                if self.can_move_box('right', [position[0], position[1] - 1], boxes, new_boxes):
                                    # if existe una caja en la lista con esas coordenadas
                                    new_boxes.remove([position[0], position[1] - 1])
                                    return True
                        else:
                            return False

        if direction == 'left':
            if [position[0], position[1] + 1] not in self.walls:
                if [position[0], position[1]+1] in boxes:
                    if self.can_move_box( 'left', [position[0], position[1] + 1], boxes, new_boxes):
                        # if existe una caja en la lista con esas coordenadas
                        new_boxes.remove([position[0], position[1] + 1])
                        return True
                else:
                    return True
            else:
                return False

        if direction == 'right':
            if [position[0], position[1] - 1] not in self.walls:
                if [position[0], position[1] - 1] in boxes:
                    if self.can_move_box('right', [position[0], position[1] - 1], boxes, new_boxes):
                        # if existe una caja en la lista con esas coordenadas
                        new_boxes.remove([position[0], position[1] - 1])
                        return True
                else:
                    return True
            else:
                return False

    def check_adjacent_moves(self, previous_node):  # version reducida de todo lo de arriba
        node_list = []
        aux_boxes = previous_node.boxes.copy()
        if self.can_move('up', previous_node.player, previous_node.boxes, aux_boxes):
            node_list.append(Node([previous_node.player[0] - 1, previous_node.player[1]], previous_node, 'up', aux_boxes))
        if self.can_move('down', previous_node.player, previous_node.boxes, aux_boxes):
            node_list.append(Node([previous_node.player[0] + 1, previous_node.player[1]], previous_node, 'down', aux_boxes))
        if self.can_move('right', previous_node.player, previous_node.boxes, aux_boxes):
            node_list.append(Node([previous_node.player[0], previous_node.player[1] + 1], previous_node, 'right', aux_boxes))
        if self.can_move('left', previous_node.player, previous_node.boxes, aux_boxes):
            node_list.append(Node([previous_node.player[0], previous_node.player[1] - 1], previous_node, 'left', aux_boxes))
        return node_list

    def check_if_win(self, node):
        for box in node.boxes:
            if box not in self.objectives:
                return False
        return True

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

