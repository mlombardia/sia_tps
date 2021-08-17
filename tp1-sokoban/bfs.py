from searchMethod import SearchMethod
from node import Node
from sequence import Sequence


class BFS(SearchMethod):

    solution = False
    depth = 0
    cost = 0
    exp_nodes = 0
    front_nodes = 0
    total_nodes = 0

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
                self.solution = True
                print("\nDepth:")
                print(current.depth)

                print("\nCost:")
                print(self.cost)

                print("\nExpanded nodes:")
                print(self.exp_nodes)

                print("\nTotal nodes:")
                print(self.total_nodes)

                print("\nFrontier nodes:")
                print(self.front_nodes)

                print("\nsequence and sequence length")
                return Sequence(current)                                              #si en este nodo encuentro que gane, devuelvo la secuencia de nodos
            else:                                                                       #sino, chequeo que movs disponibles y los agrego al stack si no fue visitado
                new_moves = game_map.check_adjacent_moves(current)
                aux=len(new_moves)
                if aux != 0:                                                            #si es distinto de cero es porque se expandio el nodo
                    self.depth += 1                                                     #entonces aumenta la profundidad
                    self.cost += 1                                                      #y el costo (que es igual a la profundidad
                    self.exp_nodes += 1                                                 #aumenta en 1 el numero de nodos expandidos
                                                                                         #y hay tantos nuevos nodos frontera como posibles movimientos
                for move in new_moves:
                    if move not in visited_nodes:
                        node_queue.append(move)
                    self.front_nodes += 1
                    self.total_nodes += 1
                self.front_nodes -= 1


        return None
