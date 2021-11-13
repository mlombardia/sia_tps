from multilayerPerceptron import *
from font_utils import *
import numpy as np
from PIL import Image

flag1 = Image.open("flags/tile010.png").convert('RGB')
data_flag1 = np.asarray(flag1)
data_flag1 = np.delete(data_flag1, [0, 15], axis=1)
data_flag1 = np.delete(data_flag1, [0,1,15,14,13], axis=0)

flag1 = Image.fromarray(data_flag1)

#flag1.show()

def choclify(flag):

    to_ret = []
    for row in flag:
        for pix in row:
            for rgb in pix:
                to_ret.append( ((rgb/255)*2)-1 ) #aux.append( ((num/255)*2)-1 )
    return to_ret

def dechoclify(arr):
    transformed = []
    for rgb in arr:
        number = round(((rgb+1)/2)*255)
        if number < 0:
            number = 0
        elif number > 255:
            number = 255
        transformed.append(number)

    color = []
    row = []
    flag = []
    color_i = 0
    pix_i = 0
    for rgb in transformed:
        color_i += 1
        color.append(rgb)
        if color_i%3 == 0:
            pix_i += 1
            row.append(color)
            color = []
            if pix_i%14 == 0:
                flag.append(row)
                row = []
    return np.array(flag).astype(np.uint8)



data_flag1 = choclify(data_flag1)



#x = np.array(get_input(2))
x = [data_flag1]
x = np.array(x)



x_mean = np.mean(x, axis=0) # normalizacion de datos
x_std = np.std(x, axis=0)   # normalizacion de datos



layers = [
    # "capa" inicial que son los valores
    NeuronLayer(300, 462, activation="tanh"), #14*11*3 de entrada
    NeuronLayer(150, activation="tanh"),
    NeuronLayer(100, activation="tanh"), #latent code Z
    NeuronLayer(150, activation="tanh"),
    NeuronLayer(300, activation="tanh"),
    NeuronLayer(462, activation="tanh")
]

encoderDecoder = MultiLayerPerceptron(layers, init_layers=True, momentum=True, eta=0.001)

min_error, errors, epochs, training_accuracies = encoderDecoder.train(x, x, iterations_qty=20000, adaptative_eta=True)
print(min_error)

encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0:int(len(layers)/2)], init_layers=False)     # desde el inicio hasta el medio

decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[int(len(layers)/2):], init_layers=False)    # las ultimas capas


for i in range(len(x)):
    to_predict = x[i, :]
    encoded = encoder.predict(to_predict)
    decoded = decoder.predict(encoded)
    #print(f"{detransform(to_predict)} -> {encoded} -> {detransform(decoded)}" )
    print(f"{to_predict} -> {decoded}")
    flag = Image.fromarray(dechoclify(to_predict))
    flag.show()
    #printFont(to_predict)#.astype(np.int64))
    print()
    print()
    flag = Image.fromarray(dechoclify(decoded))
    flag.show()
    #printFont(decoded)#.astype(np.int64))



