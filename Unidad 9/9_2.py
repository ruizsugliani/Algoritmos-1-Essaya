
"""
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena
de texto, y los devuelva en un diccionario.
c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
dados.
"""
#a)
def contar_apariciones(cadena):
    apariciones = {}
    en_minusculas = cadena.lower()
    palabras = en_minusculas.split()
    for palabra in palabras:
        apariciones[palabra] = apariciones.get(palabra, 0) + 1
    return apariciones

#b)
def contar_caracteres(cadena):
    '''
    Cuenta la cantidad de apariciones de cada caracter en
    una cadena de texto, y los devuelve en un diccionario.
    '''
    apariciones = {}
    en_minusculas = cadena.lower()
    for caracter in en_minusculas:
        if caracter not in apariciones:
            apariciones[caracter] = 0
        apariciones[caracter] += 1

        if " " in apariciones:
            apariciones.pop(" ")
    return apariciones

#c)
import random

# La siguiente línea de código hace que random.randint siempre genere la misma secuencia de números.
# Es necesaria para que cada vez que se corran las pruebas se obtengan los mismos resultados. En un programa "real" no debería estar.
random.seed(123)

def contar_resultados_dados(n):
    '''
    Recibe una cantidad de iteraciones de una tirada de 2 dados a realizar y
    devuelve la cantidad de veces que se observa cada valor de la suma de los dos dados.
    '''
