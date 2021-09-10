def matriz_guardar(ruta, matriz):
    '''
    Recibe una matriz de n x m números enteros y la guarda en el archivo indicado.
    '''
    with open(ruta, "w") as f:
        for fila in matriz:
            for numero in fila:
                if numero != fila[-1]:
                    f.write(f"{numero} ")
                if numero == fila[-1]:
                    f.write(f"{numero}\n")

def matriz_cargar(ruta):
    '''
    Lee del archivo la matriz y la devuelve.
    '''
    res = []
    with open(ruta) as f:
        for fila in f:
            fila = fila.split()
            res.append(fila)

    for fila in res:
        for n in range(len(fila)):
            fila[n] = int(fila[n])
    return res


def pruebas():
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # HACER:
    # - llamar a matriz_guardar
    # - llamar a matriz_cargar
    # - verificar que la matriz cargada es idéntica a la original

    matriz_guardar("ejercicio.txt", [[1, 2, 3],[4, 5, 6]])
    resultado = matriz_cargar("ejercicio.txt")
    assert resultado == matriz

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
