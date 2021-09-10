import csv
import random
from datetime import datetime
import random
#59
'''
Dada una partida en forma de una lista de tuplas de la forma <personaje>,<movimiento>
y un número k, imprimir por pantalla todos los movimientos notables de cada personaje
y cuántas veces se usaron. Se dice que un movimiento es notable si el personaje lo
utilizó más de k veces durante la partida. Ejemplo:

>>> movimientos = [("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"),
                   ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas")]
>>> imprimir_notables(movimientos, 1)
Charizard - Lanzallamas (2)
'''
def imprimir_notables(lista, k):
    movimientos = {}
    for personaje, movimiento in lista:
        if f"{personaje} - {movimiento}" not in movimientos:
            movimientos[f"{personaje} - {movimiento}"] = 0
        movimientos[f"{personaje} - {movimiento}"] += 1

    for accion in movimientos:
        if movimientos[accion] > k:
            print(f"{accion} ({movimientos[accion]})")

#lista = [("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"), ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas"), ("Pikachu", "Impactrueno")]

#60
'''
Escribir una función que dada una lista de tuplas, con el el año en el que se
disputó un mundial de fútbol y el equipo campeón de ese año, devuelva un diccionario
con la cantidad de mundiales ganados por cada equipo. Un ejemplo de la lista de tuplas:
[(1930, 'Uruguay'), (1934, 'Italia'), (1938, 'Italia'), ...] b.
Escribir otra función que reciba el diccionario generado en el punto anterior y
devuelva una lista con el/los paises que ganaron más mundiales.
'''
def mundialistas(lista):
    res = {}
    for anio, campeon in lista:
        if campeon not in res:
            res[campeon] = 0
        res[campeon] += 1
    return res

def lista_mundialistas(dict):
    res = []
    for clave in dict:
        if dict[clave] == max(dict.values()):
            res.append(clave)
    return res

#61
'''
Se propone implementar un sistema de criptografía sencillo en dónde cada carácter
del texto a codificar sea reemplazado por otro. Por ejemplo, un esquema posible
sería transformar todas las letras "a" en "b", todas las "b" en "c", etc.
Implementar una función que dada una cadena y un diccionario que represente la
tabla de transformación, devuelva la cadena codificada. Por ejemplo: si la cadena
es 'Hola' y el diccionario contiene {'H': 'e', 'o': 'b', 'l':'m'}, debe devolver 'ebma'.
'''
def codificar(cadena, dict):
    res = ""
    for c in cadena:
        if c in dict:
            res += dict[c]
        else:
            res += c
    return res


#62
'''
Escribir una función que reciba una cadena y devuelva un diccionario cuyas claves
sean las letras y cuyos valores sean la cantidad de apariciones de dicha letra.
Por ejemplo, si recibe 'catamarca' debe devolver: {'c':2, 'a':4, 't':1, 'r':1, 'm':1}.
'''
def contar_apariciones(cadena):
    res = {}
    for c in cadena:
        if c not in res:
            res[c] = 0
        res[c] += 1
    return res
#63
'''
Escribir una función que reciba una cadena y devuelva una tupla con la palabra
que tuvo mayor cantidad de apariciones, y la cantidad de apariciones que tuvo.
Si hay dos o más palabras con máxima cantidad de apariciones, devolver cualquiera
de ellas. La cadena contiene únicamente palabras y espacios.
Ejemplo: "la cama la silla y la mesa." → ("la", 3).
'''
def mayores_apariciones(cadena):
    dict = {}
    palabras_y_apariciones = []
    palabras = cadena.split()
    for palabra in palabras:
        if palabra not in dict:
            dict[palabra] = 0
        dict[palabra] += 1
    tuplas = dict.items()
    print(tuplas)
    return max(tuplas, key=lambda x: x[1])

#64
'''
Se tiene un diccionario de la forma {nombre_vendedor : total_vendido}, con la
suma total de lo vendido por distintos vendedores, y otro con forma
{local : [nombre_vendedor_1, nombre_vendedor_2, …]}, con los vendedores que
trabajan en cada local. Escribir una función que reciba diccionarios como los
mencionados, y devuelva un nuevo diccionario cuyas claves sean los nombres de
los locales y sus valores el total vendido por los vendedores de ese local.
'''
def ventas_locales(vendedores, locales):
    ventas = {}
    for local in locales:
        lista_vendedores = locales[local]
        if local not in ventas:
            ventas[local] = 0
        for vendedor in lista_vendedores:
            ventas[local] += vendedores[vendedor]

    return ventas

#vendedores = {'nombre_vendedor_1' : 1, 'nombre_vendedor_2' : 3, 'nombre_vendedor_3' : 2}
#locales = {'local1' : ['nombre_vendedor_1', 'nombre_vendedor_2'], 'local2' : ['nombre_vendedor_3'], 'local3' : ['nombre_vendedor_3']}

#65
'''
Escribir una función que reciba una cadena (formada únicamente por letras y espacios),
y devuelva un diccionario donde para cada palabra muestre la cantidad de veces que
es precedida por otra palabra.
Ejemplo: “a la a hola es a es la hora a hola” → {“a”: {“hora”: 1, “es”: 1, “la”: 1}, “hola”: {“a”: 2}, ... }
'''
def palabras_precedidas(cadena):
    res = {}
    palabras = cadena.split()
    for i in range(0, len(palabras) - 1):
        if palabras[i] not in res:
            res[palabras[i]] = {}
        if palabras[i+1] not in res[palabras[i]]:
            res[palabras[i]][palabras[i+1]] = 0
        res[palabras[i]][palabras[i+1]] += 1
    return res

#66
'''
Un grupo de amigos quieren juntarse a cenar pero tienen todos calendarios muy
ajustados y les es difícil ver qué días pueden juntarse todos. Se pide escribir
una función que reciba un diccionario con los nombres de cada persona, y que
como valor asociado tenga los días del mes en los que esa persona no puede juntarse
(una lista de números, que pueden ser del 1 al 31), y que devuelva un diccionario
con todos los días como claves (también del 1 al 31), y como valor qué amigos
pueden asistir cada día.
'''
def dias_libres(dias_ocupados):
    dias_libres = {}
    for i in range(1, 32):
        if i not in dias_libres:
            dias_libres[i] = []
        for persona in dias_ocupados:
            if dias_libres[i] in dias_ocupados[persona]:
                dias_libres[i].append(persona)
            else:
                continue
    return dias_libres

#67
'''
Escribir una función que reciba por parámetro una cadena y devuelva un diccionario
cuyas claves sean las primeras letras de cada palabra y cuyo valor asociado sea
una lista de palabras que empiezan con cada letra.
Por ejemplo, si recibe: 'Este es el parcial de algoritmos'. Debe devolver:
{'d':['de'], 'a':['algoritmos'], 'e':['Este','es','el'],'p':['parcial']}
'''
def iniciales(cadena):
    res = {}
    en_minusculas = cadena.lower()
    palabras = en_minusculas.split()
    for palabra in palabras:
        if palabra[0] not in res:
            res[palabra[0]] = []
        res[palabra[0]].append(palabra)
    return res

#68
'''
Se desea escribir una nota de rescate recortando letras de una revista. Escribir
una función que reciba por parámetro la nota que se desea escribir y el texto
completo de la revista, y devuelva True si la revista contiene todas las letras
necesarias para escribir la nota (ignorando mayúsculas y minúsculas), False en caso contrario.

Ejemplo: Si la revista contiene "Algoritmos y Programacion", podemos escribir la
nota "Gracias por la moto", pero no se puede escribir "Porotos amargos" (falta una s).
'''
def nota_rescate(nota, texto):
    letras = []
    res = []
    for letra in texto:
        letras.append(letra.lower())
        letras.append(letra.upper())

    for c in nota:
        if c in letras:
            res.append(c)
            letras.remove(c)

    res = "".join(res)
    if res == nota:
        return True
    else:
        return False

#69
'''
Se pide escribir una función que calcule el ganador de una liga de fútbol a
partir de los resultados de los partidos realizados. La función recibe una lista
de tuplas de 4 elementos con el siguiente formato:

(nombre_equipo1, goles_equipo1, nombre_equipo2, goles_equipo2)

Ejemplo: ("Barcelona", 1, "Real Madrid", 2).

La función devuelve el nombre del equipo ganador. En caso de haber más de un
equipo con puntuación máxima, devolver uno cualquiera de entre ellos.
Reglas de puntaje de la liga: el equipo ganador de un partido recibe 2 puntos,
y el perdedor 0 puntos. En caso de empate, cada uno de los dos equipos recibe 1 punto.
'''
def campeon_liga(lista):
    res = {}
    posibles_campeones = []
    for equipo1, goles1, equipo2, goles2 in lista:
        if goles1 > goles2:
            if equipo1 not in res:
                res[equipo1] = 0
            res[equipo1] += 3

        elif goles2 > goles1:
            if equipo2 not in res:
                res[equipo2] = 0
            res[equipo2] += 3

        elif goles1 == goles2:
            if equipo1 not in res and equipo2 not in res:
                res[equipo1] = 0
                res[equipo2] = 0
            res[equipo1] += 1
            res[equipo2] += 1

    for equipo in res:
        if res[equipo] == max(res.values()):
            posibles_campeones.append(equipo)
    return random.choice(posibles_campeones)
