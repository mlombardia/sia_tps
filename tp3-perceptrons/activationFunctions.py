import numpy


def sign_act(x):
    if x >= 0:
        return 1
    return -1


def lineal_act(x):
    return x


def der_lineal_act(x):
    return 1

def sigmoid_act(x):
    return 1 / (1 + numpy.exp(-1  * x))

def der_sigmoid_act(x):
    return sigmoid_act(x) * (1 - sigmoid_act(x))

def tanh_act(x):
    return numpy.tanh(1 * x)


def der_tanh_act(x):
    return 1 / ((numpy.cosh(x)) ** 2)
