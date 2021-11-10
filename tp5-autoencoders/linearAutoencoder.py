from multilayerPerceptron import *
from font_utils import *
import numpy as np


x = np.array(get_input(2))
x = [x[6]]
x = np.array(x)


print(x)

x_mean = np.mean(x, axis=0) # normalizacion de datos
x_std = np.std(x, axis=0)   # normalizacion de datos

# printFont(x[4])

def transform(t):
    return t/255

def detransform(t):
    to_detransform = np.rint(t*255)
    for i in range(len(to_detransform)):
        if to_detransform[i] > 255:
            to_detransform[i] = 255
        if to_detransform[i] < 0:
            to_detransform[i] = 0
    return to_detransform

x = transform(x)

layers = [
    # "capa" inicial que son los valores
    NeuronLayer(30, 7, activation="tanh"),
    NeuronLayer(10, activation="tanh"),
    NeuronLayer(5, activation="tanh"), #latent code Z
    NeuronLayer(10, activation="tanh"),
    NeuronLayer(30, activation="tanh"),
    NeuronLayer(7, activation="tanh")
]

encoderDecoder = MultiLayerPerceptron(layers, init_layers=True, momentum=True, eta=0.05)

min_error, errors, epochs, training_accuracies = encoderDecoder.train(x, x, iterations_qty=10000, adaptative_eta=False)
print(min_error)

encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0:int(len(layers)/2)], init_layers=False)     # desde el inicio hasta el medio

decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[int(len(layers)/2):], init_layers=False)    # las ultimas capas


for i in range(len(x)):
    to_predict = x[i, :]
    encoded = encoder.predict(to_predict)
    decoded = decoder.predict(encoded)
    print(f"{detransform(to_predict)} -> {encoded} -> {detransform(decoded)}" )
    printFont(detransform(to_predict).astype(np.int64))
    print()
    print()
    printFont(detransform(decoded).astype(np.int64))



