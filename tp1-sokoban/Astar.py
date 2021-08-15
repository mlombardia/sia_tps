from node import Node
from searchMethod import SearchMethod
from sequence import Sequence
from heuristics import *


class Astar:

    def __init__(self, heuristic):
        self.heuristic = heuristic
        super().__init__()


    def search(self, game_map): #la power mega
        openSet = [Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)] #estado inicial
        closedSet = set()

        while(len(openSet) > 0):
            winner = openSet[0]
            id = 0
            #for node in openSet:
            #    if(node.f() < winner.f()):
            #        winner = node
            for i in range(len(openSet)):
                if openSet[i].f() < winner.f():
                    winner=openSet[i]
                    id = i
                break

            if(game_map.check_if_win(winner)):
                print("Solution found! Calculating...")
                return Sequence(winner)

            openSet.remove(openSet[id])
            closedSet.add(winner)
            #print(winner)

            new_moves = game_map.check_adjacent_moves(winner)
            for move in new_moves:
                if move not in closedSet:
                    self.heuristic(move, game_map.objectiveList)
                    if(openSet.__contains__(move)):
                        if(winner.depth+1 < move.depth):
                            move.depth = winner.depth + 1
                    else:
                        openSet.append(move)
