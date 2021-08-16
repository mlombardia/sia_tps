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
    summed=0
    node_stack = []
    bound = 0

    def __init__(self, heuristic):
        self.maxDepth = 0      #profundidad maxima
        self.heuristic=heuristic
        super().__init__()


    def search(self, game_map):
        visited_nodes = set()
        self.node_stack = [Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)]  # arranco algoritmo con la posicion inicial del player, no tiene previos ni ninguna direccion asociada
        self.heuristic(self.node_stack[0], game_map.objectiveList)
        self.bound = self.node_stack[0].heuristic

        while True:
            t = self.search2(game_map)
            print(t)
            if isinstance(t, Node):
                print("Solution found! Calculating...")
                self.solution = True
                print("\nDepth:")
                print(t.depth)
                print("\nCost:")
                print(self.cost)
                print("\nExpanded nodes:")
                print(self.exp_nodes)
                print("\nFrontier nodes:")
                print(self.front_nodes)
                print("summed: ", self.summed)
                print("\nsequence and sequence length")
                return Sequence(t)  # si en este nodo encuentro que gane, devuelvo la secuencia de nodos
            self.bound = t

    def search2(self, game_map):
        current = self.node_stack[len(self.node_stack) -1]
        if current.f() > self.bound:
            return current.f()
        if game_map.check_if_win(current):
            return current
        min = math.inf
        new_moves = game_map.check_adjacent_moves(current)

        #aux = len(new_moves)
        #if aux != 0:  # si es distinto de cero es porque se expandio el nodo
        #    self.depth += 1  # entonces aumenta la profundidad
        #    self.cost += 1  # y el costo (que es igual a la profundidad
        #    self.exp_nodes += 1  # aumenta en 1 el numero de nodos expandidos

        for move in new_moves:
            if move not in self.node_stack:
                self.heuristic(move, game_map.objectiveList)
                self.node_stack.append(move) #bisect.insort(self.node_stack, move)
                t = self.search2(game_map)
                if isinstance(t, Node):
                    return current
                if t<min:
                    min = t
                self.node_stack.pop()
        return min




