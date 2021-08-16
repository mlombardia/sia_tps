import math

from searchMethod import SearchMethod
from node import Node
from sequence import Sequence
import bisect

BLOCK = 5

class IDAstar(SearchMethod):
    maxDepth = 0

    solution = False
    depth = 0
    cost = 0
    exp_nodes = 0
    front_nodes = 0
    total_nodes = 0
    summed = 0

    def __init__(self, heuristic):
        self.heuristic = heuristic
        super().__init__()

    def search(self, game_map):
        first_node = Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)
        self.heuristic(first_node, game_map.objectiveList)
        lim = first_node.f()
        min_exceeded_lim = -1

        q1 = []
        q2 = []

        out_of_frontier = [] #ordered list

        q1.append(first_node)
        known_nodes = set()

        known_nodes.add(first_node)

        nodes_processed = 0
        total_nodes = 0

        won = False

        while (q1 or q2) and not won:
            if not q1:
                q1 = q2
                q2 = []
                lim = min_exceeded_lim
                min_exceeded_lim = -1

            node = q1.pop()
            self.heuristic(node, game_map.objectiveList)
            f = node.f()

            if f > lim:
                q2.append(node)
                continue

            if game_map.check_if_win(node):
                won = True
            else:
                nodes_processed += 1
                new_moves = game_map.check_adjacent_moves(node)

                for move in new_moves:
                    total_nodes += 1
                    self.heuristic(move, game_map.objectiveList)
                    proc_node = None
                    if move in known_nodes:
                        proc_node = move

                    if proc_node and node.depth + 1 >= proc_node.depth:
                        continue

                    known_nodes.add(move)

                    #children.append(move)

                    if move.f() > lim:
                        q2.append(move)
                        if min_exceeded_lim == -1 or move.f() < min_exceeded_lim:
                            min_exceeded_lim = move.f()
                    else:
                        q1.append(move)
        if won:
            print("Solution found! Calculating...")
            self.solution = True
            print("\nDepth:")
            print(node.depth)

            print("\nCost:")
            print(node.depth)

            print("\nExpanded nodes:")
            print(nodes_processed)

            print("\nTotal nodes:")
            print(total_nodes)

            print("\nFrontier nodes:")
            print(total_nodes - nodes_processed)

            print("\nsequence and sequence length (in reverse)")
            return Sequence(node)
        else:
            print("perdiste")
            exit()







        '''
        visited_nodes = set()
        front_nodes_set = set()
        first_node = Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)
        startDepth = 0

        minh = math.inf

        node_stack = [Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)]  # arranco algoritmo con la posicion inicial del player, no tiene previos ni ninguna direccion asociada

        self.maxDepth=node_stack[0].f()

        print("istic ", node_stack[0].heuristic)

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
                    print(self.cost)
                    print("\nExpanded nodes:")
                    print(self.exp_nodes)
                    print("\nFrontier nodes:")
                    print(self.front_nodes)

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
                            node_stack.append(move)
                        self.front_nodes += 1
                        self.total_nodes += 1
                    self.front_nodes -= 1

                    startDepth = current.f()

            for node in front_nodes_set:
                if node.f() < minh:
                    minh=node.f()

            startDepth=self.maxDepth
            self.maxDepth+=minh

        return None
        '''

