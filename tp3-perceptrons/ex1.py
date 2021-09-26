import matplotlib.pyplot as plt
from perceptron import StepPerceptron
from activationFunctions import *
from utils import *


def ex1(config):
    epochs = 0
    training_accuracies = []
    error_list = []
    train_data = np.array([
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1]
        ])

    if config['gate'] == 'and':
        print("And")
        and_expected_data = np.array([-1, -1, -1, 1])

        perceptron = StepPerceptron(train_data.shape[1], sign_act, der_sign_act)
        min_err, epochs, error_list, training_accuracies, mean_squared_error = perceptron.train(train_data, and_expected_data)

        i = 0
        while i < len(and_expected_data):
            print("input: ", train_data[i])
            print("expected: ", and_expected_data[i])
            print("guessed: ", perceptron.predict(train_data[i]))
            i += 1

        plot(epochs, [training_accuracies], ['train acc'], 'Epoch', 'Accuracies', 'Accuracies vs Epochs - step')
        plot(epochs, [error_list], ['error'], 'Epoch', 'Errors', 'Mean Squared Error vs Epochs - step')


    if config['gate'] == 'xor':
        print("Xor")
        xor_expected_data = np.array([-1, 1, 1, -1])

        perceptron = StepPerceptron(train_data.shape[1], sign_act, der_sign_act)
        min_err, epochs, error_list, training_accuracies, mean_squared_error = perceptron.train(train_data, xor_expected_data)

        i = 0
        while i < len(xor_expected_data):
            print("input: ", train_data[i])
            print("expected: ", xor_expected_data[i])
            print("guessed: ", perceptron.predict(train_data[i]))
            i += 1

        plot(epochs, [training_accuracies], ['train acc'], 'Epoch', 'Accuracies', 'Accuracies vs Epochs - step')
        plot(epochs, [error_list], ['error'], 'Epoch', 'Errors', 'Mean Squared Error vs Epochs - step')

