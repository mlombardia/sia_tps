
class Node:
    def __init__(self, player, previous, direction, boxes):
        self.player = player
        self.previous = previous
        self.direction = direction
        self.boxes = boxes
        self.heuristic = 0
        if previous is not None:
            self.depth = previous.depth + 1
        else:
            self.depth = 0

    def f(self):
        return self.depth+self.heuristic

    def get_direction(self):
        return self.direction

    def __lt__(self, other):
        if not isinstance(other, Node):
            return self.f() < other

        f1 = self.f()
        f2 = other.f()
        if f1 == f2:
            return self.heuristic < other.heuristic
        return f1 < f2

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.player == self.player and other.boxes == self.boxes

    def __hash__(self):
        return hash((self.player, frozenset(self.boxes)))
