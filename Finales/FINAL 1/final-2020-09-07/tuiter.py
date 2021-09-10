#EJERCICIO 1
class Autor:
    def __init__(self, id_autor, nombre):
        self.id_autor = id_autor
        self.nombre = nombre
        self.muro = []

class Tuit:
    def __init__(self, id_tuit, id_autor, mensaje):
        self.id_tuit = id_tuit
        self.id_autor = id_autor
        self.mensaje = mensaje
        self.veces_compartido = 0
        self.likes = []
        self.respuestas = []

class Tuiter:
    "Modela el funcionamiento de una plataforma sospechosamente similar a Twitter"
    def __init__(self):
        self.autores = {}
        self.tuits = {}
        self.hilos = {}

    def crear_autor(self, nombre):
        id_autor = len(self.autores)
        self.autores[id_autor] = Autor(id_autor, nombre)
        return id_autor

    def publicar(self, id_autor, mensaje):
        id_tuit = len(self.tuits)
        nuevo_tuit = Tuit(id_tuit, id_autor, mensaje)
        self.tuits[id_tuit] = nuevo_tuit
        self.autores[id_autor].muro.append(nuevo_tuit)
        return id_tuit

    def compartir(self, id_tuit, id_autor):
        if self.tuits[id_tuit].id_autor != id_autor:
            self.autores[id_autor].muro.append(self.tuits[id_tuit])
            self.tuits[id_tuit].veces_compartido += 1
            return True
        return False

    def tuit_id_autor(self, id_tuit):
        return self.tuits[id_tuit].id_autor

    def tuit_mensaje(self, id_tuit):
        return self.tuits[id_tuit].mensaje

    def muro_cantidad(self, id_autor):
        return len(self.autores[id_autor].muro)

    def muro_id_tuit(self, id_autor, p):
        return self.autores[id_autor].muro[p].id_tuit

#EJERCICIO 2
    def muro_escribir_csv(self, id_autor, archivo):
        with open(archivo, "w") as f:
            f.write("autor|mensaje\n")
            for tuit in self.autores[id_autor].muro:
                nombre_autor = tuit.id_autor
                f.write(f"{self.autores[nombre_autor].nombre}|{tuit.mensaje}\n")

#EJERCICIO 3
    def tuits_mas_compartidos(self):
        res = []
        for tuit in self.tuits:
            res.append((self.tuits[tuit].id_tuit, self.tuits[tuit].veces_compartido))
        return sorted(res, key=lambda x: x[1], reverse=True)

#EJERCICIO 4
    def tuit_dar_like(self, id_tuit, id_autor):
        if self.tuits[id_tuit].id_autor != id_autor and id_autor not in self.tuits[id_tuit].likes:
            self.tuits[id_tuit].likes.append(id_autor)
            return True
        return False

    def tuit_fue_likeado_por(self, id_tuit, id_autor):
        if id_autor in self.tuits[id_tuit].likes:
            return True
        return False

#EJERCICIO 5
    def responder(self, id_tuit, id_autor, mensaje):
        id_hilo = len(self.hilos)
        self.hilos[id_hilo] = []
        id_tuit_respuesta = publicar(id_autor, mensaje)
        self.tuits[id_tuit].respuestas.append(id_tuit_respuesta)
        self.hilos[id_hilo].append(id_tuit)
        self.hilos[id_hilo].append(id_tuit_respuesta)

    def tuit_respuestas(self, id_tuit):
        return self.tuits[id_tuit].respuestas

    def tuit_en_respuesta_de(self, id_tuit):
        for hilo in self.hilos:
            if id_tuit == hilo[0]:
                return None
            return hilo[0]

    def tuit_cantidad_hilo(self, id_tuit):
        for hilo in self.hilos:
            if id_tuit == hilo[0]:
                wrapper(hilo, contador=0)

    def wrapper(lista, contador):
        if not lista:
            return contador
        return wrapper(lista[1:], contador+1)

t =Tuiter()

# creamos 2 autores
id_grace = t.crear_autor("Grace")
id_barbara = t.crear_autor("Barbara")

# grace publica un tuit
id_tuit = t.publicar(id_grace, "Hola")

# el tuit no tiene respuestas
assert list(t.tuit_respuestas(id_tuit)) == []

# el tuit no es en respuesta de otro tuit
assert t.tuit_en_respuesta_de(id_tuit) is None

# la cantidad del hilo es 1
print(t.tuit_cantidad_hilo(id_tuit))
