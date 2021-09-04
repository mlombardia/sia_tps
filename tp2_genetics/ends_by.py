# tiempo, cant de generaciones, solucion aceptable, estructura, contenido
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