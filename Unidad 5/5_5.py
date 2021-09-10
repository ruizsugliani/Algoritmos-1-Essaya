def calcular_mcd(n, m):
    '''
    Calcula el maximo comun divisor entre N y M,
    '''
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
        continue

    return n
