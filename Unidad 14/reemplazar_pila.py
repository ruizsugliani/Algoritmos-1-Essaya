from pila import Pila
from cola import Cola

def reemplazar(pila, valor_viejo, valor_nuevo):
	temporal = Pila()
	while not pila.esta_vacia():
		numero_inicial = pila.desapilar()
		if numero_inicial == valor_viejo:
			numero_inicial = valor_nuevo
			temporal.apilar(numero_inicial)

		else:
			temporal.apilar(numero_inicial)

	while not temporal.esta_vacia():
			numero_final = temporal.desapilar()
			pila.apilar(numero_final)
	return pila

pila = Pila()
pila.apilar(1)
pila.apilar(3)
pila.apilar(5)
pila.apilar(1)
pila_nueva = reemplazar(pila, 1, 7)
print(pila_nueva)
