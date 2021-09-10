#a)
def invertir_lista(lista):
	'''
	Dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida.
	'''
	res = []
	while not len(lista) == 0:
		dato = lista.pop()
		res.append(dato)
	return res

#b)
