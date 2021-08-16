from searchMethod import SearchMethod
from node import Node
from sequence import Sequence


def sort_by_heuristic_value(node):
    return node.heuristic


class Greedy(SearchMethod):
    solution = False
    depth = 0
    cost = 0
    exp_nodes = 0
    front_nodes = 0
    total_nodes = 0

    def __init__(self, heuristic):
        self.heuristic = heuristic
        super().__init__()

    def search(self, game_map):
        #inicializo visitados
        visited_nodes = set()
        #inicializo frontera
        first_node = Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)
        self.heuristic(first_node, game_map.objectiveList)
        frontier = [first_node]
        while len(frontier) > 0:
            current = frontier.pop(0)
            visited_nodes.add(current)                          # agarro el nodo con menor heuristica
            if game_map.check_if_win(current):                  # si con este se gana, CONGRATULATIONS y te pasamos
                print("Solution found! Calculating...")         # los movimientos
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
                return Sequence(current)
            else:
                new_moves = game_map.check_adjacent_moves(current)          # sino, fijate los movs que podes hacer
                if len(new_moves) != 0:                                     # desde aca
                    self.depth += 1
                    self.cost += 1
                    self.exp_nodes += 1
                for move in new_moves:
                    if move not in visited_nodes:                           # si estos nodos no fueron visitados,
                        self.heuristic(move, game_map.objectiveList)        # calculale la heuristica y agregalo a la
                        frontier.append(move)                               # frontera
                        frontier = sorted(frontier, key=sort_by_heuristic_value) # que vaya ordenada tambien, ya q tamo
                    self.total_nodes += 1
                    self.front_nodes += 1
                self.front_nodes -= 1
        return None
        #mientras haya frontera
            #saco el primero
            #si en este el mapa esta completo
                #ggwp y te paso la secuencia
            #me fijo si hay movimientos posibles
            #recorro los posibles movimientos
                #si el movimiento no esta en visitados
                    #le asigno valor de heuristica
                    #lo agrego a visitados
                    #me fijo de ordenar en base al valor de heuristica
        #no encontro solucion entonces no devuelvo nada


