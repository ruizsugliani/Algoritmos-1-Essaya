def main():
    '''
    Recibe un número inicial y uno final , entre ellos menciona a los pares
    '''
    inicio = int(input("Ingrese el primer numero: "))
    fin = int(input("Ingrese el segundo numero: "))

    inicio = inicio + inicio%2
    fin = fin - fin%2
    
    for i in range(inicio, fin + 1, 2):
        print(i)

main()
