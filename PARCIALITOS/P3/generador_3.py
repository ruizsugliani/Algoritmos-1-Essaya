from pila import Pila
from cola import Cola
#144
'''
Se está organizando una fiesta y se conoce la hora de entrada y salida de los
N invitados. A cada invitado se le asigna uno de los 3 espacios que hay para
estacionar. Cada espacio tiene el ancho de un auto pero el largo de varios,
por lo que cada auto que llega bloquea a los que ya estaban previamente.
Hacer una función que dada una lista con tuplas (<hora>,<entra/sale>,<invitado>,<espacio>)
que están ordenadas por hora, indique si la asignación de espacios es válida.
Una asignación es inválida si algún invitado no puede salir a su horario designado porque hay otro auto bloqueándole la salida.

Ejemplo: [(21,ENTRA,"Blas",2), (22,ENTRA,"Ailín",2), (23.5,SALE,"Blas",2), (24,SALE,"Ailín",2)]
no es una asignación válida porque el auto de Ailín no deja salir a Blas a horario.
En cambio ésta sí es válida: [(21,ENTRA,"Blas",2), (22,ENTRA,"Ailín",2), (23,SALE,"Ailín",2), (23.5,SALE,"Blas",2)].
'''
#145
'''
Escribir una función reemplazar que tome una pila, un valor_nuevo y un valor_viejo
y reemplace en la pila todas las ocurrencias de valor_viejo por valor_nuevo. Al
finalizar la ejecución, la pila debe quedar en el mismo estado que tenía antes de ejecutarse.
'''
def reemplazar(pila, valor_viejo, valor_nuevo):
	temporal = Pila()
	while not pila.esta_vacia():
		dato = pila.desapilar()
		if dato == valor_viejo:
			temporal.apilar(valor_nuevo)
		else:
			temporal.apilar(dato)

	while not temporal.esta_vacia():
		numero_final = temporal.desapilar()
		pila.apilar(numero_final)


pila_inicial = Pila()
pila_inicial.apilar(1)
pila_inicial.apilar(2)
pila_inicial.apilar(4)
pila_inicial.apilar(1)
pila_inicial.apilar(1)
pila_inicial.apilar(1)
pila_inicial.apilar(1)
pila_inicial.apilar(1)
reemplazar(pila_inicial, 1, 7)


#146
'''
Implementar el siguiente algoritmo para convertir un entero positivo n de base 10 a binario.
a. Crear una pila.
b. Obtener el resto de la división entre el número n y 2 y apilarlo.
c. Dividir a n por 2
d. Volver al paso $b$ y continuar mientras que el valor de n sea mayor a 0. e. Imprimir el contenido de la pila.
'''
#147
'''
Escribir una función que reciba por parámetro dos pilas y modifique su contenido
de manera que los elementos de la primer pila queden en la segunda, y los de la
segunda en la primera manteniendo el orden original de los elementos. Como
estructuras auxiliares, se pueden utilizar únicamente pilas y/o colas.
'''
def intercambiar_pilas(pila1, pila2):
    temp1 = Pila()
    temp2 = Pila()
    while not pila1.esta_vacia():
        temp1.apilar(pila1.desapilar())
    while not pila2.esta_vacia():
        temp2.apilar(pila2.desapilar())

    while not temp1.esta_vacia():
        pila2.apilar(temp1.desapilar())
    while not temp2.esta_vacia():
        pila1.apilar(temp2.desapilar())

pila1 = Pila()
pila1.apilar(3)
pila1.apilar(2)
pila1.apilar(1)

pila2 = Pila()
pila2.apilar(9)
pila2.apilar(8)
pila2.apilar(7)

intercambiar_pilas(pila1, pila2)

