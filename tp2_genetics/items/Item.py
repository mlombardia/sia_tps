import linecache
import random
from tp2_genetics.mutation import *


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
