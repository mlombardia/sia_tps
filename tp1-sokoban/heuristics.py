import math

# distancia entre las cajas y sus objetivos mas cercanos
def heuristic1(node, objectives):
    curr_heuristic = 0
    for box in node.boxes:
        min_distance_to_obj = math.inf  #infinito
        for objective in objectives:
            current_distance_to_obj = abs(box[0] - objective.x)
            current_distance_to_obj += abs(box[1] - objective.y)
            if current_distance_to_obj < min_distance_to_obj:
                min_distance_to_obj = current_distance_to_obj
        curr_heuristic += min_distance_to_obj
        node.heuristic = curr_heuristic
    return curr_heuristic

# distancia entre el jugador a su caja mas cercana y de esa caja a su objetivo mas cercano
def heuristic2(node, objectives):
    curr_heuristic = 0
    for box in node.boxes:
        closest_box = math.inf
        closest_obj = math.inf
        current_distance_to_box = abs(box[0] - node.player[0])
        current_distance_to_box += abs(box[1] - node.player[1])
        if current_distance_to_box < closest_box:
            closest_box = current_distance_to_box
        for objective in objectives:
            current_distance_to_obj = abs(objective.x - box[0])
            current_distance_to_obj += abs(objective.y - box[1])
            if current_distance_to_obj < closest_obj:
                closest_obj = current_distance_to_obj
        curr_heuristic += closest_box + closest_obj
        node.heuristic = curr_heuristic
    return curr_heuristic

# distancia entre una caja a su objetivo mas cercano y de esa caja al jugador
def heuristic3(node, objectives):
    curr_heuristic = 0
    for box in node.boxes:
        min_distance_to_obj = math.inf  #infinito
        for objective in objectives:
            current_distance_to_obj = abs(box[0] - objective.x)
            current_distance_to_obj += abs(box[1] - objective.y)
            if current_distance_to_obj < min_distance_to_obj:
                min_distance_to_obj = current_distance_to_obj
        distance_to_player = abs(box[0] - node.player[0])
        distance_to_player += abs(box[1] - node.player[1])
        curr_heuristic += min_distance_to_obj + distance_to_player
    return curr_heuristic