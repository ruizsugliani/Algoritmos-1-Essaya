def obtener_cadenas_largas_por_caracter(texto):
    '''
    Recibe un texto y para cada caracter presente en el texto
    devuelve la cadena más larga en la que se encuentra ese caracter.
    En el caso de que haya más de una cadena posible para elegir, se debe seleccionar la última.
    '''
    res = {}
    minusculas = texto.lower()
    palabras = minusculas.split()
    for palabra in palabras:
        for caracter in palabra:
            if res.get(caracter, ""):
                if len(palabra) >= len(res[caracter]):
                    res[caracter] = palabra
            else:
                res[caracter] = palabra
    return res

print(obtener_cadenas_largas_por_caracter('Pero que hermoso dia hay'))
