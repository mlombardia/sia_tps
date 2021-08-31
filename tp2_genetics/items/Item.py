import linecache
import random


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
    wrand = random.randint(2, 12)
    brand = random.randint(2, 12)
    hrand = random.randint(2, 12)
    grand = random.randint(2, 12)
    vrand = random.randint(2, 12)
    itemList = []

    arma = linecache.getline('armasTest.txt', wrand)
    weapon = Item("weapon", arma.split("\t")[0], arma.split("\t")[1], arma.split("\t")[2], arma.split("\t")[3],
                  arma.split("\t")[4], arma.split("\t")[5])
    itemList.append(weapon)

    bota = linecache.getline('botasTest', brand)
    boot = Item("boot", bota.split("\t")[0], bota.split("\t")[1], bota.split("\t")[2], bota.split("\t")[3],
                bota.split("\t")[4], bota.split("\t")[5])
    itemList.append(boot)

    casco = linecache.getline('cascosTest', hrand)
    helmet = Item("helmet", casco.split("\t")[0], casco.split("\t")[1], casco.split("\t")[2], casco.split("\t")[3],
                  casco.split("\t")[4], casco.split("\t")[5])
    itemList.append(helmet)

    guantes = linecache.getline('guantesTest', grand)
    gloves = Item("gloves", guantes.split("\t")[0], guantes.split("\t")[1], guantes.split("\t")[2],
                  guantes.split("\t")[3], guantes.split("\t")[4], guantes.split("\t")[5])
    itemList.append(gloves)

    pechera = linecache.getline('pecherasTest', vrand)
    vest = Item("vest", pechera.split("\t")[0], pechera.split("\t")[1], pechera.split("\t")[2],
                pechera.split("\t")[3], pechera.split("\t")[4], pechera.split("\t")[5])
    itemList.append(vest)

    return itemList