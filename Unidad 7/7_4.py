#a)
def producto_escalar(vector1, vector2):
	'''
	Recibe dos vectores como tuplas y devuelve su producto escalar.
	'''
	vector1 = list(vector1)
	vector2 = list(vector2)
	res = 0
	while not len(vector1) == 0 and not len(vector2) == 0:
		producto = vector1.pop() * vector2.pop()
		res += producto
	return res

#b)
def verificar_ortogonalidad(vector1, vector2):
	if producto_escalar(vector1, vector2) == 0:
		return True
	return False
#c)
def verificar_paralelismo(vector1, vector2):
    vector1 = list(vector1)
    vector2 = list(vector2)
    if not vector2.pop() % vector1.pop() == 0 or vector1.pop() % vector2.pop() == 0:
        return False
    return True

#d)
def calcular_norma(vector):
    '''
    Recibe un vector y calcula su norma.
    '''
    suma = 0
    for numero in vector:
        dato = numero ** 2
        suma += dato
        norma =suma ** 0.5
    return norma
