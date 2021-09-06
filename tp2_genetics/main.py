import linecache
import math
import random
import multiprocessing
import signal
import sys

import yaml
import keyboard

from items.Item import generateItems
from mutation import *
from characters.Character import Warrior
from characters.Character import Archer
from characters.Character import Tank
from characters.Character import Rogue
from Crossovers import *
from selectMets import *
from implementations import *
from ends_by import *
from graphics import *


config_filename = 'config.yaml'

with open(config_filename) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

switcher_clase={
    "warrior": Warrior,
    "archer": Archer,
    "rogue": Rogue,
    "tank": Tank,
}

K = config['K']
N = config['N']
Class = config['class']
Clase = switcher_clase[Class]

select_method_1 = config['selection_method_1']
select_method_2 = config['selection_method_2']
select_method_3 = config['selection_method_3']
select_method_4 = config['selection_method_4']
select_params = config['select_params']
t0 = select_params['t0']
tc = select_params['tc']
k = select_params['k']
crossover = config['crossover']
mutation = config['mutation']
mutation_probability = config['probability']
implementation = config['implementation']
end_by_type = config['end_by']
params = config['params']
time = params['time']
max_gens = params['gen_number']
obj_fitness = params['fitness']
content_max_gen = params['content_gen']
percent = params['percent']
relevant = params['relevant']
A = config['A']
B = config['B']

people = []

gloves_set = set()
height_set = set()
helmet_set = set()
weapon_set = set()
chestplate_set = set()
boots_set = set()


def sigint_handler(sig, frame):
    print('Exiting')

    global fitness_plotter, diversity_plotter, best_ind_stats_plotter

    if not fitness_plotter is None:
        fitness_plotter.terminate()

    if not diversity_plotter is None:
        diversity_plotter.terminate()

    if not best_ind_stats_plotter is None:
        best_ind_stats_plotter.terminate()

    sys.exit(0)


def get_first_gen():

    for i in range(N):
        people.append(Clase(get_random_height(), generateItems())) #first gen

    random.shuffle(people)
    return people


