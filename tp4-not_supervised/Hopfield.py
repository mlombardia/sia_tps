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
        S.append(unknown) #S[0]
        S.append(np.sign(np.dot(self.weights, S[-1]))) #S[1]
        S.append(np.sign(np.dot(self.weights, S[-1]))) #S[2]
        i = 2
        while S[i].all() != S[i - 1].all():
            S.append(np.sign(np.dot(self.weights, S[-1])))
            i += 1
        #se estancó
        if S[-1] in self.patterns:
            return S[-1], True #el patrón
        else:
            return S[-1], False #estado espureo

    # def iteration(self):
    #     for i in range(len(self.S)):
    #         S_aux = []
    #         aux = 0
    #         for j in range(len(self.weights)):
    #             if j != i:
    #                 aux += self.weights[i][j] * self.S[j]
    #         S_aux.append(np.sign(aux))
    #     self.S = S_aux


# - init weights (con patrones almacenados/conocidos)

# para primer patron desconocido
# - viene nuevo patrón -> S(t+1), S(t+2), ... , S(t) = S(t-1)
# - este es el patron

# para segundo patron desconocido
# - viene nuevo patrón -> S(t+1), S(t+2), ... , S(t) = S(t-1)
# - este es el patron
