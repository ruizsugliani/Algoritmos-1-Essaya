import math
import string
#1
'''
Dado el siguiente código en Python

for x in range(2, 29, 7):
    print("Valor al inicio de la iteracion:", x)
    x = (x * 2) - 3
    print("Valor al final de la iteracion:", x)

Hacer una tabla con los valores de x iniciales y finales de cada iteración.
En caso de que el ciclo no termine nunca, colocar una fila con "...". b.
Transformar el ciclo anterior a un ciclo while que implemente el mismo comportamiento.
'''

#2
'''
Escribir una función que recibe un número entero $n$ e imprime un tablero de
ajedrez de tamaño $N \times N$. Por ejemplo, el tablero deberá imprimirse de la
siguiente forma para un tablero de $N = 3$:

b n b
n b n
b n b

Nota: b denota un casillero blanco, n denota un casillero negro.
'''

#3
'''
Escribir una función que imprima los números de 1 a 100; pero para los múltiplos
de 3 imprima "Miki" en lugar del número; y para los múltiplos de 5 imprima "Moko".
Para los múltiplos de 3 y 5 debe imprimir "MikiMoko".
'''
def miki_moko():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            i = "MikiMoko"
            print(i)
        else:
            if i % 3 == 0:
                i = "Miki"
                print(i)
            else:
                if i % 5 == 0:
                    i = "Moko"
                    print(i)
                else:
                    print(i)

#4
'''
Escribir una función que dado un número entero positivo devuelva la mínima unidad
del número, que se calcula según el siguiente ejemplo: minima_unidad(546) → 6
porque $5+4+6=15$ y $1+5=6$.
'''

#5
'''
Escribir una función que reciba por parámetro un número n e imprima los primeros
n números curiosos.Un número curioso es todo número natural $x$ que cumple que
$x^2$ tiene al propio $x$ en sus últimas cifras. Por ejemplo, 6 y 25 son números
curiosos ($6^2 = 36$, $25^2 = 625$), pero 7 y 11 no lo son ($7^2 = 49$, $11^2 = 121$)
'''
def numeros_curiosos(n):
    contador = 0
    for i in range(1, 100):
        potencia = str(i*i)
        if i >= 10:
            if str(i) == potencia[1:]:
                print(i)
                contador += 1

        elif str(i) == potencia[-1]:
                print(i)
                contador += 1
        if contador == n:
            break

#6
'''
Escribir una función que sirva para pintar las filas de una tabla. La función
recibe el número de fila y debe devolver una cadena que representa el color que
se debe utilizar para esa fila. El color de las filas es:

    0 a 7: 'AZUL' y 'ROJO' intercalados (A-R-A-R-...)
    8 a 15: 'BLANCO' y 'NEGRO' intercalados cada dos (B-B-N-N-B-B...)
    A partir de 16: 'AZUL' y 'VERDE' intercalados cada tres (A-A-A-V-V-V...).
'''

#7
'''
Escribir una función que le pida al usuario que ingrese un número. Se debe luego
validar la entrada del usuario según las siguientes condiciones:

    Debe ser positivo
    Debe ser primo (considerar que está implementada la función es_primo(n))

La función debe repetir este proceso hasta que el usuario ingrese un número válido
o ingrese un caracter especial de fin (que se recibe por parámetro). La función
debe devolver el número válido o -1 en caso de que haya ingresado el caracter de fin.
'''
def es_primo(n):
    '''
    Indica si un natural es primo.
    '''
    divisible = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divisible += 1
    if divisible == 2:
        return True
    else:
        return False

def validar_entrada(caracter):
        while True:
            n = input("Ingrese un numero: ")
            if n == caracter:
                return -1

            elif int(n) < 0 or not es_primo(int(n)):
                continue
            else:
                if int(n) > 0 and es_primo(int(n)):
                    return n

