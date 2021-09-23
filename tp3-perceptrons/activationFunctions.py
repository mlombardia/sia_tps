import numpy
import numpy as np


def sign_act(x):
    if x >= 0:
        return 1
    return -1


def der_sign_act(x):
    return 1


def lineal_act(x):
    return x


def der_lineal_act(x):
    return 1


def sigmoid_act(x):
    return 1 / (1 + numpy.exp(-2 * x))


def der_sigmoid_act(x):
    return (2*numpy.exp(-2*x)) / ((1+numpy.exp(-2*x))**2)


def tanh_act(x):
    return numpy.tanh(1 * x)


def der_tanh_act(x):
    return 1 / ((numpy.cosh(x)) ** 2)


def softmax_act(x):
    aux = np.exp(x-np.max(x))
    return aux / np.sum(aux)
