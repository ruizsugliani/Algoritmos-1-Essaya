def sentido_inverso(cadena):
    for i in range(len(cadena) - 1, -1, -1):
        print(cadena[i], end = '')

def agregar_separador_miles(numero):
    '''
    Recibe un nùmero entero y devuelve la cadena con el nùmero
    y las separaciones de miles.
    '''
    numero_invertido = sentido_inverso(numero)
    contador = 0
    resultado = ""
    for c in numero:
        resultado += c
        contador += 1
        if contador % 3 == 0:
            resultado += "."
    return sentido_inverso(resultado)

print(agregar_separador_miles('1234567890'))
