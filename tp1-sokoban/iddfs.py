from searchMethod import SearchMethod
from node import Node
from sequence import Sequence

BLOCK = 5

class IDDFS(SearchMethod):

    maxDepth = 0

    def __init__(self, maxDepth):
        self.maxDepth = maxDepth       #profundidad maxima
        super().__init__()

    def search(self, game_map):
        startDepth=0
        visited_nodes = set()

        node_stack = [Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)]  # arranco algoritmo con la posicion inicial del player, no tiene previos ni ninguna direccion asociada

        while len(node_stack) > 0:
            while startDepth < self.maxDepth:
                current = node_stack.pop()                                             # agarro un nodo, lo agrego a visitados
                visited_nodes.add(current)
                if game_map.check_if_win(current):
                    print("Solution found! Calculating...")
                    return Sequence(current)                                                # si en este nodo encuentro que gane, devuelvo la secuencia de nodos
                else:
                    new_moves = game_map.check_adjacent_moves(current)
                    for move in new_moves:                                                  # sino, chequeo que movs disponibles
                        if move not in visited_nodes:                                       # y los agrego al stack si no fue visitado
                            startDepth += 1                                                 # le sumo 1 a la profundidad
                            node_stack.append(move)

            #si sale del while es porque no encontro en esa profundidad, entonces busco "un nivel" mas abajo
            startDepth = self.maxDepth          #hago que empiece donde dejo
            self.maxDepth += BLOCK              #hasta BLOCK mas de profundidad
        return None


