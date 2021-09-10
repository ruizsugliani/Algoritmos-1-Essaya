def transponer(m):
    res = list()
    for col in range(len(m[0])):
        fila_traspuesta = []
        for fila in range(len(m)):
            fila_traspuesta.append(m[fila][col])
        res.append(fila_traspuesta)
    return res

def pruebas():
    m = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    mt = transponer(m)

    assert mt == [
        [1, 3, 5],
        [2, 4, 6],
    ]

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