def run_through_generations(fitness_queue, diversity_queue):
    parents = get_first_gen()   #tengo N

    if end_by_type == "time":
        gen=0
        start_time = datetime.now()
        mean_fitness = 0
        curr_fitness = 0
        if time < 0:
            print("el tiempo debe ser mayor que 0")
            exit()

        min_fitness = parents[0].performance
        for ind in parents:
            if ind.performance < min_fitness:
                min_fitness = ind.performance
            if ind.performance > curr_fitness:
                curr_fitness = ind.performance
            mean_fitness += ind.performance


        mean_fitness = mean_fitness / len(parents)

        fitness_queue.put([parents, gen, min_fitness, curr_fitness, mean_fitness])
        while ends_by_specified_time(start_time, time):
            #print("gen:", gen, "\n", parents)
            a1 = math.ceil(A*K)
            selected_parents1 = select_K_parents1(parents, a1, gen)    # elijo K padres
            a2 = K-a1
            selected_parents2 = select_K_parents2(parents, a2, gen)
            selected_parents = selected_parents1 + selected_parents2
            #print("selected parents:\n", selected_parents)

            children = do_crossover(selected_parents)       # genero K hijos

            b1 = math.ceil(B*N)
            selected_children1 = do_selection1(selected_parents, children, b1, t0, tc, k, gen)
            b2 = N-b1
            selected_children2 = do_selection2(selected_parents, children, b2, t0, tc, k, gen)
            selected = selected_children1 + selected_children2

            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion
            #print("gen++:\n", selected)
            #print("\n")
            gen += 1
            parents = selected  # los N elegidos pasan a ser los padres de la nueva generacion
            for ind in selected:
                if ind.performance < min_fitness:
                    min_fitness = ind.performance
                if ind.performance > curr_fitness:
                    curr_fitness = ind.performance
                mean_fitness += ind.performance

            mean_fitness = mean_fitness/len(selected)

            fitness_queue.put([selected, gen, min_fitness, curr_fitness, mean_fitness])     # armo una cola de generaciones

    elif end_by_type == "max_gen":
        gen = 0
        mean_fitness = 0
        curr_fitness = 0
        diversity_gloves = 0
        diversity_height = 0
        diversity_helmet = 0
        diversity_weapon = 0
        diversity_chestplate = 0
        diversity_boots = 0

        if max_gens < 0:
            print("el numero de generaciones debe ser mayor que 0")
            exit()

        min_fitness = parents[0].performance


        for ind in parents:
            if ind.performance < min_fitness:
                min_fitness = ind.performance
            if ind.performance > curr_fitness:
                curr_fitness = ind.performance
            mean_fitness += ind.performance
            items = ind.getItems()
            gloves_set.add(items[3])
            height_set.add(ind.getHeight())
            helmet_set.add(items[2])
            weapon_set.add(items[0])
            chestplate_set.add(items[4])
            boots_set.add(items[1])

        mean_fitness = mean_fitness / len(parents)
        diversity_gloves = len(gloves_set) / len(parents)
        diversity_height = len(height_set) / len(parents)
        diversity_helmet = len(helmet_set) / len(parents)
        diversity_weapon = len(weapon_set) / len(parents)
        diversity_chestplate = len(chestplate_set) / len(parents)
        diversity_boots = len(boots_set) / len(parents)

        fitness_queue.put([parents, gen, min_fitness, curr_fitness, mean_fitness])
        diversity_queue.put([parents, gen, diversity_weapon, diversity_boots, diversity_helmet, diversity_gloves,
                             diversity_chestplate, diversity_height])

        gloves_set.clear()
        helmet_set.clear()
        weapon_set.clear()
        helmet_set.clear()
        height_set.clear()
        boots_set.clear()
        chestplate_set.clear()


        while ends_by_generations(gen, max_gens):
            a1 = math.ceil(A*K)
            selected_parents1 = select_K_parents1(parents, a1, gen)    # elijo K padres
            a2 = K-a1
            selected_parents2 = select_K_parents2(parents, a2, gen)
            selected_parents = selected_parents1 + selected_parents2

            children = do_crossover(selected_parents)       # genero K hijos

            b1 = math.ceil(B*N)
            selected_children1 = do_selection1(selected_parents, children, b1, t0, tc, k, gen)
            b2 = N-b1
            selected_children2 = do_selection2(selected_parents, children, b2, t0, tc, k, gen)
            selected = selected_children1 + selected_children2

            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion

            gen += 1
            for ind in selected:
                if ind.performance < min_fitness:
                    min_fitness = ind.performance
                if ind.performance > curr_fitness:
                    curr_fitness = ind.performance
                mean_fitness += ind.performance
                items = ind.getItems()
                gloves_set.add(items[3])
                height_set.add(ind.getHeight())
                helmet_set.add(items[2])
                weapon_set.add(items[0])
                chestplate_set.add(items[4])
                boots_set.add(items[1])

            mean_fitness = mean_fitness/len(selected)
            diversity_gloves = len(gloves_set) / len(selected)
            diversity_height = len(height_set) / len(selected)
            diversity_helmet = len(helmet_set) / len(selected)
            diversity_weapon = len(weapon_set) / len(selected)
            diversity_chestplate = len(chestplate_set) / len(selected)
            diversity_boots = len(boots_set) / len(selected)

            fitness_queue.put([selected, gen, min_fitness, curr_fitness, mean_fitness])     # armo una cola de generaciones
            diversity_queue.put([selected, gen, diversity_weapon, diversity_boots, diversity_helmet, diversity_gloves,
                                 diversity_chestplate, diversity_height])
            gloves_set.clear()
            helmet_set.clear()
            weapon_set.clear()
            helmet_set.clear()
            height_set.clear()
            boots_set.clear()
            chestplate_set.clear()

    elif end_by_type == "fitness":
        gen = 0
        mean_fitness = 0
        curr_fitness = 0
        if obj_fitness < 0:
            print("el fitness objetivo debe ser mayor que 0")
            exit()

        min_fitness = parents[0].performance
        for ind in parents:
            if ind.performance < min_fitness:
                min_fitness = ind.performance
            if ind.performance > curr_fitness:
                curr_fitness = ind.performance
            mean_fitness += ind.performance

        mean_fitness = mean_fitness / len(parents)

        fitness_queue.put([parents, gen, min_fitness, curr_fitness, mean_fitness])
        while ends_by_fitness(curr_fitness, obj_fitness):
            a1 = math.ceil(A*K)
            selected_parents1 = select_K_parents1(parents, a1, gen)    # elijo K padres
            a2 = K-a1
            selected_parents2 = select_K_parents2(parents, a2, gen)
            selected_parents = selected_parents1 + selected_parents2

            children = do_crossover(selected_parents)       # genero K hijos

            b1 = math.ceil(B*N)
            selected_children1 = do_selection1(selected_parents, children, b1, t0, tc, k, gen)
            b2 = N-b1
            selected_children2 = do_selection2(selected_parents, children, b2, t0, tc, k, gen)
            selected = selected_children1 + selected_children2

            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion
            gen += 1

            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion
            for ind in selected:
                if ind.performance > curr_fitness:
                    curr_fitness = ind.performance
                if ind.performance < min_fitness:
                    min_fitness = ind.performance
                mean_fitness += ind.performance

            mean_fitness = mean_fitness/len(selected)

            fitness_queue.put([selected, gen, min_fitness, curr_fitness, mean_fitness])     # armo una cola de generaciones

    elif end_by_type == "content":
        max_previous_local_fitness = 0
        max_current_local_fitness = 0
        genIter=0
        gen = 0
        mean_fitness = 0
        curr_fitness = 0
        if content_max_gen < 1:
            print("la cantidad de generaciones debe ser mayor o igual que 1")
            exit()

        min_fitness = parents[0].performance
        for ind in parents:
            if ind.performance < min_fitness:
                min_fitness = ind.performance
            if ind.performance > curr_fitness:
                curr_fitness = ind.performance
            mean_fitness += ind.performance

        mean_fitness = mean_fitness / len(parents)

        fitness_queue.put([parents, gen, min_fitness, curr_fitness, mean_fitness])
        while ends_by_generations(genIter, content_max_gen):
            a1 = math.ceil(A*K)
            selected_parents1 = select_K_parents1(parents, a1, gen)    # elijo K padres
            a2 = K-a1
            selected_parents2 = select_K_parents2(parents, a2, gen)
            selected_parents = selected_parents1 + selected_parents2

            children = do_crossover(selected_parents)       # genero K hijos

            b1 = math.ceil(B*N)
            selected_children1 = do_selection1(selected_parents, children, b1, t0, tc, k, gen)
            b2 = N-b1
            selected_children2 = do_selection2(selected_parents, children, b2, t0, tc, k, gen)
            selected = selected_children1 + selected_children2

            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion
            gen += 1

            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion
            for ind in selected:
                if ind.performance > max_current_local_fitness:
                    max_current_local_fitness = ind.performance
                if ind.performance > curr_fitness:
                    curr_fitness = ind.performance
                if ind.performance < min_fitness:
                    min_fitness = ind.performance
                mean_fitness += ind.performance

            if max_previous_local_fitness == max_current_local_fitness:
                genIter += 1
                gen += 1
            else:
                genIter = 0
                gen += 1
            max_previous_local_fitness = max_current_local_fitness

            mean_fitness = mean_fitness/len(selected)

            fitness_queue.put([selected, gen, min_fitness, curr_fitness, mean_fitness])     # armo una cola de generaciones


    elif end_by_type == "structure":
        not_ends = True
        genIter = 0
        gen = 0
        mean_fitness = 0
        curr_fitness = 0
        #percent = numero de 0 a 1 #parametrizable
        #relevant = "best" o "worst" #parametrizable
        if percent > 1 or percent<0:
            print("genPercentage debe ser 0<percent<1")
            exit()

        min_fitness = parents[0].performance
        for ind in parents:
            if ind.performance < min_fitness:
                min_fitness = ind.performance
            if ind.performance > curr_fitness:
                curr_fitness = ind.performance
            mean_fitness += ind.performance

        mean_fitness = mean_fitness / len(parents)

        fitness_queue.put([parents, gen, min_fitness, curr_fitness, mean_fitness])
        while not_ends:
            a1 = math.ceil(A*K)
            selected_parents1 = select_K_parents1(parents, a1, gen)    # elijo K padres
            a2 = K-a1
            selected_parents2 = select_K_parents2(parents, a2, gen)
            selected_parents = selected_parents1 + selected_parents2

            children = do_crossover(selected_parents)       # genero K hijos

            b1 = math.ceil(B*N)
            selected_children1 = do_selection1(selected_parents, children, b1, t0, tc, k, gen)
            b2 = N-b1
            selected_children2 = do_selection2(selected_parents, children, b2, t0, tc, k, gen)
            selected = selected_children1 + selected_children2

            gen += 1

            if not ends_by_structure(parents, selected, relevant, percent):
                genIter = 0
                gen += 1
            elif gen < max_gens:
                genIter += 1
                gen += 1
            else:
                not_ends = False

            parents = selected

            for ind in selected:
                if ind.performance > curr_fitness:
                    curr_fitness = ind.performance
                if ind.performance < min_fitness:
                    min_fitness = ind.performance
                mean_fitness += ind.performance

            mean_fitness = mean_fitness/len(selected)

            fitness_queue.put([selected, gen, min_fitness, curr_fitness, mean_fitness])     # armo una cola de generaciones


