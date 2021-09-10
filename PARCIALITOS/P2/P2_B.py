import csv
'''
1) Se tiene un archivo con el siguiente formato <nombre persona>;<lugar>;<momento en que la persona estuvo alli> .
Escribir una funcion que reciba la ruta a este archivo y el nombre de una persona y devuelva un conjunto con
todas las personas con las que tuvo contacto. Una persona tuvo contacto con otra si estuvieron en el mismo
lugar en el mismo momento).
Notas:

- El archivo no se encuentra ordenado bajo ningún criterio y no posee errores de formato ni de tipo de datos.
No posee encabezado.
- El archivo puede recorrerse una única vez.
- Cada persona puede haber estado en multiples lugares en múltiples momentos distintos
(inclusive múltiples momentos para el mismo lugar).
- El tipo de dato para el "momento" no importa, tratarlo como una cadena.
'''
def sociales(archivo, persona_elegida):
	ubicaciones = {}
	res = []
	with open(archivo) as file:
		reader = csv.reader(file, delimiter=';')
		for nombre, lugar, momento in reader:
			if nombre not in ubicaciones:
				ubicaciones[nombre] = []
			ubicaciones[nombre].append((lugar, momento))

	for persona in ubicaciones:
		if persona != persona_elegida:
			for posicion in ubicaciones[persona]:
				if posicion in ubicaciones[persona_elegida]:
					res.append(persona)

	return res


'''
2) Escribir una función que reciba una ruta a un archivo de pokemones con el siguiente formato
<pokemon>;<tipo>;<pos_x>,<pos_y>, y un diccionario de gimnasios (cada clave es el nombre de un gimnasio,
y el valor asociado, su posicion, dada como una tupla (pos_x, pos_y)) y escriba en un archivo de salida el
pokemon, su tipo y su gimnasio más cercano. El archivo de salida debe tener el siguiente formato: <pokemon;<tipo>;<gimnasio más cercano>.
Para calcular la distancia entre pokemon y gimnasio se utiliza distancia manhattan: dist(p1, p2) = |p1_x - p2_x| + |p1_y - p2_y|
Notas:

- El archivo no se encuentra ordenado bajo ningún criterio y no posee errores de formato ni de tipo de datos. No posee encabezado.
- El archivo puede recorrerse una única vez y no entra entero en memoria.
'''
def encontrar_gym(archivo, dict):
    menor_distancia = None
    gym_mas_cercano = None
    res = []
    with open(archivo) as input_file:
        reader = csv.reader(input_file, delimiter=';')
        for pokemon, tipo, pos_x, pos_y in reader:
            p1 = (int(pos_x), int(pos_y))
            for gym in dict:
                p2 = dict[gym]
                distancia = distancia_manhatan(p1, p2)
                if gym_mas_cercano == None or distancia < menor_distancia:
                    menor_distancia = distancia
                    gym_mas_cercano = gym
                    res.append((pokemon, tipo, gym_mas_cercano))
    with open("gims.csv", "w") as output_file:
        writer = csv.writer(output_file, delimiter=';')
        for pokemon in res:
            writer.writerows([pokemon])
#dict = {"aqua_gym": (210, 140), "fire_gym": (140, 210), "thunder_gym": (100, 100), "green_gym": (300, 300)}
#encontrar_gym("origen.csv", dict)
'''
3) Modelar en python:
Una clase App que permita crear aplicaciones con su nombre y el espacio que ocupa.
Una clase Smartphone que permita crear smartphones con su nombre de modelo y memoria total, además de permitir instalar y desinstalar apps (debe poder almacenar la instancia de la App).
Los objetos instanciados de dichas clases deberán cumplir con el siguiente comportamiento:

>>> app_ig = App("Instagram", 65)
>>> app_tw = App("Twitter", 35)
>>> app_itunes = App("iTunes", 150)
>>> pixel = Smartphone("Pixel 4a", 100)
>>> oneplus = Smartphone("OnePlus 8T", 200)
>>> print(pixel)
Pixel 4a, espacio libre: 100, apps instaladas:
>>> pixel.instalar(app_ig)
>>> print(pixel)
Pixel 4a, espacio libre: 35, apps instaladas: Instagram
>>> pixel.instalar(app_ig)
Exception: La app ya está instalada
>>> oneplus.instalar(app_ig)
>>> oneplus.instalar(app_itunes)
Exception: El smartphone no cuenta con espacio suficiente
>>> oneplus.instalar(app_tw)
>>> print(oneplus)
OnePlus 8T, espacio libre: 100, apps instaladas: Instagram, Twitter
>>> oneplus.desinstalar(app_ig)
>>> oneplus.instalar(app_itunes)
>>> print(oneplus)
OnePlus 8T, espacio libre: 15, apps instaladas: Twitter, Itunes
>>> oneplus.desinstalar(app_ig)
Exception: El smartphone no tiene esa app instalada
'''
class App:
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio

class Smartphone:
    def __init__(self, modelo, memoria):
        self.modelo = modelo
        self.memoria = memoria
        self.instaladas = []

    def __str__(self):
        return f"{self.modelo}, espacio libre: {self.memoria}, apps instaladas: {self.instaladas}"

    def instalar(self, app):
        if app.nombre in self.instaladas:
            raise Exception("La app ya está instalada")
        else:
            if self.memoria - app.espacio < 0:
                raise Exception("El smartphone no cuenta con espacio suficiente")
            else:
                self.memoria -= app.espacio
                self.instaladas.append(app.nombre)

    def desinstalar(self, app):
        if app.nombre not in self.instaladas:
            raise Exception("El smartphone no tiene esa app instalada")
        else:
            self.memoria += app.espacio
            self.instaladas.remove(app.nombre)
