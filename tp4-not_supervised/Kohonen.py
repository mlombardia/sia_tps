import random

import numpy as np
import math

from matplotlib import pyplot as plot
from sklearn.preprocessing import StandardScaler


class Neuron:
    def __init__(self):
        self.weights = None
        self.registers = 0
        self.country = None
        self.final_registers = 0

    def init_weights(self, length):
        self.weights = np.random.uniform(low=-1, high=1, size=(length,))


class Kohonen:
    def __init__(self, k, data, neurons, radius):
        self.data_with_names = np.array(data)
        self.data = self.standarize(data)
        print(self.data_with_names)
        print()
        print(self.data)
        print()
        self.k = k
        self.iter = 50*k
        self.neurons = neurons
        self.radius = radius
        self.init_neurons(self.data.shape[1])   # misma dimension que los datos de entrada

    def init_neurons(self, length):
        for neuron_row in self.neurons:
            for neuron in neuron_row:
                neuron.init_weights(length)

    def get_neuron(self, i):
        winner = None
        row = 0
        neuron = 0
        winner_row = row
        winner_column = neuron
        min_distance = math.inf
        for row in range(len(self.neurons)):
            for neuron in range(len(self.neurons[row])):
                # uso la distancia euclidea
                distance = np.linalg.norm(self.data[i] - self.neurons[row][neuron].weights)
                if distance < min_distance:
                    min_distance = distance
                    winner = self.neurons[row][neuron]
                    winner_row = row
                    winner_column = neuron
        return winner, winner_row, winner_column

    def find_winner_neuron(self):
        winner = None
        winner_row = 0
        winner_column = 0
        ii = 0
        shuffled_list = [a for a in range(0, len(self.data))]
        random.shuffle(shuffled_list)
        initial_eta = 0.95
        while ii < self.iter:
            for i in shuffled_list:
                winner, winner_row, winner_column = self.get_neuron(i)
                self.get_and_update_neighbours(winner_row, winner_column, self.data[i], initial_eta if ii == 0 else 1/ii)
                winner.registers += 1
                if ii == self.iter-1:
                    winner.final_registers += 1
            ii += 1
        return winner, winner_row, winner_column

    def standarize(self, data):
        to_transform = data.loc[:, data.columns != "Country"]
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


    def graphic_countrys_agrupations(self):
        to_display = np.zeros((self.k, self.k))
        countries_matrix = [[[] for x in range(self.k)] for y in range(self.k)]     # matriz de listas
        countries_list = list(self.data_with_names[:, 0])

        for i in range(len(self.data)):
            neuron, row, col = self.get_neuron(i)
            countries_matrix[row][col].append(countries_list[i])
            to_display[row][col] = len(countries_matrix[row][col])

        to_display_countries_matrix = [['' for x in range(self.k)] for y in range(self.k)]

        for x in range(self.k):
            for y in range(self.k):
                string = ''
                for c in countries_matrix[x][y]:
                    string += c
                    string += '\n'
                to_display_countries_matrix[x][y] = string

        fig, axis = plot.subplots()
        axis.set_title(f'Countries per node - k={self.k}')
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
                text = axis.text(j, i, f'{(to_display_countries_matrix[i][j])}', ha="center", va="center", color=color)

        plot.colorbar(im)
        plot.show()

    def graphic_final_entries_per_node(self):
        to_display = np.zeros((self.k, self.k))
        for i in range(self.k):
            for j in range(self.k):
                to_display[i][j] = self.neurons[i][
                    j].final_registers  # le pongo cuantos registros hay en cada nodo de la matriz de neuronas

        fig, axis = plot.subplots()
        axis.set_title(f'Final registers per node - k={self.k}')
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

    def do_kohonen(self):
        winner, row, column = self.find_winner_neuron()
        print("winner weights")
        print(winner.weights)
        print("winner row", row, "winner_column", column)
        self.graphic_entries_per_node()
        self.graphic_u_matrix()
        self.graphic_countrys_agrupations()
        self.graphic_final_entries_per_node()



