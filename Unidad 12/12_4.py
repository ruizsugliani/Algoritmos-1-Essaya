'''
Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
>>> c = Caja({500: 6, 100: 7, 2: 4})
>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
>>> c.agregar({50: 2, 2: 1})
>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
>>> c.quitar({50: 2, 100: 1})
200
>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'
'''

def validar(diccionario):
    permitidos = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    for clave in diccionario:
        if clave in permitidos:
            continue
        else:
            raise ValueError(f'Denominación "' f"{clave}" '" no permitida')
    return diccionario

def sumar_claves_y_valores(diccionario):
    suma = 0
    if validar(diccionario):
        for clave in diccionario:
            suma += clave * diccionario.get(clave, ' ')
    return suma

class Caja:
    def __init__(self, billetes):
        self.billetes = validar(billetes)

    def __str__(self):
        return f"Caja {self.billetes} total: {sumar_claves_y_valores(self.billetes)} pesos"

    def agregar(self, otros_billetes):
        if validar(otros_billetes):
            for clave in otros_billetes:
                if not clave in self.billetes:
                    self.billetes[clave] = otros_billetes.get(clave, ' ')
                else:
                    self.billetes[clave] += otros_billetes.get(clave, ' ')

    def quitar(self, otros_billetes):
        for clave in otros_billetes:
            if clave in self.billetes:
                if self.billetes.get(clave, ' ') < otros_billetes.get(clave, ' '):
                    raise ValueError(f'No hay suficientes billetes de denominación "' f"{clave}" '"')

                elif self.billetes.get(clave, ' ') == otros_billetes.get(clave, ' '):
                    resta = sumar_claves_y_valores(otros_billetes)
                    self.billetes.pop(clave)

                elif self.billetes.get(clave, ' ') > otros_billetes.get(clave, ' '):
                    resta = sumar_claves_y_valores(otros_billetes)
                    self.billetes[clave] = self.billetes.get(clave, ' ') - otros_billetes.get(clave, ' ')
                else:
                    return self.billetes
        return(resta)
