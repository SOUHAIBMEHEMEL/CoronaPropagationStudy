import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylab import *
from random import randint, randrange
from src.Data import Data
import numpy as np

data_size = int(input("Entrez la taille de votre population: "))
duration = int(input("Donner la duree pour votre etude : "))
# get data generated randomly (1% of people are infected as an initial cases)
dataObject = Data(data_size)
# get people list
data = dataObject.data
# table des statistiques chaque jour { 0: 'S' , 1: 'I' , 2: 'D', 3: 'G'}
statistiques = {(i, j): 0 for i in range(duration) for j in range(4)}

# tableau de la duree d'infection pour chaque personne infectee
jourInfectee = [0 for _ in range(data_size)]

degrees = []
graph_transitivity = []
fig1 = plt.figure()

G = nx.Graph()
G.add_nodes_from(range(data_size))


def setJourStatistics(i):
    if i == 0:
        statistiques[0, 0] = 0
        statistiques[0, 1] = 0
        statistiques[0, 2] = 0
        statistiques[0, 3] = 0

    for d in data:
        if d.estSain():
            statistiques[i, 0] += 1
        elif d.estInfecte():
            statistiques[i, 1] += 1
        elif d.estDecede():
            statistiques[i, 2] += 1
        elif d.estGueri():
            statistiques[i, 3] += 1


def animate(i):
    global degrees, graph_transitivity
    plt.clf()
    for d in data:
        if d.estSain():
            contact = [randint(0, data_size-1) for _ in range(10)]
            distance = randint(0,data_size)
            if distance < 3:
                for y in contact:
                    G.add_edge(d.getId(), y)
                    if data[y].estInfecte():
                        d.setType('I')

        elif d.estInfecte():
            if d.getDureeInfection() < 14:
                d.setDureeInfection(d.getDureeInfection() + 1)
            else:
                d.setType('G')
                d.setDureeInfection(0)

    setJourStatistics(i)
    degrees.append(i)
    graph_transitivity.append(nx.average_clustering(G))
    plt.title('Est connexe:' + str(nx.is_connected(G))+' Degré= '+str(i))
    nx.draw_networkx(G)


ani = animation.FuncAnimation(fig1, animate, duration, interval=5, repeat=False)
plt.show()
fig2 = plt.plot(degrees, graph_transitivity)
plt.show()

def showType(type):
    x = []
    y = []
    for i in range(duration):
        y.append(i)
    for i in range(duration):
        x.append(statistiques[i, type])
    print(x)
    plt.plot(y, x)
    plt.show()

# visualisation de la propagation chaque jour
showType(0) # population saine
showType(1) # population infectee
showType(2) # population decedee
showType(3) # population guerie



