import numpy


def sign_act(x):
    if x >= 0:
        return 1
    return -1


def lineal_act(x):
    return x


def tanh_act(x):
    return numpy.tanh(1*x)