#70
'''
Se tiene un diccionario con las fechas de nacimiento de un conjunto de personas.
Las fechas están en formato DD/MM/YYYY. Ejemplo:

{"Juan": "27/05/1993", "Alicia": "30/11/1990", "Elena": "27/05/1985"}

Se pide escribir una función que reciba este diccionario y agrupe las personas
que celebran su cumpleaños el mismo día, devolviendo un diccionario en el que las
claves son fechas en formato DD/MM, y los valores listas de nombres. Ejemplo:

{"30/11": ["Alicia"], "27/05": ["Juan", "Elena"]}
'''
def mismo_cumpleanios(dict):
    res = {}
    fechas_cumpleanios = dict.values()
    for fecha in fechas_cumpleanios:
        fecha = fecha[0:5]
        if fecha not in res:
            res[fecha] = []
            for clave in dict:
                if fecha in dict[clave]:
                    res[fecha].append(clave)
    return res


#71
'''
Se cuenta con un diccionario cuyas claves son títulos de películas, y su valor
asociado su fecha de estreno, una cadena en formato DD/MM/AAAA. Escribir una
función que dado un diccionario de estas características, devuelva otro diccionario
cuyas claves sean el mes y el año en formato MM/AAAA, y su valor una lista con
todas las películas que se estrenaron en dicho mes y año.
'''
def lanzamientos(dict):
    res = {}
    for pelicula in dict:
        mes_anio = dict[pelicula][3:]
        if mes_anio not in res:
            res[mes_anio] = []
        res[mes_anio].append(pelicula)
    return res

#72
'''
Se tiene un diccionario donde cada clave es el título de una canción (cadena),
y cada valor la duración de la canción (en segundos).
Se tiene asimismo otro diccionario donde cada clave es el título de una lista de
reproducción (cadena), y cada valor una lista con títulos de canción que la componen.
Se pide implementar una función que reciba como parámetros ambos diccionarios,
y devuelva en forma de diccionario las duraciones de cada lista de reproducción.
(El diccionario devuelto debe tener como claves los títulos de lista, y como valor la duración en segundos.)
'''
def duraciones(canciones, listas):
    res = {}
    for lista in listas:
        if lista not in res:
            res[lista] = 0
        temas = listas[lista]
        for tema in temas:
            res[lista] += canciones[tema]

    return res


#73
'''
>>Escribir una función que dado un texto, devuelva un diccionario con la frecuencia
de cada palabra del texto.
>>Escribir una función que reciba un diccionario como el generado por la función
del ítem a y devuelva una lista con la/s palabras que tienen la máxima frecuencia.
'''
def frecuencia(cadena):
    res = {}
    palabras = cadena.split()
    for palabra in palabras:
        if palabra not in res:
            res[palabra] = 0
        res[palabra] += 1
    return res

def maxima_frecuencia(dict):
    res = []
    max_frecuencia = max(dict.values())
    for clave in dict:
        if dict[clave] == max_frecuencia:
            res.append(clave)
    return res

#74
'''
Escribir una función que dado un diccionario cuyas claves son los nombres de los
integrantes de un grupo de amigos, y los valores asociados una lista de los días
de la semana que están disponibles, devuelva una lista de los días que pueden
juntarse. Por ejemplo, si recibe: {'Juan':['MIE', 'VIE', 'SAB'],
'Jose':['VIE', 'SAB', 'DOM'], 'Jorge':['JUE', 'VIE', 'SAB']} debe devolver ['VIE', 'SAB']
'''
def dias_en_comun(dict):
    res = []
    temp = {}
    for persona in dict:
        for dia in dict[persona]:
            if dia not in temp:
                temp[dia] = 0
            temp[dia] += 1

    for dia in temp:
        if temp[dia] == len(dict):
            res.append(dia)
    return res

#75
'''
Escribir una función traducir_a_ingles, que recibe una cadena a traducir y un
diccionario cuyas claves son palabras en español y el valor asociado a cada una
es su traducción al inglés, y devuelva la cadena traducida. En caso que una palabra
de la cadena no se encuentre en el diccionario, la función debe incluir la palabra
sin traducir. Asumir que todas las palabras, tanto de la cadena como las del
diccionario, están en minúscula.
'''
def traducir_a_ingles(cadena, dict):
    palabras = cadena.lower().split()
    for i in range(len(palabras)):
        if palabras[i] in dict:
            palabras[i] = dict[palabras[i]]
        else:
            continue
    return " ".join(palabras)

#dict = {"hola": "hello", "cual": "what", "es": "is", "tu": "your", "nombre": "name"}
#cadena = "HOla cuAl es TU Nombre Amigo"

#76
'''
Escribir una función que reciba 3 diccionarios: cumpleaños: sus claves son nombres
de personas y los valores asociados, sus fecha de nacimiento (dd/mm/aaaa).
regalos: sus claves son nombres de personas y los valores asociados, el nombre
del regalo que quiere cada uno para su cumpleaños. precios: sus claves son nombres
de regalos y sus valores asociados, el precio de cada uno.

La función debe devolver otro diccionario donde la clave es el mes y el valor
asociado es la suma de los precios de los regalos de quienes cumplen años en ese mes.
'''
def calculadora_de_regalos(cumpleanios, regalos, precios):
    res = {}
    for nombre in cumpleanios:
        fecha = cumpleanios[nombre]
        dia, mes, anio = fecha.split("/")
        if mes not in res:
            res[mes] = 0
        regalo = regalos[nombre]
        res[mes] += precios[regalo]
    return res

#cumples = {"Santiago": "31/08/2000", "Magali": "10/04/2000", "Facundo": "10/01/2005", "Jose": "25/01/2005"}
#regalos = {"Santiago": "mouse", "Magali": "celular", "Facundo": "escritorio", "Jose": "campera"}
#precios = {"mouse": 500, "celular": 1600, "escritorio": 1000, "campera": 2000}

#77
'''
Se tiene un diccionario en el que la clave es el nombre de una persona y el valor
una lista con sus amigos. Ejemplo: {'Juan': ['Caro', 'José', 'Daniela', 'Alejandro'],
'Caro': ['José', 'Daniela'], 'José': ['Caro', 'Juan'], 'Daniela': [], 'Alejandro': ['Caro', 'José', 'Juan']}

Se quiere obtener una lista de tuplas con aquellas amistades que son correspondidas.
Se considera correspondida la amistad si un nombre está en mi lista y yo estoy
en la lista de ese nombre. Según el ejemplo dado, debe devolver:
[('Juan', 'José'), ('José', ‘Juan’), ('Juan', 'Alejandro'), ('Caro', 'José'), ('José', ‘Caro’) ('Alejandro', 'Juan')]
'''
def amistades_correspondidas(dict):
    res = []
    for amigo1 in dict:
        for amigo2 in dict[amigo1]:
            if amigo1 in dict[amigo2]:
                res.append((amigo1, amigo2))
    return res
#78
'''
Dado un diccionario cuyas claves son strings y sus valores son listas de enteros,
escribir una función que invierta dicho diccionario de la siguiente forma: cada
valor de cada lista pasará a ser una clave del diccionario resultante, que tendrá
como valor una lista de todas las claves en las que era un valor. Por ejemplo,
d = {"clave_1": [1,2,3], "clave_2": [4,6], "clave_3": [1,4]} dara como resultado
{1: ["clave_1", "clave_3"], 2: ["clave_1"], 3: ["clave_1"], 4: ["clave_2", "clave_3"], 6: ["clave_2"]}.
'''
def valor_a_clave(dict):
    res = {}
    for clave in dict:
        lista_enteros = dict[clave]
        for numero in lista_enteros:
            if numero not in res:
                res[numero] = []
            res[numero].append(clave)
    return res

#dict = {"clave_1": [1,2,3], "clave_2": [4,6], "clave_3": [1,4]}
#print(valor_a_clave(dict))

#79
'''
Escribir una función que dado un texto, una ruta a un archivo destino y una función
de traducción, escriba en el archivo destino de a una por linea las palabras
originales del texto cuya traducción sea más corta que la palabra original.

Por ejemplo, dada la función de traducción j del japonés y el texto "Día gracias",
debe escribir "Día" ya que j("Día") -> "hi" y j("gracias") -> "arigatou"
'''
def j(cadena):
    if cadena == "Día":
        return "hi"
    else:
        return "arigatou"

def funcion(texto, destino, f):
    palabras = texto.split()
    with open(destino, 'w', encoding="utf8") as traducciones:
        for palabra in palabras:
            traducida = f(palabra)
            if len(traducida) < len(palabra):
                traducciones.write(f'{palabra}\n')

    return

