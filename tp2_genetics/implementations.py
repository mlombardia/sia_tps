from selectMets import *


def fill_all(K, select_method, parents, children):
    total=len(parents+children)     #bien??????

    if select_method == 'roulette':
        return Roulette(parents+children, K)    #habria que seleccionar N? WTF
    elif select_method == 'universal':
        return Universal(parents+children, K)
    elif select_method == 'elite':
        return Elite(parents+children, K)
    elif select_method == 'ranking':
        return Ranking(parents+children, K)
    elif select_method == 'boltzmann':
        return Boltzmann(parents+children, K, 50, 10, 2, 1)
    elif select_method == 'det_tourney':
        return DetTourney(parents+children, K)
    else:
        return ProbTourney(parents+children, K)


def fill_parent(K, select_method, parents, children):
    N = len(parents + children)     #bien??????

    if K <= N:
        if select_method == 'roulette':
            return children + Roulette(parents, N-K)
        elif select_method == 'universal':
            return children + Universal(parents, N-K)
        elif select_method == 'elite':
            return children + Elite(parents, N-K)
        elif select_method == 'ranking':
            return children + Ranking(parents, N-K)
        elif select_method == 'boltzmann':
            return children + Boltzmann(parents, N-K, 50, 10, 2, 1)
        elif select_method == 'det_tourney':
            return children + DetTourney(parents, N-K)
        else:
            return children + ProbTourney(parents, N-K)

    else:
        if select_method == 'roulette':
            return Roulette(children, N)
        elif select_method == 'universal':
            return Universal(children, N)
        elif select_method == 'elite':
            return Elite(children, N)
        elif select_method == 'ranking':
            return Ranking(children, N)
        elif select_method == 'boltzmann':
            return Boltzmann(children, N, 50, 10, 2, 1)
        elif select_method == 'det_tourney':
            return DetTourney(children, N)
        else:
            return ProbTourney(children, N)
