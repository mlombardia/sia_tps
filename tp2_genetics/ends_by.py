# tiempo, cant de generaciones, solucion aceptable, estructura, contenido
import math
from datetime import datetime
from datetime import timedelta


def ends_by_specified_time(start, time):
    return (datetime.now() - start).total_seconds() < time


def ends_by_generations(gen_qty, gen_max):
    return gen_qty < gen_max


def ends_by_fitness(current_fit, obj_fit):
    return current_fit < obj_fit


def ends_by_content(gen_qty, gen_max):
    return gen_qty != gen_max

def ends_by_structure(gen0, gen1, part, percent):
    def compare(ind):
        return ind.performance
                    # ordeno segun el fitness
    gen0.sort(key=compare, reverse=True)
    gen1.sort(key=compare, reverse=True)

    maxSize = len(gen0)
    size = math.floor(maxSize * percent)

    if part != "best" and part != "worst":
        print("error: variable Part debe ser 'best' o 'worst'")
        exit()


    if part == "best":
        for i in range(size):
            if gen0[i] != gen1[i]:
                return False
    elif part == "worst":
        for i in range(size):
            if gen0[maxSize-1-i] != gen1[maxSize-1-i]:
                return False
    return True




