# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Map import Map
from AI import AI
from dfs import DFS

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('sokoban')

# crear un mapa
##estaticos
##dinamicos
###y sus movimientos

#   # es pared
#   . es objetivo
#   $ es la caja
#   @ es el player
#     es blanco

asciiMap = [["#", "#", "#", "#", "#"],
            ["#", ".", " ", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", " ", "$", " ", "#"],
            ["#", "@", " ", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#"]]

'''
for i in asciiMap:
    print()
    for j in i:
        print(j, end="")
        '''

map = Map(asciiMap, 10, 5)

'''
map.printBoard()
map.movePlayer("up")
map.printBoard()

map.movePlayer("right")
map.printBoard()

map.movePlayer("up")
map.printBoard()

map.movePlayer("right")
map.printBoard()


map.movePlayer("down")
map.printBoard()

map.movePlayer("down")
map.printBoard()
'''

#ai = AI(map)
#ai.DFS()

dfs = DFS()
seq = dfs.search(map)
print(seq)
print(len(seq))
