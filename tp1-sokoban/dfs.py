from searchMethod import SearchMethod


class DFS(SearchMethod):
    def __init__(self):
        pass

    def search(self, start_node):
        visited_nodes = set([])
        node_stack = [start_node]

        while len(node_stack) > 0:
            current = node_stack.pop()
            visited_nodes .add(current)

            #si este es el nodo ganador, CONGRATULATIONS

            #chequear moves

            #en cada move, fijarse si esta en visited_nodes; si no esta lo agregamos en node_stack


        # no se llego a solucion, jodete