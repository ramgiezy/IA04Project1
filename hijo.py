import networkx as nx 

def hijo(grafo, nodo, indice):
    vertices=grafo.edges(data=False)
    hijos=[]
    for i,j in vertices:
        if i==nodo:
            hijos.append(j)
        if j==nodo:
            hijos.append(i)
    return hijos