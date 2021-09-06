from selectMets import *


def fill_all(N, select_method, parents, children, t0, tc, k, gen):

    if select_method == 'roulette':
        return Roulette(parents+children, N)
    elif select_method == 'universal':
        return Universal(parents+children, N)
    elif select_method == 'elite':
        return Elite(parents+children, N)
    elif select_method == 'ranking':
        return Ranking(parents+children, N)
    elif select_method == 'boltzmann':
        return Boltzmann(parents+children, N, t0, tc, k, gen)
    elif select_method == 'det_tourney':
        return DetTourney(parents+children, N)
    else:
        return ProbTourney(parents+children, N)


def fill_parent(N, K, select_method, parents, children, t0, tc, k, gen):

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
            return children + Boltzmann(parents, N-K, t0, tc, k, gen)
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

