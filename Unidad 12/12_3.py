"""
a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
misma cantidad de elementos debe levantar una excepción.
c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
los elementos multiplicados por ese número.
"""

class Vector:
#a)
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return f'{"".join(str(self.vector).split(" "))}'

#b)
    def __add__(self, otro):
        if len(self.vector) == len(otro.vector):
            nuevo_vector = []
            for i in range(len(self.vector)):
                nuevo_vector.append(self.vector[i] + otro.vector [i])
            return Vector(nuevo_vector)
        raise Exception("Vectores no tienen la misma cantidad de elementos.")
#c)
    def __mul__(self, numero):
        nuevo_vector = []
        for i in self.vector:
            nuevo_vector.append(i * numero)
        return Vector(nuevo_vector)
