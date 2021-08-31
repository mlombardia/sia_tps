import math
import random
from characters.Character import *


def Roulette(individualsList, K):
    # caclulo fitness relativos
    totalFitness = 0  # fitness total
    acumRelFitness = 0  # fitness relativo acumulado
    individualsData = []  # para guardar los datos de cada individuo
    for i in individualsList:
        totalFitness += i.Performance()
        relativeFitness = (i.Performance() / totalFitness)  # fitness relativo para ese individuo
        acumRelFitness += relativeFitness  # fitness relativo acumulado
        individualsData.append((i, relativeFitness, acumRelFitness))

    selectedIndividuals = []
    randomNumbers = []

    for i in range(0, K):
        randomNumbers[i] = random.uniform(0, 1)  # genero K numeros random

    # tengo que ver si: racumRelFitness-1 < numero random <= acumRelFitness
    for n in randomNumbers:
        for k in range(0, len(individualsData)):
            if (individualsData[k][2] - 1 < n) and (n <= individualsData[k][2]):
                selectedIndividuals.append(
                    individualsData[k][0])  # si cumple agrego al individuo a los seleccionados

    return selectedIndividuals


def Universal(individualsList, K):

    # caclulo fitness relativos
    totalFitness = 0  # fitness total
    acumRelFitness = 0  # fitness relativo acumulado
    individualsData = []  # para guardar los datos de cada individuo
    for i in individualsList:
        totalFitness += i.Performance()
        relativeFitness = (i.Performance() / totalFitness)  # fitness relativo para ese individuo
        acumRelFitness += relativeFitness  # fitness relativo acumulado
        individualsData.append((i, relativeFitness, acumRelFitness))

    selectedIndividuals = []
    randomNumbers = []

    r = random.uniform(0, 1)

    for i in range(0, K):
        randomNumbers[i] = (r + i) / K  # genero K numeros random

    # tengo que ver si: racumRelFitness-1 < numero random <= acumRelFitness
    for n in randomNumbers:
        for k in range(0, len(individualsData)):
            if (individualsData[k][2] - 1 < n) and (n <= individualsData[k][2]):
                selectedIndividuals.append(
                    individualsData[k][0])  # si cumple agrego al individuo a los seleccionados

    return selectedIndividuals


def Elite(individualsList, K):

    def compare(ind):
        return ind.Performance()

    # ordeno segun el fitness
    sortedInd = individualsList.sorted(individualsList, key=compare, reverse=True)

    # selecciono
    selectedIndividuals = []
    N = len(individualsList)  # ordeno de un conjunto de tamaño N
    i = 0
    while N < K:
        n = math.ceil((K - i) / N)
        # ahora elijo n(i) veces
        while (n > 0) and (N < K):
            selectedIndividuals.append(sortedInd[i])  # queda seleccionado
            N -= 1  # ahora hay uno menos en el conjunto a elegir
            n -= 1
        i += 1

    return selectedIndividuals


def Ranking(self, individualsList, K):
    def compare(ind):
        return ind.Performance()

    individualsToRoulette = []
    sortedInd = individualsList.sorted(individualsList, key=compare, reverse=True)  # ordeno los pjs en base a los
    N = len(individualsList)  # que tienen mejor aptitud
    for i, character in enumerate(sortedInd):
        pseudo_fitness = (N - i) / N  # se calcula la pseudo-aptitud
        if isinstance(character, Warrior):
            aux_character = Warrior(character.getHeight(), character.getItems())  # y armamos un pj aux
            aux_character.performance = pseudo_fitness  # con esa aptitud
            individualsToRoulette.append(aux_character)
        elif isinstance(character, Archer):
            aux_character = Archer(character.getHeight(), character.getItems())
            aux_character.performance = pseudo_fitness
            individualsToRoulette.append(aux_character)
        elif isinstance(character, Rogue):
            aux_character = Rogue(character.getHeight(), character.getItems())
            aux_character.performance = pseudo_fitness
            individualsToRoulette.append(aux_character)
        elif isinstance(character, Tank):
            aux_character = Tank(character.getHeight(), character.getItems())
            aux_character.performance = pseudo_fitness
            individualsToRoulette.append(aux_character)
        else:
            print("Unexpected error")

    roulette = Roulette()  # y despues aca se usa ruleta
    roulette.selection(individualsToRoulette, K)

    # habria que ver forma de devolver esto


#a este lo dejé porque necesita un mini refactor antes de borrar la clase
class Boltzmann(SelectionMethod):
    def __init__(self, t0, tc, k, t):
        super().__init__()
        self.temperature = tc + (t0 - tc) * math.exp(-k * t)  # formula de la temperatura, si vemos alguna
        # que converga mejor podemos usar esa

    def selection(self, individualsList, K):
        individualsToRoulette = []
        population_average = self.calculateAverage(individualsList, self.temperature)  # se calcula la temp promedio
        for i in individualsList:
            pseudo_fitness = math.exp(
                i.Performance / self.temperature) / population_average  # se calcula la pseudo-aptitud
            if isinstance(i, Warrior):
                aux_character = Warrior(i.getHeight(), i.getItems())  # y armamos un pj aux
                aux_character.performance = pseudo_fitness  # con esa aptitud
                individualsToRoulette.append(aux_character)
            elif isinstance(i, Archer):
                aux_character = Archer(i.getHeight(), i.getItems())
                aux_character.performance = pseudo_fitness
                individualsToRoulette.append(aux_character)
            elif isinstance(i, Rogue):
                aux_character = Rogue(i.getHeight(), i.getItems())
                aux_character.performance = pseudo_fitness
                individualsToRoulette.append(aux_character)
            elif isinstance(i, Tank):
                aux_character = Tank(i.getHeight(), i.getItems())
                aux_character.performance = pseudo_fitness
                individualsToRoulette.append(aux_character)
            else:
                print("Unexpected error")

        roulette = Roulette()  # y despues aca se usa ruleta
        roulette.selection(individualsToRoulette, K)

        # habria que ver forma de devolver esto

    def calculateAverage(self, individualsList, temperature):
        avg = 0
        for i in individualsList:
            avg += math.exp(i.Performance / temperature)
        return avg / len(individualsList)



def DetTourney(individualsList, K):
    championList = []
    M = 0
    best = 0
    bestChar = None

    while len(championList) < K:
        M = random.randint(0, len(individualsList))
        best = 0
        bestChar = None
        for i in range(M):
            if individualsList[i].Performance() > best:
                best = individualsList[i].Performance()
                bestChar = individualsList[i]
        championList.append(bestChar)

    return championList


def ProbTourney(individualsList, K):
    championList = []
    thresh = random.randrange(0.5, 1, 0.00001)

    while len(championList) < K:
        charA = random.choice(individualsList)
        charB = random.choice(individualsList)

        winner = None
        r = random.randrange(0, 1, 0.00001)

        if r<thresh:
            if charA.Performance() >= charB.Performance:
                winner = charA
            else:
                winner = charB
        else:
            if charA.Performance() >= charB.Performance:
                winner = charB
            else:
                winner = charA

        championList.append(winner)
    return championList
