"""
Escribir funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
's,e,p,a,r,a,r'
b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
debería devolver 'mi_archivo_de_texto.txt'
c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
'X' debería devolver 'su clave es: XXXX'
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
'255.255.255.0'
"""
#a)
def insertar_entre_letras(cadena, caracter):
    '''
    Dada una cadena, inserta el caracter entre cada letra de la cadena y la devuelve
    '''
    resultado = ""
    if caracter == "":
        return cadena

    for c in cadena:
        resultado += c + caracter

    return resultado[:-1]

#b)
def reemplazar_espacios(cadena, caracter):
    resultado = ""
    for c in cadena:
        if c != " ":
            resultado += c
        else:
            resultado += caracter

    return resultado

#c)
def reemplazar_digitos(cadena, caracter):
    '''
    Dada una cadena y un caracter, reemplaza todos los digitos en la cadena
    por el caracter dado
    '''
    resultado = ""
    for c in cadena:
        if not c.isdigit():
            resultado += c
        else:
            resultado += caracter

    return resultado

#d)
def insertar_cada_tres(cadena, caracter):
    '''
    Dada una cadena, inserta el caracter ingresado cada 3 dìgitos en la cadena.
    '''
    resultado = ""
    contador = 0
    for c in cadena:
        if not c.isdigit():
            resultado += c
        else:
            contador += 1
            resultado += c

        if contador % 3 == 0:
            resultado += caracter

    return resultado
'''
print(insertar_cada_tres('2552552550' , '.'))
print(insertar_cada_tres('12+618' , '='))
print(insertar_cada_tres('Su turno es 18 hs' , 'X'))
'''
