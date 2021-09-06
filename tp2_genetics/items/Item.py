import linecache
import random
#from tp2_genetics.mutation import *
# from mutation import *


class Item:
    def __init__(self, type, id, strength, agility, xp, resistance, hp):
        self.type = type #armas, botas, cascos, guantes, pecheras, son 5
        self.id = id
        self.strengthI = strength
        self.agilityI = agility
        self.XPI = xp
        self.resistanceI = resistance
        self.HPI = hp

    def __repr__(self):
        return self.type + " " + self.id


def generateItems():
    return [get_random_weapon(), get_random_boots(), get_random_helmet(), get_random_gloves(), get_random_chest_plate()]

def get_random_height():
    return random.uniform(1.3, 2)

def get_random_weapon():
    rand = random.randint(2, 1000001)
    item = linecache.getline('armas.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_boots():
    rand = random.randint(2, 1000001)
    item = linecache.getline('botas.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_helmet():
    rand = random.randint(2, 1000001)
    item = linecache.getline('cascos.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_gloves():
    rand = random.randint(2, 1000001)
    item = linecache.getline('guantes.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_chest_plate():
    rand = random.randint(2, 1000001)
    item = linecache.getline('pecheras.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem
