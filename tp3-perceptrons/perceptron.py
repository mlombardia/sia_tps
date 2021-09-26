import random

import numpy as np

from activationFunctions import *


class SimplePerceptron:
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, input_size, activation_function, der_activation_function, eta=0.001, delta=0.0049, iterations_qty=1000):
        self.eta = eta
        self.activation_function = activation_function
        self.weights = np.array(np.random.rand(input_size + 1))
        self.der_activation_function = der_activation_function
        self.delta = delta
        self.iterations_qty = iterations_qty


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
            aux = (predicted - y) ** 2
            sum += aux
        return sum / len(training_set)

    def calculate_local_accuracies(self, test_set, expected_set):
        j = 0
        test_correct_cases = 0
        while j < len(test_set):
            error = expected_set[j] - self.predict(test_set[j])
            if error < self.delta:
                test_correct_cases += 1
            j += 1

        return test_correct_cases/len(test_set)

    def train(self, training_set, expected_set, test_set, test_expected_test, error_epsilon=0, print_data=True):
        errors = []
        epochs = []
        training_accuracies = []
        training_set = np.array(training_set)
        expected_set = np.array(expected_set)
        ii = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        p = len(training_set)
        Error = 1
        min_error = 2 * p
        mean_square_error = 0
        test_accuracies = []
        while ii < self.iterations_qty and Error > error_epsilon:
            j = 0
            training_correct_cases = 0
            while j < len(shuffled_list):
                biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
                predicted_value = self.predict_with_biased(biased_input)
                error = expected_set[shuffled_list[j]] - predicted_value
                if error < self.delta:
                    training_correct_cases += 1
                self.weights = self.weights + (self.eta * error * self.der_activation_function(
                    self.weights.T.dot(biased_input)) * biased_input.T)
                j += 1

            Error = self.calculate_mean_square_error(training_set, expected_set)
            if Error < min_error:
                min_error = Error
            errors.append(Error)
            training_accuracies.append(training_correct_cases / len(training_set))
            if print_data:
                print("Epoch: ", ii)
                print("min error", min_error)
            print("weights: ", self.weights)

            mean_square_error = self.calculate_mean_square_error(test_set, test_expected_test)
            test_accuracies.append(self.calculate_local_accuracies(test_set, test_expected_test))
            epochs.append(ii)
            ii += 1
        return min_error, epochs, errors, training_accuracies, mean_square_error, test_accuracies

    def test(self, test_set, expected_test):
        mean_square_error = self.calculate_mean_square_error(test_set, expected_test)
        accuracies = self.calculate_local_accuracies(test_set, expected_test)
        return mean_square_error, accuracies


class NeuronLayer:  # es una matriz
    def __init__(self, neurons_qty, inputs=None, activation="tanh"):
        self.neurons_qty = neurons_qty
        self.inputs = inputs
        (f, df) = self.get_functions(activation)
        self.f = f
        self.df = df
        self.weights = None
        self.h = None
        self.v = None

    def init_weights(self, inputs=None):
        self.inputs = inputs if inputs is not None else self.inputs
        self.weights = 2 * np.random.random((self.neurons_qty, self.inputs+1)) - 1  # esto ES una matriz

    def get_functions(self, activation_function):
        if activation_function == "tanh":
            f = tanh_act
            df = der_tanh_act
        elif activation_function == "sigmoid":
            f = sigmoid_act
            df = der_sigmoid_act
        elif activation_function == "linear":
            f = lineal_act
            df = der_lineal_act
        else:
            raise LookupError("falta funcion")
        return f, df

    def forward(self, a_input):
        # [w1 w2 B] . [i0, i1, i2] = k

        # [w1, w2, B] x [i0     = [k]
        #                i1
        #                i2]

        #         [B1, w11, w12] x [i0     = [o1    # salida de la primera neurona
        #         [B2, w21, w22]    i1        o2]   # salida de la segunda neurona
        #                           i2]
        a_input_biased = np.insert(a_input, 0, 1)
        output = np.matmul(self.weights, np.transpose(a_input_biased))  # h
        output = np.transpose(output)
        self.h = output
        output = self.f(output)
        self.v = output
        return output

    def back_propagate(self, dif, v, eta):
        v = np.insert(v, 0, 1)
        delta = np.multiply(self.df(self.h), dif)
        aux = v.reshape((-1,1))
        d_w = eta*v.reshape((-1,1))*delta
        self.weights = self.weights + np.transpose(d_w)
        return delta


class MultiLayerPerceptron:
    def __init__(self, neuron_layers, eta=0.01):
        self.eta = eta
        self.neuron_layers = neuron_layers
        self._init_layers()

    def _init_layers(self):
        for i in range(len(self.neuron_layers)):
            if i != 0:  # la capa 0 no depende de nadie, depende de los inputs
                self.neuron_layers[i].init_weights(inputs=self.neuron_layers[
                    i - 1].neurons_qty)  # se fija cuantas salidas tiene la capa anterior y se lo pone a esta nueva capa
            else:
                self.neuron_layers[i].init_weights()  # no le paso nada porque ya lo tenia

    def predict(self, a_input):
        res = a_input
        for i in range(len(self.neuron_layers)):
            res = self.neuron_layers[i].forward(res)
        return res

    def calculate_mean_square_error(self, training_set, expected_set):
        sum = 0
        for i in range(len(training_set)):
            x = training_set[i]
            y = expected_set[i]

            predicted = self.predict(x)
            aux = np.linalg.norm(predicted - y, ord=2) ** 2
            sum += aux
        return sum / len(training_set)

    def back_propagate(self, predicted, x, y):
        delta = None
        for i in reversed(range(len(self.neuron_layers))):
            if i == 0:
                v = x
            else:
                v = self.neuron_layers[i-1].v
            if i != len(self.neuron_layers)-1:
                dif = np.matmul(np.transpose(self.neuron_layers[i+1].weights[:, 1:]), np.transpose(delta))
                dif = np.transpose(dif)
                # dif = [0 for n in range(self.neuron_layers[i].neurons_qty)]
                # for n in range(self.neuron_layers[i].neurons_qty):
                #     d = 0
                #     w = self.neuron_layers[i+1].weights[:, n+1]
                #     d = np.dot(w, delta)
                #     dif[n] = d
                #     # for j in range(self.neuron_layers[i+1].neurons_qty):
                #     #     w_jn = self.neuron_layers[i+1].weights[j, n+1]
                #     #     aux2 = w_jn * delta[j]
                #     #     dif[n] += aux2    #todas las filas y la columna n+1 porque la 0 es el biased para la neurona n
                dif = np.array(dif)
            else:
                dif = y - predicted

            delta = self.neuron_layers[i].back_propagate(dif, v, self.eta)


    def train(self, training_set, expected_set, error_epsilon=0, iterations_qty=1000, print_data=True):
        training_set = np.array(training_set)
        expected_set = np.array(expected_set)
        ii = 0
        i = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        p = len(training_set)
        Error = 1
        min_error = 2 * p
        errors = []
        while ii < iterations_qty and Error > error_epsilon:
            j = 0
            while j < len(training_set):
                x = training_set[shuffled_list[j]]
                y = expected_set[shuffled_list[j]]

                predicted_value = self.predict(x)  # forward propagation

                self.back_propagate(predicted_value, x, y)
                j += 1

            Error = self.calculate_mean_square_error(training_set, expected_set)
            if Error < min_error:
                min_error = Error
            errors.append(Error)
            ii += 1
        return min_error, errors, ii

    def test(self, test_set, expected_test):
        return self.calculate_mean_square_error(test_set, expected_test)


