from main import Map


class Cell:
    is_steppable = True
    is_moveable = True
    symbol = ""
    curr_pos = [0,0]

    def isType(self, type):
        return self.kind == type

'''
    def is_changeable(self):
        return self.is_moveable and self.is_steppable

    def check_move_up(self, upper_element):
        if upper_element.is_changeable():
            upper_element.move_up()

    def move_up(self):
        if self.check_move_up(Map[self.curr_pos[0]][self.curr_pos[1]+1]):
            self.curr_pos[1] = self.curr_pos[1] + 1

    def move_down(self):
        self.curr_pos[1] = self.curr_pos[1] - 1
'''



class Player:
    is_moveable = True
    is_steppable = False
    symbol = "@"
    curr_pos = []
    kind = "player"

    def move_up(self):
        if self.up.isType("blank") or self.up.isType("objective"):
            self.curr_pos[1] = self.curr_pos[1] + 1
            #borrá lo que dejaste atrás
        elif self.up.isType("box"):
            if self.up.up.isType("box") or self.up.up.isType("wall"):
                return False
            else:
                self.up.curr_pos[1] = self.up.curr_pos[1] + 1
                self.curr_pos[1] = self.curr_pos[1] + 1
                #borrá lo que dejaste atrás
        else:
            return False





class Box:
    is_moveable = True
    is_steppable = False
    symbol = "$"
    curr_pos = []
    kind="box"


class Wall:
    is_moveable = False
    is_steppable = False
    symbol = "#"
    curr_pos = []
    kind="wall"


class Blank:
    is_moveable = True
    is_steppable = True
    symbol = " "
    curr_pos = []
    kind="blank"

    def move_up(self):
        return True


class Objective:
    is_moveable = True
    is_steppable = True
    symbol = "."
    curr_pos = []
    kind="objective"