class Producto:
    def __init__(self, id, nombre, cantidad):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad

def guardar(productos, ruta):
    with open(ruta, "w") as f:
        for producto in productos:
            f.write(f"{producto.id},{producto.nombre},{producto.cantidad}\n")

def cargar(ruta):
    productos = []
    with open(ruta) as f:
        for producto in f:
             id, nombre, cantidad = producto.split(",")
             productos.append(Producto(int(id), nombre, cantidad))

def verificar_ids(productos):
    verificacion = {}
    for producto in productos:
        if producto.id not in verificacion:
            verificacion[producto.id] = 0
        verificacion[producto.id] += 1

    for id in verificacion:
        if verificacion[id] > 1:
            return False
    return True

def pruebas():
    productos = [
        Producto(1, "chocolate", 5),
        Producto(2, "harina", 10),
        Producto(3, "salsa", 20)
    ]
    
    # HACER: llamar a la función guardar()
    guardar(productos, "productos.txt")

    # HACER: llamar a la función cargar()
    productos_cargado = cargar("productos.txt")

    # HACER: verificar que productos_cargado y productos son equivalentes
    assert verificar_ids(productos)

    # OPCIONAL: probar verificar_ids() con una lista que contiene repeticiones

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
