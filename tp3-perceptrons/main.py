import os
import re
import random

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

    perceptron = SimplePerceptron(train_data.shape[1], sign_act, der_sign_act)
    perceptron.train(train_data, and_expected_data, iterations_qty=2)

    i = 0
    while(i < len(and_expected_data)):
        print("input: ", train_data[i])
        print("expected: ", and_expected_data[i])
        print("guessed: ", perceptron.predict(train_data[i]))
        i += 1


    '''
    print("Xor")
    or_expected_data = numpy.array([-1, 1, 1, -1])

    second_perceptron = SimplePerceptron(train_data, or_expected_data, sign_act, der_sign_act)
    second_perceptron.train(train_data, and_expected_data)

    i = 0
    while(i < len(or_expected_data)):
        print("input: ", train_data[i])
        print("expected: ", or_expected_data[i])
        print("guessed: ", second_perceptron.guess(train_data[i]))
        i += 1

    print(second_perceptron.guess([-1, -1]))
    '''


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


def parseNumbers(path):
    file = open(path, "r")
    lines = file.readlines()
    length = len(lines)

    numbers = []
    auxMatrix = []
    i = 0

    while i < length:
        for j in range(i, i+7):
            for k in range(9):
                if lines[i][k] == '0':
                    auxMatrix.append(0)
                if lines[i][k] == '1':
                    auxMatrix.append(1)
        numbers.append(auxMatrix)
        auxMatrix = []
        i += 7

    #for num in numbers:
    #    print(num)

    return numbers


def ex2():
    ex2_training = os.path.join(data_folder, config['ex2_training'])
    desired_training = os.path.join(data_folder, config['ex2_output'])

    training_matrix = parse_data(ex2_training)
    expected_matrix = parse_data(desired_training)

    i = 0
    max_value = numpy.max(expected_matrix)
    min_value = numpy.min(expected_matrix)
    expected_matrix_normalized = numpy.zeros(len(expected_matrix))
    while i < len(expected_matrix):
        expected_matrix_normalized[i] = (expected_matrix[i][0] - min_value) / (max_value - min_value)
        i += 1

    training_set = training_matrix[:50]
    training_set = np.array(training_set)
    training_expected = expected_matrix_normalized[:50]
    training_expected = np.array(training_expected)
    test_set = training_matrix[50:]
    test_set = np.array(test_set)
    test_expected = expected_matrix_normalized[50:]
    test_expected = np.array(test_expected)

    perceptron_lineal = SimplePerceptron(training_set.shape[1], lineal_act, der_lineal_act, eta=0.01)   # aprende poquito
    perceptron_lineal.train(training_set, training_expected)

    # perceptron_nolineal2 = SimplePerceptron(training_set.shape[1], tanh_act, der_tanh_act)
    # perceptron_nolineal2.train(training_set, training_expected)
    # perceptron_nolineal2.test(test_set, test_expected)

    '''
    plt.plot(it2, tr2, label='train')
    plt.plot(it2, t2, label='train')

    plt.xlabel('Epoch', fontsize=16)
    plt.ylabel('Accuracy', fontsize=16)
    plt.legend(title='Accuracy vs Epochs')
    plt.show()
    '''


def ex3():
    np.random.seed(1)
    subitem = config['subitem']
    if subitem == 1:
        ex3_1()
    elif subitem == 2:
        ex3_2()
    elif subitem == 3:
        ex3_3()


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
    xor_expected_data = numpy.array([[1], [1], [-1], [-1]])

    perceptron = MultiLayerPerceptron(train_data, xor_expected_data, sigmoid_act, der_sigmoid_act, [hidden_layer_1, hidden_layer_2], output_layer)
    perceptron.train()

    output = perceptron.guess(np.array([-1, 1]))
    print('[0 xor 1] is ~', output[-1])
    print('\n')

    output = perceptron.guess(np.array([-1, -1]))
    print('[0 xor 0] is ~', output[-1])
    print('\n')

    output = perceptron.guess(np.array([1, -1]))
    print('[1 xor 0] is ~', output[-1])
    print('\n')

    output = perceptron.guess(np.array([1, 1]))
    print('[1 xor 1] is ~', output[-1])
    print('\n')


def ex3_2():
    ex3_training = os.path.join(data_folder, config['ex3_training'])
    numbers = parseNumbers(ex3_training)
    q = 7   # entreno con q numeros y testeo con 10-q
    to_train = random.sample(range(10), q)
    train_data = []
    expected_data = []
    to_test = []
    test_data = []
    expected_test = []

    for i in range(q):
        train_data.append(numbers[to_train[i]])

    for i in range(10):
        if i not in to_train:
            to_test.append(i)
            test_data.append(numbers[i])

    for n in to_train:
        if n % 2 == 0:
            expected_data.append([1])
        else:
            expected_data.append([-1])

    print("to train:", to_train)
    print("train data:", train_data)
    print("expected data:", expected_data)
    print()

    hidden_layer_1 = NeuronLayer(5, 35)     # 5 neuronas y 7 inputs por cada una
    output_layer = NeuronLayer(1, 5)       # una neurona y tantos inputs como numeros para entrenar

    perceptron = MultiLayerPerceptron(train_data, expected_data, tanh_act, der_tanh_act, [hidden_layer_1], output_layer)
    perceptron.train()

    for i in range(len(train_data)):
        output = perceptron.guess(np.array(train_data[i]))
        print(to_train[i], 'is ~', output[-1])

    for n in to_test:
        if n % 2 == 0:
            expected_test.append([1])
        else:
            expected_test.append([-1])

    print()
    print("to test", to_test)
    print("test", test_data)
    print("expected test", expected_test)
    print()

    for i in range(len(test_data)):
        output = perceptron.guess(np.array(test_data[i]))
        print(to_test[i], 'is ~', output[-1])


def ex3_3():
    pass



if exercise == 1:
    ex1()
if exercise == 2:
    ex2()
if exercise == 3:
    ex3()



