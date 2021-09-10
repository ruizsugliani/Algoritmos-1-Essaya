#EJERCICIO 1
class Aeropuerto:
    def __init__(self, designacion, nombre, ciudad, pais, latitud, longitud):
        self.designacion = designacion
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.ubicacion = (latitud, longitud)

class RutaAerea:
    def __init__(self, codigo, origen, destino):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.terna = (codigo, origen, destino)

class AeroDB:
    def __init__(self):
        self.aeropuertos = {}
        self.rutas = []

    def aeropuerto_agregar(self, designacion, nombre, ciudad, pais, latitud, longitud):
        self.aeropuertos[designacion] = Aeropuerto(designacion, nombre, ciudad, pais, latitud, longitud)

    def cantidad_aeropuertos(self):
        return len(self.aeropuertos)

    def aeropuerto_get_nombre(self, designacion):
        return self.aeropuertos[designacion].nombre

    def aeropuerto_get_ciudad(self, designacion):
        return self.aeropuertos[designacion].ciudad

    def aeropuerto_get_pais(self, designacion):
        return self.aeropuertos[designacion].pais

    def aeropuerto_get_coords(self, designacion):
        return self.aeropuertos[designacion].ubicacion

    def ruta_agregar(self, codigo, origen, destino):
        nueva_ruta = RutaAerea(codigo, origen, destino)
        if nueva_ruta.terna not in self.rutas:
            self.rutas.append(nueva_ruta)

    def cantidad_rutas(self):
        return len(self.rutas)

#EJERCICIO 2
    def rutas_desde_ciudad(self, nombre):
        res = []
        for ruta in self.rutas:
            if self.aeropuerto_get_ciudad(ruta.origen) == nombre:
                res.append(ruta.terna)
        return res

    def rutas_hacia_ciudad(self, nombre):
        res = []
        for ruta in self.rutas:
            if self.aeropuerto_get_ciudad(ruta.destino) == nombre:
                res.append(ruta.terna)
        return res

#EJERCICIO 4
    def aeropuertos_ordenados_por_distancia(self, latitud, longitud):
        temp = []
        cercanos = []
        for aeropuerto in self.aeropuertos:
            x = (latitud - self.aeropuertos[aeropuerto].ubicacion[0]) ** 2
            y = (longitud - self.aeropuertos[aeropuerto].ubicacion[1]) ** 2
            d = (x + y) ** 0.5
            temp.append((d, aeropuerto))

        temp = sorted(temp)
        for calculo in temp:
            cercanos.append(calculo[1])
        return cercanos

#EJERCICIO 5
    def armar_itinerario(self, c_origen, c_destino):
        res = []
        posibles_rutas = []
        visitadas = []
        for ruta in self.rutas:
            if c_origen == ruta.origen or c_origen == ruta.destino:
                posibles_rutas.append(ruta)

        


#EJERCICIO 3
'''
    def aeropuerto_con_mas_rutas(self):
        rutas_servidas = {}
        for aeropuerto in self.aeropuertos:
            if aeropuerto not in rutas_servidas:
                rutas_servidas[aeropuerto] = 0
            for ruta in self.rutas:
                if ruta.origen == aeropuerto or ruta.destino == aeropuerto:
                    rutas_servidas[aeropuerto] += 1

        for designacion in rutas_servidas:
            if rutas_servidas[designacion] ==  max(rutas_servidas.values()):
                return (designacion, rutas_servidas[designacion])

def cargar(archivo_aeropuertos, archivo_rutas):
    i = AeroDB()
    with open(archivo_aeropuertos, encoding='utf8') as f:
        for linea in f:
            designacion, nombre, ciudad, pais, latitud, longitud = linea.rstrip('\n').split('|')
            i.aeropuerto_agregar(designacion, nombre, ciudad, pais, latitud, longitud)

    with open(archivo_rutas, encoding='utf8') as f:
        for linea in f:
            codigo, origen, destino = linea.rstrip('\n').split('|')
            i.ruta_agregar(codigo, origen, destino)

    return i
'''
