import os

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


def parse_data():
    pass


def ex2():
    ex2_training = os.path.join(data_folder, config['ex2_training'])
    desired_training = os.path.join(data_folder, config['ex2_output'])


if exercise == 1:
    ex1()
if exercise == 2:
    parse_data()
    ex2()