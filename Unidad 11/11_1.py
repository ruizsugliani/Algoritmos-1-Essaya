def head(nombre_archivo, N):
    '''
   	Recibe un nombre de archivo y un número N e imprime las primeras N líneas del archivo.
    '''
    with open(nombre_archivo, encoding="utf8") as archivo:
        for _ in range(N):
            linea = archivo.readline().rstrip('\n')
            if not linea:
                break

            print(linea)
head("materias.txt", 167)
