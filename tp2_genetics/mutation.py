import random



def gen(probability, parents_genes, items):
    for genes in parents_genes:                             # agarro a los padres
        mutation_probability = random.uniform(0,1)          # elijo una probabilidad
        if mutation_probability <= probability:
            gen_to_mutate = random.randint(0, len(genes)-1)     # elijo un gen al azar
            genes[gen_to_mutate] = mutate(gen_to_mutate, items) # lo muto
    return parents_genes


def limited_multigen(probability, parents_genes, items):
    for genes in parents_genes:                            # agarro a los padres
        mutation_probability = random.uniform(0, 1)        # elijo una probabilidad
        if mutation_probability <= probability:
            mutation_qty = random.randint(1, len(genes))    #elijo random cantidad de genes a mutar
            mutation_indexes = [random.randint(0, len(genes) - 1) for a in range(0, mutation_qty)]
            for i in mutation_indexes:
                genes[i] = mutate(i, items)                 #los muto
    return parents_genes

def mutate(index, items):
    randomizer = {
        0: get_random_height,
        1: get_random_weapon,
        2: get_random_boots,
        3: get_random_helmet,
        4: get_random_gloves,
        5: get_random_chest_plate
    }

    func = randomizer.get(index, None)

    if func is None:
        print("Unexpected error")
        exit(1)
    else:
        return func(items)

def get_random_height(items):
    return random.uniform(1.3,2)

def get_random_weapon(items):
    return get_item(items.weapons) # esto cuando este ready lo de leer el archivo

def get_random_boots(items):
    return get_item(items.boots)

def get_random_helmet(items):
    return get_item(items.helmets)

def get_random_gloves(items):
    return get_item(items.gloves)

def get_random_chest_plate(items):
    return get_item(items.get_random_chest_plate)
