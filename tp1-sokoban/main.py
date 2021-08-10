# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('sokoban')


#crear un mapa
##estaticos
##dinamicos
###y sus movimientos

#   # es pared
#   . es objetivo
#   $ es la caja
#   @ es el player
#     es blanco

asciiMap =  [['#', '#', '#'],
        ['#', '.', '#'],
        ['#', ' ', '#'],
        ['#', ' ', '#'],
        ['#', ' ', '#'],
        ['#', '$', '#'],
        ['#', ' ', '#'],
        ['#', '@', '#'],
        ['#', '#', '#']]



Map.fillMap(asciiMap, 9, 3)




state = {'player': [7,1],
         'box': [5,1],
         }




