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
Class = config['class']
Clase = switcher_clase[Class]
select_method = config['selection_method']
crossover = config['crossover']
mutation = config['mutation']
mutation_probability = config['probability']
implementation = config['implementation']
end_by_type = config['end by']
params = config['params']
time = params['time']
max_gens = params['gen_number']

people = []


def get_first_gen():

    for i in range(K):
        people.append(Clase(get_random_height(), generateItems())) #first gen

    print("first gen:")
    print(people)
    print("\n")

    random.shuffle(people)
    return people

def run_through_generations():
    parents = get_first_gen()
    if end_by_type == "time":
        while ends_by_specified_time(datetime.now(), time):
            children = do_crossover()
            do_selection(parents, children)
            parents = children
    elif end_by_type == "gen":
        gen = 0
        while ends_by_generations(gen, max_gens):
            children = do_crossover()
            do_selection(parents, children)
            parents = children
            gen += 1
    #elif...

def do_crossover():
    j = 0
    oldSize = len(people)
    newChildren = []

    while j < oldSize:
        if crossover == 'uniform':
            newChildren = Uniform(people[j], people[j+1], Clase, mutation, mutation_probability) #[hijo1, hijo2]
        elif crossover == 'point':
            newChildren = Point(people[j], people[j+1], Clase, mutation, mutation_probability) #[hijo1, hijo2]
        elif crossover == 'two_point':
            newChildren = TwoPoint(people[j], people[j+1], Clase, mutation, mutation_probability) #[hijo1, hijo2]
        else:
            newChildren = Anular(people[j], people[j + 1], Clase, mutation, mutation_probability)  # [hijo1, hijo2]
        for child in newChildren:
            people.append(child)
        j += 2

    return newChildren


def do_selection(parents, newChildren):
    # implementations
    if implementation == 'fill_all':
        fill_all(K, select_method, parents, newChildren)
    else:
        fill_parent(K, select_method, parents, newChildren)

'''
if oldSize % 2 != 0:
    newChildren = Uniform(people[oldSize-1], people[0]) #[hijo1, hijo2]
    for child in newChildren:
        people.append(child)
'''
print("intermedio:")
print(people)
print("\n")



#random.shuffle(gen2) ##people ahora es la generacion 2
print("second gen:")
print(people)
print("\n")








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



