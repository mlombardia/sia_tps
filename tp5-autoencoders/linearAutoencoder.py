from multilayerPerceptron import *
from font_utils import *
import numpy as np



x = np.array(get_input())
x_mean = np.mean(x, axis=0) # normalizacion de datos
x_std = np.std(x, axis=0)   # normalizacion de datos

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
    NeuronLayer(5, x.shape[1], activation="linear"),
    NeuronLayer(x.shape[1], activation="linear")
]

encoderDecoder = MultiLayerPerceptron(layers)

min_error, errors, epochs, training_accuracies = encoderDecoder.train(x, x, iterations_qty=5000)
print(min_error)

encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0:int(len(layers)/2)], init_layers=False)     # desde el inicio hasta el medio

decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[int(len(layers)/2):], init_layers=False)    # las ultimas capas

for i in range(0, x.shape[0]):
    to_predict = x[i, :]
    encoded = encoder.predict(to_predict)
    decoded = decoder.predict(encoded)
    print(f"[{i}] - {detransform(to_predict)} -> {encoded} -> {detransform(decoded)}" )



