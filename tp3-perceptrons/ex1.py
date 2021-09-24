import matplotlib.pyplot as plt
from perceptron import SimplePerceptron
from activationFunctions import *

def ex1(config):
    train_data = np.array([
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1]
        ])

    if config['gate'] == 'and':
        print("And")
        and_expected_data = np.array([-1, -1, -1, 1])

        perceptron = SimplePerceptron(train_data.shape[1], sign_act, der_sign_act)
        min_err, epochs, error_list, training_accuracies = perceptron.train(train_data, and_expected_data)

        i = 0
        while i < len(and_expected_data):
            print("input: ", train_data[i])
            print("expected: ", and_expected_data[i])
            print("guessed: ", perceptron.predict(train_data[i]))
            i += 1

        plt.plot(epochs, error_list, label='train')

        plt.xlabel('Epoch', fontsize=16)
        plt.ylabel('Mean square error', fontsize=16)
        plt.legend(title='Mean square error vs Epochs - step and')
        plt.show()

    if config['gate'] == 'xor':
        print("Xor")
        xor_expected_data = np.array([-1, 1, 1, -1])

        perceptron = SimplePerceptron(train_data.shape[1], sign_act, der_sign_act)
        min_err, epochs, error_list = perceptron.train(train_data, xor_expected_data)

        i = 0
        while i < len(xor_expected_data):
            print("input: ", train_data[i])
            print("expected: ", xor_expected_data[i])
            print("guessed: ", perceptron.predict(train_data[i]))
            i += 1

        plt.plot(epochs, error_list, label='train')

        plt.xlabel('Epoch', fontsize=16)
        plt.ylabel('Mean square error', fontsize=16)
        plt.legend(title='Mean square error vs Epochs - step xor')
        plt.show()
