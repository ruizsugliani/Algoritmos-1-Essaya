"""
Escribir una funcion que reciba por parametro una lista de numeros y devuelva otra lista
con los numeros de la ingresada que terminan en cero. Por ejemplo, si se recibe la lista: [4, 23,
40, -7, 0, 14, 1000, -760] debe devolver [40, 0, 1000, -760].
"""

#Creo una lista nueva.
#Itero por numero (elemento):
#Si termina en cero lo agrego a la lista
#Devuelvo la lista

def terminan_en_cero(numeros):
    """
    Recibe una lista de numeros y devuelve solo los que terminan en cero.
    """
    terminados_en_cero = []
    for numero in numeros:
        if (numero % 10) == 0:
            terminados_en_cero.append(numero)
    return terminados_en_cero

print(terminan_en_cero([4, 23,
40, -7, 0, 14, 1000, -760]))
