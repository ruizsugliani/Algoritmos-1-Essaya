canciones = {"hola": 60, "chau": 100, "nos vemos": 80, "a": 50, "b": 30, "c": 90}
listas_reproduccion = {"saludos": ["hola", "chau", "nos vemos"], "algo": ["hola", "chau"], "acdc": ["a", "b", "c"]}

def obtener_duracion_listas(canciones, listas_reproduccion):
    '''
    Recibe como parametro dos diccionarios , uno con canciones y su duracion en
    segundos y el otro con listas de reproduccion y listas de canciones como valores.
    Devuelve en forma de diccionario las duraciones de cada lista de reproduccion.
    '''
    res = {}
    for lista in listas_reproduccion:
        suma = 0
        for cancion in listas_reproduccion[lista]:
            if cancion in canciones:
                suma += canciones[cancion]
                res[lista] = suma

    return res
