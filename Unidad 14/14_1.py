from cola import Cola
class TorreDeControl:
    def __init__(self):
        self.esperan_aterrizar = Cola()
        self.esperan_despegar = Cola()

    def nuevo_arribo(self, avion):
        self.esperan_aterrizar.encolar(avion)

    def nueva_partida(self, avion):
        self.esperan_despegar.encolar(avion)

    def ver_estado(self):
        print("Vuelos esperando para aterrizar: "f"{self.esperan_aterrizar.frente.dato}")
        print("Vuelos esperando para despegar: " f"{self.esperan_despegar.frente.dato}")

    def asignar_pista(self):
        if not self.esperan_aterrizar.esta_vacia():
            print("El vuelo " f"{self.esperan_aterrizar.desencolar()}" " aterrizó con éxito.")

        elif not self.esperan_despegar.esta_vacia():
            print("El vuelo " f"{self.esperan_despegar.desencolar()}" " despegó con éxito.")

        else:
            print("No hay vuelos en espera.")


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
