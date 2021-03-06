from searchMethod import SearchMethod
from node import Node
from sequence import Sequence

BLOCK = 2


class IDDFS(SearchMethod):
    solution = False
    depth = 0
    cost = 0
    exp_nodes = 0
    front_nodes = 0
    total_nodes = 0
    summed = 0

    def __init__(self, maxDepth):
        self.maxDepth = maxDepth  # profundidad maxima
        super().__init__()

    def search(self, game_map):
        startDepth = 0
        visited_nodes = set()

        node_stack = [Node((game_map.playerFila, game_map.playerColumna), None, None,
                           game_map.boxes)]  # arranco algoritmo con la posicion inicial del player, no tiene previos ni ninguna direccion asociada

        while len(node_stack) > 0:
            while startDepth < self.maxDepth:
                current = node_stack.pop()  # agarro un nodo, lo agrego a visitados
                visited_nodes.add(current)
                if game_map.check_if_win(current):
                    print("Solution found! Calculating...")
                    self.solution = True
                    print("\nDepth:")
                    print(current.depth)
                    print("\nCost:")
                    print(current.depth)
                    print("\nExpanded nodes:")
                    print(self.exp_nodes)
                    print("\nFrontier nodes:")
                    print(self.front_nodes)
                    print("\nTotal nodes:")
                    print(self.total_nodes)
                    print("summed: ", self.summed)
                    print("\nsequence and sequence length")
                    return Sequence(current)  # si en este nodo encuentro que gane, devuelvo la secuencia de nodos
                else:  # sino, chequeo que movs disponibles y los agrego al stack si no fue visitado
                    new_moves = game_map.check_adjacent_moves(current)
                    aux = len(new_moves)
                    if aux != 0:  # si es distinto de cero es porque se expandio el nodo
                        self.depth += 1  # entonces aumenta la profundidad
                        self.cost += 1  # y el costo (que es igual a la profundidad
                        self.exp_nodes += 1  # aumenta en 1 el numero de nodos expandidos

                    for move in new_moves:
                        if move not in visited_nodes:
                            if (startDepth+1)%self.maxDepth == 0:
                                node_stack.insert(0,move)
                            else:
                                node_stack.append(move)
                        self.front_nodes += 1
                        self.total_nodes += 1
                    self.front_nodes -= 1
                    startDepth += 1

            # si sale del while es porque no encontro en esa profundidad, entonces busco "un nivel" mas abajo
            startDepth = self.maxDepth  # hago que empiece donde dejo
            self.maxDepth += BLOCK  # hasta BLOCK mas de profundidad
            self.summed += 1
        return None