import os
import random

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
    for i in range(5):
        print(letter[i*5], letter[(i*5)+1], letter[(i*5)+2], letter[(i*5)+3], letter[(i*5)+4])
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
    return aux

def ex2(config):

    letters = parse(config)
    # printLetter(letters[3])
    # print(len(letters))
    print("Letra C")
    printLetter(letters[2])
    print()
    print("Letra U")
    printLetter(letters[20])
    print()
    print("Letra X")
    printLetter(letters[23])
    print()
    print("Letra Y")
    printLetter(letters[24])
    print()

    learn = []
    learn.append(letters[2]) #C
    learn.append(letters[20]) #U
    learn.append(letters[23]) #X
    learn.append(letters[24]) #Y

    hopfield = Hopfield(learn)
    # print(hopfield.weights)

    p = 0.1
    print("Noise percentage", p)

    for i in range(len(learn)):
        print("\nletter without noise being tested:")
        printLetter(learn[i])
        print(hopfield.stimulus(noise(learn[i], p)))



