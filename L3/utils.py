from random import randint


def generateChromosome(nr, x, y):
    chromosome = []
    for i in range(0, nr):
        chromosome.append(randint(x, y))
    return chromosome
