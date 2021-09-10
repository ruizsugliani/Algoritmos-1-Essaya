def buscar_nombres_de_mayores(nombre_archivo):
    dict = {}
    with open(nombre_archivo, "r", encoding = "utf8") as file:
        for linea in file:
            linea = linea.rstrip("\n")
            linea = linea.split(", ")

            nombre = linea[0]
            edad = int(linea[1])
            nueva_edad_mas_alta = 0

            if edad not in dict:
                
                nueva_edad_mas_alta = edad

            elif edad_mas_alta[0] < edad:
                edad_mas_alta[0] = edad
                nueva_edad_mas_alta = edad

            if edad_mas_alta[0] == nueva_edad_mas_alta:
                mayores.append(nombre)

    res = edad_mas_alta, mayores
    return res

print(buscar_nombres_de_mayores("personas.txt"))
