
def compareSol(soluciones):
    menorPrecio=0
    if soluciones!= []:
        for i,j in soluciones:
            if j<menorPrecio:
                menorPrecio=j
                mejorSolucion=i
        return mejorSolucion
    else:
        return [[None, None]]