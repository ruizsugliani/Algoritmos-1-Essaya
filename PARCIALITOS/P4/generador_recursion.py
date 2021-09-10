from pila import Pila
from cola import Cola

#177
'''
Alan, Bárbara y Grace juegan al ping-pong. El que gana un partido sigue jugando,
mientras que el que lo pierde es reemplazado por el que no jugaba. El primer
partido es entre Romeo y Dante. Se gana una cerveza el primero que gana tres
partidos seguidos. Implementar una función recursiva que simule este juego y
devuelva quien ganó. Suponer que la probabilidad de ganar un partido es igual para ambos.
Nota: para simular el resultado de cada parido en forma aleaoria, utilizar la función random.choice.
'''

#178
def producto_digital(n):
    '''
    Recibe un número entero y devuelve el producto de sus dígitos.
    Ejemplo: producto_digital(356) → 90, pues $3 \cdot 5 \cdot 6 = 90$.
    '''
    numero = str(n)
    return wrapper(numero, res=1)

def wrapper(numero, res):
    if not numero:
        return res
    res = res * int(numero[0])
    return wrapper(numero[1:], res)

#179
def es_primo(n):
    '''
    Devuelve true si es un numero primo, false en caso contrario
    '''
    for i in range(2, n):
        if (n % i) == 0:
        	return False
    return True

def eliminar_sucedidos_primo(lista):
    '''
    Recibe una lista de Python de números y devuelve una nueva lista eliminando
    los dígitos que son sucedidos por un número primo.
    Ejemplo: eliminar_sucedidos_primo([4,7,6,11,13]) → [7,13]
    '''
    return wrapper(lista, res=[])

def wrapper(lista, res):
    if len(lista) == 1:
        res.append(lista[0])
        return res
    siguiente_dato = lista[1]
    if es_primo(siguiente_dato):
        return wrapper(lista[1:], res)
    res.append(lista[0])
    return wrapper(lista[1:], res)

#180
def eliminar_pares(lista):
    '''
    Función recursiva que elimina los números pares de una lista de Python que contiene únicamente números.
    '''
    return wrapper(lista, res=[])

def wrapper(lista, res):
    if not lista:
        return res

    if lista[0] % 2 == 0:
        return wrapper(lista[1:], res)
    res.append(lista[0])
    return wrapper(lista[1:], res)

#181
def producto(pila):
    '''
    Recibe una pila con números, devuelve el producto de los mismos.
    La pila debe quedar en su estado original al final de la ejecución.
    '''
    return wrapper(pila, res=1)

def wrapper(pila, res):
    if pila.esta_vacia():
        return res
    dato = pila.desapilar()
    res = wrapper(pila, res= res * dato)
    pila.apilar(dato)
    return res

#pila = Pila()
#pila.apilar(1)
#pila.apilar(2)
#pila.apilar(3)
#print(pila)
#print(producto(pila))
#print(pila)

#182
def es_par(n):
    return n % 2 == 0

def particionar(lista, f):
    '''
    Recibe una lista y una funcion, devuelve una nueva lista con los elementos de
    la misma que devuelve True tras aplicarlos a f al principio y luego los que
    devuelven False.
    '''
    return wrapper(lista, f, cumplen=[], no_cumplen=[])

def wrapper(lista, f, cumplen, no_cumplen):
    if not lista:
        return cumplen + no_cumplen
    if f(lista[0]):
        cumplen.append(lista[0])
        return wrapper(lista[1:], f, cumplen, no_cumplen)
    no_cumplen.append(lista[0])
    return wrapper(lista[1:], f, cumplen, no_cumplen)

#183
def suma_digital(n):
    '''
    La suma digital de un número n es la suma de sus dígitos. Recibe un número entero
    positivo y devuelve su suma digital.
    Ejemplo: suma_digital(2019) → 12 (porque 2+0+1+9 = 12).
    '''
    return wrapper(n, res=0)

def wrapper(n, res):
    if not n:
        return res
    dato = n % 10
    res += dato
    n = n // 10
    return wrapper(n, res)

#184
def collatz(n):
    '''
    Sea la siguiente operación, aplicable a cualquier número entero positivo:
    Si el número es par, se divide por 2.
    Si el número es impar, se multiplica por 3 y se suma 1.
    Función recursiva que imprime la secuencia de operaciones comenzando desde el
    número n, y terminando en el número 1. Ejemplo: collatz(5) → 5 16 8 4 2 1
    '''
    if n == 1:
        print(n)
        return

    if n % 2 != 0:
        print(n)
        n = (n * 3) + 1
        return collatz(n)
    else:
        print(n)
        n = n // 2
        return collatz(n)

#185
def euclides(a, b):
    '''
    Funcion recursiva que devuelve el m.c.d entre dos numeros a y b, donde a > b.
    '''
    r = a % b
    if r == 0:
        return b
    else:
        a = b
        b = r
        return euclides(a, b)

#186
def es_palindromo(cadena):
    '''
    Recibe una cadena (sin espacios), y devuelve un booleano indicando si la
    cadena es o no un palíndromo.
    '''
    medio = len(cadena) // 2
    return wrapper(cadena, medio, bool=False)

def wrapper(cadena, medio, bool):
    if len(cadena) == 1:
        return bool
    if cadena[0] == cadena[-1]:
        return wrapper(cadena[1:-1], medio, bool=True)
    return bool

#def es_palindromo(cadena):
#    if not cadena:
#        return True
#
#    if cadena[0] != cadena[-1]:
#        return False
#
#    else:
#        return es_palindromo(cadena[1:-1])

#187
def contar_apariciones(s, c):
    '''
    Función recursiva que recibe una cadena s y un caracter c, y
    devuelve la cantidad de apariciones de c en s.
    '''
    return wrapper(s, c, apariciones=0)

def wrapper(s, c, apariciones):
    if not s or c not in s:
        return apariciones

    elif c == s[0]:
        return wrapper(s[1:], c, apariciones+1)
    return wrapper(s[1:], c, apariciones)

#188
def busqueda_binaria_recursiva(lista, elemento):
    '''
    Implementar el algoritmo de búsqueda binaria de manera recursiva.
    '''
    izq = 0
    der = len(lista) - 1
    return wrapper(lista, elemento, izq, der)

def wrapper(lista, elemento, izq, der):
    if der <= izq:
        return -1
    medio = (izq + der) // 2
    if lista[medio] == elemento:
        return medio

    if lista[medio] > elemento:
        return wrapper(lista, elemento, izq, medio-1)
    return wrapper(lista, elemento, medio+1, der)

#189
def merge(lista1, lista2):
    '''
    Función recursiva que recibe dos listas ordenadas y devuelve una lista con
    los elementos intercalados ordenadamente.
    '''
    return wrapper(lista1, lista2, i=0, j=0, res=[])

def wrapper(lista1, lista2, i, j, res):
    if not lista1 and not lista2:
        return res
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            res.append(lista1[i])
            return wrapper(lista1, lista2, i+1, j, res)
        res.append(lista2[j])
        return wrapper(lista1, lista2, i, j+1, res)

    res += lista1[i:]
    res += lista2[j:]
    return res

#190
def invertir_in_place(cola):
    '''
    Invierte in place la cola sin usar estructuras auxiliares
    '''
    if cola.esta_vacia():
        return
    dato = cola.desencolar()
    invertir_in_place(cola)
    cola.encolar(dato)
    return
