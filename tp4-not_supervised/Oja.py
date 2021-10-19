import numpy as np
import math
import random
from sklearn.preprocessing import StandardScaler

class Oja:
    def __init__(self, input_size, data_size, eta=0.0001):
        self.eta = eta
        self.weights = np.random.uniform(-1, 1, input_size)
        self.iterations_qty = 500*data_size

    def train(self, training_set, error_epsilon=0.1):
        training_set = self.standarize(training_set)
        ii = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        past_w = self.weights
        # print(training_set)
        while ii < self.iterations_qty and self.euclidean(self.weights - past_w) < error_epsilon:
            j = 0
            while j < len(shuffled_list):
                past_w = self.weights
                #OJA:
                y = np.dot(training_set[j], self.weights)
                self.weights = self.weights + self.eta * y * (training_set[j]-(y*self.weights))
                j += 1
            ii += 1

        # normalizo los pesos (converge |w|)
        norm_weights = self.weights
        norma2 = math.sqrt(sum(norm_weights * norm_weights))   # calculo la norma 2
        norm_weights = norm_weights / norma2                   # lo divido por la norma
        print(ii)
        return norm_weights

    def standarize(self, data):
        to_transform = data.loc[:, data.columns != "Country"]
        return StandardScaler().fit_transform(to_transform)

    def euclidean(self, a):
        aux = 0
        for i in range(len(a)):
            aux += (a[i])**2
        return math.sqrt(aux)