#80
'''
Implementar una función que dado el nombre de un archivo CSV de la forma
película;año;actor1,actor2,...,actorN devuelva un diccionario donde cada actor
tenga asociado una lista con todos los años en los que actuó sin repetir
(puede haber hecho varias peliculas en un mismo año). Cualquier línea con datos
inválidos (cualquier campo vacío o el año no es un número) debe ser ignorada y
la ejecución debe continuar. Se puede suponer que todas las líneas contienen
siempre tres elementos separados por ;.

peliculas.csv                                  >>> actores_años('peliculas.csv')
-------------                                  {"Guy Pearce": [2000, 2013, 2000],
Memento;2000;Guy Pearce,Joe Pantoliano          "Joe Pantoliano": [2000],
Iron Man 3;2013;Robert Downey Jr,Guy Pearce     "Robert Downey Jr": [2013]}
Sexto Sentido;;Bruce Willis
Rules Of Engagement;2000;Guy Pearce
'''
def anios_actuados(archivo):
    res = {}
    with open(archivo) as peliculas:
        peliculas_csv = csv.reader(peliculas, delimiter = ";")
        for pelicula, anio, reparto in peliculas_csv:
            reparto = reparto.split(",")
            for actor in reparto:
                if actor not in res:
                    res[actor] = []
                res[actor].append(anio)
    return res

#81
'''
Implementar una función que dado el nombre de un archivo de entrada y el de un
archivo de salida, reemplace todas las "s" del archivo original por "ch" y guarde
el resultado en el archivo de salida. El archivo no puede ser cargado en memoria
en su totalidad.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no),
todos los archivos abiertos deben quedar cerrados.
'''
def reemplazar_caracter(archivo_e, archivo_s):
    with open(archivo_e) as input_file, open(archivo_s, "w") as output_file:
        for linea in input_file:
            n_linea = ''
            for c in linea:
                if c in "sS":
                    n_linea += "ch"
                else:
                    n_linea += c
            output_file.write(n_linea)

#82
'''
Escribir una función que dado el nombre de un archivo devuelva un diccionario donde
la clave es el número de línea y su valor asociado la cantidad de palabras que tiene
esa línea. Asumir que cada línea contiene palabras separadas únicamente por espacios.
'''
def palabras_por_linea(archivo):
    res = {}
    with open(archivo) as file:
        for i, linea in enumerate(file):
            palabras = linea.rstrip("\n").split()
            if i not in res:
                res[i] = 0
            for palabra in palabras:
                res[i] += 1
    return res

#83
'''
Escribir una función que reciba el nombre de un archivo, el cual en cada línea
tiene como información un nombre y una edad, separados por una coma. Devolver en
forma de tupla la edad más alta y una lista de nombres de todas las personas que
tienen dicha edad. Se puede recorrer el archivo sólo una vez.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos
los archivos abiertos deben quedar cerrados.
'''
def personas_mayores(archivo):
    edad_personas = {}
    with open(archivo) as input_file:
        for linea in input_file:
            nombre, edad = linea.rstrip().split(",")
            if int(edad) not in edad_personas:
                edad_personas[int(edad)] = []
            edad_personas[int(edad)].append(nombre)

    return max(edad_personas.items())

#84
'''
Se cuenta con un archivo en formato csv que guarda información de pasajes de avión,
respetando la siguiente estructura: fecha,destino,precio. Escribir una función que
dada la ruta del archivo, devuelva un diccionario cuyas claves sean cada uno de
los destinos, y el valor asociado a cada clave una tupla (fecha, precio) con el
pasaje más barato para el destino.
'''
def pasajes(archivo):
    res = {}
    with open(archivo) as vuelos:
        vuelos_csv = csv.reader(vuelos, delimiter = ",")
        next(vuelos_csv)
        for fecha, destino, precio in vuelos_csv:
            fecha_actual, precio_actual = res.get(destino, (fecha, precio))
            if precio_actual <= precio:
                res[destino] = (fecha_actual, precio_actual)

    return res

#85
'''
Se tiene un archivo de texto donde cada línea es de la forma
nombre_jugador,puntaje_1,puntaje_2,...,puntaje_n, representando una serie de puntajes
obtenidos por un jugador (puede haber cualquier cantidad de puntajes para cada
jugador, pero todos tienen al menos uno). Los puntajes no tienen decimales.
Escribir un función que reciba el nombre de un archivo con la forma descripta y
el nombre de un archivo destino, y escriba en él líneas de la forma
nombre_jugador,puntaje_mas_alto, siendo puntaje_mas_alto el más alto de entre los puntajes de ese jugador.
'''
def escribir_mejores_puntajes(origen, destino):
    with open(origen) as file_o:
        with open(destino, "w") as file_d:
            for linea in file_o:
                dato = []
                linea = linea.rstrip("\n").split(",")
                dato.append(linea[0])
                dato.append(max(linea[1:]))

                file_d.write(dato[0])
                file_d.write(",")
                file_d.write(dato[1])
                file_d.write("\n")

    return

#86
'''
Se tiene una lista de los alumnos de una materia y se desea dividirlos en 3
grupos según resto del cociente entre el padrón del alumno y 3.

    Si el padrón es $12345$, se deberá hacer $12345 % 3 = 2$
    Si el padrón es $7774$ se deberá hacer $7774 % 3 = 1$
    Si el padrón es $36$ se deberá hacer $36 % 3 = 0$

La lista de los alumnos se encuentra en un archivo que tiene un número de padrón
por línea. Se pide escribir una función que reciba por parámetro el nombre del
archivo de alumnos y devuelva 3 archivos cuyos nombres tendrán el formato:
<nombre archivo alumnos>_Enunciado<número de grupo>.txt con la lista de padrones
correspondientes a cada grupo uno por línea.
'''
def agrupar_alumnos(archivo):
    grupos = {}
    with open(archivo) as file:
        for padron in file:
            numero_grupo = int(padron) % 3
            if numero_grupo not in grupos:
                grupos[numero_grupo] = []
            grupos[numero_grupo].append(padron.rstrip("\n"))

    for numero_de_grupo in grupos:
        with open(f"archivo_alumnos_grupo{numero_de_grupo}.txt", "w") as file:
            for padron in grupos[numero_de_grupo]:
                file.write(f"{padron}\n")

#87
'''
Se dispone de un archivo .csv sin encabezado. Se desconoce el total de columnas del mismo,
pero se sabe que:
    En la segunda columna se encuentran nombres de libros.
    En la tercer columna, los autores que los escribieron.
    Si lo escribió más de un autor, estarán separados por el caracter - .

Por lo que el archivo tendrá la forma: [Columna1, NombreLibro, Autores, Columna4, …, ColumnaN]
Escribir una función que reciba el nombre de dicho archivo y devuelve un diccionario
donde la clave sea un autor y el valor asociado una lista con los nombres de los libros escritos por el mismo.
Nota: al finalizar la ejecución de la función(haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
'''
def autores_y_obras(archivo):
    res = {}
    with open(archivo) as file:
        for linea in file:
            linea = linea.rstrip("\n").split(',')
            libro = linea[1]
            autores = linea[2].split("-")
            for autor in autores:
                if autor not in res:
                    res[autor] = []
                res[autor].append(libro)
    return res

#88
'''
Dado un archivo con el siguiente encabezado: Día,Mes,Año,Rubro,Gasto, ordenado
cronológicamente (el gasto más reciente está al final): escribir una función que
reciba el nombre de archivo y dos tuplas de la forma (mes, año). La función debe
devolver el nombre del rubro que más gastos lleva acumulados entre las fechas
dadas y dicho gasto acumulado.
'''
def obtener_mayor_gasto(archivo, tupla1, tupla2):
    gastos_por_rubro = {}
    with open(archivo) as file:
        for linea in file:
            dia, mes, anio, rubro, gasto = linea.rstrip("\n").split(",")
            if (tupla1[0] <= int(mes) <= tupla2[0]) and (tupla1[1] <= int(anio) <= tupla2[1]):
                if rubro not in gastos_por_rubro:
                    gastos_por_rubro[rubro] = 0
                gastos_por_rubro[rubro] += int(gasto)

#89
'''
Escribir una función que reciba la ruta a un archivo de texto, y devuelva el
promedio del largo de las palabras de dicho texto (considerando signos de puntuación
y otros símbolos como parte de la palabra).
'''
def promedio_len_palabras(archivo):
    suma_letras = 0
    suma_palabras = 0
    with open(archivo) as file:
        for linea in file:
            palabras = linea.rstrip("\n").split()
            for palabra in palabras:
                suma_palabras += 1
                for letra in palabra:
                    suma_letras += 1

    return suma_letras // suma_palabras

#90
'''
Se tiene un archivo que guarda las notas de los alumnos de una materia, con formato:
padron,nombre,nota1;nota2;nota3;....
Se sabe que para cada alumno hay por lo menos una nota, pero no cuántas hay exactamente.
Escribir una función que reciba la ruta a un archivo con ese formato y cree uno nuevo
llamado promedios.csv con formato nombre;promedio, calculando dicho promedio a partir
de las notas del alumno correspondiente.
'''
def alumno_promedio(archivo):
    with open(archivo) as file:
        with open("promedios.csv", "w") as dest:
            alumnos_csv = csv.writer(dest)
            for linea in file:
                datos_alumno = []
                datos = linea.rstrip("\n").split(",")
                nombre = datos[1]
                notas = datos[2:]
                suma = 0
                for nota in notas:
                    suma += int(nota)
                promedio = suma / len(notas)
                datos_alumno.append(nombre)
                datos_alumno.append(promedio)

                alumnos_csv.writelines(f"{datos_alumno[0]},{str(datos_alumno[1])}\n")
    return

