import random

from tp2_genetics.items.Item import Item
import math

class Character:
    def __init__(self):
        self.DEFcte = None
        self.ATTcte = None
        self.DEF = None
        self.ATT = None
        self.height = None
        self.itemList = []
        self.ATTmod = None
        self.DEFmod = None
        self.performance = None


    def __repr__(self):
        aux = ""
        for i in range(5):
            aux+=str(self.itemList[i])
            aux+="; "
        return str(self.performance)
        #return aux + " height:" + str(self.height)

    def calculatePerformance(self):
        perf = (self.DEFcte * self.DEF) + (self.ATTcte * self.ATT)
        self.performance = perf
        return perf  #fitness

    def calculateItemsP(self):
        agilityP = 0
        strengthP = 0
        XPP = 0
        resistanceP = 0
        HPP = 0
        for item in self.itemList:
            agilityP += float(item.agilityI)
            strengthP += float(item.strengthI)
            XPP += float(item.XPI)
            resistanceP += float(item.resistanceI)
            HPP += float(item.HPI)
        agilityP *= 0.01
        strengthP *= 0.01
        XPP *= 0.01
        resistanceP *= 0.01
        HPP *= 0.01

        agilityP = math.tanh(agilityP)
        strengthP = math.tanh(strengthP)
        XPP = math.tanh(XPP)
        resistanceP = math.tanh(resistanceP)
        HPP = math.tanh(HPP)

        strengthP *= 100
        XPP *= 0.6
        HPP *= 100
        #listo todos los Ps calculados

        self.ATT = (agilityP + XPP) * strengthP * self.calculateATTmod()
        self.DEF = (resistanceP + XPP) * HPP * self.calculateDEFmod()


    def calculateATTmod(self):
        aux = 0.7 - (3*self.height - 5)**4 + (3*self.height - 5)**2 + (self.height / 4)
        self.ATTmod = aux
        return aux

    def calculateDEFmod(self):
        aux = 1.9 + (2.5*self.height - 4.16)**4 - (2.5*self.height-4.16)**2 - ((3*self.height)/10)
        self.DEFmod = aux
        return aux

    def getHeight(self):
        return self.height

    def getItems(self):
        return self.itemList


##  subclases:

class Warrior(Character):
    def __init__(self, height, items):
        super().__init__()
        self.height = height
        self.itemList = items
        self.DEFcte = 0.6
        self.ATTcte = 0.6

        self.calculateItemsP()
        self.calculatePerformance()

class Tank(Character):
    def __init__(self, height, items):
        super().__init__()
        self.height = height
        self.itemList = items
        self.DEFcte = 0.8
        self.ATTcte = 0.3


        self.calculateItemsP()
        self.calculatePerformance()

class Rogue(Character):
    def __init__(self, height, items):
        super().__init__()
        self.height = height
        self.itemList = items
        self.DEFcte = 0.3
        self.ATTcte = 0.8


        self.calculateItemsP()
        self.calculatePerformance()

class Archer(Character):
    def __init__(self, height, items):
        super().__init__()
        self.height = height
        self.itemList = items
        self.DEFcte = 0.1
        self.ATTcte = 0.9


        self.calculateItemsP()
        self.calculatePerformance()

