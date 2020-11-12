#Implementación del algoritmo de búsqueda en profundidad para la resolución del TSP
import networkx as nx 
from hijo import hijo
from compareSol import compareSol
from size import sizeCH
from verifica import verifica

def DPS(grafo, nodoActual, nodosRequeridos, nodosVisitados, costoTotal, nodoPasado):
    nodosVisitados.append(nodoActual) #Se añade el nodo actual a la lista de visitados
    costoTemp=0
    #Verificacion de posible solución
    if verifica(nodosVisitados, nodosRequeridos) == 1:
        return [nodosVisitados, costoTotal] #formato de una solución
    soluciones=[]
    #visita de cada hijo
    for i in range(sizeCH(grafo, nodoActual)):
        newHijo=hijo(grafo, nodoActual, i) #hijo número i
        #Sección para comprobar que el nodo no haya sido visitado antes
        bandera=0 
        for k in nodosVisitados:
            if newHijo==k:
                bandera=1
        if newHijo!=nodoPasado and bandera!=1:
            costoTemp=costoTotal
            costoTotal=costoTotal+grafo.get_edge_data(nodoActual, newHijo)["weight"] #se suma el costo obtenido de rama
            solucion=DPS(grafo, newHijo, nodosRequeridos, nodosVisitados.copy(), costoTotal, nodoActual)
            soluciones.append(solucion) #Si se obtiene una solución, se añade a una lista de soluciones
            costoTotal=costoTemp #Para recuperar el costo antes del hijo pasado
    return compareSol(soluciones) #Devuelve únicamente la mejor solución