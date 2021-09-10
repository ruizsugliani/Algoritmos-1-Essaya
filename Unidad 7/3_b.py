def imprimir_mensajes(nombres,p,n):
    contador = 0
    if not n == 0:
        for tupla in nombres[p:]:
            if tupla[1] == "Masculino":
                print(f"Estimado {tupla[0]}, vote por mi.")
                contador += 1
            if tupla[1] == "Femenino":
                print(f"Estimada {tupla[0]}, vote por mi.")
                contador += 1

            if contador == n:
                break
imprimir_mensajes((('Juan', 'Masculino'), ('Pedro', 'Masculino'), ('Agus', 'Femenino')), 1, 2)
