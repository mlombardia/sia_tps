# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Map import Map
from AI import AI
from dfs import DFS
from bfs import BFS
from time import perf_counter
from iddfs import IDDFS

# crear un mapa
##estaticos
##dinamicos
###y sus movimientos

#   # es pared
#   . es objetivo
#   $ es la caja
#   @ es el player
#     es blanco

asciiMap = [[" "," "," "," "," "," ","#","#","#"," "," "," "," "," "," "],
            [" "," "," "," "," "," ","#",".","#"," "," "," "," "," "," "],
            [" "," ","#","#","#","#","#",".","#","#","#","#","#"," "," "],
            [" ","#","#"," "," "," "," "," "," "," "," "," ","#","#"," "],
            ["#","#"," "," ","#"," ","#"," ","#"," ","#"," "," ","#","#"],
            ["#"," "," ","#","#"," "," "," "," "," ","#","#"," "," ","#"],
            ["#"," ","#","#"," "," ","#"," ","#"," "," ","#","#"," ","#"],
            ["#"," "," "," "," "," ","$","@","$"," "," "," "," "," ","#"],
            ["#","#","#","#"," "," ","#","#","#"," "," ","#","#","#","#"],
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]

asciiMap1 = [["#","#","#"],
             ["#",".","#"],
             ["#"," ","#"],
             ["#","$","#"],
             ["#","@","#"],
             ["#","#","#"]]

file = open("maps/map1.txt", "r")
lines = []
for line in file:
    lines.append(line[:-1])

asciiMap2 = []
for line in lines:
    aux = []
    for character in line:
        aux.append(character)
    asciiMap2.append(aux)


'''
for i in asciiMap2:
    print()
    for j in i:
        print(j, end="")
'''


map = Map(asciiMap2, 6, 9)


iddfs = IDDFS(15)
t1_start = perf_counter()
seq = iddfs.search(map)
t1_stop = perf_counter()
if seq is not None:
    print(seq.directions)
    print(len(seq.directions))
    print((t1_stop-t1_start)*1000)
else:
    print("No path was found")

'''
dfs = DFS()
t1_start = perf_counter()
seq = dfs.search(map)
t1_stop = perf_counter()
if seq is not None:
    print(seq.directions)
    print(len(seq.directions))
    print((t1_stop-t1_start)*1000)
else:
    print("No path was found")
'''

'''
bfs = BFS()
t1_start = perf_counter()
seq = bfs.search(map)
t1_stop = perf_counter()
if seq is not None:
    print(seq.directions)
    print(len(seq.directions))
    print((t1_stop-t1_start)*1000)
else:
    print("No path was found")
'''
