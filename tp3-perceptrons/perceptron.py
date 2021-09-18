import numpy as np
from activationFunctions import *


class StepPerceptron():
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, training_set, expected_set, activation_function, error_ponderation=0.25, iterations_qty=1000):
        self.training_set = np.array(training_set)
        self.expected_set = expected_set
        self.error_ponderation = error_ponderation
        self.iterations_qty = iterations_qty
        self.weights = np.array(np.random.rand(len(training_set[0]) + 1))
        self.activation_function = activation_function

    def predict(self, a_input):
        dot_product = self.weights.T.dot(a_input)
        return self.activation_function(dot_product)

    def train(self):
        for _ in range(self.iterations_qty):
            for training_row, expected_row in zip(self.training_set, self.expected_set):
                biased_input = np.insert(training_row, 0, 1)
                predicted_value = self.predict(biased_input)
                error = expected_row - predicted_value
                self.weights = self.weights + self.error_ponderation * error * biased_input

        print("weights: ", self.weights)

    def guess(self, a_input):
        return self.predict(np.insert(a_input, 0, 1))


class SimplePerceptron:
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, training_set, expected_set, activation_function, der_activation_function, error_ponderation=0.25,
                 iterations_qty=1000):
        self.training_set = np.array(training_set)
        self.expected_set = expected_set
        self.error_ponderation = error_ponderation
        self.iterations_qty = iterations_qty
        self.activation_function = activation_function
        self.weights = np.array(np.random.rand(len(training_set[0]) + 1))
        self.der_activation_function = der_activation_function

    def predict(self, a_input):
        dot_product = self.weights.T.dot(a_input)
        return self.activation_function(dot_product)

    def calculate_square_error(self, expected_value, prediction):
        return 0.5 * ((expected_value - prediction) ** 2)

    def train(self, test_input, test_expected_values, delta=0.0001, print_data=True):
        iters = []
        training_accuracies = []
        test_accuracies = []
        for ii in range(self.iterations_qty):
            training_correct_cases = 0
            for training_row, expected_row in zip(self.training_set, self.expected_set):
                biased_input = np.insert(training_row, 0, 1)
                predicted_value = self.predict(biased_input)
                error = expected_row - predicted_value
                self.weights = self.weights + (self.error_ponderation * error * self.der_activation_function(
                    self.weights.T.dot(biased_input)) * biased_input.T)

                if abs(error) < delta:
                    training_correct_cases += 1

            training_accuracy = training_correct_cases / len(self.expected_set)
            training_accuracies.append(training_accuracy)
            test_correct_cases = 0
            i = 0
            while i < len(test_expected_values):
                if abs(test_expected_values[i] - self.guess(test_input[i])) < delta:
                    test_correct_cases += 1
                i += 1
            test_accuracy = test_correct_cases / len(test_expected_values)
            test_accuracies.append(test_accuracy)
            iters.append(ii)
            if print_data:
                print("Epoch: ", ii)
                print("Training accuracy: ", training_accuracy)
                print("Test accuracy: ", test_accuracy)
            print("weights: ", self.weights)
        return training_accuracies, test_accuracies, iters

    def guess(self, a_input):
        return self.predict(np.insert(a_input, 0, 1))
