"""
Escribir una función que reciba un número entero 𝑘 e imprima su descomposición
en factores primos.
"""
def descomposicion_en_factores_primos(k):
    while k != 1:
        for i in range(2, k + 1):
            if k % i == 0:
                print(i, end = " * ")
                k = k // i
                break
                print(k, "|", i)

descomposicion_en_factores_primos(71)
