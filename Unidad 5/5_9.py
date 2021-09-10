"""
Escribir una función que reciba dos números como parámetros, y devuelva cuántos
múltiplos del primero hay, que sean menores que el segundo.
a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que
sea mayor que el segundo.
"""

#a)
def multiplos_antes_v_for(n1, n2):
    '''
    Recibe dos numeros como parametros , y devuelve cuántos múltiplos del primero
    hay, que sean menores que el segundo.
    '''
    cantidad_de_multiplos = 0
    for i in range(n1, n2):
        if i % n1 == 0:
            cantidad_de_multiplos += 1
            continue
        else:
            continue
    return cantidad_de_multiplos

#b)
def multiplos_antes_v_while(n1, n2):
    '''
    Recibe dos numeros como parametros , y devuelve cuántos múltiplos del primero
    hay, que sean menores que el segundo.
    '''
    cantidad_de_multiplos = 0
    i = 1
    while True:
        multiplo = n1 * i
        cantidad_de_multiplos += 1
        i += 1
        if multiplo > n2:
            break
    return cantidad_de_multiplos - 1
print(multiplos_antes_v_while(7, 50))
