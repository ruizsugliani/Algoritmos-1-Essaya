"""
Escribir una funcion reducir que reciba por parametro una cola y una funcion f de dos
parametros, y aplique sucesivamente la funcion f a los dos primeros elementos de la cola (luego
de desencolarlos) y encole el resultado, hasta que solo quede un elemento. La funcion reducir
debe devolver el unico elemento restante en la cola.
"""

from cola import Cola

def reducir(cola, funcion):
    while not cola.esta_vacia():
        elemento_1 = cola.desencolar()
        if cola.esta_vacia():
            return elemento_1

        elemento_2 = cola.desencolar()
        resultado = funcion(elemento_1, elemento_2)
    return cola.encolar(resultado)
