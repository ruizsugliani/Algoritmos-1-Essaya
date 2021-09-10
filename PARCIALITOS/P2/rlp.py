#5)
def buscar_nombres_de_mayores(nombre_archivo):
    personas = {}
    mayores = []
    with open(nombre_archivo) as file:
        for linea in file:
            nombre, edad = linea.rstrip("\n").split(",")
            if nombre not in personas:
                personas[nombre] = edad

    for persona in personas:
        if personas[persona] == max(personas.values()):
            mayores.append(persona)
    return (int(max(personas.values())), mayores)
#print(buscar_nombres_de_mayores("origen.txt"))


#4)
canciones = {"Cerca de ti": 150, "Sola": 200, "Morado": 215, "Rojo":190, "Blanco": 210}
listas_reproduccion = {"Reggaeton": ["Morado", "Rojo", "Blanco"], "Rap": ["Cerca de ti", "Sola"]}

def obtener_duracion_listas(canciones, listas_reproduccion):
    duracion_lista = {}
    for cancion in canciones:
        duracion = canciones.get(cancion, [])
        for lista in listas_reproduccion:
            if cancion in listas_reproduccion(lista, []):
                duracion_lista[listas_reproduccion] = duracion
    return duracion_lista


#3)
class Cuenta:
    def __init__(self, persona):
        self.persona = str(persona)
        self.movimiento = []
        self.dinero = 0

    def __str__(self):
        return f"Cuenta de {self.persona}"

    def acreditar(self, monto, accion):
        self.movimiento.append(("acreditación", monto, accion))
        self.dinero += monto

    def extraer(self, monto, accion):
        if monto > self.dinero:
            raise ValueError("Fondos Insuficientes")
        self.movimiento.append(("extracción", monto, accion))
        self.dinero -= monto

    def saldo(self):
        return self.dinero

    def movimientos(self):
        return self.movimiento

    def transferir(self, monto, otra_persona):
        self.extraer(monto, f"Cuenta de {otra_persona.persona}")
        otra_persona.acreditar(monto, f"Cuenta de {self.persona}")

#6)
'''
>>> caja = CajaFuerte(9158)
>>> caja.esta_abierta()
False
>>> caja.guardar("pulsera")
Exception: La caja fuerte está cerrada
>>> caja.abrir(1234)
Exception: La clave es inválida
>>> caja.abrir(9158)
>>> caja.esta_abierta()
True
>>> caja.guardar("pulsera")
>>> caja.guardar("reloj de oro")
Exception: No se puede guardar más de una cosa
>>> caja.cerrar()
>>> caja.sacar()
Exception: La caja fuerte está cerrada
>>> caja.abrir(9158)
>>> caja.sacar()
'pulsera'
>>> caja.sacar()
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
            raise Exception("La clave es invalida")

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
caja = CajaFuerte(9158)
caja.esta_abierta()
caja.abrir(9158)
caja.guardar("pulsera")
caja.cerrar()
caja.abrir(9158)
caja.sacar()
caja.sacar()
