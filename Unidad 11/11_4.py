def grep(nombre_archivo, cadena):
    '''
    Recibe una cadena y un archivo e imprime las
    líneas del archivo que contienen la cadena recibida.
    '''
    with open(nombre_archivo, "r", encoding="utf8") as f:
        for linea in f:
            if cadena in linea:
                print(linea.rstrip('\n'))
            continue

grep("materias.txt", "Análisis")