#8
'''
Escribir una función validar_contraseña que reciba una palabra clave y un número
de intentos n. Dicha función debe pedir al usuario que ingrese la contraseña un
máximo de n veces. En caso de que la contraseña ingresada coincida con la recibida
por la función, se devuelve True, caso contrario se devuelve False.
'''
def validar_contrasenia(clave, intentos):
    contrasenia = input("Ingrese una contrasenia: ")
    while contrasenia != clave:
        intentos -= 1
        if intentos == 0:
            return False
        contrasenia = input("Ingrese una contrasenia: ")
    return True

#9
'''
Escribir un programa que pida dos números enteros al usuario (a y b) e imprima
los primeros a múltiplos de b. El programa debe validar que cada número que
ingrese el usuario sea un entero positivo y, en caso de que no lo sea, solicitarlo
nuevamente (hasta que se ingrese algo correcto).
'''
def main():
    a = input("Ingrese un numero entero positivo A: ")
    while not a.isdigit() or int(a) < 0:
        a = input("Ingrese un numero entero positivo A: ")
    b = input("Ingrese un numero entero positivo B:")
    while not b.isdigit() or int(b) < 0:
        b = input("Ingrese un numero entero positivo B:")
    for i in range(1, int(a) + 1):
        print(i*int(b))


#10
'''
Escribir un programa que pida al usuario que ingrese el valor de un ángulo en grados,
entre 0 y 360, e imprima su conversión a radianes. Si el usuario no ingresa un
número válido, se le debe pedir que lo ingrese nuevamente (y repetir hasta que
el usuario ingrese un número válido). Nota: recordar que la medición en radianes
de los ángulos van de 0 a 2π.
'''
def main():
    angulo = input("Ingrese un angulo entre 0 y 360 grados: ")
    while not angulo.isdigit() or not 0 <= int(angulo) <= 360:
        angulo = input("Ingrese un angulo entre 0 y 360 grados: ")
    radianes = int(angulo) / 180
    print(f"{radianes}π")

#11
'''
Escribir una función que reciba un número secreto (entero) y le pregunte un número
al usuario. Si el número ingresado es distinto, debe indicarle si es mayor o menor
al número secreto y volver a pedirle otro número. Si es igual, debe felicitar al
usuario y mostrar en cuántos intentos adivinó. No hay un máximo de intentos pero
el usuario debe adivinar para terminar el programa.
'''
def adivinar_numero(secreto):
    intentos = 0
    entrada = input("Ingrese un numero entre [1..100]:")
    while not entrada.isdigit():
        intentos += 1
        entrada = input("Ingrese un numero y no ingrese caracteres:")

    while not 1 <= int(entrada) <= 100:
        intentos += 1
        input("PORFAVOR Ingrese un numero entre [1...100]:")

    while entrada.isdigit():
        if int(entrada) < secreto:
            intentos += 1
            entrada = input("El numero secreto es mayor, ingrese un otro numero:")

        elif int(entrada) > secreto:
            intentos += 1
            entrada = input("El numero secreto es menor, ingrese un otro numero:")

        if int(entrada) == secreto:
            break

    print(f"Felicitaciones, usted ha adivinado el numero en {intentos} intentos")

#12
'''
Se pide implementar una función que reciba por parámetro una contraseña
(en forma de cadena) y verifique que la misma sea válida, devolviendo un valor
booleano. Para que una contraseña sea válida, debe cumplir con los siguientes requisitos:

    Debe tener entre 10 y 20 caracteres
    Si tiene menos de 15 caracteres, debe contener al menos dos vocales maýusculas
    Si tiene al menos 15 caracteres, no debe contener ninguno de los siguientes símbolos: % $ - ( ) = # ! ?
'''
def validar_password(contrasenia):
    if not 10 <= len(contrasenia) <= 20:
        return False
    return True

    if len(contrasenia) == 15:
        if '%' in contrasenia or '$' in contrasenia or '-' in contrasenia or '('in contrasenia or ')' in contrasenia or '=' in contrasenia or '#' in contrasenia or '!' in contrasenia or '?' in contrasenia:
            return False
        return True

    if len(contrasenia) < 15:
        contador = 0
        for c in contrasenia:
            if c == c.upper():
                contador += 1
        if contador >= 2:
            return True
        return False

