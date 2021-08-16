from Astar import Astar
from Map import Map
from AI import AI
from dfs import DFS
from bfs import BFS
from time import perf_counter
from greedy import Greedy
from idAstar import IDAstar
from iddfs import IDDFS
import yaml
import os
from heuristics import heuristic1, heuristic2, heuristic3

config_filename = 'config.yaml'

with open(config_filename) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

maps_folder = config['maps_folder']
chosen_map = config['map']
algorithm = config['algorithm']
alg_params = config['alg_params']


#   # es pared
#   . es objetivo
#   $ es la caja
#   @ es el player
#     es blanco

file = open(os.path.join(maps_folder, chosen_map), "r")
lines = []
cols = 0
for line in file:
    lines.append(line[:-1])

asciiMap = []
for line in lines:
    aux = []
    for character in line:
        aux.append(character)
        cols+=1
    asciiMap.append(aux)

cols//=len(lines)

print("el mapa seleccionado es:")

for i in asciiMap:
    print()
    for j in i:
        print(j, end="")

print('\n')


map = Map(asciiMap, len(lines), cols)

heuristic_switcher={
    "h1": heuristic1,
    "h2": heuristic2,
    "h3": heuristic3,
}

switcher={
    "DFS": lambda : DFS(),
    "BFS": lambda : BFS(),
    "IDDFS": lambda : IDDFS(alg_params["IDDFS_depth"]),
    "A*": lambda : Astar(heuristic_switcher[alg_params["heuristic"]]),
    "IDA*": lambda : IDAstar(heuristic_switcher[alg_params["heuristic"]]),
    "Greedy": lambda : Greedy(heuristic_switcher[alg_params["heuristic"]]),
}

alg = switcher[algorithm]()
t1_start = perf_counter()
seq = alg.search(map)
t1_stop = perf_counter()

if seq is not None:
    print(seq.directions[::-1])
    print(len(seq.directions))
    print("\ntime (in ms)")
    print((t1_stop-t1_start)*1000)


else:
    print("No path was found")




