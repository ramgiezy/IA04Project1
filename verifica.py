#Función que verifica si ya se han visitado todos los nodos requeridos en el TSP

def verifica(nodosVisitados, nodosRequeridos):
    contador=0
    for i in nodosVisitados:
        for j in nodosRequeridos:
            if i==j:
                contador += 1
    if contador==len(nodosRequeridos):
        return 1
    else:
        return 0