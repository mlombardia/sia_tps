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
Clas = config['class']
Clase = switcher_clase[Clas]
select_method = config['selection_method']
crossover = config['crossover']
mutation = config['mutation']
mutation_probability = config['probability']


people = []


for i in range(K):
    people.append(Clase(get_random_height(), generateItems())) #first gen

print("first gen:")
print(people)
print("\n")

random.shuffle(people)

j = 0
oldSize = len(people)
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

'''
if oldSize % 2 != 0:
    newChildren = Uniform(people[oldSize-1], people[0]) #[hijo1, hijo2]
    for child in newChildren:
        people.append(child)
'''
print("intermedio:")
print(people)
print("\n")

# selection method: roulette / universal / elite / ranking / boltzmann / det_tourney / prob_tourney
if select_method == 'roulette':
    people = Roulette(people, K)
elif select_method == 'universal':
    people = Universal(people, K)
elif select_method == 'elite':
    people = Elite(people, K)
elif select_method == 'ranking':
    people = Ranking(people, K)
elif select_method == 'boltzmann':
    people = Boltzmann(people, K, 50, 10, 2, 1)
elif select_method == 'det_tourney':
    people = DetTourney(people, K)
else:
    people = ProbTourney(people, K)

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