#91
'''
Se tiene un archivo CSV de cuatro columnas con formato equipo,jugador,fecha,goles.
Se pide implementar una función que reciba el nombre del archivo como parámetro
y devuelva un diccionario con los goles por jugador por equipo.
Por ejemplo: { equipo1: { jugador1: 3, jugador2: 1 }, equipo2: { ... } ... }
'''
def goles_por_equipo(archivo):
    res = {}
    with open(archivo) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for equipo, jugador, fecha, goles in reader:
            if equipo not in res:
                res[equipo] = {}
            if jugador not in res[equipo]:
                res[equipo][jugador] = 0
            res[equipo][jugador] += int(goles)
    return res

#92
'''
Dado el nombre del archivo en el que están listadas las materias de la facultad con el formato:

dd.cc - nombre de materia

en dónde dd es el número del departamento y cc es el número de la materia, se pide escribir
una función que devuelva un diccionario que asocie códigos de departamento con una lista de
los nombres de las materias del departamento.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los
archivos abiertos deben quedar cerrados.
'''
def agrupar_departamento_materias(archivo):
    res = {}
    with open(archivo) as input_file:
        for linea in input_file:
            linea = linea.rstrip().split(" - ")
            departamento = linea[0].split(".")[0]
            materia = linea[1]
            if departamento not in res:
                res[departamento] = []
            res[departamento].append(materia)
    return res

#93
'''
Se tiene una lista de los alumnos de una materia, y se desea dividirlos en
dos grupos de prácticas: grupo 1 para los alumnos con padrón impar,
grupo 2 para los alumnos con padrón par.

La lista de alumnos se encuentra en un archivo en formato CSV.
Se desconoce el número de columnas, pero se sabe que la primera columna es siempre el padrón,
y que no hay cabecera.

Se pide escribir una función que reciba como parámetro el nombre del archivo de alumnos
y escriba dos archivos, grupo1.txt y grupo2.txt, con la lista de padrones correspondientes,
uno por línea.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no),
todos los archivos abiertos deben quedar cerrados.
'''
def agrupar_practicas(archivo):
    pares = []
    impares = []
    with open(archivo) as file:
        for linea in file:
            linea = linea.rstrip("\n").split(",")
            padron = linea[0]
            if int(padron) % 2 == 0:
                pares.append(str(padron))
            else:
                impares.append(str(padron))

    with open("grupo1.txt", "w") as file1:
        for padron in impares:
            file1.write(f"{padron}\n")

    with open("grupo2.txt", "w") as file2:
        for padron in pares:
            file2.write(f"{padron}\n")

#94
'''
Se tiene un archivo CSV de tres columnas llamado operaciones.csv. Las columnas son:
Cuenta (nombre de la cuenta, cadena), Operacion (tipo de la operación: "extraccion" o "deposito")
y Monto (valor de la operación, un entero positivo). El archivo está ordenado por el campo “Cuenta”.
Se pide escribir un programa que imprima por pantalla el balance de cada cuenta
tras procesar las operaciones presentes en el archivo. Se debe asumir un balance
inicial de 0. (Nota: las extracciones restan al valor del balance y los depósitos suman al mismo.)
'''
def procesar_balance(archivo):
    balances = {}
    with open(archivo) as file:
        for linea in file:
            cuenta, operacion, monto = linea.rstrip("\n").split(",")
            if cuenta not in balances:
                balances[cuenta] = 0
            if operacion == "extraccion":
                balances[cuenta] -= int(monto)
            if operacion == "deposito":
                balances[cuenta] += int(monto)
    return balances

def main():
    balances = procesar_balance("operaciones.csv")
    for clave in balances:
        print(f"{clave},{balances[clave]}")
#main()


#95
'''
Implementar una función que recibe el nombre de un archivo, cuyo contenido esta
en formato csv, con el ganador del torneo de water polo de cada año, y genere un
nuevo archivo con la cantidad de veces que ganó cada equipo. El archivo que se
recibe tiene los datos de la forma año,equipoCampeon, de a uno por línea.
'''
def campeones_waterpolo(archivo):
    res = {}
    with open(archivo) as file_i:
        reader = csv.reader(file_i, delimiter=',')
        next(reader)
        for año, campeon in reader:
            if campeon not in res:
                res[campeon] = 0
            res[campeon] += 1

    with open("res.csv", "w") as file_o:
        writer = csv.writer(file_o, delimiter=';')
        for campeon in res.items():
            writer.writerows([campeon])

#96
'''
Se cuenta con un archivo llamado ratings.csv que contiene en cada línea los puntajes
que los usuarios de un conocido sitio de música dan a los artistas que escuchan.
El formato del archivo es usuario,genero,artista,puntaje. Se pide realizar una
función que reciba por parámetro un nombre de género musical y cree un nuevo
archivo .csv que contenga todos los puntajes correspondientes a los artistas del
género. El formato debe ser usuario,artista,puntaje, y el nombre del archivo
creado debe ser el nombre del género.
(ejemplo, si el género recibido es "rock", el archivo se debe llamar rock.csv).
'''
def musica(archivo, genero_ingresado):
    res = []
    with open(archivo) as input_file:
        reader = csv.reader(input_file, delimiter=',')
        next(reader)
        for usuario, genero, artista, puntaje in reader:
            if genero_ingresado == genero:
                res.append((usuario, artista, puntaje))
    with open(f"{genero_ingresado}.csv", "w") as output_file:
        writer = csv.writer(output_file, delimiter=',')
        for puntuacion in res:
            writer.writerows([puntuacion])

#97
'''
Se tienen dos archivos cuyos campos son DNI,Apellido,Nombre, y están ordenados
por DNI. Escribir una función que reciba los nombres de dos archivos como los
mencionados, y genere un nuevo archivo que incluya los datos de ambos archivos
de entrada, también ordenados por DNI y sin duplicados.
'''
def ordenar_dnis(archivo1, archivo2):
    res = []
    with open(archivo1) as file1:
        for linea1 in file1:
            linea1 = linea1.rstrip("\n")
            if linea1 not in res:
                    res.append(linea1)
            else:
                continue

    with open(archivo2) as file2:
        for linea2 in file2:
            linea2 = linea2.rstrip("\n")
            if linea2 not in res:
                res.append(linea2)
    res = sorted(res)
    with open("organizados.txt", "w") as file3:
        for linea in res:
            file3.write(f"{linea}\n")

#98
'''
Escribir una función que reciba el nombre de un archivo cuyas líneas son de la
forma nombre_producto,cantidad_vendida, siendo nombre_producto una cadena con el
nombre de un producto y cantidad_vendida un entero con la cantidad que se vendió
de dicho producto. Los productos pueden repetirse, o sea que puede haber más de
una línea con el mismo nombre_producto. Crear un nuevo archivo con el mismo
formato, pero que cada nombre_producto sea único y la cantidad_vendida asociada
sea la suma de las cantidades vendidas de dicho producto del archivo recibido.
Puede suponerse que el archivo recibido no tiene errores de formato.
'''
def productos_vendidos(archivo):
    ventas = {}
    with open(archivo) as input_file, open("final.txt", "w") as output_file:
        for linea in input_file:
            producto, cant_ventas = linea.rstrip().split(",")
            if producto not in ventas:
                ventas[producto] = 0
            ventas[producto] += int(cant_ventas)

        for producto in ventas:
            output_file.write(f"{producto},{ventas[producto]}\n")

#99
'''
Escribir una función que dada una lista de compras en un diccionario de la forma
código:cantidad y una ruta a un archivo donde se encuentra la lista de precios
en formato csv: código,nombre,precio,descripción, imprima un listado por pantalla
de la forma <Nombre Producto> x <cantidad>: <precio total>
(Precio unidad: <precio unitario>) de aquellos productos comprados.
'''
#100
'''
Se tiene un archivo de valores separados por comas con los siguientes campos:
Provincia,Ciudad,Habitantes. Escribir una función que reciba la ruta de este
archivo y el nombre de una provincia, y devuelva la cantidad total de habitantes
que hay en ella.
'''
def obtener_habitantes(archivo, provincia):
    habitantes = 0
    with open(archivo) as file:
        for linea in file:
            datos = linea.rstrip("\n").split(",")
            if datos[0] == provincia:
                habitantes += int(datos[2])
    return habitantes

#101
'''
Escribir una funcion que reciba una lista de pedidos a un supermercado, donde
cada pedido es hecho por una persona distinta y puede tener cualquier producto,
y tiene la siguiente formato: { nombre_producto1: cant1, …, nombre_producto_n: cant_n }.
La función debe escribir a un archivo que tenga el resumen de los pedidos con el siguiente formato:
nombre_producto;cant_total
donde cada producto está una única vez y la cantidad total es la cantidad de todas las personas que compraron ese producto.
'''
def lista_de_pedidos(lista, mandados):
    temp = {}
    for pedido in lista:
        for producto in pedido:
            if producto not in temp:
                temp[producto] = 0
            temp[producto] += pedido[producto]

    with open(mandados, "w") as file:
        for pedido in temp:
            file.write(f"{pedido};{str(temp[pedido])}\n")
    return

#dict1 = {"choclo": 3, "jugo": 2, "papa": 5, "arroz": 1}
#dict2 = {"jugo": 3, "choclo":2}
#dict3 = {"arroz": 1, "pollo": 3}
#lista = [dict1, dict2, dict3]

