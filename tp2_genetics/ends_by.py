# tiempo, cant de generaciones, solucion aceptable, estructura, contenido
from datetime import datetime


def ends_by_specified_time(start, time):
    return datetime.now() - start <= time

def ends_by_generations(gen_qty, gen_max):
    return gen_qty < gen_max

