from pila import Pila

def sumar_pilas(pila1, pila2):
    auxiliar1 = Pila()
    auxiliar2 = Pila()
    resultado = Pila()
    while not pila1.esta_vacia() and not pila2.esta_vacia():
        if not pila1.esta_vacia():
            auxiliar1.apilar(pila1.desapilar())
        if not pila2.esta_vacia():
            auxiliar2.apilar(pila2.desapilar())

    while not auxiliar1.esta_vacia() and not auxiliar2.esta_vacia():
        suma = auxiliar1.desapilar() + auxiliar2.desapilar()
        if suma >= 10:
            digito = (suma - 10)
            sumo = 1
            resultado.apilar(digito)
            

pila1 = Pila()
pila1.apilar(1)
pila1.apilar(4)
pila1.apilar(6)

pila2 = Pila()
pila2.apilar(9)
pila2.apilar(8)
pila2.apilar(7)

print(pila1)
print(pila2)
print(sumar_pilas(pila1, pila2))
