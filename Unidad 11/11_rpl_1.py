def resumir_pedidos(pedidos, nombre_archivo_dest):
    res = {}
    for pedido in pedidos:
        for producto in pedido:
            if producto not in res:
                res[producto] = 0
            res[producto] += pedido[producto]

    with open(nombre_archivo_dest, "w", encoding = "utf8") as file:
        for clave in res:
            file.write(f"{clave};{res[clave]}\n")

    return



dict = {"polenta": 2, "jugo": 3, "arroz": 1}
dict2 = {"jugo": 1, "arroz": 5}
dict3 = {"verduras": 4, "polenta": 2}

prods = [dict, dict2, dict3]

print(resumir_pedidos(prods, "test_file.txt"))
