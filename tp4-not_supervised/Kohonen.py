import random

import numpy as np
import math

from matplotlib import pyplot as plot
from sklearn.preprocessing import StandardScaler


class Neuron:
    def __init__(self):
        self.weights = None
        self.registers = 0

    def init_weights(self, length):
        self.weights = np.random.uniform(low=-1, high=1, size=(length,))


class Kohonen:
    def __init__(self, k, data, neurons, radius):
        self.data_with_names = data
        self.data = self.standarize(data)
        self.k = k
        self.iter = 50*k
        self.neurons = neurons
        self.radius = radius
        self.init_neurons(self.data.shape[1])   # misma dimension que los datos de entrada

    def init_neurons(self, length):
        for neuron_row in self.neurons:
            for neuron in neuron_row:
                neuron.init_weights(length)

    def find_winner_neuron(self):
        ii = 0
        winner = self.neurons[0][0]
        random.shuffle(self.data)
        row = 0
        neuron = 0
        winner_row = row
        winner_column = neuron
        initial_eta = 0.95
        while ii < self.iter:
            for x_p in self.data:
                min_distance = math.inf
                # busco la neurona que tenga el vector de pesos mas cercano a x_p
                # calculo la distancia entre x_p y los pesos de las neuronas
                for row in range(len(self.neurons)):
                    for neuron in range(len(self.neurons[row])):
                        # uso la distancia euclidea
                        distance = np.linalg.norm(x_p-self.neurons[row][neuron].weights)
                        if distance < min_distance:
                            min_distance = distance
                            winner = self.neurons[row][neuron]
                            winner_row = row
                            winner_column = neuron
                self.get_and_update_neighbours(winner_row, winner_column, x_p, initial_eta if ii == 0 else 1/ii)
                winner.registers += 1
            ii += 1
        return winner, winner_row, winner_column

    def standarize(self, data):
        to_transform = data.loc[1:, data.columns != "Country"]
        return StandardScaler().fit_transform(to_transform)

    def update_neuron(self, eta, x_p, neuron):
        neuron.weights += eta * (x_p-neuron.weights)

    def get_and_update_neighbours(self, i, j, x_p, eta):
        neighbours = self.get_neighbours(i, j)
        for n in neighbours:
            self.update_neuron(eta, x_p, n[0])

    def get_neighbours(self, i, j):
        neighbours = []
        if 0 <= i-self.radius < len(self.neurons):
            bottom_limit = i-self.radius
        else:
            bottom_limit = 0
        if 0 <= i+self.radius < len(self.neurons):
            upper_limit = i + self.radius
        else:
            upper_limit = len(self.neurons)
        if 0 <= j+self.radius < len(self.neurons[0]):
            right_limit = j + self.radius
        else:
            right_limit = len(self.neurons[0])
        if 0 <= j-self.radius < len(self.neurons[0]):
            left_limit = j - self.radius
        else:
            left_limit = 0

        for m in range(bottom_limit, upper_limit):
            for n in range(left_limit, right_limit):
                dist = math.sqrt((i-m)**2+(j-n)**2)  # norma 2
                if dist <= self.radius:
                    if m != i or n != j:
                        neighbours.append((self.neurons[m][n], m, n))

        return neighbours

    def graphic_entries_per_node(self):
        to_display = np.zeros((self.k, self.k))
        for i in range(self.k):
            for j in range(self.k):
                to_display[i][j] = self.neurons[i][j].registers     # le pongo cuantos registros hay en cada nodo de la matriz de neuronas

        fig, axis = plot.subplots()
        axis.set_title(f'Registers per node - k={self.k}')
        im = plot.imshow(to_display, cmap='hot', interpolation='nearest')
        axis.set_xticks(np.arange(self.k))
        axis.set_yticks(np.arange(self.k))
        axis.set_xticklabels(range(self.k))
        axis.set_yticklabels(range(self.k))

        # Loop over data dimensions and create text annotations.
        max_val = np.amax(np.array(to_display))

        for i in range(self.k):
            for j in range(self.k):
                if to_display[i][j] > max_val / 2:
                    color = "k"
                else:
                    color = "w"
                text = axis.text(j, i, f'{int(to_display[i][j])}', ha="center", va="center", color=color)

        plot.colorbar(im)
        plot.show()

    # me base en esto https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

    def graphic_u_matrix(self): # promedio de las distancia euclidea entre los pesos del nodo y sus vecinos
        to_display = np.zeros((self.k, self.k))

        for i in range(self.k):
            for j in range(self.k):
                neighbours = self.get_neighbours(i, j)
                aux = 0.0
                if len(neighbours) != 0:
                    for n in neighbours:
                        euclidean = np.linalg.norm(self.neurons[i][j].weights-n[0].weights)
                        aux += euclidean
                    to_display[i][j] = aux/len(neighbours)  # le pongo cuantos registros hay en cada nodo de la matriz de neuronas

        fig, axis = plot.subplots()
        axis.set_title(f'U matrix - k={self.k}')
        im = plot.imshow(to_display, cmap='Greys', interpolation='nearest')
        axis.set_xticks(np.arange(self.k))
        axis.set_yticks(np.arange(self.k))
        axis.set_xticklabels(range(self.k))
        axis.set_yticklabels(range(self.k))

        # Loop over data dimensions and create text annotations.
        max_val = np.amax(np.array(to_display))

        for i in range(self.k):
            for j in range(self.k):
                if to_display[i][j] > max_val / 2:
                    color = "w"
                else:
                    color = "k"
                text = axis.text(j, i, f'{to_display[i][j]:.3f}', ha="center", va="center", color=color)

        plot.colorbar(im)
        plot.show()



