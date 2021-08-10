import Classes
import Player


class Map:
    objMap = []

    def fillMap(self, asciiMap, cantFilas, cantColumnas):
        for x in range(cantFilas):
            for y in range(cantColumnas):
                match asciiMap[x][y]:
                    case '#':
                        self.objMap[x][y] = Classes.Wall
                    case ' ':
                        self.objMap[x][y] = Classes.Blank
                    case '$':
                        self.objMap[x][y] = Classes.Box
                    case '@':
                        self.objMap[x][y] = Player
                    case '.':
                        self.objMap[x][y] = Classes.Objective
                        
    def update(self, coordinates, element, move):
        aux = 
        self.objMap[coordinates[0]][coordinates[1]] = element
        match move:
            case 'up':
                self.objMap[coordinates[0]][coordinates[1]-1] = aux
            case 'down':
                12312
            case 'left':
                13212
            case 'right':
                123
        