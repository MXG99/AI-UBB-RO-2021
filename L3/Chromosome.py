from random import randint

from utils import generateChromosome


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = generateChromosome(problParam["noNodes"], 1, int(problParam["noNodes"] // 2))
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=None):
        if l is None:
            l = []
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        r = randint(0, len(self.__repres) - 1)
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        for i in range(0, len(self.__problParam["mat"][pos])):
            if self.__problParam["mat"][pos][i] == 1:
                self.__repres[i] = self.__repres[pos]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