#13
'''
Escribir una función que recibe una cadena y devuelve la cadena eliminando los
caracteres repetidos consecutivos. Ejemplo: sin_repetir('aaabbaac') → 'abac'
'''
def sin_repetir(cadena):
    if not cadena:
        return ""
    res = ""
    res += cadena[0]
    for c in cadena[1:]:
        if c == res[-1]:
            continue
        else:
            res += c
    return res

#14
'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo
n y una cadena, e imprima la misma cadena pero con un guión (-) cada n lugares.
Ejemplo: n = 2, cadena = Esto es un ejemplo.; debe imprimir Es-to- e-s -un- e-je-mp-lo-.
'''
def main():
    res = ""
    entrada = input("Ingrese un numero entero positivo N: ")
    while not entrada.isdigit() or int(entrada) < 0:
        entrada = input("Ingrese un numero entero positivo N: ")

    cadena = input("Ingrese una cadena de texto: ")
    contador = 0
    for c in cadena:
        contador += 1
        res += c
        if contador % int(entrada) == 0:
            res += "-"
    print(res)

#15
'''
Escribir una función que reciba una cadena y devuelva el resultado de reemplazar
todas las apariciones de la primera letra (ignorando mayúsculas o minúsculas)
con un asterisco.
Nota: no se puede usar la funcion str.replace() de Python
'''
def reemplazar(cadena):
    res = ""
    primera = cadena[0]
    for c in cadena:
        if c == primera:
            res += "*"
        else:
            res += c
    return res

#16
'''
Escribir una función que reciba una cadena y devuelva su encriptación en formato
rot13. Para encriptar una cadena con rot13 se debe reemplazar cada caracter por
el caracter que se encuentra a 13 posiciones de distancia en el abecedario. Si
la cadena contiene números, caracteres especiales o mayúsculas se debe devolver
una cadena vacía.

Ayuda: usar la constante ascii_lowercase del módulo string que contiene “abcd...xyz”.

Ejemplo:

