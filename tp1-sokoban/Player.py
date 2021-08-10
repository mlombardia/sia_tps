import Map
from Classes import Blank, Cell, Objective, Box, Wall

class Player:
    is_moveable = True
    is_steppable = False
    symbol = "@"
    curr_pos = []
    kind = "player"

    def move_up(self, map):
        if isinstance(self.up(map), Blank) or isinstance(self.up(map), Objective):
            self.curr_pos[1] = self.curr_pos[1] + 1
            map.update(self.curr_pos, self, "up")
            #borrá lo que dejaste atrás
        elif self.up.isType("box"):
            if self.up.up.isType("box") or self.up.up.isType("wall"):
                return False
            else:
                map.update(self.curr_pos, self)
                map.update(box.curr_pos, box)
                self.up.curr_pos[1] = self.up.curr_pos[1] + 1
                self.curr_pos[1] = self.curr_pos[1] + 1
                #borrá lo que dejaste atrás
        else:
            return False

    def up(self, map):
        return map[self.curr_pos[0]][self.curr_pos[1]+1]

    def isType(self, tipo):
        return tipo==self.kind