class Sequence:
    def __init__(self, node):
        self.node = node
        self.directions = self.get_sequence(node, [])

    def get_sequence(self, node, direction_list):
        if(node.direction == None):
            return
        self.get_sequence(node.previous, direction_list)
        direction_list.append(node.direction)
        return direction_list
#voy recursivamente al primero, y despues voy imprimiendo secuencialmente las direcciones