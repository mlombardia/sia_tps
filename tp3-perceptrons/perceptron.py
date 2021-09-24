import random

import numpy as np
from activationFunctions import *


class SimplePerceptron:
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, input_size, activation_function, der_activation_function, eta=0.01):
        self.eta = eta
        self.activation_function = activation_function
        self.weights = np.array(np.random.rand(input_size + 1))
        self.der_activation_function = der_activation_function

    def predict_with_biased(self, a_input):
        dot_product = self.weights.T.dot(a_input)
        return self.activation_function(dot_product)

    def predict(self, a_input):
        return self.predict_with_biased(np.insert(a_input, 0, 1))

    def calculate_mean_square_error(self, training_set, expected_set):
        sum = 0
        for i in range(len(training_set)):
            x = training_set[i]
            y = expected_set[i]

            predicted = self.predict(x)
            aux = (predicted-y)**2
            sum += aux
        return sum / len(training_set)

    def train(self, training_set, expected_set, error_epsilon = 0, iterations_qty=1000, print_data=True):
        errors = []
        epochs = []
        training_set = np.array(training_set)
        expected_set = np.array(expected_set)
        ii = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        p = len(training_set)
        Error = 1
        min_error = 2*p
        while ii < iterations_qty and Error > error_epsilon:
            j = 0
            while j < len(shuffled_list):
                biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
                predicted_value = self.predict_with_biased(biased_input)
                error = expected_set[shuffled_list[j]] - predicted_value
                self.weights = self.weights + (self.eta * error * self.der_activation_function(self.weights.T.dot(biased_input)) * biased_input.T)
                j += 1

            Error = self.calculate_mean_square_error(training_set, expected_set)
            if Error < min_error:
                min_error = Error
            errors.append(Error)

            if print_data:
                print("Epoch: ", ii)
                print("min error", min_error)
            print("weights: ", self.weights)
            epochs.append(ii)
            ii += 1
        return min_error, epochs, errors

    def test(self, test_set, expected_test):
        return self.calculate_mean_square_error(test_set, expected_test)


class NeuronLayer:
    def __init__(self, neurons_qty, inputs_per_neuron_qty):
        self.weights = 2 * np.random.random((inputs_per_neuron_qty, neurons_qty)) - 1

# class MultilayerPerceptron:
#     def __init__(self, input_size, activation_function, der_activation_function, hidden_layers, output_layer, eta=0.01):
#         self.eta = eta
#         self.activation_function = activation_function
#         self.weights = np.array(np.random.rand(input_size + 1))
#         self.der_activation_function = der_activation_function
#         self.hidden_layers = hidden_layers
#         self.output_layer = output_layer
#
#     def predict_with_biased(self, a_input):
#         dot_product = self.weights.T.dot(a_input)
#         return self.activation_function(dot_product)
#
#     def predict(self, a_input):
#         return self.predict_with_biased(np.insert(a_input, 0, 1))
#
#     def train(self, training_set, expected_set, error_epsilon = 0, iterations_qty=1000, print_data=True):
#         errors = []
#         epochs = []
#         training_set = np.array(training_set)
#         expected_set = np.array(expected_set)
#         ii = 0
#         shuffled_list = [a for a in range(0, len(training_set))]
#         random.shuffle(shuffled_list)
#         p = len(training_set)
#         Error = 1
#         min_error = 2 * p
#         while ii < iterations_qty and Error > error_epsilon:
#             j = 0
#             # aplico a la capa 0
#             biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
#             predicted_value = self.predict_with_biased(biased_input)
#             error = expected_set[shuffled_list[j]] - predicted_value
#             self.weights = self.weights + (self.eta * error * self.der_activation_function(
#                 self.weights.T.dot(biased_input)) * biased_input.T)
#             j += 1
#             while j < len(shuffled_list):


# class MultiLayerPerceptron:
#     # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
#     # y genero random los pesos
#     def __init__(self, training_set, expected_set, activation_function, der_activation_function, hidden_layers,
#                  output_layers, iterations_qty=50000):
#         self.training_set = np.array(training_set)
#         self.expected_set = expected_set
#         self.iterations_qty = iterations_qty
#         self.activation_function = activation_function
#         self.der_activation_function = der_activation_function
#         self.hidden_layers = hidden_layers
#         self.output_layers = output_layers
#
#     def train(self):
#         for _ in range(self.iterations_qty):
#             outputs = self.guess(self.training_set)
#             errors, deltas = self.get_errors(self.expected_set, outputs)
#             adjustments = self.get_adjustments(self.training_set, deltas, outputs)
#             self.adjust_weights(adjustments)
#
#     def guess(self, inputs):
#         outputs = []
#         input=inputs
#         input = self.activation_function(np.dot(input, self.hidden_layers[0].weights))
#         outputs.append(input)
#
#         i = 1
#         # product between hidden layers
#         while i < len(self.hidden_layers):
#             input = self.activation_function(np.dot(input, self.hidden_layers[i].weights))
#             outputs.append(input)
#             i += 1
#
#         outputs.append(self.activation_function(np.dot(input, self.output_layers.weights)))
#         return outputs
#
#     def get_errors(self, expected, outputs):
#         errors = []
#         deltas = []
#
#         output_error = expected - outputs[-1]
#         output_delta = output_error * self.der_activation_function(outputs[-1])
#         errors.append(output_error)
#         deltas.append(output_delta)
#
#         previous_error = output_error
#         previous_delta = output_delta
#         previous_weights = self.output_layers.weights.T
#         current_hidden_layer = len(self.hidden_layers) - 1
#         index = len(outputs) - 2
#
#         while index >= 0:
#             previous_error = previous_delta.dot(previous_weights)
#             errors.append(previous_error)
#             previous_delta = previous_error * self.der_activation_function(outputs[index])
#             deltas.append(previous_delta)
#
#             previous_weights = self.hidden_layers[current_hidden_layer].weights.T
#             current_hidden_layer -= 1
#
#             index -= 1
#         return errors, deltas
#
#     def get_adjustments(self, training_set, deltas, outputs):
#         adjustments = []
#         adjustments.append(training_set.T.dot(deltas[-1]))
#
#         outputs_index = len(outputs) -2
#         deltas_index = len(deltas) -2
#
#         while outputs_index >= 0:
#             adjustments.append(outputs[outputs_index].T.dot(deltas[deltas_index]))
#             outputs_index -= 1
#             deltas_index -= 1
#         return adjustments
#
#     def adjust_weights(self, adjustments):
#         idx = 0
#         while idx < len(self.hidden_layers):
#             self.hidden_layers[idx].weights += adjustments[idx]
#             idx += 1

