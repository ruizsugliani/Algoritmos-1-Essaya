"""
Escribir una funcion que reciba dos secuencias A y B como parametro,
y devuelva un valor booleano indicando si todos los elementos de A estan en B.
"""
#funcion
#recibe dos secuenciascomo parametro
#devuelve un booleano si todos los elementos de A estan en B
def elementos_incluidos(secuencia_a, secuencia_b):
    for elemento in secuencia_a:
        if not elemento in secuencia_b:
            return False
        return True

print(elementos_incluidos("hola", "wywaoafafl"))
