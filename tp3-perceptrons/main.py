import os
import re

import yaml

from perceptron import *
import numpy as np
import yaml
from activationFunctions import *
import matplotlib.pyplot as plt

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

    i = 0
    max_value = numpy.max(expected_matrix)
    min_value = numpy.min(expected_matrix)
    expected_matrix_normalized = numpy.zeros(len(expected_matrix))
    while (i < len(expected_matrix)):
        expected_matrix_normalized[i] = (expected_matrix[i][0] - min_value) / (max_value - min_value)
        i += 1

    training_set = training_matrix[:50]
    training_expected = expected_matrix_normalized[:50]
    test_set = training_matrix[50:]
    test_expected = expected_matrix_normalized[50:]

    perceptron_lineal = SimplePerceptron(training_set, training_expected, lineal_act, der_lineal_act)
    perceptron_nolineal = SimplePerceptron(training_set, training_expected, tanh_act, der_tanh_act)
    perceptron_nolineal2 = SimplePerceptron(training_set, training_expected, sigmoid_act, der_sigmoid_act)

    perceptron_lineal.train(test_set, test_expected)
    tr1, t1, it1 = perceptron_nolineal.train(test_set, test_expected)
    tr2, t2, it2 = perceptron_nolineal2.train(test_set, test_expected)

    plt.plot(it1, tr1, label='train')
    plt.plot(it1, t1, label='train')

    plt.xlabel('Epoch', fontsize=16)
    plt.ylabel('Accuracy', fontsize=16)
    plt.legend(title='Accuracy vs Epochs')
    plt.show()

    plt.plot(it2, tr2, label='train')
    plt.plot(it2, t2, label='train')

    plt.xlabel('Epoch', fontsize=16)
    plt.ylabel('Accuracy', fontsize=16)
    plt.legend(title='Accuracy vs Epochs')
    plt.show()


def ex3():
    np.random.seed(1)
    subitem = config['subitem']
    if subitem == 1:
        ex3_1()
    elif subitem == 2:
        ex3_2()
    elif subitem == 3:
        ex3_3()
    elif subitem == 4:
        ex3_4()


def ex3_1():
    hidden_layer_1 = NeuronLayer(5, 2)
    hidden_layer_2 = NeuronLayer(5, 5)
    output_layer = NeuronLayer(1, 5)
    train_data = numpy.array([
        [-1, 1],
        [1, -1],
        [-1, -1],
        [1, 1]
    ])
    xor_expected_data = numpy.array([1, 1, -1, -1])

    perceptron = MultiLayerPerceptron(train_data, xor_expected_data, sigmoid_act, der_sigmoid_act, [hidden_layer_1, hidden_layer_2], output_layer)
    perceptron.train()

    output = perceptron.think(np.array([-1, 1]))
    print('[0 xor 1] is ~', output[-1])
    print('\n')

    output = perceptron.think(np.array([-1, -1]))
    print('[0 xor 0] is ~', output[-1])
    print('\n')

    output = perceptron.think(np.array([1, -1]))
    print('[1 xor 0] is ~', output[-1])
    print('\n')

    output = perceptron.think(np.array([1, 1]))
    print('[1 xor 1] is ~', output[-1])
    print('\n')


def ex3_2():
    pass


def ex3_3():
    pass


def ex3_4():
    pass


def main():
    if exercise == 1:
        ex1()
    if exercise == 2:
        ex2()
    if exercise == 3:
        ex3()


main()
