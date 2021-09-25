import os

import numpy as np

from perceptron import *
from activationFunctions import *
from utils import *
import random

def ex3(config):
    np.random.seed(1)
    subitem = config['subitem']
    if subitem == 1:
        ex3_1()
    elif subitem == 2:
        ex3_2(config)
    elif subitem == 3:
        ex3_3(config)


def ex3_1():
    train_data = np.array([
        [-1, 1],
        [1, -1],
        [-1, -1],
        [1, 1]
    ])
    xor_expected_data = np.array([[1], [1], [-1], [-1]])

    perceptron = MultiLayerPerceptron([
        NeuronLayer(3, inputs=train_data.shape[1], activation="linear"),
        NeuronLayer(5),
        NeuronLayer(xor_expected_data.shape[1])
    ])

    min_error, errors, ii = perceptron.train(train_data, xor_expected_data, iterations_qty=10000)

    print(min_error)


def ex3_2(config):
    data_folder = config['data_folder']
    ex3_training = os.path.join(data_folder, config['ex3_training'])
    numbers = parseNumbers(ex3_training)
    q = 7  # entreno con q numeros y testeo con 10-q
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

    train_data=np.array(train_data)
    expected_data = np.array(expected_data)

    print("to train:", to_train)
    print("train data:", train_data)
    print("expected data:", expected_data)
    print()

    perceptron = MultiLayerPerceptron([
        NeuronLayer(3, inputs=train_data.shape[1], activation="linear"),
        NeuronLayer(5),
        NeuronLayer(expected_data.shape[1])
    ])

    min_error, errors, ii = perceptron.train(train_data, expected_data)

    print("min error", min_error)

    for i in range(len(train_data)):
        output = perceptron.predict(np.array(train_data[i]))
        print(to_train[i], 'is ~', output[-1])

    for n in to_test:
        if n % 2 == 0:
            expected_test.append([1])
        else:
            expected_test.append([-1])

    test_data = np.array(test_data)
    expected_test = np.array(expected_test)

    print()
    print("TESTING")
    print("to test", to_test)
    print("test", test_data)
    print("expected test", expected_test)
    print()

    for i in range(len(test_data)):
        output = perceptron.predict(np.array(test_data[i]))
        print(to_test[i], 'is ~', output[-1])


def ex3_3(config):
    data_folder = config['data_folder']
    ex3_training = os.path.join(data_folder, config['ex3_training'])
    numbers = parseNumbers(ex3_training)
    q = 7  # entreno con q numeros y testeo con 10-q
    to_train = [] #random.sample(range(10), q)
    train_data = []
    expected_data = []
    to_test = []
    test_data = []
    expected_test = []

    for i in range(10):
        to_train.append(i)
        train_data.append(numbers[to_train[i]])
        to_test.append(i)
        test_data.append(numbers[i])


    # for i in range(10):
    #     if i not in to_train:
    #         to_test.append(i)
    #         test_data.append(numbers[i])

    for n in to_train:
        if n == 0:
            expected_data.append([1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
        elif n == 1:
            expected_data.append([-1, 1, -1, -1, -1, -1, -1, -1, -1, -1])
        elif n == 2:
            expected_data.append([-1, -1, 1, -1, -1, -1, -1, -1, -1, -1])
        elif n == 3:
            expected_data.append([-1, -1, -1, 1, -1, -1, -1, -1, -1, -1])
        elif n == 4:
            expected_data.append([-1, -1, -1, -1, 1, -1, -1, -1, -1, -1])
        elif n == 5:
            expected_data.append([-1, -1, -1, -1, -1, 1, -1, -1, -1, -1])
        elif n == 6:
            expected_data.append([-1, -1, -1, -1, -1, -1, 1, -1, -1, -1])
        elif n == 7:
            expected_data.append([-1, -1, -1, -1, -1, -1, -1, 1, -1, -1])
        elif n == 8:
            expected_data.append([-1, -1, -1, -1, -1, -1, -1, -1, 1, -1])
        elif n == 9:
            expected_data.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, 1])
        else:
            exit("error else ej 3")

    print("to train:", to_train)
    print("train data:", train_data)
    print("expected data:", expected_data)
    print()

    train_data = np.array(train_data)
    expected_data = np.array(expected_data)

    perceptron = MultiLayerPerceptron([
        NeuronLayer(3, inputs=train_data.shape[1], activation="sigmoid"),
        NeuronLayer(50),
        NeuronLayer(50),
        NeuronLayer(50),
        NeuronLayer(expected_data.shape[1])
    ], eta=0.01)

    min_error, errors, ii = perceptron.train(train_data, expected_data, iterations_qty=10000)

    print(min_error)

    for i in range(len(train_data)):
        output = perceptron.predict(np.array(train_data[i]))
        print(to_train[i], 'is ~', to_num(output))

    for n in to_test:
        if n == 0:
            expected_test.append([1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
        elif n == 1:
            expected_test.append([-1, 1, -1, -1, -1, -1, -1, -1, -1, -1])
        elif n == 2:
            expected_test.append([-1, -1, 1, -1, -1, -1, -1, -1, -1, -1])
        elif n == 3:
            expected_test.append([-1, -1, -1, 1, -1, -1, -1, -1, -1, -1])
        elif n == 4:
            expected_test.append([-1, -1, -1, -1, 1, -1, -1, -1, -1, -1])
        elif n == 5:
            expected_test.append([-1, -1, -1, -1, -1, 1, -1, -1, -1, -1])
        elif n == 6:
            expected_test.append([-1, -1, -1, -1, -1, -1, 1, -1, -1, -1])
        elif n == 7:
            expected_test.append([-1, -1, -1, -1, -1, -1, -1, 1, -1, -1])
        elif n == 8:
            expected_test.append([-1, -1, -1, -1, -1, -1, -1, -1, 1, -1])
        elif n == 9:
            expected_test.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, 1])
        else:
            exit("error else ej 3")

    print()
    print("to test", to_test)
    print("test", test_data)
    print("expected test", expected_test)
    print()

    for i in range(len(test_data)):
        output = perceptron.predict(np.array(test_data[i]))

        print(to_test[i], 'is ~', to_num(output))

def to_num(array):
    aux = -math.inf
    num = 0
    for i in range(len(array)):
        if array[i] > aux:
            aux = array[i]
            num = i
    return num

def noise(array):
    for i in range(len(array)):
        rand = random.uniform(0, 1)
        if rand <= 0.02:
            if array[i] == 0:
                array[i] = 1
            elif array[i] == 1:
                array[i] = 0
            else:
                exit("error adding noise")
    return array
