def obtener_bigramas(cadena):
    '''
    Recibe un texto y devuelve una lista con todos sus bigramas, los mismos
    estan representados con una tupla (,).
    '''
    if cadena != "":
        cadena = cadena.split()[0:]
        copia = cadena[1:]
        cadena.pop()
        res = []
        while not cadena == [] and not copia == []:
            lista = []
            lista.append(cadena.pop(0))
            lista.append(copia.pop(0))
            res.append(tuple(lista))
        return res

    else:
        return []

def main():
    frecuencia = int(input("Ingrese una frecuencia: "))
    frase = str(input("Ingrese una frase: "))
    contador = 0
    res = ""
    if frecuencia > 0 or frase == "":
        for caracter in frase:
            contador += 1
            res += caracter
            if contador % frecuencia == 0:
                res += "-"

    if res[-1] == "-":
        print(res[0:-1])

    else:
        print(res)

def main():
    while True:
        a = input("Ingrese el número 'a': ")
        b = input("Ingrese el número 'b': ")
        contador = 0
        if a.isdigit() and b.isdigit() and int(a) > 0 and int(b) > 0:
            for n in range(1, int(a) + 1):
                print(n * int(b))
            break
        else:
            continue
main()
