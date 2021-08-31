import linecache
import random
from items.Item import generateItems
from mutation import get_random_height
from characters.Character import Warrior
from characters.Character import Archer
from characters.Character import Tank
from characters.Character import Rogue
from Crossovers import Uniform
from selectMets import *

K = 10
Clase = Warrior
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
    newChildren = Uniform(people[j], people[j+1], Clase) #[hijo1, hijo2]
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

people = Elite(people, K)
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



