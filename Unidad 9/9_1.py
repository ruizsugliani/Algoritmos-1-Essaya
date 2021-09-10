"""
Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
segundos.
Por ejemplo:
>>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
('Buenos', 'días') ]
>>> print(tuplas_a_diccionario(l))
{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }
"""
def tuplas_a_diccionario(tuplas):
    '''
    Recibe una lista de tuplas, y devuelve un diccionario en donde las claves
    son los primeros elementos de las tuplas, y los valores una lista con los
    segundos.
    '''
    nuevo_dicc = {}
    for clave, valor in tuplas:
        if clave not in nuevo_dicc:
            nuevo_dicc[clave] = []
        nuevo_dicc[clave].append(valor)
    return nuevo_dicc
