import math

def buscar_cero(f, n_min, n_max):
    valor_intermedio = (n_min + n_max) // 2
    if f(valor_intermedio) == 0:
        return valor_intermedio
    else:
        if f(valor_intermedio) < 0:
            return buscar_cero(f, valor_intermedio + 1, n_max)
        else:
            return buscar_cero(f, n_min, valor_intermedio - 1)

def pruebas():

    def f(n):
        return math.factorial(n) - 40320

    assert buscar_cero(f, 0, 20) == 8   # porque f(8) == 0

    # OPCIONAL: agregar más casos de prueba.

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
