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

    min_error, errors, ii, training_accuracies, test_accuracies, min_error_test = perceptron.train(train_data, xor_expected_data, train_data, xor_expected_data, 1, iterations_qty=10000)

    plot(ii, [errors], ['errors'], 'Epoch', 'Errors', 'Mean Squared Error vs Epochs - multilayer')

    print(min_error)
    print(min_error_test)

def ex3_2(config):
    data_folder = config['data_folder']
    ex3_training = os.path.join(data_folder, config['ex3_training'])
    numbers = parseNumbers(ex3_training)
    expected = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]

    #Start Cross validations::
    k = 3

    splitsA = chunkIt(numbers, k)
    splitsE = chunkIt(expected, k)
    train_data = []
    expected_data = []

    perceptron = MultiLayerPerceptron([
        NeuronLayer(3, inputs=35, activation="sigmoid"),
        NeuronLayer(25),
        NeuronLayer(1)
    ])

    for i in range(k):
        testID = i
        test_data = splitsA[testID]
        expected_test = splitsE[testID]

        train_data = []
        expected_data = []
        for j in range(k):
            if j != testID:
                for num in splitsA[j]:
                    train_data.append(num)
                for num in splitsE[j]:
                    expected_data.append(num)

        to_test = []
        lenn = math.floor(10 / k)
        for j in range(lenn):
            to_test.append((lenn * (testID)) + j)
        if testID == k - 1:
            to_test.append((lenn * (testID)) + lenn)
        to_train = []
        for j in range(10):
            if j not in to_test:
                to_train.append(j)

        train_data = np.array(train_data)
        expected_data = np.array(expected_data)

        print("to train:", to_train)
        print("train data:", train_data)
        print("expected data:", expected_data)
        print()

        test_data = np.array(test_data)
        expected_test = np.array(expected_test)

        min_error, errors, ii, training_accuracies, test_accuracies, min_error_test = perceptron.train(train_data, expected_data, test_data, expected_test, 2)
        plot(ii, [training_accuracies, test_accuracies], ['train acc', 'test acc'], 'Epoch', 'Accuracies',
             'Accuracies vs Epochs - multilayer')
        plot(ii, [errors], ['errors'], 'Epoch', 'Errors', 'Mean Squared Error vs Epochs - multilayer')
        print("min error", min_error)
        print("min error test", min_error_test)

        A = [0, 1, 2]

        for j in range(len(to_train)):
            output = perceptron.predict(np.array(train_data[j]))
            print(to_train[j], 'is ~', to_word(output[-1]))

        print()
        print("TESTING")
        # print("to test", to_test)
        print("test", test_data)
        print("expected test", expected_test)
        print()

        for j in range(len(test_data)):
            output = perceptron.predict(np.array(test_data[j]))
            print(to_test[j], 'is ~', to_word(output[-1]))


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
        NeuronLayer(expected_data.shape[1])
    ])

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

    test_data = noise(test_data)

    min_error, errors, ii, training_accuracies, test_accuracies, min_error_test  = perceptron.train(train_data, expected_data, test_data, expected_test, 3, iterations_qty=10000)

    plot(ii, [training_accuracies, test_accuracies], ['train acc', 'test acc'], 'Epoch', 'Accuracies', 'Accuracies vs Epochs - multilayer')
    plot(ii, [errors], ['errors'], 'Epoch', 'Errors', 'Mean Squared Error vs Epochs - multilayer')
    print("training min error", min_error)
    print("testing min error", min_error_test)

    for i in range(len(train_data)):
        output = perceptron.predict(np.array(train_data[i]))
        print(to_train[i], 'is ~', to_num(output))

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

def to_word(num):
    if num > 0:
        return "par " + str(num*100) + " %"
    elif num < 0:
        return "impar " + str(num*-100) + " %"
    else:
        return "wtf this shouldn't be printed"


def noise(array):
    for letter in array:
        for i in range(len(letter)):
            rand = random.uniform(0, 1)
            if rand <= 0.02:
                if letter[i] == 0:
                    letter[i] = 1
                elif letter[i] == 1:
                    letter[i] = 0
                else:
                    exit("error adding noise")
    return array

