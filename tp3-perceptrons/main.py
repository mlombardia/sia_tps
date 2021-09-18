import os
import re

import yaml

from perceptron import *
import numpy
import yaml
from activationFunctions import *

config_filename = 'config.yaml'

with open(config_filename) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

exercise = config['exercise']
data_folder = config['data_folder']


def ex1():
    train_data = numpy.array([
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1]
        ])

    print("And")
    and_expected_data = numpy.array([-1, -1, -1, 1])

    perceptron = StepPerceptron(train_data, and_expected_data, sign_act)
    perceptron.train()

    i = 0
    while(i < len(and_expected_data)):
        print("input: ", train_data[i])
        print("expected: ", and_expected_data[i])
        print("guessed: ", perceptron.guess(train_data[i]))
        i += 1

    print(perceptron.guess([-1,-1]))
    print()

    print("Xor")
    or_expected_data = numpy.array([-1, 1, 1, -1])

    second_perceptron = StepPerceptron(train_data, or_expected_data, sign_act)
    second_perceptron.train()

    i = 0
    while(i < len(or_expected_data)):
        print("input: ", train_data[i])
        print("expected: ", or_expected_data[i])
        print("guessed: ", second_perceptron.guess(train_data[i]))
        i += 1

    print(second_perceptron.guess([-1, -1]))



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
        if aux[len(aux)-1] == "":
            aux.pop()
        matrix.append(stringToNum(aux))
    return matrix

def stringToNum(matrix):
    aux = []
    for string in matrix:
        aux.append(float(string))
    return aux

def ex2():
    ex2_training = os.path.join(data_folder, config['ex2_training'])
    desired_training = os.path.join(data_folder, config['ex2_output'])

    training_matrix = parse_data(ex2_training)
    expected_matrix = parse_data(desired_training)

    perceptron_lineal = SimplePerceptron(training_matrix, expected_matrix, lineal_act, der_lineal_act)
    perceptron_nolineal = SimplePerceptron(training_matrix, expected_matrix, tanh_act, der_tanh_act)
    perceptron_nolineal2 = SimplePerceptron(training_matrix, expected_matrix, sigmoid_act, der_sigmoid_act)

    test = training_matrix[150:]
    expected = expected_matrix[150:]
    perceptron_lineal.train(test, expected)
    perceptron_nolineal.train(test, expected)
    perceptron_nolineal2.train(test, expected)









if exercise == 1:
    ex1()
if exercise == 2:
    ex2()