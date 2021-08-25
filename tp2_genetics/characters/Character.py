from tp2_genetics.items.Item import item
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

    def Performance(self):
        return (self.DEFcte * self.DEF) + (self.ATTcte * self.ATT)

    def calculateP(self):
        agilityP = 0
        strengthP = 0
        XPP = 0
        resistanceP = 0
        HPP = 0
        for item in self.itemList:
            agilityP += item.agilityI
            strengthP += item.strengthI
            XPP += item.XPI
            resistanceP += item.resistanceI
            HPP += item.HPI
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
        return 0.7 - (3*self.height - 5)**4 + (3*self.height - 5)**2 + (self.height / 4)

    def calculateDEFmod(self):
        return 1.9 + (2.5*self.height - 4.16)**4 - (2.5*self.height-4.16)**2 - ((3*self.height)/10)


