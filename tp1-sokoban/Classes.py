
class Parent():
    name="pepito"
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def __init__(self,name):
        super().__init__(name)

    def show_name(self):
        print(self.name)

class Cell:
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



class Box(Cell):
    symbol = "$"
    curr_pos = []
    kind="box"


class Wall(Cell):
    symbol = "#"
    curr_pos = []
    kind="wall"


class Blank(Cell):
    symbol = " "
    curr_pos = []
    kind="blank"

    def move_up(self):
        return True


class Objective(Cell):
    isCompleted = False
    symbol = "."
    curr_pos = []
    kind="objective"