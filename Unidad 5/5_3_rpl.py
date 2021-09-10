"""
#a)
def main():
    '''
    Pide al usuario contrasenias hasta que se ingresa la correcta.
    '''
    contrasenia = '333' # no modificar (pruebas automáticas)
    password = str(input("Ingrese la contrasenia: "))
    while not password == contrasenia:
        password = str(input("Contrasenia incorrecta. Intentelo nuevamente: "))
    print("Contrasenia correcta.")
main()

#b)
def main():
    '''
    Pide al usuario contrasenias hasta que se ingresa la correcta o hasta que gaste los 3 intentos.
    '''
    contrasenia = '333' # no modificar (pruebas automáticas)
    intentos = 3
    password = str(input("Ingrese la contrasenia: "))
    while not password == contrasenia and intentos != 0:
        intentos -= 1
        if intentos == 0:
            print("Contrasenia incorrecta (0 intento/s restante/s).")
            break
        password = str(input(f"Contrasenia incorrecta ({intentos} intento/s restante/s). Intentelo nuevamente: "))

    if password == contrasenia:
        print("Contrasenia correcta.")
main()

#c)
def validar(contrasenia, intentos):
    '''
    Recibe por parámetros una contraseña y una cantidad de intentos (N),
    que le pregunte al usuario la contraseña, y no le permita continuar hasta que
    la haya ingresado correctamente, dandole como máximo N intentos.
    La función debe retornar un booleano indicando si el usuario ingresó la contraseña correctamente.
    '''
    password = int(input("Ingrese la contraseña: "))
    while not password == contrasenia:
        intentos -= 1
        password = int(input(f"Contrasenia incorrecta ({intentos} intento/s restante/s). Intentelo nuevamente: "))
        if intentos == 0:
            return False
    if password == contrasenia:
        return True
validar(333, 3)
