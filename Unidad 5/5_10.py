import math

def es_primo(n):
    """
    Recibe un numero natural y devuelve True si es primo y False en caso contrario
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:    #% --> el resto de dividir n por i
            return False
    return True

def primos_h_natural(n):
    '''
    Recibe un natural e imprime todos los numeros primos hasta ese número.
    '''
    for x in range(2, n + 1):
        if not es_primo(x):
            continue
        print(x, end = " ")