#148
'''
Escribir una función que reciba una pila de números y elimine de la misma los
elementos consecutivos que estén repetidos. La función debe actuar in place
sobre la pila que recibe por parámetro. Por ejemplo:

remover_duplicados_consecutivos(Pila([2, 5, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 8, 7]))
    → Pila([2, 5, 8, 3, 2, 3, 1, 8, 7])

En caso afirmativo, Indicar el orden en que se efectuaron las operaciones. En caso contrario, justificar.
'''
#149
'''
Escribir una función intercalar(pilas) que reciba una secuencia de pilas y
devuelva una pila con los elementos de todas las pilas intercalados, manteniendo
el orden relativo. Las pilas originales deben quedar vacías. Ejemplo:

intercalar([Pila(1, 2), Pila(3, 4, 5, 6), Pila(7)]) → Pila(1, 3, 7, 2, 4, 5, 6)
'''
#150
'''
Escribir una funcion transferir(p1, p2) que recibe dos pilas y transfiere todos
los elementos de p1 al tope de p2, de forma tal que queden en el mismo orden
(es decir, el elemento que estaba inicialmente en el tope de p1 debe quedar en
el tope de p2). La pila p1 debe quedar vacía al finalizar la función
'''
def transladar_a_p2(pila1, pila2):
	temp = Pila()
	while not pila1.esta_vacia():
		temp.apilar(pila1.desapilar())

	while not temp.esta_vacia():
		pila2.apilar(temp.desapilar())

pila1 = Pila()
pila1.apilar(6)
pila1.apilar(5)
pila1.apilar(4)

pila2 = Pila()
pila2.apilar(9)
pila2.apilar(8)
pila2.apilar(7)

transladar_a_p2(pila2, pila1)

#151
'''
Implementar una función que calcule el promedio de los elementos de una pila de
números que recibe por parámetro. La pila debe quedar en el mismo estado en el
que fue recibida (con los mismos elementos y en el mismo orden).
'''
def promediar_pila(pila):
	temp = Pila()
	suma = 0
	cantidad = 0
	while not pila.esta_vacia():
		dato = pila.desapilar()
		suma += dato
		cantidad += 1
		temp.apilar(dato)

	while not temp.esta_vacia():
		pila.apilar(temp.desapilar())
	return suma / cantidad

pila2 = Pila()
pila2.apilar(9)
pila2.apilar(8)
pila2.apilar(7)

promediar_pila(pila2)

#152
'''
Dada una pila y un número n que representa una cantidad de elementos, se pide
implementar una función que devuelva una lista con pilas de n elementos,
preservando el orden de los elementos en la pila original. La pila original
debe quedar vacía. Ejemplo:

dividir_pila(Pila(1,2,3,4,8,6,7), 3) → [Pila(1,2,3), Pila(4,8,6), Pila(7)]

Nota: el tope de las pilas representadas es el primer elemento listado; por ejemplo, el tope de la pila original es el 1.
'''
#153
'''
Se cuenta con una cadena de caracteres que representa un conjunto de operaciones
a realizar con una pila: cada caracter representa la inserción de un número o
extracción. En caso de que el caracter sea numérico, se deberá insertar el valor
numérico en la pila. Caso contrario, se quita el tope de la pila. Se pide realizar
una función que, dada una pila y una cadena, realice sobre la pila las operaciones
indicadas en la cadena y luego devuelva la sumatoria de los elementos que quedaron
en la pila al terminar las operaciones. Nota: Se garantiza que el orden de las
operaciones indicadas por la cadena pueden realizarse sobre la pila recibida por
parámetro. Ejemplo: procesar('85x179xx') → (8 + 1) → 9
'''
#154
'''
Implementar una función que reciba una pila de números enteros ordenados
ascendentemente y determine si todos los números son consecutivos.
La pila debe preservar su estado inicial. Ejemplo:

consecutivos(Pila(1,2,3,4,5,6)) → True
consecutivos(Pila(1,2,4,5,6,7)) → False # 2 y 4 no son consecutivos
'''
#155
'''
Implementar una función que, dada una pila de números, devuelva otra pila que
contenga únicamente los números pares de ésta (manteniendo el orden relativo de
los elementos según como estaban en la original). La pila original debe preservar
su estado original al salir de la función. Es decir, debe conservar todos los
elementos que tenía y el orden de los mismos antes de que la función fuese invocada.
'''
def elementos_pares(pila):
	temp = Pila()
	pila_pares = Pila()
	while not pila.esta_vacia():
		temp.apilar(pila.desapilar())

	while not temp.esta_vacia():
		dato = temp.desapilar()
		if dato % 2 == 0:
			pila.apilar(dato)
			pila_pares.apilar(dato)
		else:
			pila.apilar(dato)

	return pila_pares

