def es_impar(n):
    '''Dado un número entero devuelva 1 si el mismo es impar y 0 si fuera par.'''
    return n % 2

def es_par(n):
    '''Dado un número entero devuelva 0 si el mismo es impar y 1 si fuera par.'''
    return (n + 1) % 2

def digito_de_unidad(n):
    '''Dado un número entero devuelva el dígito de las unidades.'''
    return n % 10

def multiplo_10_inferior(n):
    '''Dado un número devuelva el primer número múltiplo de 10 inferior a él.'''
    resto = n % 10
    if resto == 0:
        return n - 10
    return n - resto

print(multiplo_10_inferior(20))
print(multiplo_10_inferior(231))
print(multiplo_10_inferior(27))