rot13("zambia") -> "mnzovn"
rot13("mnzovn") -> "zambia"
rot13("z4mbi4") -> ""
'''
from string import ascii_lowercase
from string import ascii_uppercase
def rot13(cadena):
    res = ""
    for c in cadena:
        if c.isdigit() or c in ascii_uppercase or c in "!#$%&/()=?¿¡+-*":
            return ""
        indice = ascii_lowercase.index(c)
        indice_rotado = (indice + 13) % len(ascii_lowercase)
        res += ascii_lowercase[indice_rotado]
    return res

#17
'''
Escribir una función que realice lo siguiente: - Le pida al usuario que ingrese una
contraseña. Luego debe validar que la misma: - Tenga al menos dos numeros, pero
no tenga más números que letras (a-z, A-Z, no es necesario incluir letras acentuadas
o especiales de otros idiomas que no sea el ingles). - Tenga alguno de estos
caracteres ("!", "@", "~", "/", "#") pero no más de tres. - Si no ingresa una
contraseña válida debe volver a preguntarle hasta quedarse sin intentos. - Cuando
sea válida, se deben devolver la cantidad de intentos restante. Si se acaban los
intentos, debe mostrar un mensaje por pantalla y devolver -1. La cantidad de
intentos es recibida por parametro.
'''
def validar_contrasenia():
    c_numeros = 0
    c_letras = 0
    c_especiales = 0
    intentos_restantes = 5
    es_valida = False
    while intentos_restantes > 0:
        clave = input("Ingrese la contraseña a validar: ")
        for c in clave:
            if c.isdigit():
                c_numeros += 1
            elif c.isalpha():
                c_letras += 1
            elif c in "!@~/#":
                c_especiales += 1

        if c_numeros >= 2 and c_numeros < c_letras and 0 <= c_especiales <= 3:
            return intentos_restantes
        else:
            intentos_restantes -= 1
            continue
    print("Se acabaron los intentos.")
    return -1

#18
'''
Escribir una función que reciba una cadena que contiene únicamente palabras separadas
por espacios, y que devuelva una nueva cadena con las letras de cada una de las
palabras invertidas. Ejemplo: "Qué día tan bonito" → "éuQ aíd nat otinob"
'''
def invertir_palabras(cadena):
    res = []
    palabras = cadena.split()
    for palabra in palabras:
        palabra = palabra[::-1]
        res.append(palabra)
    return " ".join(res)

#19
'''
Se tiene una lista de listas que representa un laberinto en forma de matriz
(dos dimensiones). En cada posición $i, j$ habrá una tupla que indicará cuantos
casilleros moverse y en qué dirección, por ejemplo (3,'v') debe moverse 3 posiciones
en sentido vertical hacia abajo; (-1, 'h') indica que se debe mover en una posición
hacia la izquierda. Implementar una función que reciba un laberinto de este tipo
y que empezando por el 0, 0 indique en cuántos pasos se sale del laberinto, es decir,
llegar a la posición $n-1, n-1$ (está garantizado que se puede salir).
'''

#20
'''
Escribir una función que recibe una lista de números y devuelve una nueva lista
con los elementos reordenados, de forma tal que todos los números pares aparecen
antes que todos los números impares. No es necesario mantener el orden relativo
de los elementos originales. Ejemplo: f([3,5,2,6,18,7,40,11]) → [2,6,18,40,11,3,5,7]
'''
def ordenar(lista):
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares + impares

#22
'''
El estilo de nomenclatura snake_case permite representar un conjunto de palabras
separándolas por un guión bajo, mientras que el estilo CamelCase las representa
sin separadores, utilizando letras mayúsculas para la primera letra de cada palabra.
Se pide realizar una función que reciba una cadena escrita en snake_case y devuelva
su representación en CamelCase. Ejemplos:

