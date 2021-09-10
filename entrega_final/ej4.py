class Libro:
    '''
    Clase libro la cual cuenta con titulo, autor y año de publicación en su constructor.
    '''
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"{self.titulo, self.autor, self.anio}"

    def __eq__(self, otro):
        if self.titulo == otro.titulo and self.autor == otro.autor and self.anio == otro.anio:
            return True
        else:
            return False

def ordenar_libros(libros):
    '''
    Ordena la lista de instancias de Libro en forma creciente según el valor del titulo.
    '''
    return sorted(libros, key=lambda l: l.titulo)

def buscar_libro(libros, titulo):
    '''
    Recibe una lista de libros ordenados por título, y devuelve el libro con el
    título indicado, o None si no existe, usando búsqueda binaria.
    '''
    izq = 0
    der = len(libros) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if libros[medio].titulo == titulo:
            return libros[medio]

        if libros[medio].titulo > titulo:
            der = medio - 1
        else:
            izq = medio + 1

    return None

def pruebas():

    libros = [
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("Giant's Bread", "Agatha Christie", 1930),
    ]

    libros = ordenar_libros(libros)

    assert libros == [Libro("Giant's Bread", "Agatha Christie", 1930),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
    ]

    libro = buscar_libro(libros, "The Floating Admiral")
    assert libro is libros[1]

    libro2 = buscar_libro(libros, "Harry Potter y El Prisionero de Azkaban")
    assert libro2 is None
    # OPCIONAL: pruebas adicionales. Ejemplo: buscar un libro que no exista

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
