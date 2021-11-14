from multilayerPerceptron import *
from font_utils import *
import numpy as np
import matplotlib.pyplot as plt


x = np.array(get_input(2))
text_names = get_annotation(2)
##x = [x[6], x[7], x[8], x[9], x[10]]
#x = np.array(x)


#print(x)

x_mean = np.mean(x, axis=0) # normalizacion de datos
x_std = np.std(x, axis=0)   # normalizacion de datos

# printFont(x[4])

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

def detransform(t): #no se usa
    t = (t+1)/2 #ahora tengo en 0-1

    to_detransform = np.rint(t*255)
    for i in range(len(to_detransform)):
        if to_detransform[i] > 255:
            to_detransform[i] = 255
        if to_detransform[i] < 0:
            to_detransform[i] = 0
    return to_detransform

x = transform(x)
#print(x)

layers = [
    # "capa" inicial que son los valores
    NeuronLayer(30, 35, activation="tanh"), #35 de entrada
    NeuronLayer(20, activation="tanh"),
    NeuronLayer(2, activation="tanh"), #latent code Z
    NeuronLayer(20, activation="tanh"),
    NeuronLayer(30, activation="tanh"),
    NeuronLayer(35, activation="tanh")
]

encoderDecoder = MultiLayerPerceptron(layers, init_layers=True, momentum=False, eta=0.00001)

min_error, errors, epochs, training_accuracies = encoderDecoder.train(x, x, iterations_qty=30000, adaptative_eta=True)
print(min_error)

encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0:int(len(layers)/2)], init_layers=False)     # desde el inicio hasta el medio

decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[int(len(layers)/2):], init_layers=False)    # las ultimas capas

aux_1 = []
aux_2 = []
for i in range(len(x)):
    to_predict = x[i, :]
    encoded = encoder.predict(to_predict)
    decoded = decoder.predict(encoded)
    #print(f"{detransform(to_predict)} -> {encoded} -> {detransform(decoded)}" )
    print(f"{to_predict} -> {decoded}")
    printFont(to_predict)#.astype(np.int64))
    print()
    print()
    printFont(decoded)#.astype(np.int64))
    aux_1.append(decoded[0])
    aux_2.append(decoded[1])
    #print("(",decoded[0],",",decoded[1],")")

print(aux_1)
print(aux_2)

#ej 1.a 4)
print("\n\n\n-------------------------\n")
values = [-1,0,1]
for i in values:
    for j in values:
        print(i, " ", j, ": ")
        new_letter = [i, j]
        decoded = decoder.predict(new_letter)
        printFont(decoded)

plt.xlim([-1, 1])
plt.ylim([-1, 1])
for i, txt in enumerate(text_names):
    plt.annotate(txt, (aux_1[i], aux_2[i]))
plt.scatter(aux_1, aux_2)
plt.show()
