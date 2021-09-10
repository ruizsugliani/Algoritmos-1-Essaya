def wc(nombre_archivo):
    '''
    Dado un archivo de texto, lo procesa e imprime por pantalla
    cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.
    '''
    c_lineas = 0
    c_palabras = 0
    c_caracteres = 0
    with open(nombre_archivo, 'r', encoding="utf8") as file:
        lista_de_lineas = file.readlines()
        for linea in lista_de_lineas:
            c_lineas += 1
        print(lista_de_lineas)
        

    print(f"Cantidad de lineas: {c_lineas}")
    print(f"Cantidad de palabras: {c_palabras}")
    print(f"Cantidad de caracteres: {c_caracteres}")
wc("test_file.txt")
