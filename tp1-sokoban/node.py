class Node:
    def __init__(self, player, previous, direction, boxes):
        self.player = player
        self.previous = previous
        self.direction = direction
        self.boxes = boxes

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.player == self.player and other.boxes == self.boxes

    def __hash__(self):
        return hash((self.player, frozenset(self.boxes)))
