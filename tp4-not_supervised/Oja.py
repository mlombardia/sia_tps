import numpy as np
import math
import random
from sklearn.preprocessing import StandardScaler

class Oja:
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, input_size, eta=0.001):
        self.eta = eta
        self.weights = np.array(np.random.rand(input_size))
        self.iterations_qty = 50*input_size

    def train(self, training_set, error_epsilon=0.1):
        training_set = self.standarize(training_set)
        ii = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        past_w = self.weights
        # print(training_set)
        while ii < self.iterations_qty and self.euclidean(self.weights - past_w) < error_epsilon:
            j = 0
            training_correct_cases = 0
            while j < len(shuffled_list):
                past_w = self.weights
                #OJA:
                # y = np.dot(self.weights.T, np.transpose(training_set[j]).T)
                y = np.dot(training_set[j], self.weights)
                self.weights += self.eta * y * (training_set[j]-y*past_w)

                # self.weights += self.eta * (np.dot(y, np.transpose(training_set))- np.dot(y ** 2, self.weights))  # sanger y=Wtx
                # self.weights += np.dot(y, np.transpose(training_set[j]))
                # # self.weights -= np.dot(y ** 2, self.weights)
                # a = self.scalar(self.eta, y)
                # b = (np.dot(np.transpose(y), self.weights))
                # for k in range(len(self.weights)):
                #     aux1 = self.scalar(self.eta, y)
                #     aux2 = self.dot(y, training_set)
                #     aux2 = training_set - aux2
                #     arr = self.dot(aux1, aux2)
                #     self.weights[k] += arr[k]
                #LO QUE HABÍA ANTES:
                # self.weights = self.weights + (self.eta * error * self.der_activation_function(
                #     self.weights.T.dot(biased_input)) * biased_input.T)
                j += 1


            ii += 1
        print("Epoch: ", ii)
        print("weights: ", self.weights)
        return

    def standarize(self, data):
        to_transform = data.loc[:, data.columns != "Country"]
        return StandardScaler().fit_transform(to_transform)

    def euclidean(self, a):
        aux = 0
        for i in range(len(a)):
            aux += (a[i])**2
        return math.sqrt(aux)

    def dot(self, a, b):
        aux = []
        for i in range(len(a)):
            aux.append(a[i] * b[i])
        return aux

    def scalar(self, num, arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] *= num
        return arr



# class Oja:
#
#     def __init__(self, k, data, neurons, radius, eta):
#         self.data_with_names = np.array(data)
#         self.data = self.standarize(data)
#         self.k = k
#         self.iter = 50 * k
#         self.neurons = neurons
#         self.eta = 0.5
#         self.radius = radius
#         self.init_neurons(self.data.shape[1])  # misma dimension que los datos de entrada
#
#     def init_neurons(self, length):
#         for neuron_row in self.neurons:
#             for neuron in neuron_row:
#                 neuron.init_weights(length)
#
#     def get_neuron(self, i):
#         winner = None
#         winner_row = 0
#         winner_column = 0
#         ii = 0
#         shuffled_list = [a for a in range(0, len(self.data))]
#         random.shuffle(shuffled_list)
#         initial_eta = 0.5
#         while ii < self.iter:
#             for i in shuffled_list:
#
#             ii += 1
#         return winner, winner_row, winner_column