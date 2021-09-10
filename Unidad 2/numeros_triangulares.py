def calcular_numero_triangular(n):
    '''
    Recibe un número y calcula su número triangular mediante la suma de los números naturales desde 1 hasta n.
    '''
    T = ((n * (n + 1) ) // 2)
    return T

def main():
    '''
    El programa le pide al usuario un numero n
    e imprime por pantalla los primeros n numeros triangulares.
    '''

    n = int(input("Ingrese un número: "))
    c = 1
    for i in range(1, n + 1):
            c += 1
            triangular = calcular_numero_triangular(i)

            print(i, "-", triangular)
main()
