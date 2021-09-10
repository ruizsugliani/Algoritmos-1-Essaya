from cola import Cola
from pila import Pila

def ordenar_fases(fases):
	fases_ordenadas = Cola()
	while not fases.esta_vacia():
		fase = fases.desencolar()

		if fases_ordenadas.esta_vacia():
			fases_ordenadas.encolar(fase)

		elif not fases_ordenadas.esta_vacia() and fase > fases_ordenadas.ultimo.dato:
			fases_ordenadas.encolar(fase)
	return fases_ordenadas
