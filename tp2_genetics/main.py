import linecache
import random
from items.Item import generateItems
from characters.Character import generateHeight
from characters.Character import Warrior
from characters.Character import Archer
from characters.Character import Tank
from characters.Character import Rogue
from Crossovers import Uniform

warrior1 = Warrior(generateHeight(), generateItems())
warrior2 = Warrior(generateHeight(), generateItems())

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



