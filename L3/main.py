import warnings
from random import randint
from time import sleep

from GA import GA
from fitness_functions import modularity
from utils import generateChromosome
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import re

warnings.simplefilter('ignore')

G = nx.Graph()
G = nx.read_gml("searched//powergrid//power.gml", label='id')
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
nx.draw_networkx_nodes(G, pos, node_size=60, cmap=plt.cm.RdYlBu, node_color='green')
nx.draw_networkx_edges(G, pos, alpha=0.3)
plt.show()
mat = nx.adjacency_matrix(G).todense()

invalid = re.compile('[^0-9]')
matx = []
for i in range(0, len(mat)):
    a = str(mat[i])
    cleaned = [int(i) for i in a if not invalid.search(i)]
    matx.append(cleaned)

degrees = []
noEdges = 0

for i in range(len(matx)):
    d = 0
    for j in range(len(matx)):
        if matx[i][j] == 1:
            d += 1
        if (j > i):
            noEdges += matx[i][j]
        degrees.append(d)
param = {'noNodes': len(matx), 'mat': matx, "noEdges": noEdges, "degrees": degrees}


def run():
    param['popSize'] = 100
    ga = GA(param)
    ga.initialisation()
    ga.evaluation()
    for i in range(0, 101):
        print("Generatia " + str(i))
        ga.oneGenerationElitism()
        A = np.matrix(param["mat"])
        G = nx.from_numpy_matrix(A)
        pos = nx.spring_layout(G)  # compute graph layout
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=60, cmap=plt.cm.RdYlBu, node_color=ga.bestChromosome().repres)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        print(ga.bestChromosome().repres)
        plt.show()
    print(ga.bestChromosome().fitness)


run()