#102
'''
Se tiene un archivo de texto que contiene un díálogo entre una cantidad de personas
desconocida, de manera que cada línea del archivo tiene este formato:

PersonaN: una frase de cierta cantidad de palabras

(asumir que las frases contienen únicamente palabras, no contienen signos de puntuacion,
ni numeros, ni ningun caracter que no sean letras o espacios).

Escribir una funcion que reciba la ruta a un archivo de este tipo y devuelva
cuantas veces dijo cada palabra cada una de las personas involucradas en el díalogo.
Es decir, debe devolver un diccionario con el siguiente formato:
{ persona_1: { palabra_1: cant_1, palabra_2: cant_2 }, persona_2: { ... } .. }
'''
def conversacion(archivo):
    res = {}
    with open(archivo, "r", encoding = "utf8") as file:
        for linea in file:
            linea = linea.rstrip("\n").split()
            persona = linea[0][0:-1]
            palabras = linea[1:]
            if not persona in res:
                res[persona] = {}
            for palabra in palabras:
                if not palabra in res[persona]:
                    res[persona][palabra] = 0
                if palabra in palabras:
                    res[persona][palabra] += 1
    return res

#103
'''
Suponiendo que se cuenta con la clase Vaca con el método sondear() que se comporta según el siguiente ejemplo:

>>> vaca = Vaca()
>>> vaca.sondear()
>>> "Muuuuu!"

Implementar la clase Ovni que cumpla el siguiente comportamiento:

>>> ovni = Ovni(“Stargazer”)                  >>> ovni.abducir(Vaca())
>>> print(ovni)                               EstacionDeSondeoOcupadaError
"Nave Stargazer (estación de sondeo vacía)"   >>> ovni.sondear()
>>> ovni.sondear()                            "Sondeando... ‘Muuuuu!’... Ups, el sujeto explotó"
EstacionDeSondeoVaciaError                    >>> print(ovni)
>>> ovni.abducir(Vaca())                      "Nave Stargazer (estación de sondeo vacía)"
>>> print(ovni)
"Nave Stargazer (estación de sondeo ocupada)"

Nota: Suponer que las excepciones EstacionDeSondeoVaciaError y EstacionDeSondeoOcupadaError ya existen.
'''
class EstacionDeSondeoVaciaError(Exception):
    pass

class EstacionDeSondeoOcupadaError(Exception):
    pass

class Vaca:
    def __init__(self):
        pass

    def sondear(self):
        return "Muuuuu!"

class Ovni:
    def __init__(self, nave):
        self.nave = nave
        self.estacion_de_sondeo = []

    def __str__(self):
        return f"Nave {self.nave} (estacion de sondeo {self.esta_vacia()})"

    def abducir(self, animal):
        if self.esta_vacia() == "vacia":
            self.estacion_de_sondeo.append(animal)
        else:
            raise EstacionDeSondeoOcupadaError

    def esta_vacia(self):
        if len(self.estacion_de_sondeo) == 0:
            return "vacia"
        else:
            return "ocupada"

    def sondear(self):
        if self.esta_vacia() == "vacia":
            raise EstacionDeSondeoVaciaError
        else:
            self.estacion_de_sondeo.pop(0)
            return "Sondeando... ‘Muuuuu!’... Ups, el sujeto explotó"

#104
'''
Se tiene implementada la clase Tatuaje(nombre,area,dolor) cuya área y dolor son enteros mayores a 0.
Implementar las clases Tatuador(nombre) y Brazo(area, aguante), que se comporten de la siguiente forma:

>>> tatuaje_dragon = Tatuaje("Dragón",10,30)    >>> tatuador.tatuar(brazo2, tatuaje_panda)
>>> tatuaje_panda = Tatuaje("Panda",10,10)      ValueError: Ya no te queda más lugar
>>> brazo1 = Brazo(20, 10)                      >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> brazo2 = Brazo(10, 100)                     >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> tatuador = Tatuador("Miguel")               >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> tatuador.tatuar(brazo1, tatuaje_dragon)     ValueError: Ya no te queda más lugar
ValueError: No te lo vas a bancar               >>> print(tatuador)
>>> tatuador.tatuar(brazo2, tatuaje_dragon)     Miguel: 3 tatuajes realizados
'''
class Tatuaje:
    def __init__(self, nombre, area, dolor):
        self.nombre = nombre
        self.area = area
        self.dolor = dolor

class Tatuador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.realizados = 0

    def __str__(self):
        return f"{self.nombre}: {self.realizados} tatuajes realizados"
    def tatuar(self, brazo, tatuaje):
        if brazo.aguante < tatuaje.dolor:
            raise ValueError("No te la vas a bancar")
        else:
            if brazo.area - tatuaje.area < 0:
                raise ValueError("Ya no te queda más lugar")
            else:
                brazo.area -= tatuaje.area
                self.realizados += 1

class Brazo:
    def __init__(self, area, aguante):
        self.area = area
        self.aguante = aguante

#105
'''
Asumiendo que ya existe una clase Pasajero(destino) cuyo destino es una cadena, implementar la clase Colectivo con los siguientes métodos:

    Un constructor, que crea un Colectivo vacío.
    Un método subir, que recibe un destino (en forma de cadena) y un pasajero lo agrega al colectivo.
    Un método bajar, que recibe un destino, saca del colectivo a los pasajeros que tienen dicho destino asignado, devolviéndolos en una lista.
'''
class Colectivo:
    def __init__(self):
        self.pasajeros = {}

    def __str__(self):
        return f"Pasajero : destino --> {self.pasajeros}"

    def subir(self, destino, pasajero):
        self.pasajeros[pasajero] = destino

    def bajar(self, destino):
        bajaron = []
        for pasajero in self.pasajeros:
            if self.pasajeros[pasajero] == destino:
                bajaron.append(pasajero)
        return bajaron

#106
'''
Escribir la clase Polinomio, utilizando una lista para guardar los coeficientes del mismo. Debe permitir las siguientes operaciones:

>>> p1 = Polinomio([2, 0, -1, 3])     >>> p1 == Polinomio([2, 0, -1, 3])
>>> print(p1)                         True
"2x^3 - x + 3"                        >>> p1 + p2
>>> p2 = Polinomio([1, 3])            ValueError("No tienen el mismo grado")
>>> print(p2)                         >>> p3 = p1 + Polinomio([0,1,1,-5])
"x + 3"                               >>> print(p3)
>>> p1 == p2                          "2x^3 + x^2 - 2"
False

Nota: no es necesario que el resultado de str() sea exactamente como en el ejemplo. Es válido también una representación como 2x^3 - 1x^1 + 3x^0

class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
        self.grado = len(coeficientes)

    def __str__(self):
        return f"{self.mostrar_complejo()}"

    def mostrar_complejo(self):
        res = ""
        contador = self.grado
        for c in self.coeficientes:
            if c >= 0 and c == self.coeficientes[0]:
                res += f"{c}x^{contador} "
            elif c > 0 and c == self.coeficientes[0]:
                res += f"-{c}x^{contador} "
            else:
                if c >= 0:
                    res += f"+ {c}x^{contador-1}"
                else:
                    res += f"- {c}x^{contador-1}"
        return res

    def __add__(self, otro_polinomio):
        nuevos_coeficientes = []
        if self.grado == otro.grado:
            for i in self.coeficientes:
                for j in otro_polinomio.coeficientes:
                    nuevos_coeficientes.append(i + j)
        else:
            raise ValueError("No tienen el mismo grado.")

        nuevo_polinomio = Polinomio([nuevos_coeficientes])
        return nuevo_polinomio

    def __sub__(self, otro_polinomio):
        nuevos_coeficientes = []
        if self.grado == otro.grado:
            for i in self.coeficientes:
                for j in otro_polinomio.coeficientes:
                    nuevos_coeficientes.append(i - j)

        else:
            raise ValueError("No tienen el mismo grado.")
        nuevo_polinomio = Polinomio([nuevos_coeficientes])
        return nuevo_polinomio

    def __eq__(self, otro_polinomio):
        return self.coeficientes == otro_polinomio.coeficientes
'''
#107
'''
Se tiene una clase Ejercicio con los métodos calificar(n) y obtener_nota(), que
reciben y devuelven, respectivamente, un número entero entre 0 y 10 (si no está
calificado, obtener_nota debe levantar una excepción).
Escribir una clase Examen que tenga los siguientes métodos:

    un constructor que cree un Examen nuevo en base a una lista de Ejercicios
    calificar(i,n), con i el número de ejercicio y n la calificación del mismo
    esta_aprobado(), que devuelve si un Examen está aprobado o no. Un examen está aprobado si tiene el 60% de los ejercicios con nota mayor o igual a 6.
    obtener_nota(), que devuelve la nota del Examen. Si esta aprobado, la misma es un promedio de la nota de todos los ejercicios. Sino, es un 2 independientemente del promedio.

class Ejercicio:
    def __init__(self):
        self.nota = None

    def calificar(self, n):
        self.nota = n
        return self.nota

    def obtener_nota(self):
        if self.nota is None:
            raise Exception("El ejercicio no fue calificado.")
        else:
            return self.nota

class Examen:
    def __init__(self, ejercicios):
        self.ejercicios = ejercicios
        self.nota_final = 0

    def calificar(i, n):
        self.ejercicios[i].calificar(n)

    def esta_aprobado(self):
'''


