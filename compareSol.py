
def compareSol(soluciones):
    menorPrecio=10000
    mejorSolucion=[None, None]
    if soluciones!= []:
        for i,j in soluciones:
            if j!=None:
                if j<menorPrecio:
                    menorPrecio=j
                    mejorSolucion=[i,j]
        return mejorSolucion
    else:
        return [None,None]