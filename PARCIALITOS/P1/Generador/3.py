"""
Escribir una funcion que reciba una palabra y devuelva una lista
con todas las rotaciones de esa palabra.
Por ejemplo, si recibe: 'rotar', debe devolver:
['rotar','otarr','tarro','arrot','rrota']
"""
#funcion
#recibe una palabra
#devuelve una lista con todas las rotaciones de esa palabra
def rotar_palabra(palabra):
    rotaciones = []
    for c in range(0, len(palabra)):
        rotacion = palabra[c:] + palabra[:c]
        rotaciones.append(rotacion)
    return rotaciones
print(rotar_palabra("rotar"))