snake_a_camel(“alan_turing”) → “AlanTuring”
snake_a_camel(“hoy_es_el_parcial”) → “HoyEsElParcial”
'''
def snake_a_camel(cadena):
    res = ""
    palabras = cadena.split("_")
    for palabra in palabras:
        inicial = palabra[0]
        palabra = inicial.upper() + palabra[1:]
        res += palabra
    return res

#23
'''
Escribir una función que recibe dos secuencias A y B de igual longitud, y devuelve
una lista donde el elemento en la posición i es una tupla con los elementos de
A y B en la posición i. Ejemplo: f([1, 2, 3], [4, 5, 6]) → [(1, 4), (2, 5), (3, 6)]
'''
def a_tuplas(lista1, lista2):
    res = []
    while len(lista1) != 0 and len(lista2) != 0:
        for i in lista1:
            for j in lista2:
                tupla = []
                tupla.append(lista1.pop(0))
                tupla.append(lista2.pop(0))
                res.append(tuple(tupla))
    return res

#24
'''
Se pide realizar un programa que le pida al usuario un texto (formado únicamente
por letras y espacios) y una letra, y cuente el total de palabras que inician o
terminan con esa letra.
'''
def main():
    cadena = input('Ingrese una cadena de texto: ')
    letra =  input('Ingrese una letra: ')
    cadena = cadena.split()
    contador = 0
    for palabra in cadena:
        if palabra[0] == letra or palabra[-1] == letra:
            contador += 1
    print(f"Un total de {contador} palabras comienzan o terminan con la letra indicada.")

#25
'''
Implementar una función que reciba una matriz (representada por una lista de listas)
y devuelva una nueva matriz que sea la traspuesta de la original.Aclaración:
dada la matriz $M$ de dimensiones $n \times m$, la matriz traspuesta $M^T$ de
dimensiones $m \times n$ es aquella tal que para todo $i$, $0 \leq i \leq n$ y
para todo $j$, $0 \leq j \leq m$: $M^T_{[i][j]} == M_{[j][i]}$
'''

#26
'''
Implementar una función que reciba una cadena y que cuente en la misma la cantidad
de palabras que empiezan y terminan con la misma letra, indistintamente de si
alguna de éstas es mayúscula y la otra minúscula.
Aclaración: el texto solo contiene palabras separadas por espacios. No contiene
signos de puntuación de ningún tipo.
'''
def inicial_y_final_iguales(cadena):
    res = 0
    cadena = cadena.lower()
    cadena = cadena.split()
    for palabra in cadena:
        if palabra[0] == palabra[-1]:
            res += 1
    return res

#31
'''
Un bigrama es una secuencia de dos palabras contiguas dentro de un texto. Escribir
una función que reciba un texto y devuelva una lista con todos sus bigramas. Los
mismos deberán estar representados con una tupla (<palabra1>, <palabra2>). Ejemplo:
>>> obtener_bigramas(“Uno se alegra de resultar útil”)
[(“Uno”, “se”), (“se”, “alegra”), (“alegra”, “de”), (“de”, “resultar”), (“resultar”, “útil”)]
'''
def bigrama(cadena):
    res = []
    cadena = cadena.split()
    for elemento in range(1, len(cadena)):
            bigrama = (cadena[elemento-1], cadena[elemento])
            res.append(tuple(bigrama))
    return res

#32
'''
Escribir una función que reciba una cadena por parámetro y devuelva la misma
cadena con todas sus palabras capitalizadas. Por ejemplo, si la función recibe
"hola, cómo estás?” Debe devolver “Hola, Cómo Estás?”.
Nota: no se permite utilizar la función title() de string.
'''
def capitalizar(cadena):
    res = ""
    palabras = cadena.split()
    for palabra in palabras:
        palabra = palabra[0].upper() + palabra[1:] + " "
        res += palabra
    return res[:-1]

#34
'''
Escribir una función que reciba una lista y la invierta sobre la misma lista sin
usar estructuras adicionales.
Nota: Al usar slices (lista[::]) se crea una nueva lista, por lo que no se pueden
utilizar para resolver este ejercicio.
'''
def invertir_lista_in_place(lista):
    for i in range(len(lista)):
        lista.insert(i, lista.pop())
    return lista

def invertir_cadena_in_place(cadena):
    for i in range(0, len(cadena)):
        cadena[i] = cadena[len(cadena)-1-i]
        cadena[len(cadena)-1-i] = cadena[i]
    return cadena

print(invertir_cadena_in_place("hola"))
#36
'''
Escribir una función que recibe una cadena y un número $n$ y divide la cadena en
subcadenas de longitud $n$ (con una posible subcadena final de longitud menor a
$n$). Ejemplo: subcadenas("algoritmos", 3) → ["alg", "ori", "tmo", "s"]
'''
def dividir_cadena(cadena, n):
    res = []
    act = ""
    for c in cadena:
        act += c
        if len(act) % n == 0:
            res.append(act)
            act = ""
    if act:
        res.append(act)
    return res

#37
'''
Un pangrama es una frase o texto que usa todas las letras de un alfabeto. Por
ejemplo, la frase the quick brown fox jumps over the lazy dog usa todas las letras
del alfabeto inglés.
Escribir una función que reciba una cadena y devuelva si es un pangrama o no.
Ayuda: la constante ascii_lowercase del módulo string es una cadena que contiene
todas las letras del alfabeto: abcdefghijklmnopqrstuvwxyz.
'''
def es_pangrama(cadena):
    letras = list("abcdefghijklmnopqrstuvwxyz")
    for c in cadena:
        if c in letras:
            letras.remove(c)
    if letras == []:
        return True
    else:
        return False
#print(es_pangrama("the quick brown fox jumps over the lazy dog"))


#39
'''
Escribir un programa que pida al usuario que ingrese líneas de texto, hasta que
ingrese una línea vacía. El programa deberá imprimir todas las líneas encerradas
en un marco. Ejemplo:

