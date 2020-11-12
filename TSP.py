##############Problema del agente viajero resuelto con búsqueda en profundidad##############
#Autores: 
# Jorge Alberto Alcaraz Cardenas
# Giezy Alberto Ramírez Rivera
# Diana Paola Sanjuan Aldape
#Programa que muestra la mejor solución del problema del agente viajero (TSP) conforme al grafo seleccionado
#y las condiciones iniciales dadas
#Materia: Inteligencia artificial
#Grupo: 4
#Equipo 8

import networkx as nx 
from CreateGraph import crearGrafo
import matplotlib.pyplot as plt
from Search import DPS
import time

#Experimento 1
map = crearGrafo(0)
#sección para dibujar el grafo y guardarlo como .png
pos=nx.get_node_attributes(map,'pos')
nx.draw(map,pos)
labels = nx.get_edge_attributes(map,'weight')
nx.draw_networkx_edge_labels(map,pos,edge_labels=labels)
nx.draw_networkx_labels(map, pos)
plt.savefig("grafo.png")
plt.clf()

Requeridos=["Hof", "Gera", "Frankfurt"] 
inicio="Hof"
start_time = time.time() #para contar tiempo de ejecución
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("Esperimento 1. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 2
Requeridos=["Hof", "Gera", "Culmbach"]
inicio="Frankfurt"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 2. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 3
map = crearGrafo(3)
pos=nx.get_node_attributes(map,'pos')
nx.draw(map,pos)
labels = nx.get_edge_attributes(map,'weight')
nx.draw_networkx_edge_labels(map,pos,edge_labels=labels)
nx.draw_networkx_labels(map, pos)
plt.savefig("grafo2.png")
plt.clf()

Requeridos=["B", "E"]
inicio="A"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 3. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 4
Requeridos=["A", "C", "D"]
inicio="E"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 4. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 5
map = crearGrafo(1)
pos=nx.get_node_attributes(map,'pos')
nx.draw(map,pos)
labels = nx.get_edge_attributes(map,'weight')
nx.draw_networkx_edge_labels(map,pos,edge_labels=labels)
nx.draw_networkx_labels(map, pos)
plt.savefig("grafo3.png")
plt.clf()

Requeridos=["nodo6", "nodo7"]
inicio="nodo8"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 5. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 6
Requeridos=["nodo2", "nodo11", "nodo1", "nodo7"]
inicio="nodo5"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 6. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 7
Requeridos=["nodo8", "nodo2", "nodo4"]
inicio="nodo10"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 7. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 8
map = crearGrafo(2)
pos=nx.get_node_attributes(map,'pos')
nx.draw(map,pos)
labels = nx.get_edge_attributes(map,'weight')
nx.draw_networkx_edge_labels(map,pos,edge_labels=labels)
nx.draw_networkx_labels(map, pos)
plt.savefig("grafo4.png")
plt.clf()

Requeridos=["Lugoj", "Mehadia"]
inicio="Sibiu"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 8. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 9
Requeridos=["Arad", "Bucharest", "Fagaras"]
inicio="Oradea"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 9. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)

#Experimento 10
Requeridos=["Sibiu", "Bucharest", "Neamt", "Urziceni", "Iasi"]
inicio="Timisoara"
start_time = time.time()
solucion=DPS(map, inicio, Requeridos, [], 0, "")
print("\n\nEsperimento 10. Solución: ",solucion)
print("Tiempo de ejecución: ",time.time() - start_time)