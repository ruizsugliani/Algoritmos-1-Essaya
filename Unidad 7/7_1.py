def esta_ordenada(tupla):
	'''
	Recibe una tupla de elementos e indica si se encuentran ordenados de menor a mayor o no.
	'''
	temp = list(tupla)
	fin = sorted(temp)
	if tupla == tuple(fin):
		return True
	return False