#108
'''
Implementar una clase Rectangulo que permita representar un rectángulo en R²
dadas sus coordenadas cartesianas (x1, y1, x2, y2).
Debe permitir las siguientes operaciones:

>>> r = Rectangulo(1, 6, 4, 4)
>>> r.ancho()
3
>>> r.alto()
2
>> q = r.mover(-2, 1)
>> print(r)
"Rectangulo(1, 6, 4, 4)"
>> print(q)
"Rectangulo(-1, 7, 2, 5)"
'''
class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.eje_x = (x1, x2)
        self.eje_y = (y1, y2)

    def __str__(self):
        return f"Rectangulo({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    def ancho(self):
        return max(self.eje_x) - min(self.eje_x)

    def alto(self):
        return max(self.eje_y) - min(self.eje_y)

    def mover(self, dx, dy):
        trasladado = Rectangulo(self.x1 + dx, self.y1 + dy, self.x2 + dx, self.y2 + dy)
        return trasladado

#109
'''
Implementar la clase Vector que replica el comportamiento de un vector de N dimensiones, de manera que se adecúe al funcionamiento mostrado por las siguientes sentencias:

>>> vector1 = Vector([3,4])                     >>> print(vector_suma)
>>> print(vector1)                              "(8, 9)"
"(3, 4)"                                        >>> vector1 + Vector([1,2,3])
>>> vector2 = Vector([])                        ValueError: No se pueden sumar dos vectores de distintas
ValueError: No se puede crear un vector vacío   dimensiones
>>> vector2 = Vector([5, 5])                    >>> vector1.norma()
>>> vector_suma = vector1 + vector2             5

Nota: no es necesario hacer más validaciones que las que se muestran en el ejemplo.
'''
class Vector:
    def __init__(self, coordenadas):
        if not coordenadas:
            raise ValueError(" No se puede crear un vector vacío")
        else:
            self.coordenadas = coordenadas

    def __str__(self):
        return f"{tuple(self.coordenadas)}"

    def norma(self):
        suma = 0
        for n in self.coordenadas:
            suma += n**2
        return suma**0.5

    def __add__(self, otro_vector):
        if len(self.coordenadas) != len(otro_vector.coordenadas):
            raise ValueError(" No se pueden sumar dos vectores de distintas dimensiones")
        else:
            res = []
            while len(self.coordenadas) > 0 and len(otro_vector.coordenadas) > 0:
                res.append(self.coordenadas.pop(0) + otro_vector.coordenadas.pop(0))
            return res

#110
'''
Escribir una clase Item, que recibe en su constructor el nombre del objeto y su peso.
Escribir también una clase Caja, que recibe en su constructor la capacidad de la misma (o sea, cuánto peso puede cargar).
Además, esta clase debe tener los siguientes métodos:
 >>>guardar_item, que recibe un Item y lo guarda en su interior, siempre y cuando tenga capacidad. Si no tiene capcidad, debe lanzar una excepción.
 >>>obtener_mas_pesado y obtener_mas_liviano, que devuelven el Item con mayor y menor peso, respectivamente.
    En ambos casos devuelve None si no hay items guardados, y si hay más de uno con el mismo peso devuelve cualquiera de ellos.
'''
class Item:
    def __init__(self, objeto, peso):
        self.objeto = objeto
        self.peso = peso

class Caja:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.objetos = []

    def guardar_item(self, item):
        if self.capacidad - item.peso < 0:
            raise ValueError("No hay capacidad para guardar el objeto.")
        else:
            self.capacidad -= item.peso
            self.objetos.append(item)

    def obtener_mas_liviano(self):
        if not self.objetos:
            return None

        mas_liviano = 0
        for i in range(1, len(self.objetos)):
            if self.objetos[i].peso < self.objetos[mas_liviano].peso:
                mas_liviano = i
            else:
                continue
        return self.objetos[mas_liviano].objeto

    def obtener_mas_pesado(self):
        if not self.objetos:
            return None

        mas_pesado = 0
        for i in range(1, len(self.objetos)):
            if self.objetos[i].peso > self.objetos[mas_pesado].peso:
                mas_pesado = i
            else:
                continue
        return self.objetos[mas_pesado].objeto

#111
'''
Escribir la clase Partido, que recibe en el constructor dos cadenas que corresponden al nombre del equipo local y el visitante (en ese orden).
Además, tiene los siguientes métodos:

 >>>cargar_resultado: Recibe dos números enteros, que corresponden a los goles convertidos por el local y el visitante (en ese orden).
 >>>obtener_ganador: Devuelve el nombre del equipo ganador, o None si hubo un empate.
 >>>obtener_perdedor: Similar a obtener_ganador, pero devuelve el perdedor o None.

Escribir la clase Liga, que tiene los siguientes métodos:

 >>>cargar_partido: Recibe un objeto de clase Partido, y guarda los datos necesarios.
 >>>obtener_campeon: Devuelve una cadena con el nombre del equipo que más puntos tiene.
    Si hay varios equipos que tengan el puntaje máximo, devolver el nombre de cualquiera ellos.
    Se otorgan 3 puntos por partido ganado, 1 por partido empatado y 0 por partido perdido.
    Este método debe ser lo más eficiente posible.
'''
class Partido:
    def __init__(self, local, visitante):
        self.local = local
        self.visitante = visitante
        self.resultado = {}

    def cargar_resultado(self, goles_local, goles_visitante):
        self.resultado[self.local] = goles_local
        self.resultado[self.visitante] = goles_visitante

    def obtener_ganador(self):
        if self.resultado[self.local] == self.resultado[self.visitante]:
            return None
        else:
            for equipo in self.resultado:
                if self.resultado[equipo] == max(self.resultado.values()):
                    return equipo

    def obtener_perdedor(self):
        if self.resultado[self.local] == self.resultado[self.visitante]:
            return None
        else:
            for equipo in self.resultado:
                if self.resultado[equipo] == min(self.resultado.values()):
                    return equipo

class Liga:
    def __init__(self):
        self.tabla = {}
        self.posibles_campeones = []

    def cargar_partido(self, partido_finalizado):
        if partido_finalizado.local not in self.tabla and partido_finalizado.visitante not in self.tabla:
            self.tabla[partido_finalizado[partido_finalizado.local]] = 0
            self.tabla[partido_finalizado[partido_finalizado.visitante]] = 0

        if partido_finalizado.obtener_ganador() is None:
            self.tabla[partido_finalizado[partido_finalizado.local]] += 1
            self.tabla[partido_finalizado[partido_finalizado.visitante]] += 1
        else:
            ganador = partido_finalizado.obtener_ganador()
            perdedor = partido_finalizado.obtener_perdedor()
            self.tabla[partido_finalizado[ganador]] += 3

    def obtener_campeon(self):
        for equipo in self.tabla:
            if self.tabla[equipo] == max(self.tabla.values()):
                self.posibles_campeones.append(equipo)

        if len(self.posibles_campeones) == 1:
            return self.posibles_campeones[0]
        else:
            return random.choice(self.posibles_campeones)

#112
'''
Escribir una clase Cuenta que tenga el siguiente comportamiento:

>>> c = Cuenta('Pérez')              >>> d = Cuenta('López')
>>> c.acreditar(100, 'Sueldo')       >>> c.transferir(30, d)
>>> c.extraer(60, 'Shopping')        >>> c.saldo()
>>> c.saldo()                        10
40                                   >>> d.saldo()
>>> print(c)                         30
Cuenta de Pérez

>>> c.movimientos()
[('acreditación',100,'Sueldo'),('extracción',60,'Shopping'), ('extracción',30,'Cuenta de López')]
>>> d.movimientos()
[('acreditación',30,'Cuenta de Pérez')]
>>> d.extraer(100, 'Deudas')
ERROR ValueError: Fondos Insuficientes
'''
class Cuenta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 0
        self.acciones = []

    def __str__(self):
        return f"Cuenta de {self.nombre}"

    def acreditar(self, monto, tipo):
        self.dinero += monto
        self.acciones.append(("acreditación", monto, tipo))

    def extraer(self, monto, tipo):
        if self.dinero - monto >= 0:
            self.dinero -= monto
            self.acciones.append(("extracción", monto, tipo))
        else:
            raise ValueError("Fondos Insuficientes")

    def transferir(self, monto, otra_cuenta):
        self.extraer(monto, f"Cuenta de {otra_cuenta.nombre}")
        otra_cuenta.acreditar(monto, f"Cuenta de {self.nombre}")

    def saldo(self):
        return self.dinero

    def movimientos(self):
        return self.acciones

