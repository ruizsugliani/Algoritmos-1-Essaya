from pila import Pila

class PilaConMinimo:
    def __init__(self):
        self.pila = Pila()
        self.minimos = Pila()

    def apilar(self, elemento):
        if self.minimos.esta_vacia():
            self.minimos.apilar(elemento)

        elif self.minimos.ver_tope() >= elemento:
            self.minimos.apilar(elemento)
        self.pila.apilar(elemento)

    def desapilar(self):
        elemento = self.pila.desapilar()
        if elemento == self.minimo.ver_tope():
            self.minimos.desapilar()
        return elemento

    def ver_minimo(self):
        return self.minimos.ver_tope()

    def __str__(self):
        return f"Pila con minimos: {self.minimos} ({self.pila})"
