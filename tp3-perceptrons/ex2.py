import os
import matplotlib.pyplot as plt
from utils import *
from perceptron import SimplePerceptron
from activationFunctions import *

def ex2(config):
    data_folder = config['data_folder']
    ex2_training = os.path.join(data_folder, config['ex2_training'])
    desired_training = os.path.join(data_folder, config['ex2_output'])

    training_matrix = parse_data(ex2_training)
    expected_matrix = parse_data(desired_training)

    i = 0
    max_value = np.max(expected_matrix)
    min_value = np.min(expected_matrix)
    expected_matrix_normalized = np.zeros(len(expected_matrix))
    if config['perceptron_type'] == 'tanh':
        while i < len(expected_matrix):
            expected_matrix_normalized[i] = 2 * ((expected_matrix[i][0] - min_value) / (max_value - min_value)) - 1
            i += 1
    else:
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

    if config['perceptron_type'] == 'linear':
        perceptron_lineal = SimplePerceptron(training_set.shape[1], lineal_act, der_lineal_act,
                                             eta=0.01)  # aprende poquito
        min_err, epochs, error_list = perceptron_lineal.train(training_set, training_expected)
        min_err_test = perceptron_lineal.test(test_set, test_expected)
        print()
        print("training error", min_err)
        print("testing error", min_err_test)
        print()

        plt.plot(epochs, error_list, label='train')

        plt.xlabel('Epoch', fontsize=16)
        plt.ylabel('Mean square error', fontsize=16)
        plt.legend(title='Mean square error vs Epochs - linear')
        plt.show()

    elif config['perceptron_type'] == 'non_linear_tanh':
        perceptron_nolineal2 = SimplePerceptron(training_set.shape[1], tanh_act, der_tanh_act, eta=0.01)
        min_err, epochs, error_list = perceptron_nolineal2.train(training_set, training_expected)
        min_err_test = perceptron_nolineal2.test(test_set, test_expected)

        print()
        print("training error", min_err)
        print("testing error", min_err_test)
        print()

        plt.plot(epochs, error_list, label='train')

        plt.xlabel('Epoch', fontsize=16)
        plt.ylabel('Mean square error', fontsize=16)
        plt.legend(title='Mean square error vs Epochs - tanh')
        plt.show()

    elif config['perceptron_type'] == 'non_linear_sigmoid':
        perceptron_nolineal2 = SimplePerceptron(training_set.shape[1], sigmoid_act, der_sigmoid_act, eta=0.25)
        min_err, epochs, error_list = perceptron_nolineal2.train(training_set, training_expected)
        min_err_test = perceptron_nolineal2.test(test_set, test_expected)

        print()
        print("training error", min_err)
        print("testing error", min_err_test)
        print()

        plt.plot(epochs, error_list, label='train')

        plt.xlabel('Epoch', fontsize=16)
        plt.ylabel('Mean square error', fontsize=16)
        plt.legend(title='Mean square error vs Epochs - sigmoid')
        plt.show()
