"""
Recibe un número entero n y calcula su factorial.
"""

def factorial(n):
    contador = 1
    for i in range(1, n + 1):
        contador *= i

    return contador 
