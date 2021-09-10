def menores_mayores_iguales(enteros, k):
    '''
    Devuelve tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
    '''
    menores = []
    iguales = []
    mayores = []
    for numero in enteros:
    	if numero < k:
    		menores.append(numero)
    	elif numero > k:
    		mayores.append(numero)
    	else:
    		iguales.append(numero)
    return menores, mayores, iguales

def multiplos(enteros, k):
    '''
    Devuelve una lista con aquellos que son múltiplos de k.
    '''
    multiplos = []
    for numero in enteros:
    	if numero % k == 0:
    		multiplos.append(numero)
    return multiplos
