#a)
def map(funcion, lista):
	'''
	Recibe una función y una lista, y devuelve la lista que resulta de aplicar
	la función recibida a cada uno de los elementos de la lista recibida.
	'''
	res = []
	for elemento in lista:
		dato = funcion(elemento)
		res.append(dato)
	return res

#b)
def filter(funcion, lista):
	'''
	Recibe una función y una lista, y devuelve una lista con los elementos de la
	lista recibida para los cuales la función recibida devuelve un valor verdadero.
	'''
	res = []
	for elemento in lista:
		if funcion(elemento):
			res.append(elemento)
	return res
