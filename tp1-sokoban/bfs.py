from searchMethod import SearchMethod
from node import Node
from sequence import Sequence


class BFS(SearchMethod):
    def __init__(self):
        super().__init__()

    def search(self, game_map):
        visited_nodes = set()

        node_queue = [Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)]  #arranco algoritmo con la posicion inicial del player, no tiene
                                                                                                        #previos ni ninguna direccion asociada, como es bf es queue y no stack

        while len(node_queue) > 0:
            current = node_queue.pop(0)                                                 #popeo el primer elemento porque es una cola
            visited_nodes.add(current)                                                  #agarro un nodo, lo agrego a visitados
            if game_map.check_if_win(current):
                print("Solution found! Calculating...")
                return Sequence(current)                                                #si en este nodo encuentro que gane,
            else:                                                                       #devuelvo la secuencia de nodos
                new_moves = game_map.check_adjacent_moves(current)
                for move in new_moves:                                                  #sino, chequeo que movs disponibles
                    if move not in visited_nodes:                                       #y los agrego al stack si no fue visitado
                        node_queue.append(move)

        return None