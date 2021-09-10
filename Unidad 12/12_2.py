'''
a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.
b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
con la suma de ambas.
c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
con el producto de ambas.
d) Crear un método simplificar que modifica la fracción actual de forma que los valores
del dividendo y divisor sean los menores posibles.
'''
from math import gcd
#a)
class Fraccion:
    def __init__(self, dividendo, divisor):
        self.dividendo = int(dividendo)
        self.divisor = int(divisor)

        if self.divisor == 0:
            raise ValueError("El denominador debe ser distinto de 0.")

    def __str__(self):
        X = self.dividendo
        Y = self.divisor
        return f"{X}/{Y}"

#b)
    def __add__(self, otra_fraccion):
        nuevo_dividendo = self.dividendo * otra_fraccion.divisor + otra_fraccion.dividendo * self.divisor
        nuevo_divisor =  self.divisor * otra_fraccion.divisor
        return Fraccion(nuevo_dividendo, nuevo_divisor).simplificar()

#c)
    def __mul__(self, otra_fraccion):
        nuevo_dividendo = self.dividendo * otra_fraccion.dividendo
        nuevo_divisor =  self.divisor * otra_fraccion.divisor
        return Fraccion(nuevo_dividendo, nuevo_divisor).simplificar()

#d)
    def simplificar(self):
        factor_comun = gcd(self.dividendo, self.divisor)
        return Fraccion(self.dividendo / factor_comun, self.divisor / factor_comun)


f1 = Fraccion(4, 5)
f2 = Fraccion(3, 2)
f3 = Fraccion(15, 10)
print(f1.__mul__(f2))
