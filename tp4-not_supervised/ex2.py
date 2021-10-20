import os
import random

import numpy as np

from Hopfield import *

def parse(config):
    data_folder = config['data_folder']
    path = os.path.join(data_folder, config['letters'])
    file = open(path, 'r')
    lines = file.readlines()
    letters = []
    letter = []
    for line in lines:
        if line[0] != "-" and line[0] != "1":
            letters.append(letter)
            letter = []
        else:
            i = 0
            while i < len(line):
                if line[i] == "1":
                    letter.append(1.)
                    i += 1
                elif line[i] == "-":
                    letter.append(-1.)
                    i += 2
                else:
                    i += 1
    return letters

def reverse(letter):
    aux = []
    for c in letter:
        aux.append(c * -1)
    return aux

def printLetter(letter):
    edited = []
    if letter is False:
        return False
    for i in range(len(letter)):
        if letter[i] == -1:
            edited.append(" ")
        else:
            edited.append("*")
    for i in range(5):
        print(edited[i*5], edited[(i*5)+1], edited[(i*5)+2], edited[(i*5)+3], edited[(i*5)+4])
        # d += 1
        # if d%5 == 0:
        #     print("\n")

def noise(letter, p):
    aux = []
    for c in letter:
        num = random.uniform(0, 1)
        if p > num:
            aux.append(c * -1)
        else:
            aux.append(c)
    print("\nLetter with noise:")
    printLetter(aux)
    return aux

def eq(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def ex2(config):

    letters = parse(config)
    learn = []

    # learn.append(letters[2]) #C
    learn.append(letters[10]) #K
    learn.append(letters[20]) #U
    # learn.append(letters[23]) #X
    learn.append(letters[9]) #J
    learn.append(letters[24]) #Y
    # learn.append(letters[18]) #S
    # learn.append(letters[14]) #O
    # learn.append(letters[8]) #I

    hopfield = Hopfield(learn)


    #ACÁ PARA DIBUJAR LOS RESULTADOS
    for i in range(len(learn)):
        print("\nLetter without noise:")
        printLetter(learn[i])
        ans = hopfield.stimulus(noise(learn[i], 0.3))
        print("\nFound state:")
        print(printLetter(ans[0]))

    x = []
    hits_list = []
    miss_list = []
    spur_list = []

    #ACÁ PARA LOS DATOS DEL GRAFICO:
    for j in range(100):
        hits = 0
        miss = 0
        spur = 0
        p = j/100
        x.append(p)     # en x appendeo el ruido asi en ese eje queda el ruido
        print()
        print("Noise percentage", p)
        for i in range(len(learn)):
            # print("\nLetter without noise:")
            # printLetter(learn[i])
            ans = hopfield.stimulus(noise(learn[i], p))
            if ans[0] is False:
                miss += 1
            elif ans[1] == True:
                if eq(ans[0], learn[i]):
                    hits += 1
                else:
                    # printLetter(learn[i])
                    # printLetter(ans[0])
                    miss += 1
                hits += 1
            else:
                spur += 1
        hits_list.append(hits)
        miss_list.append(miss)
        spur_list.append(spur)
            # print("\nFound state:")
            # print(printLetter(ans[0]))
        print("i", j, " hits ", hits, ", misses ", miss, ", spur ", spur)



