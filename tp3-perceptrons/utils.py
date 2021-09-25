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
    lines = file.readlines()
    length = len(lines)

    numbers = []
    auxMatrix = []
    i = 0

    while i < length:
        for j in range(i, i + 7):
            for k in range(9):
                if lines[i][k] == '0':
                    auxMatrix.append(0)
                if lines[i][k] == '1':
                    auxMatrix.append(1)
        numbers.append(auxMatrix)
        auxMatrix = []
        i += 7

    # for num in numbers:
    #    print(num)

    return numbers


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
