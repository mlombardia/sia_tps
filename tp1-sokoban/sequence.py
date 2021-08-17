from node import Node

class Sequence:
    def __init__(self, node):
        self.node = node
        self.directions = self.get_sequence(node, [])
        self.nodes = self.get_node_list(node, [])

    def get_sequence(self, node, direction_list):
        iter_node = node
        while iter_node is not None and iter_node.previous is not None:
            direction_list.append(iter_node.direction)
            iter_node = iter_node.previous
        return direction_list

    def get_node_list(self, node, node_list):
        iter_node = node

        while iter_node is not None:
            node_list.append(iter_node)
            iter_node = iter_node.previous
        return node_list

#voy recursivamente al primero, y despues voy imprimiendo secuencialmente las direcciones