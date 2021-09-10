def cargar_datos(nombre_archivo):
    '''
    Recibe el nombre de un archivo con el contenido en formato "clave, valor" y
    devuelve un diccionario con el primer campo como clave y el segundo como lista.
    '''
    res = {}
    with open(nombre_archivo, "r", encoding = "utf8") as f:
        for linea in f:
            linea = linea.rstrip("\n").split(", ")
            clave = linea[0]
            valor = linea[1]
            if not clave in res:
                res[clave] = [valor]
            if clave in res:
                continue
    return res

def guardar_datos(datos, nombre_archivo):
    '''
    Recibe un diccionario y el nombre de un archivo, finalmente guarda el contenido del
    diccionario en el archivo con el formato clave valor.
    '''
    with open(nombre_archivo, "w", encoding = "utf8") as f:
        for clave in datos:
            linea = ""
            linea += str(clave) + ", " + str(datos[clave]) + "\n"
            f.write(linea)
    return

dict = {'The Godfather': 'Crime', 'The Dark Knight': 'Drama'}

guardar_datos(dict, 'prueba.txt')
print(cargar_datos("test_file.txt"))