pila = Pila()
pila.apilar(6)
pila.apilar(5)
pila.apilar(4)
pila.apilar(3)
pila.apilar(2)
pila.apilar(1)
elementos_pares(pila)

#156
'''
Dada una pila de enteros, escribir una función que determine si es piramidal.
Una pila de enteros es piramidal si cada elemento es menor a su elemento inferior
(el elemento inferior es el siguiente en el sentido hacia la base de la pila).
Al finalizar la ejecución, la pila debe quedar en el mismo estado con el que empezó.
'''
def es_piramidal(pila):
	temp = Pila()
	res = True
	while not pila.esta_vacia():
		dato = pila.desapilar()
		if temp.esta_vacia():
			temp.apilar(dato)
		else:
			if dato == temp.ver_tope() +1:
				temp.apilar(dato)
			else:
				temp.apilar(dato)
				res = False
	while not temp.esta_vacia():
		pila.apilar(temp.desapilar())
	return res

pila = Pila()
pila.apilar(6)
pila.apilar(5)
pila.apilar(4)
pila.apilar(3)
pila.apilar(2)
pila.apilar(1)

es_piramidal(pila)

#157
'''
Se realizan sobre una pila, una secuencia de operaciones de apilar() y desapilar().
Las operaciones de apilar() apilarán, de a uno, los números del 0 al 9 en orden
(el primer apilar() apilará el 0, el segundo apilar() el 1, y así hasta que el
décimo apilar() apile el 9). Cada operación de desapilar(), además de desapilar
el elemento, lo imprimirá por pantalla. Determinar cuáles de las siguientes
opciones no es posible que ocurra. Para cada una de las que sí son posibles,
dar una secuencia de llamadas a apilar() y desapilar() que la cumpla.

a. 4 3 2 1 0 9 8 7 6 5
b. 4 6 8 7 5 3 2 9 0 1
c. 2 5 6 7 4 8 9 3 1 0
d. 4 3 2 1 0 5 6 7 8 9
'''
#158
'''
Se quiere escribir una función que sea capaz de sumar dos números que se
encuentran representados como pilas de sus dígitos. Los números a sumar pueden
tener cualquier cantidad de dígitos, y a su vez, no tener la misma cantidad de
dígitos uno que el otro.
'''
#159
'''
Escribir una función clonar_pila, que reciba por parámetro una pila y
devuelva una nueva pila con los elementos de la primera manteniendo el
orden original.
Nota: la pila recibida debe quedar en su estado original.
'''
def clonar(pila):
	temp = Pila()
	res = Pila()
	while not pila.esta_vacia():
		temp.apilar(pila.desapilar())

	while not temp.esta_vacia():
		dato = temp.desapilar()
		pila.apilar(dato)
		res.apilar(dato)
	return res

pila = Pila()
pila.apilar(6)
pila.apilar(5)
pila.apilar(4)

clonar(pila)

