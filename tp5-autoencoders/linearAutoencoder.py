from multilayerPerceptron import *
from font_utils import *

class LinearAutoencoder:

    layer1 = NeuronLayer(32, 7)
    layer2 = NeuronLayer(2)
    layer3 = NeuronLayer(32, 7)

    encoderDecoder = MultiLayerPerceptron([layer1, layer2, layer3])

    encoderDecoder.train(get_input(), get_output())

    encoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[0])     # la primera capa
    # la capa del medio
    decoder = MultiLayerPerceptron(encoderDecoder.neuron_layers[-1])    # la ultima capa