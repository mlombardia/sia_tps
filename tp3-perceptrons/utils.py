import math
import random
import re
import matplotlib.pyplot as plt
import numpy as np


def parse_data(path):
    file = open(path, "r")
    lines = file.readlines()

    matrix = []
    count = 0
    for line in lines:
        count += 1
        aux = re.split("\s+", line)
        if aux[0] == "":
            aux.pop(0)
        if aux[len(aux) - 1] == "":
            aux.pop()
        matrix.append(stringToNum(aux))
    return matrix


def stringToNum(matrix):
    aux = []
    for string in matrix:
        aux.append(float(string))
    return aux


def parseNumbers(path):
    file = open(path, "r")
    lines = file.read()
    length = len(lines)
    numbers = []
    auxMatrix = []
    i = 0
    line = 0
    print("length", length)

    #print(lines)

    while i < length:
        if lines[i] == "0":
            auxMatrix.append(0)
        elif lines[i] == "1":
            auxMatrix.append(1)
        elif lines[i] == "\n":
            if line == 6:
                line = 0
                numbers.append(auxMatrix)
                auxMatrix = []
            else:
                line += 1
        else: #es un " "
            pass
        i += 1
    return numbers

    #
    #
    # while i < length: #70 lineas
    #     for j in range(i, i + 6): #las primeras 7 lineas
    #         for k in range(5): #en una línea
    #             if lines[j][k] == '0':
    #                 auxMatrix.append(0)
    #             elif lines[j][k] == '1':
    #                 auxMatrix.append(1)
    #     numbers.append(auxMatrix)
    #     auxMatrix = []
    #     i += 7

    # for num in numbers:
    #    print(num)

    #return numbers


def plot(x_info, y_info, line_label, xlabel, ylabel, legend):
    plt.plot(x_info, y_info, label=line_label)

    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.legend(title=legend)
    plt.show()

def cross_validations(array, expected, K):
    splitsA = np.array_split(array, K)
    splitsE = np.array_split(expected, K)
    testId = random.randint(0, K-1)
    test = splitsA[testId]
    testExp = splitsE[testId]

    train = np.empty(K-1)
    trainExp = np.empty(K-1)
    for i in range(K-1):
        if i != testId:
            for num in splitsA[i]:
                np.append(train, num)
            for num in splitsE[i]:
                np.append(trainExp, num)

#toma todos los datos, los divide en k partes, devuelve k-1 como training y 1 como test
#devuelve np.arrays
    return train, trainExp, test, testExp
