#a)
def main():
'''
Pide al usuario contrasenias hasta que se ingresa la correcta.
'''
    contrasenia = '333' # no modificar (pruebas automáticas)
    password = input("Ingrese la contrasenia: ")
    while password != contrasenia:
        password = input("Contrasenia incorrecta. Intentelo nuevamente: ")

    print("Contrasenia correcta.")

main()

#b)
def main():
    '''
    Pide al usuario contrasenias hasta que se ingresa la correcta o hasta que gaste los 3 intentos.
    '''
    contrasenia = '333' # no modificar (pruebas automáticas)
    password = input("Ingrese la contrasenia: ")
    intentos = 0
    while password != contrasenia and intentos < 3:
        intentos += 1
        password = input("Contrasenia incorrecta (2 intento/s restante/s). Intentelo nuevamente: ")
        if password != contrasenia and intentos < 3:
            intentos += 1
            password = input("Contrasenia incorrecta (1 intento/s restante/s). Intentelo nuevamente")

    print("Contrasenia correcta.")

main()

#c)
def validar(contrasenia, intentos):
    '''
    Pide la contrasenia al usuario y no le permite continuar hasta que la haya ingresado correctamente.
    Devuelve un booleano si el usuario ingreso la contrasenia correcta.
    '''
    contraseña = 333
    intentos = 3
    password = input("Ingrese la contrasenia: ")
    while password != contraseña and intentos != 3:
        password = input("Contrasenia incorrecta (2 intento/s restante/s). Intentelo nuevamente: ")
        if password != contraseña and intentos != 3:
            password = input("Contrasenia incorrecta (1 intento/s restante/s). Intentelo nuevamente")

    return True
