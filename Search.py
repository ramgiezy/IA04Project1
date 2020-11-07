import networkx as nx 
from hijo import hijo
from compareSol import compareSol
from size import sizeCH
from verifica import verifica

def DPS(grafo, nodoActual, nodosRequeridos, nodosVisitados, costoTotal, nodoPasado):
    nodosVisitados.append(nodoActual)
    if verifica(nodosVisitados, nodosRequeridos) == 1:
        return([nodosVisitados, costoTotal])
    soluciones=[]
    for i in range(sizeCH(grafo, nodoActual)):
        if (hijo(grafo, nodoActual, i)!=nodoPasado):
            #costo=grafo.get_edge_data(nodoActual, hijo(grafo, nodoActual, i)["weight"])
            costoTotal=costoTotal+grafo.get_edge_data(nodoActual, hijo(grafo, nodoActual, i)).get("weight")[0]
            #costoTotal=costoTotal+costo.get
            solucion=DPS(grafo, hijo(grafo, nodoActual, i), nodosRequeridos, nodosVisitados, costoTotal, nodoActual)
            soluciones.append(solucion)
    return compareSol(soluciones)