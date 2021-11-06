from multilayerPerceptron import *
from font_utils import *

class LinearAutoencoder:

    layer1 = NeuronLayer(32, get_input())
    layer2 = NeuronLayer(2, get_input())
    layer3 = NeuronLayer(32, get_input())

    encoderDecoder = MultiLayerPerceptron([layer1, layer2, layer3])

    encoderDecoder.train(get_input(), get_output())

    encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0])     # la primera capa
    # la capa del medio
    decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[-1])    # la ultima capa