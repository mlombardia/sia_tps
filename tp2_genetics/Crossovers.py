import random
from items import *
from characters import *
from mutation import *


def Uniform(char1, char2, Type):
    itemlist1 = []
    itemlist2 = []

    for i in range(5):
        r = random.randint(0,1)
        if r:
            itemlist1.append(char1.itemList[i])
            itemlist2.append(char2.itemList[i])
        else:
            itemlist1.append(char2.itemList[i])
            itemlist2.append(char1.itemList[i])

    r = random.randint(0, 1)
    if r:
        offspring1 = Type(char1.height, itemlist1)
        offspring2 = Type(char2.height, itemlist2)
    else:
        offspring1 = Type(char2.height, itemlist1)
        offspring2 = Type(char1.height, itemlist2)

    gen(0.5, 0, offspring1)
    gen(0.9, 5, offspring2)

    return [offspring1, offspring2]

def Point(char1, char2, Type):
    itemList1 = []
    itemList2 = []

    p = random.randint(0, 5) ##si toca 0, tiene hijos clones. Si toca 5, swappea solo el height. el resto son puntos medios
    n = 0
    while n<p:
        itemList1.append(char1.itemList[n])
        itemList2.append(char2.itemList[n])
        n += 1

    while n<5:
        itemList1.append(char2.itemList[n])
        itemList2.append(char1.itemList[n])
        n += 1

    #siempre swappea el ultimo ya que tiene que swappear desde tal punto en adelante
    offspring1 = Type(itemList1, char2.height)
    offspring2 = Type(itemList2, char1.height)
    return [offspring1, offspring2]


def TwoPoint(char1, char2, Type):
    p1 = random.randint(0, 5)
    p2 = random.randint(p1, 5)
    itemList1 = []
    itemList2 = []
    n=0
    while n<p1:
        itemList1.append(char1.itemList[n])
        itemList2.append(char2.itemList[n])
        n += 1

    while n<p2:
        itemList1.append(char2.itemList[n])
        itemList2.append(char1.itemList[n])
        n += 1

    while n<5:
        itemList1.append(char2.itemList[n])
        itemList2.append(char1.itemList[n])
        n += 1

    if p2==5: #quiso swappear el ultimo
        offspring1 = Type(itemList1, char2.height)
        offspring2 = Type(itemList2, char1.height)
    else:
        offspring1 = Type(itemList1, char1.height)
        offspring2 = Type(itemList2, char2.height)

    return [offspring1, offspring2]

def Anular(char1, char2, Type):
    p = random.randint(0,5)
    l = random.randint(0,5-p)
    itemList1 = []
    itemList2 = []
    n=0
    while n<p:
        itemList1.append(char1.itemList[n])
        itemList2.append(char2.itemList[n])
        n += 1

    for i in range(l):
        itemList1.append(char2.itemList[n])
        itemList2.append(char1.itemList[n])
        n += 1

    while n<5:
        itemList1.append(char2.itemList[n])
        itemList2.append(char1.itemList[n])
        n += 1

    if p+l==5: #quiso swappear el ultimo
        offspring1 = Type(itemList1, char2.height)
        offspring2 = Type(itemList2, char1.height)
    else:
        offspring1 = Type(itemList1, char1.height)
        offspring2 = Type(itemList2, char2.height)

    return [offspring1, offspring2]











