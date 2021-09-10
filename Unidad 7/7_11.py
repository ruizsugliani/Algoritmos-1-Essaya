def plegar_texto(texto, longitud):
    lista = texto.split()
    temp = []
    res = ""
    contador = 0
    for cadena in lista:
        contador += len(cadena)
        if contador < longitud:
            temp.append(cadena)

    for palabra in temp:
        if palabra is not temp[-1]:
            res += palabra + " "
        else:
            res += palabra

    return res

print(plegar_texto('Voy a aprobar Algoritmos 1', 18))
