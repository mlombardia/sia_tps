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
    print("HELLO")

    letters = parse(config)
    printLetter(letters[3])
    print("Goodbye")

    hopfield = Hopfield(letters)
    print(hopfield.weights)

    for i in range(len(letters)):
        print("\nletter without noise being tested:")
        printLetter(letters[i])
        print(hopfield.stimulus(noise(letters[i], 0.1)))



