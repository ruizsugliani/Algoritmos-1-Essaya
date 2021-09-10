def suma_de_divisores(n):
    '''
    Devuelve la suma de todos los divisores de N sin incluirlo.
    '''
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def primeros_perfectos(m):
    '''
    Imprime los primeros M numeros tales que la suma de sus divisores sea igual
    a si mismo.
    '''
    contador = 0
    for n in range(1, 500):
        if n == suma_de_divisores(n):
            contador += 1
            print(n)
            if contador == m:
                break

def primeras_parejas(m):
    contador = 0
    for a in range(1, 3000):
        b = suma_de_divisores(a)
        if a < b and suma_de_divisores(b) == a:
            contador += 1
            print(a, b)
            if contador == m:
                break

primeras_parejas(3)