#113
'''
Se pide implementar una clase CalendarioMes con los siguientes métodos:

    __init__(): toma como parámetro un entero que representa el número de días del mes (entre 28 y 31). Debe lanar una excepción si no es un día válido.
    agregar_evento(): toma como parámetro un día (número entero) y el nombre de un evento (cadena) y lo almacena en el calendario. Debe lanar una excepción si no es un día válido.
    eliminar_evento(): toma como parámetro un día y el nombre de un evento y lo elimina del calendario. Debe lanzar una excepción si no existe un evento con ese nombre.
    obtener_eventos_dia(): toma como parámetro un día y devuelve una lista con los eventos programados para ese día, o la lista vacía si no hay eventos en ese día. Debe lanar una excepción si no es un día válido.
'''
class CalendarioMes:
    def __init__(self, ultimo_dia):
        if ultimo_dia not in range(28, 32):
            raise Exception("Ultimo dia del mes no es valido.")
        else:
            self.ultimo_dia = ultimo_dia
        self.eventos = {}

    def agregar_evento(self, dia, evento):
        if dia > self.ultimo_dia:
            raise Exception("Dia no valido.")
        else:
            if dia not in self.eventos:
                self.eventos[dia] = []
            self.eventos[dia].append(evento)

    def eliminar_evento(self, dia, evento):
        if evento not in self.eventos.values():
            raise Exception("No existe un evento con ese nombre.")
        else:
            self.eventos[dia].remove(evento)

    def obtener_eventos_dia(self, dia):
        if dia not in self.eventos:
            raise Exception("No hay eventos en ese día.")
        else:
            return self.eventos[dia]

#114
'''
Se pide implementar la clase TwitterUser con los siguientes métodos:

    --->__init__(): recibe como parámetro el nombre del usuario.
    --->tweet(): recibe como parámetro un mensaje (se debe validar que no sobrepase
    los 280 caracteres) y lo agrega —con la fecha actual— a la lista de tuits del
    usuario. (Para obtener la fecha actual, se puede importar el módulo datetime, e invocar datetime.datetime.now())

    --->follow(): recibe como parámetro otro usuario (de tipo TwitterUser) y lo guarda como un usuario al que se está siguiendo.
    --->get_timeline(): devuelve una lista con los mensajes que tuitearon los usuarios a los que se está siguiendo.
    Debe ser una lista de tuplas tal que: (fecha, nombre_usuario, mensaje). Este método no toma parámetros, y la lista devuelta debe estar ordenada por fecha.
'''
class TwitterUser:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tuits = []
        self.siguiendo = []

    def __str__(self):
        for usuario in self.siguiendo:
            return f"{self.nombre}"

    def tweet(self, mensaje):
        if not len(mensaje) <= 280:
            raise Exception("El mensaje no debe sobrepasar los 280 caracteres.")
        else:
            fecha_actual = datetime.now()
            self.tuits.append((fecha_actual, mensaje))

    def follow(self, otro_usuario):
        if otro_usuario not in self.siguiendo:
            self.siguiendo.append(otro_usuario)
        else:
            raise Exception("Ya sigue a este usuario.")

    def get_timeline(self):
        res = []
        for usuario in self.siguiendo:
            for tuit in usuario.tuits:
                res.append(tuit)
        return sorted(res)

#115
'''
Implementar una clase Carta, que se crea a partir de un palo y un valor. Las cartas deben poder imprimirse de la forma <valor> de <palo>.
Las cartas deben poder compararse entre ellas: Una carta vale menos que otra si al ser del mismo palo su valor es menor,
o si al ser de distintos palos el propio es menor que el palo de la otra carta
(suponer que ya está implementada una clase Palo, que implementa los métodos __eq__, __lt__ y __str__).
'''
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}."

    def comparar(self, otra_carta):
        if self.valor < otra_carta.valor:
            print("Es menor.")
        else:
            print("Es mayor.")

#116
'''
Implementar la clase Caramelera, que recibe en su constructor la cantidad de caramelos que puede contener, y tiene el siguiente comportamiento:

>>> c = Caramelera(20)            >>> c.sacar_caramelos(50)
>>> c.poner_caramelos(10)        Traceback (most recent call last):
>>> c.sacar_caramelos(4)         ...
>>> c.caramelos()                ValueError: No quedan tantos caramelos!
6                                >>> c.poner_caramelos(50)
>>> print(c)                     Traceback (most recent call last):
Caramelera con 6/20 caramelos    ...
                                    ValueError: No queda lugar para tantos caramelos
'''
class Caramelera:
    def __init__(self, capacidad):
        self.cantidad = 0
        self.capacidad = capacidad

    def __str__(self):
        return f"Caramelera con {self.cantidad}/{self.capacidad} caramelos"

    def caramelos(self):
        return self.cantidad

    def poner_caramelos(self, cantidad):
        if self.cantidad + cantidad <= self.capacidad:
            self.cantidad += cantidad
        else:
            raise ValueError("No queda lugar para tantos caramelos")

    def sacar_caramelos(self, cantidad):
        if self.cantidad - cantidad >= 0:
            self.cantidad -= cantidad
        else:
            raise ValueError("No quedan tantos caramelos!")
#117
'''
Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la cantidad de localidades
para el mismo; de modo tal que cumpla el siguiente comportamiento:

>>> b = Boleteria("Rush",500)                       >>> b.localidades_agotadas()
>>> print(b)                                        False
Evento: Rush - Localidades vendidas: 0 de 500       >>> b.vender_localidades(100)
>>> b.vender_localidades(400)                       >>> b.localidades_agotadas()
>>> b.vender_localidades(200)                       True
Traceback (most recent call last):                  >>> print(b)
...                                                 Evento: Rush - Localidades vendidas: 500 de 500
ValueError: No hay localidades suficientes
'''
class Boleteria:
    def __init__(self, evento, localidades):
        self.evento = evento
        self.localidades = localidades
        self.vendidas = 0

    def __str__(self):
        return f"Evento: {self.evento} - Localidades vendidas: {self.vendidas} de {self.localidades}"

    def vender_localidades(self, n):
        if self.localidades - (n + self.vendidas) < 0:
            raise ValueError("No hay localidades suficientes.")
        else:
            self.vendidas += n

    def localidades_agotadas(self):
        return self.localidades == 0

#118
'''
Sabiendo que la clase Libro tiene los métodos obtener_autor y obtener_titulo que
devuelven cadenas de caracteres, escribir la clase Biblioteca con los métodos:

agregar_libro que recibe un Libro y lo agrega a la colección.

sacar_libro que recibe el nombre de un título y el de un autor y lo saca de la
biblioteca, devolviéndolo o levantando una excepción en caso de que los datos no
correspondan con los de algún libro agregado.

contiene_libro que recibe el nombre de un título y el de un autor y devuelve True
o False de acuerdo a si está en la colección o no.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} de {self.autor}"

    def obtener_autor(self):
        return f"{self.autor}"

    def obtener_titulo(self):
        return f"{self.titulo}"

class Biblioteca:
    def __init__(self):
        self.coleccion = []

    def __str__(self):
        return f"{self.mostrar_libros()}"

    def agregar_libro(self, libro):
        self.coleccion.append(libro)

    def sacar_libro(self, titulo, autor):
        if self.contiene_libro(titulo, autor):
            for libro in self.coleccion:
                if libro.titulo == titulo and libro.autor == autor:
                    self.coleccion.remove(libro)
                    return f"Sacamos --> {libro_a_devolver.titulo} de {libro_a_devolver.autor}"

        if not self.contiene_libro(titulo, autor):
            raise Exception("Ningun dato coincide con algun libro de la coleccion.")

    def contiene_libro(self, titulo, autor):
        for libro in self.coleccion:
            if libro.obtener_titulo() == titulo and libro.obtener_autor() == autor:
                return True
            else:
                return False

    def mostrar_libros(self):
        libro = ""
        for libro in self.coleccion:
            print(f"{libro}\n")
'''
#119
'''
Modelar en python:

Una clase App que permita crear aplicaciones con su nombre y una lista de sistemas operativos soportados.
Una clase Smartphone que permita crear smartphones con su nombre de modelo y su nombre de sistema operativo,
además de permitir instalar apps (debe poder almacenar la instancia de la App).

Los objetos instanciados de dichas clases deberán cumplir con el siguiente comportamiento:

>>> app_fb = App("Facebook", ["ios", "android"])    >>> nexus.instalar(app_itunes)
>>> app_tw = App("Twitter", ["ios", "android"])     Exception(“La app no es compatible
>>> app_itunes = App("iTunes", ["ios"])             con el sistema operativo”)
>>> nexus = Smartphone("Nexus 6P", "android")       >>> iphone.instalar(app_itunes)
>>> iphone = Smartphone("iPhone 7", "ios")          >>> iphone.instalar(app_tw)
>>> nexus.instalar(app_fb)                          >>> print(nexus)
>>> nexus.instalar(app_fb)                          Nexus 6P (android). Apps: Facebook
Exception(“La app ya está instalada”)               >>> print(iphone)
                                                    iPhone 7 (ios). Apps: Itunes, Twitter
'''
class App:
    def __init__(self, nombre, so_soportados):
        self.nombre = nombre
        self.so_soportados = so_soportados

class Smartphone:
    def __init__(self, modelo, so):
        self.modelo = modelo
        self.so = so
        self.instaladas = []

    def mostrar_instaladas(self):
        res = ""
        for app in self.instaladas:
            res += app.nombre + ", "
        return res[:-2]

    def __str__(self):
        return f"{self.modelo} ({self.so}). Apps : {self.mostrar_instaladas()}"

    def instalar(self, app):
        if app in self.instaladas:
            raise Exception("La app ya está instalada.")
        elif self.so not in app.so_soportados:
            raise Exception("La app no es compatible con el sistema operativo.")
        else:
            self.instaladas.append(app)

