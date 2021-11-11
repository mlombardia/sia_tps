import math

import numpy as np
import random
from activationFunctions import *


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
        self.momentum = False
        self.alpha = None
        self.last_dw = 0

    def init_weights(self, inputs=None):
        self.inputs = inputs if inputs is not None else self.inputs
        # print()
        # if inputs is None:
        #     print("inputs + 1 = ", self.inputs + 1)
        # else:
        #     print("inputs + 1 = ", inputs + 1)
        # print("neurons qty = ", self.neurons_qty)
        self.weights = 2 * np.random.random((self.neurons_qty, self.inputs + 1)) - 1
        # weights es una matriz de neurons_qty x inputs+1
        # es inputs+1 por el biased
        # los numeros de los inputs entre -1 y 1
        # print(self.weights)

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
        aux = v.reshape((-1, 1))
        d_w = eta * v.reshape((-1, 1)) * delta
        if self.momentum:
            self.weights = np.transpose(d_w) + self.weights + (self.alpha * np.transpose(self.last_dw))
        else:
            self.weights = self.weights + np.transpose(d_w)
        self.last_dw = d_w
        return delta


class MultiLayerPerceptron:
    def __init__(self, neuron_layers, eta=0.001, delta=0.049, init_layers=True, momentum = False):
        self.momentum_number = 0.8
        self.alpha = 0.0001
        self.beta = 0.0001
        self.eta = eta
        self.delta = delta
        self.neuron_layers = neuron_layers
        self.momentum = momentum
        self.k = 9
        if init_layers:
            self._init_layers()

    def _init_layers(self):
        for i in range(len(self.neuron_layers)):
            if i != 0:  # las capas que no son la 0
                self.neuron_layers[i].init_weights(inputs=self.neuron_layers[
                    i - 1].neurons_qty)  # se fija cuantas salidas (neuronas) tiene la capa anterior y se lo pone a esta nueva capa
            else:
                self.neuron_layers[i].init_weights()  # no le paso nada porque ya lo tenia del main
            self.neuron_layers[i].momentum = self.momentum
            self.neuron_layers[i].alpha = self.momentum_number

    def predict(self, a_input):
        res = a_input
        for i in range(len(self.neuron_layers)):
            res = self.neuron_layers[i].forward(res)
        return res

    def calculate_mean_square_error(self, training_set, expected_set):
        su = 0
        for i in range(len(training_set)):
            x = training_set[i]
            y = expected_set[i]

            predicted = self.predict(x)
            aux = np.linalg.norm(predicted - y, ord=2) ** 2
            su += aux
        return su / len(training_set)

    def back_propagate(self, predicted, x, y):
        delta = None
        for i in reversed(range(len(self.neuron_layers))):
            if i == 0:
                v = x
            else:
                v = self.neuron_layers[i - 1].v
            if i != len(self.neuron_layers) - 1:
                dif = np.matmul(np.transpose(self.neuron_layers[i + 1].weights[:, 1:]), np.transpose(delta))
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
        return delta

    def train(self, training_set, expected_set, error_epsilon=0, iterations_qty=10000, adaptative_eta=False):
        training_set = np.array(training_set)
        expected_set = np.array(expected_set)
        ii = 0
        i = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        p = len(training_set)
        Error = 1
        min_error = float("inf")
        errors = []
        training_accuracies = []
        epochs = []
        training_correct_cases = 0
        mean_square_error = 0
        eta_iteration = 0
        while ii < iterations_qty and Error > error_epsilon:
            j = 0
            training_correct_cases = 0
            while j < len(training_set):
                x = training_set[shuffled_list[j]]
                y = expected_set[shuffled_list[j]]

                predicted_value = self.predict(x)  # forward propagation

                error = self.back_propagate(predicted_value, x, y)
                aux_training = 0

                for i in range(len(error)):
                    if error[i] < self.delta:
                        aux_training += 1
                if aux_training == len(error):
                    training_correct_cases += 1

                j += 1
            training_accuracies.append(training_correct_cases / len(training_set))
            Error = self.calculate_mean_square_error(training_set, expected_set)

            if adaptative_eta and len(errors) > 1:
                #print(eta_iteration)
                if (Error - errors[-1]) < 0:
                    if eta_iteration <= 0:
                        eta_iteration -= 1
                    else:
                        eta_iteration = 0
                elif (Error - errors[-1]) > 0:
                    if eta_iteration >= 0:
                        eta_iteration += 1
                    else:
                        eta_iteration = 0

                if eta_iteration < -self.k: # and (errors[-1] - errors[-2]) < 0:
                    if self.eta + self.alpha * self.eta < math.inf: #MAX
                        self.eta += self.alpha
                elif eta_iteration > self.k:
                    if self.eta - self.beta * self.eta > -math.inf: #MIN
                        self.eta -= self.beta * self.eta
                #print(self.eta)

            if Error < min_error:
                min_error = Error
            errors.append(Error)

            epochs.append(ii)
            ii += 1

        return min_error, errors, epochs, training_accuracies
