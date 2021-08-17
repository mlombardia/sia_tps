from node import Node
from searchMethod import SearchMethod
from sequence import Sequence
from heuristics import *
import bisect


class Astar:

    def __init__(self, heuristic):
        self.heuristic = heuristic
        super().__init__()


    def search(self, game_map): #la power mega
        openSet = [Node((game_map.playerFila, game_map.playerColumna), None, None, game_map.boxes)] #estado inicial
        closedSet = set()

        while(len(openSet) > 0):
            winner = openSet.pop(0)

            if (game_map.check_if_win(winner)):
                print("Solution found! Calculating...")
                self.solution = True
                print("\nDepth:")
                print(winner.depth)

                print("\nCost:")
                print(winner.depth)

                print("\nExpanded nodes:")
                print(len(closedSet))

                print("\nTotal nodes:")
                print(len(closedSet) + len(openSet))

                print("\nFrontier nodes:")
                print(len(openSet))

                print("\nsequence and sequence length")
                return Sequence(winner)

            #openSet.remove(winner) #
            closedSet.add(winner)

            new_moves = game_map.check_adjacent_moves(winner)
            for move in new_moves:
                if move not in closedSet:
                    self.heuristic(move, game_map.objectiveList)

                    if(openSet.__contains__(move)):
                        if(winner.depth+1 < move.depth):
                            move.depth = winner.depth + 1
                    else:
                        bisect.insort(openSet, move) #openSet.append(move)
