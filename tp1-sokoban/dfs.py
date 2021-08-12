from searchMethod import SearchMethod
from node import Node
from sequence import Sequence


class DFS(SearchMethod):
    def __init__(self):
        pass

    def search(self, game_map):
        visited_nodes = set([])

        node_stack = [Node([game_map.playerFila, game_map.playerColumna], None, None, game_map.boxes)] #arranco algoritmo con la posicion
                                                                                        # inicial del player, no tiene
                                                                                        #previos ni ninguna direccion asociada

        while len(node_stack) > 0:
            current = node_stack.pop()                                                  #agarro un nodo, lo agrego a visitados
            visited_nodes.add(current)
            print(current.direction)
            if game_map.check_if_win():
                return Sequence(current)                                                #si en este nodo encuentro que gane,
            else:                                                                       #devuelvo la secuencia de nodos
                new_moves = game_map.check_adjacent_moves(current)
                for move in new_moves:                                                  #sino, chequeo que movs disponibles
                    if move not in visited_nodes:                                       #y los agrego al stack si no fue visitado
                        node_stack.append(move)
        return []
