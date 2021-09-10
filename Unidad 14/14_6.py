'''
Escribir una función que recibe una expresión matemática (en forma de cadena)
y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están
correctamente balanceados, False en caso contrario.Ejemplos:

validar('(x+y)/2') -> True
validar('[8*4(x+y)]+{2/5}') -> True
validar('(x+y]/2') -> False
validar('1+)2(+3') -> False
validar('(((1)+2)+3)') -> True
validar('(((1)+2+3)') -> False
'''
from pila import Pila
def validar(ecuacion):
	signos_ortograficos = Pila()
	signos = {
				"(": ")",
				"[": "]",
				"{": "}",
	}
	for caracter in ecuacion:
		if caracter in signos.keys():
			signos_ortograficos.apilar(caracter)

		elif caracter in signos.values():
			if signos_ortograficos.esta_vacia() or signos[signos_ortograficos.desapilar()] != caracter:
				return False
	return signos_ortograficos.esta_vacia()

print(validar('(x+y)/2'))
print(validar('[8*4(x+y)]+{2/5}'))
print(validar('(x+y]/2'))
print(validar('1+)2(+3'))
print(validar('(((1)+2)+3)'))
print(validar('(((1)+2+3)'))
