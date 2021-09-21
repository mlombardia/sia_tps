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

    def train(self, test_input, test_expected_values, delta=0.001, print_data=True):
        iters = []
        training_accuracies = []
        test_accuracies = []
        for ii in range(self.iterations_qty):
            training_correct_cases = 0
            for training_row, expected_row in zip(self.training_set, self.expected_set):
                biased_input = np.insert(training_row, 0, 1)
                predicted_value = self.predict(biased_input)
                error = expected_row - predicted_value
                if abs(error) < delta:
                    training_correct_cases += 1
                self.weights = self.weights + (self.error_ponderation * error * self.der_activation_function(
                    self.weights.T.dot(biased_input)) * biased_input.T)

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


class NeuronLayer:
    def __init__(self, neurons_qty, inputs_per_neuron_qty):
        self.weights = 2 * np.random.random((inputs_per_neuron_qty, neurons_qty)) - 1


class MultiLayerPerceptron:
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, training_set, expected_set, activation_function, der_activation_function, hidden_layers,
                 output_layers, iterations_qty=1000):
        self.training_set = np.array(training_set)
        self.expected_set = expected_set
        self.iterations_qty = iterations_qty
        self.activation_function = activation_function
        self.der_activation_function = der_activation_function
        self.hidden_layers = hidden_layers
        self.output_layers = output_layers

    def train(self):
        for _ in range(self.iterations_qty):
            outputs = self.think(self.training_set)
            errors, deltas = self.get_errors(self.expected_set, outputs)
            adjustments = self.get_adjustments(self.training_set, deltas, outputs)
            self.adjust_weights(adjustments)

    def think(self, inputs):
        outputs = []
        input=inputs
        input = self.activation_function(np.dot(input, self.hidden_layers[0].weights))
        outputs.append(input)

        i = 1
        # product between hidden layers
        while i < len(self.hidden_layers):
            input = self.activation_function(np.dot(input, self.hidden_layers[i].weights))
            outputs.append(input)
            i += 1

        outputs.append(self.activation_function(np.dot(input, self.output_layers.weights)))
        return outputs

    def get_errors(self, expected, outputs):
        errors = []
        deltas = []

        output_error = expected - outputs[-1]
        output_delta = output_error * self.der_activation_function(outputs[-1])
        errors.append(output_error)
        deltas.append(output_delta)

        previous_error = output_error
        previous_delta = output_delta
        previous_weights = self.output_layers.weights.T
        current_hidden_layer = len(self.hidden_layers) - 1
        index = len(outputs) - 2

        while index >= 0:
            previous_error = previous_delta.dot(previous_weights)
            errors.append(previous_error)
            previous_delta = previous_error * self.der_activation_function(outputs[index])
            deltas.append(previous_delta)

            previous_weights = self.hidden_layers[current_hidden_layer].weights.T
            current_hidden_layer -= 1

            index -= 1
        return errors, deltas

    def get_adjustments(self, training_set, deltas, outputs):
        adjustments = []
        adjustments.append(training_set.T.dot(deltas[-1]))

        outputs_index = len(outputs) -2
        deltas_index = len(deltas) -2

        while outputs_index >= 0:
            adjustments.append(outputs[outputs_index].T.dot(deltas[deltas_index]))
            outputs_index -= 1
            deltas_index -= 1
        return adjustments

    def adjust_weights(self, adjustments):
        idx = 0
        while idx < len(self.hidden_layers):
            self.hidden_layers[idx].weights += adjustments[idx]
            idx += 1

