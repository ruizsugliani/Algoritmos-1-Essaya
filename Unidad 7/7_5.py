"""
Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números
"""
#a)
import math

def es_primo(n):
    """
    Recibe un numero natural y devuelve True si es primo y False en caso contrario
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:    #% --> el resto de dividir n por i
            return False
    return True

def seleccionar_primos(enteros):
	'''
	Dada una lista de números enteros, devuelve una lista con todos los que sean primos.
	'''
	res = []
	for numero in enteros:
		if es_primo(numero):
			res.append(numero)

	if 1 in res:
		res.remove(1)
	return res
#b)
def sumatoria_y_promedio(enteros):
	'''
	Dada una lista de números enteros, devuelve la sumatoria y el promedio de los valores.
	'''
	res = []
	sumatoria = 0
	cantidad = 0
	for numero in enteros:
		sumatoria += numero
		cantidad += 1
	promedio = sumatoria / cantidad
	res.append(sumatoria)
	res.append(promedio)
	return res

#c)
def factorial(n):
	contador = 1
	for i in range(1, n + 1):
		contador *= i
	return contador

def factoriales(enteros):
	'''
	Dada una lista de números enteros, devuelve una lista con el factorial de cada uno de esos números.
	'''
	res =[]
	for numero in enteros:
		res.append(factorial(numero))
	return res