Ingrese una linea o enter para terminar: Hola
Ingrese una linea o enter para terminar: Mundo
Ingrese una linea o enter para terminar: en un marco
Ingrese una linea o enter para terminar:
***************
* Hola        *
* Mundo       *
* en un marco *
***************
'''

#38
'''
Escribir una función que dado un número entero n mayor a 0 y una lista de números
enteros, devuelva una nueva lista con los divisores de n que se encuentren en la
primera. Si n no cumple las condiciones pedidas, debe devolver una lista vacía.
Ejemplo: f([1, 7, 2, -4, 6, 9], 8) → [1, 2, -4]
'''
def divisores(lista, n):
    res = []
    for i in lista:
        if n % i == 0:
            res.append(i)
    return res

#44
'''
Escribir un programa que le pregunte al usuario dos números enteros y luego devuelva
una lista con todos los números pares que se encuentren en el rango definido por
estos dos números (incluyendo ambos).
El programa debe validar que el usuario ingrese números enteros, volviéndole a
pedir un nuevo número hasta que el ingresado cumpla con las restricciones.
'''
def main():
    res = []
    while True:
        a = input("Ingrese un primer numero entero: ")
        if not a.isdigit():
            continue
        if int(a) < 0:
            continue
        else:
            a = int(a)

            while True:
                b = input("Ingrese un segundo numero entero: ")
                if not b.isdigit():
                    continue
                if int(b) < 0:
                    continue
                b = int(b)
                break

        if a > b:
            for numero in range(b, a + 1):
                if numero % 2 == 0:
                    res.append(numero)
            return res

        else:
            for numero in range(a, b + 1):
                if numero % 2 == 0:
                    res.append(numero)
            return res

#46
'''
Escribir una función que reciba una lista de números y un número n e imprima todos
los números de la lista en n columnas ordenados por fila.

Por ejemplo, si recibe: [1,2,3,4,5,6] y 3 Debe imprimir:

1 2 3
4 5 6
'''
def imprimir_columnas(lista, n):
    contador = 0
    for i in lista:
        print(i, end=" ")
        contador += 1
        if contador % n == 0:
            print()

#47
'''
Escribir una función que reciba una lista de números y un número n e imprima todos
los números de la lista en n columnas ordenados por columna.

Por ejemplo, si recibe: [1,2,3,4,5,6,7,8,9,0,21] y 3 Debe imprimir:

