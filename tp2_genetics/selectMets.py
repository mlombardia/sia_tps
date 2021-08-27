import math
import random


class SelectionMethod:
    def __init__(self):
        pass

    def selection(self, individualsList, K):
        pass


class Roulette(SelectionMethod):

    def selection(self, individualsList, K):

        # caclulo fitness relativos
        totalFitness = 0        # fitness total
        acumRelFitness = 0      # fitness relativo acumulado
        individualsData = []    # para guardar los datos de cada individuo
        for i in individualsList:
            totalFitness += i.Performance()
            relativeFitness = (i.Performance()/totalFitness)    # fitness relativo para ese individuo
            acumRelFitness += relativeFitness                   # fitness relativo acumulado
            individualsData.append((i, relativeFitness, acumRelFitness))

        selectedIndividuals = []
        randomNumbers = []

        for i in range(0, K):
            randomNumbers[i] = random.uniform(0, 1)    # genero K numeros random

        # tengo que ver si: racumRelFitness-1 < numero random <= acumRelFitness
        for n in randomNumbers:
            for k in range(0, len(individualsData)):
                if (individualsData[k][2]-1 < n) and (n <= individualsData[k][2]):
                    selectedIndividuals.append(individualsData[k][0])       # si cumple agrego al individuo a los seleccionados


class Universal(SelectionMethod):

    def selection(self, individualsList, K):

        # caclulo fitness relativos
        totalFitness = 0        # fitness total
        acumRelFitness = 0      # fitness relativo acumulado
        individualsData = []    # para guardar los datos de cada individuo
        for i in individualsList:
            totalFitness += i.Performance()
            relativeFitness = (i.Performance()/totalFitness)    # fitness relativo para ese individuo
            acumRelFitness += relativeFitness                   # fitness relativo acumulado
            individualsData.append((i, relativeFitness, acumRelFitness))

        selectedIndividuals = []
        randomNumbers = []

        r = random.uniform(0, 1)

        for i in range(0, K):
            randomNumbers[i] = (r+i)/K    # genero K numeros random

        # tengo que ver si: racumRelFitness-1 < numero random <= acumRelFitness
        for n in randomNumbers:
            for k in range(0, len(individualsData)):
                if (individualsData[k][2]-1 < n) and (n <= individualsData[k][2]):
                    selectedIndividuals.append(individualsData[k][0])       #si cumple agrego al individuo a los seleccionados


class Elite(SelectionMethod):

    def selection(self, individualsList, K):

        def compare(ind):
            return ind.Performance()

        # ordeno segun el fitness
        sortedInd = individualsList.sorted(individualsList, key=compare, reverse=True)

        # selecciono
        selectedIndividuals = []
        N = len(individualsList)    # ordeno de un conjunto de tamaño N
        i = 0
        while N < K:
            n = math.ceil((K-i)/N)
            # ahora elijo n(i) veces
            while (n > 0) and (N < K):
                selectedIndividuals.append(sortedInd[i])    # queda seleccionado
                N -= 1                                      # ahora hay uno menos en el conjunto a elegir
                n -= 1
            i += 1





