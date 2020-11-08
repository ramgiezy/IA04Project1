import networkx as nx 
from hijo import hijo
from compareSol import compareSol
from size import sizeCH
from verifica import verifica

def DPS(grafo, nodoActual, nodosRequeridos, nodosVisitados, costoTotal, nodoPasado):
    nodosVisitados.append(nodoActual)
    if verifica(nodosVisitados, nodosRequeridos) == 1:
        return [nodosVisitados, costoTotal]
    soluciones=[]
    for i in range(sizeCH(grafo, nodoActual)):
        newHijo=hijo(grafo, nodoActual, i)
        bandera=0
        for k in nodosVisitados:
            if newHijo==k:
                bandera=1
        if newHijo!=nodoPasado and bandera!=1:
            costoTotal=costoTotal+grafo.get_edge_data(nodoActual, newHijo)["weight"]
            solucion=DPS(grafo, newHijo, nodosRequeridos, nodosVisitados.copy(), costoTotal, nodoActual)
            soluciones.append(solucion)
    return compareSol(soluciones)