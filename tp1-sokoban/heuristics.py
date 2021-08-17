import math


# distancia entre las cajas y sus objetivos mas cercanos (creo manhattan en minima distancia global)
def heuristic1(node, objectives):
    curr_heuristic = 0
    for box in node.boxes:
        min_distance_to_obj = math.inf  # infinito
        for objective in objectives:
            current_distance_to_obj = abs(box[0] - objective.x)
            current_distance_to_obj += abs(box[1] - objective.y)
            if current_distance_to_obj < min_distance_to_obj:
                min_distance_to_obj = current_distance_to_obj
        curr_heuristic += min_distance_to_obj
    node.heuristic = curr_heuristic
    return curr_heuristic

#igual a la 1 pero + distancia minima entre caja y objetivo
def heuristic2(node, objectives):
    curr_heuristic = 0
    min_distance_to_player = math.inf
    for box in node.boxes:
        min_distance_to_obj = math.inf  # infinito
        for objective in objectives:
            current_distance_to_obj = abs(box[0] - objective.x)
            current_distance_to_obj += abs(box[1] - objective.y)
            if current_distance_to_obj < min_distance_to_obj:
                min_distance_to_obj = current_distance_to_obj
        curr_heuristic += min_distance_to_obj
        current_distance_to_player = abs(box[0] - node.player[0])
        current_distance_to_player += abs(box[1] - node.player[1])
        if current_distance_to_player < min_distance_to_player:
            min_distance_to_player = current_distance_to_player
    curr_heuristic += min_distance_to_player
    node.heuristic = curr_heuristic
    return curr_heuristic


# distancia entre el jugador a su caja mas cercana y de esa caja a su objetivo mas cercano
def heuristic3(node, objectives):
    curr_heuristic = 0
    closest_box = math.inf
    closest_obj = math.inf

    for box in node.boxes:
        current_distance_to_box = abs(box[0] - node.player[0])
        current_distance_to_box += abs(box[1] - node.player[1])
        if current_distance_to_box < closest_box:
            closest_box = current_distance_to_box
        closest_obj = math.inf
        for objective in objectives:
            current_distance_to_obj = abs(objective.x - box[0])
            current_distance_to_obj += abs(objective.y - box[1])
            if current_distance_to_obj < closest_obj:
                closest_obj = current_distance_to_obj
    curr_heuristic += closest_box + closest_obj
    node.heuristic = curr_heuristic
    return curr_heuristic


# distancia entre la caja mas lejana a su objetivo mas cercano, y de esa caja al jugador
def heuristic4(node, objectives):
    curr_heuristic = 0
    min_distance_to_obj = math.inf
    furthest_box = 0
    distance_to_player = 0
    for box in node.boxes:
        min_distance_to_obj = math.inf
        for objective in objectives:
            current_distance_to_obj = abs(box[0] - objective.x)
            current_distance_to_obj += abs(box[1] - objective.y)
            if current_distance_to_obj < min_distance_to_obj: #agarro de una caja su obj mas cercano
                min_distance_to_obj = current_distance_to_obj
        if min_distance_to_obj > furthest_box:
            furthest_box = min_distance_to_obj
            distance_to_player = abs(box[0] - node.player[0])
            distance_to_player += abs(box[1] - node.player[1])
    curr_heuristic += min_distance_to_obj + distance_to_player
    node.heuristic = curr_heuristic
    return curr_heuristic


def heuristic5(node, objectives):  # distancia entre las cajas y sus objetivos mas cercanos (creo euclidiana en minima distancia global)
    curr_heuristic = 0
    for box in node.boxes:
        min_distance_to_obj = math.inf
        for objective in objectives:
            current_distance_to_obj = (abs(box[0] - objective.x) ** 2)
            current_distance_to_obj += (abs(box[1] - objective.y) ** 2)
            current_distance_to_obj = math.sqrt(current_distance_to_obj)
            if current_distance_to_obj < min_distance_to_obj:
                min_distance_to_obj = current_distance_to_obj
        curr_heuristic += min_distance_to_obj
        node.heuristic = curr_heuristic
    return curr_heuristic


def heuristic6(node, objectives): # distancia entre las cajas y sus objetivos mas cercanos (creo euclidiana sin el cuadrado en minima distancia global)
    curr_heuristic = 0
    for box in node.boxes:
        min_distance_to_obj = math.inf
        for objective in objectives:
            current_distance_to_obj = (abs(box[0] - objective.x) ** 2)
            current_distance_to_obj += (abs(box[1] - objective.y) ** 2)
            if current_distance_to_obj < min_distance_to_obj:
                min_distance_to_obj = current_distance_to_obj
        curr_heuristic += min_distance_to_obj
        node.heuristic = curr_heuristic
    return curr_heuristic