#120
'''
Escribir la clase NumeroComplejo, cuyo constructor recibe la parte real y la parte
imaginaria del número. Implementar los métodos suma y multiplicación; ambos reciben
otro NumeroComplejo, y devuelven un nuevo NumeroComplejo que es el resultado de la
operación. Además, al usar la funcion print sobre una instancia de esta clase,
se debe imprimir al número como a+bi. Realizar los chequeos correspondientes, lanzando excepciones cuando sea necesario.

Nota: la suma se calcula como $(a+bi) + (c+di) = (a+c)+(b+d)i$, y la multiplicación como $(a+bi) * (c+di) = (ac-bd)+(ad+bc)i$.
'''
class NumeroComplejo:
    def init(self, a, b):
        self.a = a
        self.b = b

    def str(self):
        return f"{self.a} + {self.b} i"

    def sumar(self, otro_complejo):
        nuevo_a = self.a + otro_complejo.a
        nuevo_b = self.b + otro_complejo.b
        nuevo_complejo = NumeroComplejo(nuevo_a, nuevo_b)
        return nuevo_complejo

    def multiplicar(self, otro_complejo):
        nuevo_a = (self.a * otro_complejo.a) - (self.b * otro_complejo.b)
        nuevo_b = (self.a * otro_complejo.b) + (self.b * otro_complejo.a)
        nuevo_complejo = NumeroComplejo(nuevo_a, nuevo_b)
        return nuevo_complejo
#121
'''
Escribir una clase FacebookUser que contenga los siguientes métodos:

    __init__: Recibe un nombre de usuario.
    __str__: Devuelve el nombre de usuario.
    publicar(post): Publica un post en el muro del usuario.
    agregar_amigo(otro_usuario): Convierte al usuario actual y a otro usuario en amigos. La amistad es recíproca, si Juan agrega como amigo a José, entonces Juan está dentro de los amigos de José.
    mostrar_amigos(): Devuelve una lista con los nombres de todos los amigos.
    mostrar_muro(): Muestra todos los posts del usuario ordenados de mas nuevo a más viejo
'''
class FacebookUser:
    def __init__(self, usuario):
        '''Inicializa la clase con un nombre de usuario pasado por parametro'''
        self.usuario = usuario
        self.posts = []
        self.amistades = []

    def __str__(self):
        '''Devuelve el nombre del usuario'''
        return f"{self.usuario}"

    def publicar_post(self, post):
        '''Publica un post en el muro del usuario'''
        self.posts.insert(0, post)

    def agregar_amigo(self, otro_usuario):
        '''Agrega a un amigo a la lista de amistades, si no existe el usuario lanza una excepcion y la amistad es reciproca'''
        if otro_usuario not in self.amistades:
            self.amistades.append(otro_usuario)
            otro_usuario.amistades.append(self.usuario)
        elif otro_usuario in self.amistades or self.usuario in otro_usuario.amistades:
            raise Exception("El usuario ya se encuentra en la lista de amigos.")

    def mostrar_amigos(self):
        '''Muestra la lista de amigos del usuario, en caso de estar vacia lanza una excepcion'''
        if not self.amistades:
            raise Exception("El usuario no tiene amigos.")
        else:
            print("Amigos recientemente agregados: ")
            for amistad in self.amistades:
                print(amistad)

    def mostrar_muro(self):
        '''Muestra las publicaciones del usuario, de la mas nueva a la mas vieja, de no haber publicaciones, lanza una excepcion'''
        if not self.posts:
            raise Exception("No hay posteos aún.")
        else:
            print("Ultimas publicaciones: ")
            for post in self.posts:
                print(f"{self.usuario}: {post}")

#122
'''
Se quiere modelar un perchero para colgar ropa. Se pide crear las clases Perchero y Prenda tal que se se puedan ejecutar las siguientes líneas de código
y se obtengan los resultados especificados. El constructor de Perchero recibe la cantidad de espacio total disponible, y el de Prenda recibe el nombre de la prenda y cuánto espacio ocupa:

>>> p = Perchero(3)
>>> p.colgar(Prenda('camisa', 1))
>>> p.colgar(Prenda('pantalon', 1))
>>> p.sacar('pantalon')
Prenda('pantalon', 1)
>>> p.sacar('remera')
Exception: No se encontró la prenda
>>> p.espacio_disponible()
2
>>> p.colgar(Prenda('campera', 3))
Exception: No hay espacio para colgar la prenda
'''
class Prenda:
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio

class Perchero:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.prendas = []

    def colgar(self, prenda):
        if self.capacidad - prenda.espacio < 0:
            raise Exception("No hay espacio para colgar la prenda.")
        else:
            self.prendas.append(prenda)
            self.capacidad -= prenda.espacio

    def sacar(self, prenda):
        for p in self.prendas:
            if p.nombre == prenda:
                print(p)
                self.prendas.remove(p)
                self.capacidad += p.espacio
        else:
            raise Exception("No se encontró la prenda")

    def espacio_disponible(self):
        print(self.capacidad)

#123
'''
Implementar la clase Botella que cumpla con el siguiente comportamiento:

>> botella = Botella(500)      >> botella.cargar(300)
>> print(botella)              Exception(“La botella no cuenta con capacidad suficiente”)
Botella: 0/500cc               >> botella.servir(200)
>> botella.esta_vacia()        >> print(botella)
True                           Botella: 100/500cc
>> botella.cargar(300)         >> botella.servir(200)
>> print(botella)              Exception(“La botella no cuenta con carga suficiente”)
Botella: 300/500cc
'''
class Botella:
    def __init__(self, capacidad):
        self.cantidad = 0
        self.capacidad = capacidad

    def __str__(self):
        return f"Botella: {self.cantidad}/{self.capacidad}cc"

    def esta_vacia(self):
        return self.cantidad == 0

    def cargar(self, cantidad):
        if self.cantidad + cantidad <= self.capacidad:
            self.cantidad += cantidad
        else:
            raise Exception("La botella no cuenta con capacidad suficiente")

    def servir(self, cantidad):
        if self.cantidad - cantidad >= 0:
            self.cantidad -= cantidad
        else:
            raise Exception("La botella no cuenta con carga suficiente")

#124
'''
Para desarrollar un videojuego necesitamos que todos los personajes tengan una cantidad de vida entre 0 y 100,
y un valor de daño de ataque. Cuando un personaje ataca a otro, se le resta el daño del atacante a su cantidad de vida.
Se dice que un personaje está muerto si su cantidad de vida llega a 0.

Implementar la clase Personaje con los siguientes métodos:

    El constructor recibe el daño que hace su ataque. La cantidad de vida arranca sendo 100.
    esta_muerto() que debe informar si el personaje está muerto
    atacar() que recibe otro personaje. Si alguno de los dos personajes está muerto debe lanzar una excepción. En caso contrario debe atacar al personaje recibido.
    curar() que recibe una cantidad de vida a regenerar. La vida máxima no se modifica. Si el personaje está muerto, debe lanzar una excepción.
'''
class Personaje:
    def __init__(self, ad):
        self.ad = ad
        self.hp = 100

    def esta_muerto(self):
        return self.hp == 0

    def atacar(self, otro_personaje):
        if self.esta_muerto() or otro_personaje.esta_muerto():
            raise Exception("Un personaje ya esta muerto.")
        else:
            otro_personaje.hp -= self.ad

    def curar(self, heal):
        if self.esta_muerto():
            raise Exception("El personaje ya esta muerto.")
        else:
            self.hp += heal

#125
'''
Implementar la clase CajaFuerte que reproduzca el siguiente comportamiento:

>> > caja = CajaFuerte(9158)
>> > caja.esta_abierta()
False
>> > caja.guardar("pulsera")
Exception: La caja fuerte está cerrada
>> > caja.abrir(1234)
Exception: La clave es inválida
>> > caja.abrir(9158)
>> > caja.esta_abierta()
True
>> > caja.guardar("pulsera")
>> > caja.guardar("reloj de oro")
Exception: No se puede guardar más de una cosa
>> > caja.cerrar()
>> > caja.sacar()
Exception: La caja fuerte está cerrada
>> > caja.abrir(9158)
>> > caja.sacar()
'pulsera'
>> > caja.sacar()
Exception: No hay nada para sacar
'''
class CajaFuerte:
    def __init__(self, clave):
        self.clave = clave
        self.abierta = False
        self.objetos = []

    def abrir(self, entrada):
        if self.clave == entrada:
            self.abierta = True
        else:
            raise Exception("La clave es inválida")

    def cerrar(self):
        self.abierta = False

    def esta_abierta(self):
        return self.abierta

    def guardar(self, objeto):
        if self.abierta and len(self.objetos) == 0:
            self.objetos.append(objeto)
        elif not self.abierta:
            raise Exception("La caja fuerte está cerrada")
        elif self.abierta and len(self.objetos) == 1:
            raise Exception("No se puede guardar más de una cosa")

    def sacar(self):
        if self.abierta and len(self.objetos) == 1:
            return self.objetos.pop()
        elif not self.abierta:
            raise Exception("La caja fuerte está cerrada")
        elif self.abierta and len(self.objetos) == 0:
            raise Exception("No hay nada para sacar")
