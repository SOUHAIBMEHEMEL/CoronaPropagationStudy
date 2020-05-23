import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint, randrange

from src.Data import Data

# get data generated randomly (1% of people are infected as an initial cases)
d= Data(10)

# table des statistiques chaque jour { 0: 'S' , 1: 'I' , 2: 'D', 3: 'G'}
statistiques = [[]]


degrees = []
graph_transitivity = []
fig1 = plt.figure()

def animate(i):
    global degrees, graph_transitivity
    plt.clf()
    G = nx.Graph()
    G.add_nodes_from(range(5))
    for x in range(10):
        for y in range(i):
            G.add_edge(x, randint(0, 2))
    degrees.append(i)
    graph_transitivity.append(nx.average_clustering(G))
    plt.title('Est connexe:' + str(nx.is_connected(G)) + ' Degré= ' + str(i))
    nx.draw_networkx(G)


ani = animation.FuncAnimation(fig1, animate, 10, interval=500, repeat=False)
plt.show()
fig2 = plt.plot(degrees, graph_transitivity)
plt.show()
