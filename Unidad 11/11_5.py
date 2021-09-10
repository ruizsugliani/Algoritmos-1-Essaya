def algoritmo_de_cifrado(linea):
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cadena = ""
    for caracter in linea:
        if caracter in abecedario:
            nuevo_caracter = (abecedario.index(caracter) + 13) % 26
            cadena += abecedario[nuevo_caracter]
        else:
            cadena += caracter
    return cadena

def rot13(archivo_origen, archivo_destino):
    '''
    Recibe un archivo de texto de origen y uno de destino, de modo que para cada
    línea del archivo origen, se guarde una línea cifrada en el archivo destino.
    >>>El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter com-
    prendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26,
    para obtener un nuevo caracter.
    '''
    lineas_cifradas = []
    with open(archivo_origen, "r", encoding="utf8") as file_o:
        lista_de_lineas = file_o.readlines()
        for cadena in lista_de_lineas:
            lineas_cifradas.append(algoritmo_de_cifrado(cadena))
            with open(archivo_destino, "w", encoding="utf8") as file_d:
                file_d.writelines(lineas_cifradas)
    return file_d

rot13("origen.txt", "destino.txt")
