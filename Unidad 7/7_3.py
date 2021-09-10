#a)
def imprimir_mensaje(nombres):
	'''
	Escribir una función que reciba una tupla con nombres,
	y para cada nombre imprima el mensaje Estimado <nombre>, vote por mi..
	'''
	for nombre in nombres:
		print(f"Estimado {nombre}, vote por mi.")

#b)
def imprimir_mensajes(nombres,p,n):
    '''
    Recibe una tupla con nombres, una posición de origen p y una
    cantidad n, e imprima el mensaje anterior para los n nombres que
    se encuentran a partir de la posición p.
    '''
    nombres = nombres[p:]
    contador = 0
    if n != 0:
        for i in range(len(nombres)):
            print(f"Estimado {nombres[i]}, vote por mi.")
            contador += 1
            if contador == n:
                break

#c)
def imprimir_mensajes(nombres,p,n):
	