def select_K_parents1(parents, num, gen):
    if select_method_1 == 'roulette':  # elijo K padres de los N
        selected_parents = Roulette(parents, num)
    elif select_method_1 == 'universal':
        selected_parents = Universal(parents, num)
    elif select_method_1 == 'elite':
        selected_parents = Elite(parents, num)
    elif select_method_1 == 'ranking':
        selected_parents = Ranking(parents, num)
    elif select_method_1 == 'boltzmann':
        selected_parents = Boltzmann(parents, num, t0, tc, k, gen)
    elif select_method_1 == 'det_tourney':
        selected_parents = DetTourney(parents, num)
    else:
        selected_parents = ProbTourney(parents, num)

    return selected_parents

def select_K_parents2(parents, num, gen):
    if select_method_2 == 'roulette':  # elijo K padres de los N
        selected_parents = Roulette(parents, num)
    elif select_method_2 == 'universal':
        selected_parents = Universal(parents, num)
    elif select_method_2 == 'elite':
        selected_parents = Elite(parents, num)
    elif select_method_2 == 'ranking':
        selected_parents = Ranking(parents, num)
    elif select_method_2 == 'boltzmann':
        selected_parents = Boltzmann(parents, num, t0, tc, k, gen)
    elif select_method_2 == 'det_tourney':
        selected_parents = DetTourney(parents, num)
    else:
        selected_parents = ProbTourney(parents, num)

    return selected_parents


