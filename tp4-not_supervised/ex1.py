import os

import pandas as pd
from Kohonen import *
from Oja import *


def ex1(config):
    data_folder = config['data_folder']
    data_csv = os.path.join(data_folder, config['ex1_training'])
    names = ["Country","Area","GDP","Inflation","Life.expect","Military","Pop.growth","Unemployment"]
    data = pd.read_csv(data_csv)
    pd.set_option("display.max_columns", 8)

    subitem = config['subitem']
    if subitem == "a":
        ex1a(data)
    elif subitem == "b":
        ex1b(data)
    else:
        print("Error")


def ex1a(data):
    k = 12
    neurons = []
    for i in range(k):
        neuron_row = []
        for j in range(k):
            neuron_row.append(Neuron())
        neuron_row = np.array(neuron_row)
        neurons.append(neuron_row)
    neurons = np.array(neurons)

    network = Kohonen(k, data, neurons, 1)
    network.do_kohonen()


def ex1b(data):
    oja = Oja(data.shape[1]-1, len(data))  # -1 por los paises
    weights = oja.train(data)
    print(weights)