1 5 9
2 6 0
3 7 21
4 8
'''

#48
'''
Escribir una función que reciba dos secuencias y devuelva una lista con los
elementos comunes a ambas, sin repetir ninguno. Ejemplo: f([7, 9, 7, 1], [6, 9, 7]) → [7, 9]
'''
def comunes(lista1, lista2):
    res = []
    for i in lista1:
        if i in lista2 and i not in res:
            res.append(i)
    return res

#49
'''
Se debe modelar el funcionamiento de una caja fuerte. Para ello, se debe implementar
una función que recibe la clave numérica que desbloquea la caja fuerte y la máxima
cantidad de intentos que puede intentar, y que le pida al usuario que vaya ingresando
los valores de la clave de a un dígito por vez. Si el usuario ingresa en algún
momento un dígito que no es correcto, se le debe informar al usuario y el mismo
debe volver a ingresar toda la clave de a un dígito por vez. Si después de la
máxima cantidad de intentos el usuario no ingresó la clave correcta, se le debe
informar que se le acabaron los intentos y la función debe terminar su ejecución.
En cualquier caso la función debe devolver un valor booleano que indique si la caja
fuerte fue abierta exitosamente o no.
'''
def caja_fuerte(clave, intentos):
    intentos_act = 0
    digito = 0
    clave_ingresada = ""
    while intentos_act != intentos:
        entrada = input("Ingrese un digito a la vez: ")
        if clave[digito] != entrada:
            intentos_act += 1
            digito = 0
            clave_ingresada = ""
            print("Digito incorrecto.")
            continue
        else:
            digito += 1
            clave_ingresada += entrada
        if clave_ingresada == clave:
            break
    if intentos == intentos_act:
        print("Se acabaron los intentos.")
        return False
    return True

#50
'''
Escribir una función que, dada una lista de nombres y una letra, devuelva una
lista con todos los nombres que empiezan por dicha letra. La función debe ignorar
mayúsculas y minúsculas; es decir, tanto "alan" como "Alan" empiezan con "A" (y con "a").
'''
def empiezan_igual(lista, letra):
    res = []
    for nombre in lista:
        nombre_min = nombre.lower()
        nombre_may = nombre.upper()
        if letra == nombre_min[0] or letra == nombre_may[0]:
            res.append(nombre)
    return res

#51
'''
Escribir una función que traduce una oración en español (formada por palabras en
minúsculas, separadas por espacios) a latín de los cerdos. Cada palabra se traduce
moviendo la primera letra al final y agregando "ay". Ejemplo: f("hola mundo") → "olahay undomay"
'''
def traduce(oracion):
    res = ""
    palabras = oracion.split()
    for palabra in palabras:
        palabra = palabra[1:] + palabra[0] + "ay"
        res += palabra + " "
    return res[0:-1]

#52
'''
Escribir una función que pida cadenas al usuario hasta que ingrese una cadena
vacía. Debe devolver una lista de las palabras ingresadas. Por ejemplo:

Cadena: hola co
Cadena: mo e
Cadena: stas ?
Cadena:

Debe devolver: ['hola', 'como', 'estas', '?']
'''
def devolver_palabras():
    temp = ""
    while True:
        cadena = input("Ingrese una cadena(enter para terminar): ")
        if cadena:
            temp += cadena
        else:
            break
    lista = temp.split()
    return lista

#53
'''
Escribir una función que reciba una palabra y devuelva una lista con todas las
rotaciones posibles de esa palabra. Ejemplo:

rotaciones('rotar') → ['rotar','otarr','tarro','arrot','rrota']

Aclaración: Para ser considerada una rotación, las letras deben mantener el orden
relativo (en forma circular). Ejemplo: 'torra' no es una rotación posible a partir de 'rotar'.
'''
def rotaciones(cadena):
    res = []
    for i in range(len(cadena)):
        rotacion = cadena[i:] + cadena[:i]
        res.append(rotacion)
    return res

#56
'''
a) Hacer el seguimiento paso por paso de la búsqueda del número 5 en la lista
[1,2,4,5,6,8,9,11,14], utilizando el algoritmo de búsqueda binaria.

b) ¿Qué condiciones debe cumplir sí o sí una lista para que se pueda realizar
una búsqueda binaria sobre ella?

c) Si una lista cumple las condiciones del punto (b) y tiene elementos repetidos,
¿puede aplicarse igual una búsqueda binaria sobre ella?
'''

#57
'''
¿Se puede modificar la búsqueda binaria vista en clase para que funcione tanto
para listas ordenadas de forma creciente como para listas en orden decreciente?
Si es posible, explicar cómo lo haría y qué problemas o casos de borde podría
encontrar. De lo contrario, explicar claramente por qué no se puede.
Nota: En ningún caso se puede modificar la lista, ni realizar algún cambio que
empeore la eficiencia del algoritmo.
'''