#160
'''
Escribir una función que recibe una cola e invierte el orden de sus elementos.
La función debe modificar la Cola recibida, no devolver una nueva ni tampoco
debe usar estructuras auxiliares.
'''
#161
'''
Escribir una función tail, que recibe una ruta a un archivo de texto y un número
n, y que imprima por pantalla las últimas n líneas del archivo. No está permitido
almacenar todo el archivo en memoria ni recorrer el archivo más de una vez.
'''
#162
'''
Se tiene una cola de gente en el Parque de la Costa y el dueño, en honor al
cumpleaños de su tía Marta decide reacomodar la cola y priorizarle el lugar a
las personas cuyo nombre comienza con M. Para ello hay que realizar una función
que reciba una cola con nombres y reubique aquellos nombres que comienzan con M
dejándolos primeros, siempre respetando el orden de llegada relativo entre
aquellos que tengan la misma condición (entre las personas que empiezan con
M por un lado, y entre los que no por otro).
'''
#163
'''
Escribir una función que, dada una cola y un elemento E, devuelva cuántos elementos
faltan para que salga E de la cola. Si E no está en la cola, debe levantarse una
excepción. Al finalizar la ejecución, La cola debe quedar en su estado original
para cualquiera de los casos posibles.
'''
#165
'''
Implementar una función que reciba una cola y un elemento y modifique la cola
original eliminando todas las apariciones del elemento recibido por parámetro.
El resto de los elementos deben preservar el orden original en el que estaban.
'''
#166
'''
El profesor $H$ dicta n materias. Para la primera fecha de final debe corregir
los trabajos prácticos de todas ellas. Nos pide un algoritmo que dada una cola
de alumnos, devuelva un diccionario cuyas claves son las materias, y el valor
una cola con los alumnos que rinden esa materia, respetando el orden original de llegada.

Considerar implementada la clase Alumno que tiene un método obtener_materia(),
que devuelve la materia que viene a presentar.
'''
#167
'''
Escribir una función que recibe una cola y un número k, y devuelve una lista de
k colas, con los elementos de la cola original asignados en forma balanceada
(las k colas deben quedar con aproximadamente la misma cantidad de elementos),
y alternada. Ejemplos:

repartir(Cola([a,b,c,d,e,f,g]), 2) → [Cola([a,c,e,g]), Cola([b,d,f])]
repartir(Cola([a,b,c,d,e,f,g]), 3) → [Cola([a,d,g]), Cola([b,e]), Cola([c,f])]
repartir(Cola([a b c]), 4)         → [Cola([a]), Cola([b]), Cola([c]), Cola([])]
'''
#168
'''
Implementar una función intercalar(colas) que reciba una secuencia de colas y
devuelva una cola con los elementos de todas las colas intercalados, manteniendo
 el orden relativo. Las colas originales deben quedar vacías. Ejemplo:

intercalar([Cola(1, 2), Cola(3, 4, 5, 6), Cola(7)]) → Cola(1, 3, 7, 2, 4, 5, 6)
'''
#169
'''
Sabiendo que se cuenta con una clase Cola con las primitivas encolar, desencolar
y esta_vacia, implementar la clase ColaConPrioridad. Este nuevo tipo debe tener
los métodos encolar(elemento), encolar_prioritario(elemento), desencolar() y
esta_vacia(); y al desencolar debe priorizar aquellos elementos que fueron encolados
con prioridad; es decir, no deben salir elementos comunes de la estructura si no
salieron previamente todos los elementos con prioridad.
'''
#170
'''
Escribir una función cola_map(cola, f) que reciba por parámetro una cola y una
función, y devuelva una nueva cola aplicando sucesivamente la función f a cada
elemento de la cola original (que debe quedar en el mismo estado con el que empezó
al finalizar la ejecución de la función)
'''
#171
'''
Escribir una función cola_dividir(cola, f) que reciba por parámetro una cola y
una función, y devuelva dos colas: una que contenga los elementos de la cola
original para los cuales f(elemento) → True (respetando el orden), y otra con
los elementos para los cuales la función dio False (también respetando el orden).
La cola original debe quedar en el mismo estado con el que empezó al finalizar la
ejecución de la función
'''
#174
'''
Escribir una función que, dada una cola y un elemento, devuelva un booleano que
indique si el elemento se encuentra o no en la cola. La cola debe quedar en su
estado original.
'''
#175
'''
Escribir una función cola_filter(cola, f) que reciba una cola y una función por
parámetro y devuelva una nueva cola que contenga sólo los elementos para los
cuales la función aplicada a ellos devuelva True. No es necesario que la cola
original quede en su estadio inicial.
'''
#176
'''
Se encontraron incongruencias en los planes preventivos de la pandemia de COBID20.
El plan del país lleva una serie de fases a cumplir las cuales estan insertadas
 en una cola de menor a mayor. De alguna manera hay fases intercaladas que no
 estaban en el plan y se nos exige removerlas. Se pide entonces escribir una
 funcion que dada dicha cola de fases, la modifique de forma que sólo quede una
 serie de fases ordenadas. Ejemplo:

Para la cola:
sale <| 1 2 6 3 5 4 5 6 7 |< entra
debería quedar la cola:
sale <| 1 2 6 7 |< entra

Para la cola:
sale <| 1 5 4 3 2 8 |< entra
debería quedar la cola:
sale <| 1 5 8 |< entra
'''
