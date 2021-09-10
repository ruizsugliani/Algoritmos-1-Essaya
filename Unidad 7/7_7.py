def escribir_nombres(lista):
	'''
	Recibe una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre)
	y devuelva una lista de cadenas donde cada una contenga primero el nombre,
	luego la inicial con un punto, y luego el apellido.
	'''
	res =[]
	for tupla in lista:
		for i in tupla:
			cadena = []
			cadena.append(tupla[1])
			cadena.append(tupla[2] + ".")
			cadena.append(tupla[0])
		res.append(" ".join(cadena))
	return res
