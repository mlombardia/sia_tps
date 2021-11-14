from multilayerPerceptron import *
from font_utils import *
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

flag1 = Image.open("flags/tile010.png").convert('RGB')
flag2 = Image.open("flags/tile020.png").convert('RGB')
flag3 = Image.open("flags/tile015.png").convert('RGB')
flag4 = Image.open("flags/tile025.png").convert('RGB')

data_flag1 = np.asarray(flag1)
data_flag1 = np.delete(data_flag1, [0, 15], axis=1)
data_flag1 = np.delete(data_flag1, [0,1,15,14,13], axis=0)

data_flag2 = np.asarray(flag2)
data_flag2 = np.delete(data_flag2, [0, 15], axis=1)
data_flag2 = np.delete(data_flag2, [0,1,15,14,13], axis=0)

data_flag3 = np.asarray(flag3)
data_flag3 = np.delete(data_flag3, [0, 15], axis=1)
data_flag3 = np.delete(data_flag3, [0,1,15,14,13], axis=0)

data_flag4 = np.asarray(flag4)
data_flag4 = np.delete(data_flag4, [0, 15], axis=1)
data_flag4 = np.delete(data_flag4, [0,1,15,14,13], axis=0)

flag1 = Image.fromarray(data_flag1)
flag2 = Image.fromarray(data_flag2)
flag3 = Image.fromarray(data_flag3)
flag4 = Image.fromarray(data_flag4)

#flag1.show()

def choclify(flag):

    to_ret = []
    for row in flag:
        for pix in row:
            for rgb in pix:
                to_ret.append( (rgb/255) ) #aux.append( ((num/255)*2)-1 )
    return to_ret

def dechoclify(arr):
    transformed = []
    for rgb in arr:
        number = round(rgb*255)
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



# print(data_flag1)
data_flag1 = choclify(data_flag1)
data_flag2 = choclify(data_flag2)
data_flag3 = choclify(data_flag3)
data_flag4 = choclify(data_flag4)
# print(data_flag2)



#x = np.array(get_input(2))
x = [data_flag1, data_flag2, data_flag3, data_flag4]
x = np.array(x)



x_mean = np.mean(x, axis=0) # normalizacion de datos
x_std = np.std(x, axis=0)   # normalizacion de datos



layers = [
    # "capa" inicial que son los valores
    NeuronLayer(300, x.shape[1], activation="linear"), #14*11*3 de entrada
    NeuronLayer(x.shape[1], activation="linear")
]

encoderDecoder = MultiLayerPerceptron(layers, init_layers=True, momentum=True, eta=0.000001)

min_error, errors, epochs, training_accuracies = encoderDecoder.train(x, x, iterations_qty=10000, adaptative_eta=False)
print(min_error)

encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0:int(len(layers)/2)], init_layers=False)     # desde el inicio hasta el medio

decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[int(len(layers)/2):], init_layers=False)    # las ultimas capas


for i in range(len(x)):
    to_predict = x[i, :]
    encoded = encoder.predict(to_predict)
    decoded = decoder.predict(encoded)
    # print(f"{detransform(to_predict)} -> {encoded} -> {detransform(decoded)}" )
    print(f"{to_predict} -> {decoded}")
    print(decoded)
    # plt.imshow(dechoclify(to_predict), cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    flag = Image.fromarray(dechoclify(to_predict))
    flag.show()
    # printFont(to_predict)#.astype(np.int64))
    print()
    print()
    # plt.imshow(dechoclify(decoded), cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    flag = Image.fromarray(dechoclify(decoded))
    flag.show()
    #printFont(decoded)#.astype(np.int64))

entry1 = x[0,:]
entry2 = x[1,:]
entry3 = x[2,:]
entry4 = x[3,:]
encoded1 = encoder.predict(entry1)
encoded2 = encoder.predict(entry2)
encoded3 = encoder.predict(entry3)
encoded4 = encoder.predict(entry4)

new_entry = (encoded1+encoded2)/2
new_decoded = decoder.predict(new_entry)

flag = Image.fromarray(dechoclify(new_decoded))
flag.show()

# 1 2
# 3 4

v12 = encoded2-encoded1
v13 = encoded3-encoded1
v24 = encoded4-encoded2
v34 = encoded4-encoded3

n = 10
h = 1.0/n
canvas = None

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
'''
for i in range(n+1):
    v_canvas = None
    v_v = v13 + (1.0 * i / n) * (v24 - v13)
    for j in range(n+1):
        h_v = v12 + (1.0 * j / n) * (v34 - v12)
        entry = encoded1+(1.0*i/n)*h_v+(1.0*j/n)*v_v
        decoded = decoder.predict(entry)
        img = Image.fromarray(dechoclify(decoded))
        if j == 0:
            v_canvas = img
        else:
            v_canvas = get_concat_v(v_canvas, img)
    if i == 0:
        canvas = v_canvas
    else:
        canvas = get_concat_h(canvas, v_canvas)

canvas.show()
'''
# canvas.save('trace.png', quality=100)

for i in range(n+1):
    h_canvas = None
    for j in range(n+1):
        min_x = encoded1+(1.0*i/n)*(encoded3-encoded1)
        max_x = encoded2+(1.0*i/n)*(encoded4-encoded2)
        min_y = encoded1+(1.0*j/n)*(encoded2-encoded1)
        max_y = encoded3+(1.0*j/n)*(encoded4-encoded3)
        entry = min_x+(1.0*j/n)*(max_x-min_x)+(1.0*i/n)*(max_y-min_y)
        decoded = decoder.predict(entry)
        img = Image.fromarray(dechoclify(decoded))
        if j == 0:
            h_canvas = img
        else:
            h_canvas = get_concat_h(h_canvas, img)
    if i == 0:
        canvas = h_canvas
    else:
        canvas = get_concat_v(canvas, h_canvas)

canvas.show()


