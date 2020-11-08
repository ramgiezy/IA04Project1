import networkx as nx 
from CreateGraph import crearGrafo
import matplotlib.pyplot as plt
from Search import DPS
import time


map = crearGrafo(0)

pos=nx.get_node_attributes(map,'pos')
nx.draw(map,pos)
labels = nx.get_edge_attributes(map,'weight')
nx.draw_networkx_edge_labels(map,pos,edge_labels=labels)
nx.draw_networkx_labels(map, pos)
plt.savefig("grafo.png")

#Requeridos=["Hof", "Gera", "Bamberg"]
Requeridos=["Hof", "Gera", "Frankfurt"]
inicio="Hof"

start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print(solucion)
print(time.time() - start_time)
