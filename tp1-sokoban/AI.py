import copy
from Map import Map
from cells import Cell


class AI:
    stateList = []
    hashList = []
    mentalMap = []
    auxMap = []
    moves = ["up", "down", "left", "right"]
    movesCustom = ["up", "down", "up", "down", "right"]

    def __init__(self, mapa):
        self.mentalMap = mapa
        #self.auxMap = copy.deepcopy(mapa)
        #self.auxMap = mapa
        #self.mentalMap = copy.deepcopy(self.auxMap)
        auxState = State(self.mentalMap)
        self.stateList.append(auxState)
        self.hashList.append(auxState.hash)
        auxState.printState()
        print("end initial---------------")

    def move(self, direction):
        if (direction == "up"):
            if self.mentalMap.movePlayer("up"):
                auxState = State(self.mentalMap)
                self.stateList.append(auxState)
                self.hashList.append(auxState.hash)
        elif (direction == "down"):
            if self.mentalMap.movePlayer("down"):
                auxState = State(self.mentalMap)
                self.stateList.append(auxState)
                self.hashList.append(auxState.hash)
        elif (direction == "left"):
            if self.mentalMap.movePlayer("left"):
                auxState = State(self.mentalMap)
                self.stateList.append(auxState)
                self.hashList.append(auxState.hash)
        elif (direction == "right"):
            if self.mentalMap.movePlayer("right"):
                auxState = State(self.mentalMap)
                self.stateList.append(auxState)
                self.hashList.append(auxState.hash)


    def search(self, start_node):
        visited_nodes = set([])
        node_stack = [start_node]

        while len(node_stack) > 0:
            current = node_stack.pop()
            visited_nodes.add(current.hash)

            #si este es el nodo ganador (el mapa corrobora que el jugador gano), CONGRATULATIONS

            #chequear moves

            #en cada move, fijarse si esta en visited_nodes; si no esta lo agregamos en node_stack


        # no se llego a solucion, jode



    def DFS(self, map):

#dfs iterativo WIP
        for i in range(1):          #la idea es que sea while not self.mentalMap.checkIfWin():
            for move in self.movesCustom:
                self.mentalMap = copy.deepcopy(self.auxMap)
                print("\nold official board:")
                self.mentalMap.printBoard()
                print("\nmove", move)
                if self.auxMap.movePlayer(move):    #ac?? da problemas
                    if State(self.auxMap).hash not in self.hashList: #porque si mejor no voy a ese state lo quiero evitar, pero el move de arriba me edit?? el original
                        print("new state-----------:")
                        State(self.auxMap).printState()
                        self.auxMap.printBoard()
                        print("old hashlist:")
                        print(self.hashList)
                        self.move(move)
                        print("new hashlist:")
                        print(self.hashList)
                        print("new official board:")
                        self.mentalMap.printBoard()
                    else:
                        print("better not move", move)
                        print(self.hashList)
                        print(State(self.auxMap).hash)
                else:
                    print("cant go", move)



class State:
    playerRow = 0
    playerCol = 0
    boxRow = 0
    boxCol = 0
    hash = 0

    def __init__(self, map):
        x = 0
        for row in map.cellMap:
            y = 0
            for col in row:
                if col.symbol == "$":
                    self.boxCol = y
                    self.boxRow = x
                elif col.symbol == "@":
                    self.playerRow = x
                    self.playerCol = y
                y += 1
            x += 1
        self.hash = hash((self.playerRow, self.playerCol, self.boxRow, self.boxCol))

    def printState(self):
        print("\nplayer: ")
        print(self.playerRow, self.playerCol)
        print("box")
        print(self.boxRow, self.boxCol)
        print(self.hash)

        print("\n")
        


# hasta aca ^ lo de Uri

# aca ??? lo de Cami

from Map import Map
from cells import Cell

'''
class AI:
    stateList = []
    hashList = []
    mentalMap = []
    auxState = ''
    #auxMap = []
    moves = ["up", "down", "left", "right"]
    movesCustom = ["up", "down", "up", "down", "right"]

    def __init__(self, mapa):
        self.mentalMap = mapa
        auxState = State(self.mentalMap)
        self.stateList.append(auxState)
        auxState.visited = True
        auxState.printState()

    def moveUp(self):
        if self.mentalMap.movePlayer("up"):
            self.stateList.append(State(self.mentalMap))
            return True
        return False

    def moveDown(self):
        if self.mentalMap.movePlayer("down"):
            self.stateList.append(State(self.mentalMap))
            return True
        return False

    def moveLeft(self):
        if self.mentalMap.movePlayer("left"):
            self.stateList.append(State(self.mentalMap))
            return True
        return False

    def moveRight(self):
        if self.mentalMap.movePlayer("right"):
            auxState = State(self.mentalMap)
            self.stateList.append(auxState)
            return True
        return False

    def move(self, direction):
        if (direction == "up"):
            self.moveUp()
            return True

        elif (direction == "down"):
            if self.mentalMap.movePlayer("down"):
                self.moveDown()
                return True

        elif (direction == "left"):
            if self.mentalMap.movePlayer("left"):
                self.moveLeft()
                return True

        elif (direction == "right"):
            if self.mentalMap.movePlayer("right"):
                self.moveRight()
                return True

        return False


    def DFS(self):
        print ("mapa inicial")
        self.mentalMap.printBoard()

        #while (not self.mentalMap.checkIfWin()) or (self.mentalMap.checkIfLoose()):          #la idea es que sea while not self.mentalMap.checkIfWin(), yo agregaria check if loose tambien
        for move in self.movesCustom:
            if self.move(move):
                State(self.mentalMap).visited = True  # marco que lo visite
                self.stateList.append(State(self.mentalMap))  # lo agrego a la lista de visitados
                if not State(self.mentalMap).visited and State(self.mentalMap) not in self.stateList:    #si se puede mover y ese estado no fue visitado
                    print ("\nmoving", move)
                    print("el nuevo estado es:")
                    State(self.mentalMap).printState()
                    self.mentalMap.printBoard()
                else:
                    print("better not move", move)
            else:
                print("cant go", move)



class State:
    playerRow = 0
    playerCol = 0
    boxRow = 0
    boxCol = 0
    visited=False

    def __init__(self, map):
        x = 0
        for row in map.cellMap:
            y = 0
            for col in row:
                if col.symbol == "$":
                    self.boxCol = y
                    self.boxRow = x
                elif col.symbol == "@":
                    self.playerRow = x
                    self.playerCol = y
                y += 1
            x += 1
        self.hash = hash((self.playerRow, self.playerCol, self.boxRow, self.boxCol))

    def printState(self):
        print("\nplayer: ")
        print(self.playerRow, self.playerCol)
        print("box")
        print(self.boxRow, self.boxCol)
'''
