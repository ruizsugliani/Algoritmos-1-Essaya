'''
a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo
entre dos instantes de tiempo (números enteros expresados en segundos), con la
condición desde < hasta.

b) Implementar el método duracion que devuelve la duración en segundos del
intervalo.

c) Implementar el método interseccion que recibe otro intervalo y devuelve un
nuevo intervalo resultante de la intersección entre ambos, o lanzar una
excepción si la intersección es nula.

d) Implementar el método union que recibe otro intervalo. Si los intervalos no
son adyacentes ni intersectan, debe lanzar una excepción. En caso contrario
devuelve un nuevo intervalo resultante de la unión entre ambos.
'''
#a)
class Intervalo:
    def __init__(self, desde, hasta):
        self.desde = int(desde)
        self.hasta = int(hasta)
        if not desde < hasta:
            raise ValueError("El parámetro (desde) debe ser estrictamente menor que (hasta)")
#b)
    def duracion(self):
        diferencia = self.hasta - self.desde
        return f"El intervalo dura {diferencia} segundos."
#c)
    def interseccion(self, otro_intervalo):
        if self.desde < otro_intervalo.desde < self.hasta:
            return Intervalo(otro_intervalo.desde, self.hasta)

        if self.desde < otro_intervalo.hasta < self.hasta:
            return Intervalo(self.desde, otro_intervalo.hasta)

        raise Exception("Intersección nula.")
#d)
    def union(self, otro_intervalo):
        if self.desde < otro_intervalo.desde < self.hasta or self.hasta == otro_intervalo.desde:
            return Intervalo(self.desde, otro_intervalo.hasta)

        if self.desde < otro_intervalo.hasta < self.hasta or self.desde == otro_intervalo.hasta:
            return Intervalo(otro_intervalo.desde, self.hasta)

        raise Exception("Intervalos no son adyacentes.")
