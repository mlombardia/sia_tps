import linecache
import random

import yaml

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
select_method = config['selection_method']
crossover = config['crossover']
mutation = config['mutation']
mutation_probability = config['probability']
implementation = config['implementation']
end_by_type = config['end_by']
params = config['params']
time = params['time']
max_gens = params['gen_number']

people = []



def get_first_gen():

    for i in range(N):
        people.append(Clase(get_random_height(), generateItems())) #first gen

    random.shuffle(people)
    return people


def run_through_generations():
    parents = get_first_gen()   #tengo N

    if end_by_type == "time":
        while ends_by_specified_time(datetime.now(), time):
            selected_parents = select_K_parents(parents)    # elijo K padres
            children = do_crossover(selected_parents)       # genero K hijos
            selected = do_selection(parents, children)      # elijo entre los N de la gen anterior y los K hijos. Tengo N elegidos
            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion
    elif end_by_type == "max_gen":
        gen = 0
        while ends_by_generations(gen, max_gens):
            print(gen)
            selected_parents = select_K_parents(parents)    # elijo K padres
            print("selected parents")
            print(selected_parents)
            print(len(selected_parents))
            print("\n")
            children = do_crossover(selected_parents)       # genero K hijos
            print("children")
            print(children)
            print(len(children))
            print("\n")
            selected = do_selection(parents, children)      # elijo entre los N de la gen anterior y los K hijos. Tengo N elegidos
            print("selected")
            print(selected)
            print(len(selected))
            print("\n")
            parents = selected                              # los N elegidos pasan a ser los padres de la nueva generacion
            gen += 1
    #elif...


def select_K_parents(parents):
    if select_method == 'roulette':  # elijo K padres de los N
        selected_parents = Roulette(parents, K)
    elif select_method == 'universal':
        selected_parents = Universal(parents, K)
    elif select_method == 'elite':
        selected_parents = Elite(parents, K)
    elif select_method == 'ranking':
        selected_parents = Ranking(parents, K)
    elif select_method == 'boltzmann':
        selected_parents = Boltzmann(parents, K, 50, 10, 2, 1)
    elif select_method == 'det_tourney':
        selected_parents = DetTourney(parents, K)
    else:
        selected_parents = ProbTourney(parents, K)

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


def do_selection(parents, newChildren):
    # implementations
    if implementation == 'fill_all':
        return fill_all(N, select_method, parents, newChildren)
    else:
        return fill_parent(N, K, select_method, parents, newChildren)


run_through_generations()

'''
if oldSize % 2 != 0:
    newChildren = Uniform(people[oldSize-1], people[0]) #[hijo1, hijo2]
    for child in newChildren:
        people.append(child)

print("intermedio:")
print(people)
print("\n")



#random.shuffle(gen2) ##people ahora es la generacion 2
print("second gen:")
print(people)
print("\n")

'''








'''
warrior1 = Warrior(get_random_height(), generateItems())
warrior2 = Warrior(get_random_height(), generateItems())

print(warrior1)
print(warrior1.performance)
print("\n")
print(warrior2)
print(warrior2.performance)
print("\n")

gen2 = Uniform(warrior1, warrior2, Warrior)
print(gen2[0])
print(gen2[0].performance)
print("\n")
print(gen2[1])
print(gen2[1].performance)
'''



