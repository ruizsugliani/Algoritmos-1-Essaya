import csv
def puntajes_musicales(archivo, genero_ingresado):
    '''
    Recibe por parametro un archivo 'ratings.csv' el cual por cada linea tiene puntajes dados por usuarios
    a sus artistas con la forma 'usuario,genero,artista,puntaje'y un nombre de un genero musical. Crea un nuevo
    archivo 'csv' llamado como el genero ingresado, el cual contiene todos los puntajes correspondientes al genero 
    y cada linea con la forma 'usuario,artista,puntaje'
    '''
    res = []
    with open(archivo) as input_file:
        reader = csv.reader(input_file, delimiter=',')
        for usuario, genero, artista, puntaje in reader:
            if genero_ingresado == genero:
                res.append((usuario, artista, puntaje))
    with open(f"{genero_ingresado}.csv", "w") as output_file:
        for puntuacion in res:
            output_file.write(f"{puntuacion[0]},{puntuacion[1]},{puntuacion[2]}\n")

def imprimir_movimientos_notables(lista, k):
    '''
    Recibe una lista con tuplas de la forma ("personaje", "movimiento") y un numero k
    para finalmente imprimir por pantalla al personaje y su movimiento (realizado mas de k veces).
    '''
    movimientos = {}
    for personaje, movimiento in lista:
        if f"{personaje} - {movimiento}" not in movimientos:
            movimientos[f"{personaje} - {movimiento}"] = 0
        movimientos[f"{personaje} - {movimiento}"] += 1

    for accion in movimientos:
        if movimientos[accion] > k:
            print(f"{accion} ({movimientos[accion]})")

class FacebookUser:
    def __init__(self, usuario):
        '''Inicializa la clase con un nombre de usuario pasado por parametro'''
        self.usuario = usuario
        self.posts = []
        self.amistades = []

    def __str__(self):
        '''Devuelve el nombre del usuario'''
        return f"{self.usuario}"

    def publicar_post(self, post):
        '''Publica un post en el muro del usuario'''
        self.posts.insert(0, post)

    def agregar_amigo(self, otro_usuario):
        '''Agrega a un amigo a la lista de amistades, si no existe el usuario lanza una excepcion y la amistad es reciproca'''
        if otro_usuario not in self.amistades:
            self.amistades.append(otro_usuario)
            otro_usuario.amistades.append(self.usuario)
        elif otro_usuario in self.amistades or self.usuario in otro_usuario.amistades:
            raise Exception("El usuario ya se encuentra en la lista de amigos.")

    def mostrar_amigos(self):
        '''Muestra la lista de amigos del usuario, en caso de estar vacia lanza una excepcion'''
        if not self.amistades:
            raise Exception("El usuario no tiene amigos.")
        else:
            print("Amigos recientemente agregados: ")
            for amistad in self.amistades:
                print(amistad)

    def mostrar_muro(self):
        '''Muestra las publicaciones del usuario, de la mas nueva a la mas vieja, de no haber publicaciones, lanza una excepcion'''
        if not self.posts:
            raise Exception("No hay posteos aún.")
        else:
            print("Ultimas publicaciones: ")
            for post in self.posts:
                print(f"{self.usuario}: {post}")