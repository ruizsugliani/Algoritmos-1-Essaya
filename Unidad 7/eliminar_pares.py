#Dada una lista eliminar todos los elementos en posiciones pares

def eliminar_pares(lista):
    borrados = 0
    for i in range(0, len(lista), 2):
        lista.pop(i - borrados)
        borrados += 1
    return eliminar_pares(lista)

lista = [1,2,3,4,5,6,7,8,9,10]
eliminar_pares(lista)
print(lista) #[2,4,6,8,10]
