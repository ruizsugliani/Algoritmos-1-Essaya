"""
2) Implementar la clase ColaDistribuidora con los siguientes métodos:
* ColaDistribuidora(ids, f): Crea una nueva instancia. ids es una lista de
    identificadores (cadenas), y f es una función que recibe cualquier cosa y
    devuelve siempre uno de los identificadores de la lista ids.
* encolar(elemento): Aplica la funcion f al elemento, y según el identificador
    obtenido encola el elemento en una cola específica para ese identificador.
* desencolar(identificador): Desencola y devuelve el elemento al frente de la
    cola para el identificador dado.
* esta_vacia(): devuelve verdadero si todas las colas están vacías.
"""

class ColaDistribuidora:
    def __init__(self, ids, f):
        self.ids = ["Juan", "Pepe", "Diego"]
        self.f = f
        self.colas = [Cola() for _ in range(len(self.ids))]

    def encolar(self, elemento):
        identificador = self.f(elemento)
        if identificador in self.ids():
            for i in range(len(self.colas)):
                self.colas[i].encolar(identificador)

    def desencolar(self, identificador):
        for cola in self.colas:
            if cola.ver_frente() == identificador:
                cola.desencolar()

    def esta_vacia(self):
        for i in range(len(self.colas)):
            return self.colas[i].esta_vacia()


"""
3) Se tiene una Cola con los números del 1 al 5 encolados en orden de menor
a mayor. Se cuenta además con una clase que posee dos pilas y tres métodos:
paso1(cola), paso2(), paso3().

* paso1(cola): desencola de la Cola y apila el numero obtenido en la primera de
    las pilas de la clase
* paso2(): desapila el tope de la primer pila y lo apila en la segunda
* paso3(): desapila el tope de la segunda pila y lo impr.ime

Determinar cuales de las siguientes opciones de impresión por pantalla son
posibles de ocurrir y cuáles no. Justficiar, en caso de que sea posible,
con el orden de las llamadas a los pasos:
a. 4 5 3 1 2
b. 2 3 1 5 4



RESPUESTA:

    En el caso (a) se llama cuatro veces seguidas al paso1 y la cola queda solo con el 5,
se llama al paso2 y quedan pila1 = Tope ---> [3, 2, 1] y pila 2 =  Tope ---> [4] , luego
se llama al paso3 y se imprime el numero 4. Se llama al paso1 y la cola queda vacia , se llama al paso2 y al paso3
asi se imprime el 5. Se llama al paso2, al paso3 y se obtiene el numero 3. Se llama al paso2 dos veces seguidas,
la pila1 queda vacia y la pila2 = Tope ---> [1, 2], seguido a esto se llama al paso3 dos veces seguidas imprimiendo así
el numero 1 y luego el numero 2 , cumpliendo entonces con (a).

    En el caso (b) se comienza llamando dos veces al paso1 , queda cola = [3, 4, 5] y pila  = Tope -->[2, 1],
se llama al paso2 y consecutivamente al paso3 para imprimir el 2. Se llama al paso1, al paso2, y al paso3 para imprimir
el numero 3. Se llama al paso2 y al paso3 , las pilas quedan vacias y se imprime el 1. Se llama al paso1 2 veces consecutivas
y la cola queda vacia, mientras la pila1 = Tope -->[5, 4] , luego se llama al paso2 y al paso3 para imprimir el numero 5.
Finalmente se llama al paso2 y al paso3 nuevamente y se imprime el numero 4.Entonces tambien se cumple (b).
"""
