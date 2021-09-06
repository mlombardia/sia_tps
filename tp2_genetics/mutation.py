import linecache
import random

#arma, bota, casco, guantes, pechera
# from tp2_genetics.items.Item import Item
from items.Item import Item

def gen(probability, gene, child): #le edito a child tal gen con tanta probabilidad de mutacion
    mutation_probability = random.uniform(0,1)          # elijo una probabilidad
    if mutation_probability <= probability:
        if gene == 0:
            child.itemList[gene] = get_random_weapon()
        elif gene == 1:
            child.itemList[gene] = get_random_boots()
        elif gene == 2:
            child.itemList[gene] = get_random_helmet()
        elif gene == 3:
            child.itemList[gene] = get_random_gloves()
        elif gene == 4:
            child.itemList[gene] = get_random_chest_plate()
        elif gene == 5:
            child.height = get_random_height()
        else:
            print("no existe el gen ", gene)
            exit()

        return child


def limited_multigen(probability, child):
    genesToEdit = random.randint(1,6)
    edited = []
    n = 0
    rand = random.uniform(1, 0)
    if rand <= probability:
        while n < genesToEdit:
            gene = random.randint(0, 5)
            if gene in edited:
                continue
            edited.append(gene)

            gen(1, gene, child)
            n += 1

    return child


def uniform_multigen(probability, child):
    for gene in range(6):
        gen(probability, gene, child)
    return child


def complete_mutation(probability, child):
    rand = random.uniform(0, 1)
    if rand <= probability:
        for gene in range(6):
            gen(1, gene, child)

    return child


def get_random_height():
    return random.uniform(1.3, 2)

def get_random_weapon():
    rand = random.randint(2, 1000001)
    item = linecache.getline('armas.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_boots():
    rand = random.randint(2, 1000001)
    item = linecache.getline('botas.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_helmet():
    rand = random.randint(2, 1000001)
    item = linecache.getline('cascos.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_gloves():
    rand = random.randint(2, 1000001)
    item = linecache.getline('guantes.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem

def get_random_chest_plate():
    rand = random.randint(2, 1000001)
    item = linecache.getline('pecheras.tsv', rand)
    newItem = Item("item", item.split("\t")[0], item.split("\t")[1], item.split("\t")[2], item.split("\t")[3], item.split("\t")[4], item.split("\t")[5])
    return newItem
