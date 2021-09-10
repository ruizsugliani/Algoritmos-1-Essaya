def leer_dialogo(nombre_archivo):
    res = {}
    with open(nombre_archivo, "r", encoding = "utf8") as file:
        for linea in file:
            linea = linea.rstrip("\n").split()
            persona = linea[0][0:-1]
            palabras = linea[1:]
            if not persona in res:
                res[persona] = {}
                for palabra in palabras:
                    if not palabra in res[persona]:
                        res[persona][palabra] = 0
                    if palabra in palabras:
                        res[persona][palabra] += 1
            else:
                for palabra in palabras:
                    if not palabra in res[persona]:
                        res[persona][palabra] = 0
                    if palabra in palabras:
                        res[persona][palabra] += 1
    return res



print(leer_dialogo('test_file.txt'))
