from pila import Pila
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = int(valor)

class Solitario:
    def __init__(self):
        self.pila = Pila()

    def apilar(self, carta):
        if self.pila.esta_vacia():
            self.pila.apilar(carta)
            return

        primera_carta = self.pila.ver_tope()

        if carta.palo != primera_carta.palo and carta.valor == primera_carta.valor - 1:
            self.pila.apilar(carta)

        else:
            raise Exception("Carta inválida.")

solitario = Solitario()
solitario.apilar(Carta('Copa', 12))
solitario.apilar(Carta('Oro', 11))
solitario.apilar(Carta('Copa', 11))
