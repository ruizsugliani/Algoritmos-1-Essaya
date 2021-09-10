from cola import Cola
#EJERCICIO 1
class Actor:
    def __init__(self, nombre, nacimiento):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.films_actuados = []

class Film:
    def __init__(self, nombre, lanzamiento, reparto):
        self.nombre = nombre
        self.lanzamiento = lanzamiento
        self.reparto = reparto
        self.calificaciones = []

class IMDB:
    "IMDB es una base de datos de cine"
    def __init__(self):
        self.actores = {}
        self.films = {}

    def actor_agregar(self, nombre, anio, mes, dia):
        id_actor = len(self.actores)
        nacimiento = (anio, mes, dia)
        self.actores[id_actor] = Actor(nombre, nacimiento)
        return id_actor

    def cantidad_actores(self):
        return len(self.actores)

    def actor_nombre(self, id_actor):
        return self.actores[id_actor].nombre

    def actor_nacimiento(self, id_actor):
        return self.actores[id_actor].nacimiento

    def film_agregar(self, nombre, anio, mes, dia, ids_actores):
        id_film = len(self.films)
        lanzamiento = (anio, mes, dia)
        for id in ids_actores:
            if id in self.actores and id_film not in self.actores[id].films_actuados:
                self.actores[id].films_actuados.append(id_film)
        self.films[id_film] = Film(nombre, lanzamiento, ids_actores)
        return id_film

    def cantidad_films(self):
        return len(self.films)

    def film_nombre(self, id_film):
        return self.films[id_film].nombre

    def film_lanzamiento(self, id_film):
        return self.films[id_film].lanzamiento

    def film_actores(self, id_film):
        return self.films[id_film].reparto

    def actor_films(self, id_actor):
        return self.actores[id_actor].films_actuados

#EJERCICIO 2
    def escribir_csv(self):
        with open('actores.csv', 'w') as f:
            for id_actor in self.actores:
                f.write(f'{id_actor},{self.actores[id_actor].nombre},{self.actores[id_actor].nacimiento[0]},{self.actores[id_actor].nacimiento[1]},{self.actores[id_actor].nacimiento[2]}\n')

        with open('films.csv', 'w') as f:
            for id_film in self.films:
                f.write(f'{id_film},{self.films[id_film].nombre},{self.films[id_film].lanzamiento[0]},{self.films[id_film].lanzamiento[1]},{self.films[id_film].lanzamiento[2]}\n')

        with open('films_actores.csv', 'w') as f:
            for id_film in self.films:
                for id_actor in self.films[id_film].reparto:
                    f.write(f'{id_film},{id_actor}\n')

#EJERCICIO 3
    def films_decadas(self):
        decadas = {}
        for id_film in self.films:
            decada = self.films[id_film].lanzamiento[0] - (self.films[id_film].lanzamiento[0] % 10)
            if decada not in decadas:
                decadas[decada] = []
            decadas[decada].append(id_film)
        return decadas

#EJERCICIO 4
    def calificar(self, id_film, calificacion):
        self.films[id_film].calificaciones.append(calificacion)

    def film_promedio(self, id_film):
        if len(self.films[id_film].calificaciones) == 0:
            return 0
        else:
            suma = 0
            cantidad = 0
            for calificacion in self.films[id_film].calificaciones:
                suma += calificacion
                cantidad += 1
            return suma / cantidad

    def films_top10(self):
        temp = []
        top_10 = []
        for id_film in self.films:
            film_score = (self.film_promedio(id_film), id_film)
            temp.append(film_score)
        temp = sorted(temp)[::-1]
        for score in temp:
            top_10.append(score[1])
        while not len(top_10) == 10:
            top_10.pop()
        return top_10

#EJERCICIO 5
    def distancia(self, id_actor1, id_actor2):
        visitados = []
        actores_tuplas = Cola()

        visitados.append(id_actor1)
        actores_tuplas.encolar((id_actor1, 0))

        while not actores_tuplas.esta_vacia():
            actor_distancia = actores_tuplas.desencolar()
            if actor_distancia[0] == id_actor2:
                return actor_distancia[1]
            for id_film in self.actores[actor_distancia[0]].films_actuados:
                for id_actor in self.films[id_film].reparto:
                    if id_actor not in visitados:
                        visitados.append(id_actor)
                        actores_tuplas.encolar((id_actor, actor_distancia[1] + 1))