def do_crossover(people_list):
    j = 0
    newChildren = []

    while j < K:
        if crossover == 'uniform':
            aux = Uniform(people_list[j], people_list[j+1], Clase, mutation, mutation_probability) #[hijo1, hijo2]
            newChildren.append(aux[0])
            newChildren.append(aux[1])
        elif crossover == 'point':
            aux = Point(people_list[j], people_list[j+1], Clase, mutation, mutation_probability) #[hijo1, hijo2]
            newChildren.append(aux[0])
            newChildren.append(aux[1])
        elif crossover == 'two_point':
            aux = TwoPoint(people_list[j], people_list[j+1], Clase, mutation, mutation_probability) #[hijo1, hijo2]
            newChildren.append(aux[0])
            newChildren.append(aux[1])
        else:
            aux = Anular(people_list[j], people_list[j + 1], Clase, mutation, mutation_probability)  # [hijo1, hijo2]
            newChildren.append(aux[0])
            newChildren.append(aux[1])
        for child in newChildren:
            people.append(child)
        j += 2

    return newChildren


def do_selection1(parents, newChildren, cant, t0, tc, k, gen):
    # implementations
    if implementation == 'fill_all':
        return fill_all(cant, select_method_1, parents, newChildren, t0, tc, k, gen)
    else:
        return fill_parent(cant, K, select_method_1, parents, newChildren, t0, tc, k, gen)

def do_selection2(parents, newChildren, cant, t0, tc, k, gen):
    # implementations
    if implementation == 'fill_all':
        return fill_all(cant, select_method_2, parents, newChildren, t0, tc, k, gen)
    else:
        return fill_parent(cant, K, select_method_2, parents, newChildren, t0, tc, k, gen)


if __name__ == '__main__':
    # sets SIGINT handler

    signal.signal(signal.SIGINT, sigint_handler)

    # sets process creation method
    multiprocessing.set_start_method('spawn')

    fitness_queue = multiprocessing.Queue()
    fitness_queue.cancel_join_thread()

    diversity_queue = multiprocessing.Queue()
    diversity_queue.cancel_join_thread()

    fitness_graphic = multiprocessing.Process(target=min_and_mean_fitness, args=(fitness_queue,))
    fitness_graphic.daemon = True
    fitness_graphic.start()

    fitness_graphic = multiprocessing.Process(target=diversity, args=(diversity_queue,))
    fitness_graphic.daemon = True
    fitness_graphic.start()

    run_through_generations(fitness_queue, diversity_queue)

    fitness_queue.put([])
    diversity_queue.put([])

    keyboard.wait("p")

