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

    def up(self):
        return Map[self.curr_pos[0]][self.curr_pos[1]+1]