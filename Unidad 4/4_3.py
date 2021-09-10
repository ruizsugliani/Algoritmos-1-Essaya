def matriz_identidad(n):
    """
    Recibe por parámetro una dimensión n, e imprime la matriz identidad
    correspondiente a esa dimensión.
    """
    contador = 0
    matriz = [[0] * n for _ in range(n)]
    for y, fila in enumerate(matriz):
        for x, columna in enumerate(matriz):
            if matriz[y][x] == contador:
                matriz[y][x] = n
                contador += 1
    print(matriz, end = " ")

matriz_identidad(3)
