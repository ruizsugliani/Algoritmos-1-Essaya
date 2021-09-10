"""
Escribir un programa que le pida al usuario que ingrese una sucesión de números
naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de
salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total
de los valores y el promedio.
"""
def main():
    suma = 0
    cantidad = 0
    print("Ingrese una sucesion de numeros naturales (o `-1` para terminar):")
    centinela = int(input())
    while True:
        if centinela == -1:
            break
        suma += centinela
        cantidad += 1
        promedio = suma / cantidad
        centinela = int(input())
    print(f"Cantidad de numeros ingresados: {cantidad}")
    print(f"Suma de los valores: {suma}" )
    print(f"Promedio de los valores: {promedio}")
main()
