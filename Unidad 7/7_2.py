#a)
def encajan(ficha1, ficha2):
	'''
 	Indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas.
	'''
	if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[1] or ficha1[1] == ficha2[0]:
		return True
	return False
