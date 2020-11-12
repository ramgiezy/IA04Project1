#Función que devuelve la cantidad de hijos que un nodo tiene dentro de un grafo dado.
import networkx as nx 

def sizeCH(grafo, nodo):
    vertices=grafo.edges(data=False)
    contador=0
    for i,j in vertices:
        if (i==nodo or j==nodo):
            contador=contador+1
    return contador
