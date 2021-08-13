from searchMethod import SearchMethod
from node import Node
from sequence import Sequence

BLOCK = 5

class IDDFS(SearchMethod):

    maxDepth = 0
    node_stack=[]

    def __init__(self, maxDepth):
        self.maxDepth = maxDepth       #profundidad maxima
        self.node_stack=[]
        super().__init__()

    def search(self, game_map):
        startDepth=0
        visited_nodes = set()

        self.node_stack = [Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)]  # arranco algoritmo con la posicion inicial del player, no tiene previos ni ninguna direccion asociada

        while len(self.node_stack) > 0:
            while startDepth < self.maxDepth:
                current = self.node_stack.pop()                                             # agarro un nodo, lo agrego a visitados
                visited_nodes.add(current)
                if game_map.check_if_win(current):
                    print("Solution found! Calculating...")
                    return Sequence(current)                                                # si en este nodo encuentro que gane, devuelvo la secuencia de nodos
                elif startDepth == self.maxDepth:                                           #no hay solucion en este nivel de profundidad
                    return None
                else:
                    new_moves = game_map.check_adjacent_moves(current)
                    for move in new_moves:                                                  # sino, chequeo que movs disponibles
                        if move not in visited_nodes:                                       # y los agrego al stack si no fue visitado
                            startDepth += 1                                                 # le sumo 1 a la profundidad
                            self.node_stack.append(move)
            startDepth = self.maxDepth                                                      #busco "un nivel" mas abajo
            self.maxDepth += BLOCK
        return None


