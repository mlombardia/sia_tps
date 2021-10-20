import numpy as np

class Hopfield:
    def __init__(self, patterns):
        self.patterns = patterns
        self.weights = self.init_weights(patterns)

    def init_weights(self, patterns):
        weights = []
        dim = len(patterns[0])
        for i in range(dim):
            aux = []
            for j in range(dim):
                if i == j:
                    aux.append(0)
                else:
                    aux2 = 0
                    for E in patterns:
                        aux2 += E[i] * E[j]
                    aux.append(aux2/dim)
            weights.append(aux)
        return weights

    def stimulus(self, unknown):
        S = []
        S.append(np.array(unknown)) #S[0]
        S.append(self.dot_sign(self.weights, S[0])) #S[1]
        i = 1
        while S[i].tolist() != S[i-1].tolist():
            S.append(self.dot_sign(self.weights, S[-1]))
            i += 1
            if i >= 25:
                return False, False
        #se estancó
        if S[-1].tolist() in self.patterns:
            return S[-1], True #el patrón
        else:
            return S[-1], False #estado espureo

    def dot_sign(self, arr1, arr2):
        aux = np.sign(np.dot(arr1, arr2))
        for j in range(len(aux)):
            if aux[j] == 0:
                aux[j] = 1
        return aux



