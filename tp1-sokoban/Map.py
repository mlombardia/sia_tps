from node import Node


class Map():
    cellMap = []
    playerFila = 0
    playerColumna = 0
    cantFilas = 0
    cantColumnas = 0
    objectiveList = []
    coordinates = []

    def __init__(self, asciiMap, cantFilas, cantColumnas):
        self.cantColumnas = cantColumnas
        self.cantFilas = cantFilas
        self.objectives = []
        self.boxes = set()
        self.walls = set()
        # for x in range(cantFilas):
        x = 0
        for j in asciiMap:
            y = 0
            aux = []
            for k in j:
                if k == "#":
                    self.walls.add((x, y))
                elif k == " ":
                    pass
                elif k == "$":
                    self.boxes.add((x, y))
                elif k == "@":
                    self.playerFila = x
                    self.playerColumna = y
                elif k == ".":
                    self.objectives.append((x, y))
                y += 1
            x += 1
            self.cellMap.append(aux)

    def printBoard(self):
        for i in self.cellMap:
            print()
            for j in i:
                print(j.symbol, end="")



    def can_move_box(self, direction, position, boxes, new_boxes):
        if direction == 'up':
            if ((position[0]-1, position[1]) not in self.walls) and ((position[0]-1, position[1]) not in boxes):
                new_boxes.add((position[0]-1, position[1]))
                return True
            else:
                return False

        elif direction == 'down':
            if ((position[0]+1, position[1]) not in self.walls) and ((position[0]+1, position[1]) not in boxes):
                new_boxes.add((position[0]+1, position[1]))
                return True
            else:
                return False
        elif direction == 'left':
            if((position[0], position[1]-1) not in self.walls) and ((position[0], position[1]-1) not in boxes):
                new_boxes.add((position[0], position[1]-1))
                return True
            else:
                return False

        elif direction == 'right':
            if((position[0], position[1]+1) not in self.walls) and ((position[0], position[1]+1) not in boxes):
                new_boxes.add((position[0], position[1]+1))
                return True
            else:
                return False

    def can_move(self, direction, position, boxes, new_boxes):  # chequeo todo el tema de instancias para ver si se puede mover
        if direction == 'up':
            if (position[0] - 1, position[1]) not in self.walls:
                if (position[0] - 1, position[1]) in boxes:
                    if self.can_move_box( 'up', (position[0]-1, position[1]), boxes, new_boxes):
                        #if existe una caja en la lista con esas coordenadas
                        new_boxes.remove((position[0]-1, position[1]))
                        return True
                else:
                    return True
            else:
                return False
        elif direction == 'down':
            if (position[0] + 1, position[1]) not in self.walls:
                if (position[0] + 1, position[1]) in boxes:
                    if self.can_move_box('down', (position[0]+1, position[1]), boxes, new_boxes):
                        #if existe una caja en la lista con esas coordenadas
                        new_boxes.remove((position[0]+1, position[1]))
                        return True
                else:
                    return True
            else:
                return False
        elif direction == 'left':
            if (position[0], position[1] - 1) not in self.walls:
                if (position[0], position[1]-1) in boxes:
                    if self.can_move_box('left', (position[0], position[1] - 1), boxes, new_boxes):
                        # if existe una caja en la lista con esas coordenadas
                        new_boxes.remove((position[0], position[1] - 1))
                        return True
                else:
                    return True
            else:
                return False
        elif direction == 'right':
            if (position[0], position[1] + 1) not in self.walls:
                if (position[0], position[1] + 1) in boxes:
                    if self.can_move_box('right', (position[0], position[1] + 1), boxes, new_boxes):
                        # if existe una caja en la lista con esas coordenadas
                        new_boxes.remove((position[0], position[1] + 1))
                        return True
                else:
                    return True
            else:
                return False

        elif direction == 'right':
            if [position[0], position[1] + 1] not in self.walls:
                if [position[0], position[1] + 1] in boxes:
                    if self.can_move_box('right', [position[0], position[1] + 1], boxes, new_boxes):
                        # if existe una caja en la lista con esas coordenadas
                        new_boxes.remove([position[0], position[1] + 1])
                        return True
                else:
                    return True
            else:
                return False

    def check_adjacent_moves(self, previous_node):  # version reducida de todo lo de arriba
        node_list = []
        aux_boxes = previous_node.boxes.copy()
        aux2_boxes = previous_node.boxes.copy()
        aux3_boxes = previous_node.boxes.copy()
        aux4_boxes = previous_node.boxes.copy()

        if self.can_move('up', previous_node.player, previous_node.boxes, aux_boxes):
            node_list.append(Node((previous_node.player[0] - 1, previous_node.player[1]), previous_node, 'up', aux_boxes))
        if self.can_move('down', previous_node.player, previous_node.boxes, aux2_boxes):
            node_list.append(Node((previous_node.player[0] + 1, previous_node.player[1]), previous_node, 'down', aux2_boxes))
        if self.can_move('right', previous_node.player, previous_node.boxes, aux3_boxes):
            node_list.append(Node((previous_node.player[0], previous_node.player[1] + 1), previous_node, 'right', aux3_boxes))
        if self.can_move('left', previous_node.player, previous_node.boxes, aux4_boxes):
            node_list.append(Node((previous_node.player[0], previous_node.player[1] - 1), previous_node, 'left', aux4_boxes))
        return node_list

    def check_if_win(self, node):
        for box in node.boxes:
            if box not in self.objectives:
                return False
        return True

