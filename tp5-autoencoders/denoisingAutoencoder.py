from multilayerPerceptron import *
from font_utils import *
import numpy as np


x = np.array(get_input(2))
x = [x[6], x[11], x[19], x[9], x[10]]
x = np.array(x)

RAND = 1/35


#print(x)

x_mean = np.mean(x, axis=0) # normalizacion de datos
x_std = np.std(x, axis=0)   # normalizacion de datos

# printFont(x[4])


def noise(t):
    to_ret = []
    for i in t:
        aux = []
        for num in i:
            a = format(num, "b").zfill(5) #a = 00111010101
            for j in a:
                rand = random.uniform(0, 1)
                if j == "0":
                    if rand < RAND:
                        aux.append(1)
                    else:
                        aux.append(-1)
                elif j == "1":
                    if rand < RAND:
                        aux.append(-1)
                    else:
                        aux.append(1)
        to_ret.append(aux)
    return np.array(to_ret)


def transform(t): #to binary: [7 6] = [0 0 1 1 1 0 0 1 1 0]
    to_ret = []
    for i in t:
        aux = []
        for num in i:
            a = format(num, "b").zfill(5)
            for j in a:
                if j == "0":
                    aux.append(-1)
                elif j == "1":
                    aux.append(1)
        to_ret.append(aux)
    return np.array(to_ret)

x_noise = noise(x)
x_noise2 = noise(x)
x = transform(x)

#printFont(x[0])
#printFont(x_noise[0])
#printFont(x_noise2[0])

layers = [
    # "capa" inicial que son los valores
    NeuronLayer(30, 35, activation="tanh"), #35 de entrada
    NeuronLayer(20, activation="tanh"),
    NeuronLayer(10, activation="tanh"), #latent code Z
    NeuronLayer(20, activation="tanh"),
    NeuronLayer(30, activation="tanh"),
    NeuronLayer(35, activation="tanh")
]

encoderDecoder = MultiLayerPerceptron(layers, init_layers=True, momentum=True, eta=0.000001)

min_error, errors, epochs, training_accuracies = encoderDecoder.train(x_noise, x, iterations_qty=25000, adaptative_eta=True)
print(min_error)

encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0:int(len(layers)/2)], init_layers=False)     # desde el inicio hasta el medio

decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[int(len(layers)/2):], init_layers=False)    # las ultimas capas


for i in range(len(x)):
    to_predict = x_noise2[i, :]
    encoded = encoder.predict(to_predict)
    decoded = decoder.predict(encoded)
    #print(f"{detransform(to_predict)} -> {encoded} -> {detransform(decoded)}" )
    print(f"{to_predict} -> {decoded}")
    printFont(x_noise[i])
    printFont(to_predict)#.astype(np.int64))
    print()
    print()
    printFont(decoded)#.astype(np.int64))