def agenda():
    '''
    El programa solicita al usuario que ingrese nombres, si el nombre se encuentra
    debe mostrar el teléfono y opcionalmente permitir modificarlo si no es correcto.
    Si el nombre no se encuentra, debe permitir ingresar el telefono correspondiente.
    El usuario puede utilizar la cadena "*" para salir del programa.
    '''
    agenda = {}
    while True:
        nombre = input("Ingrese un nombre, o * para salir: ")
        if nombre == "*":
            break

        if nombre not in agenda:
            print("Persona no agendada")
            numero = input(f"Ingrese el telefono para {nombre}: ")
            if numero == "":
                print()
                continue
            while not numero.isdigit() or not len(numero) != 0 or numero == " ":
                numero = input(f"Ingrese el telefono para {nombre}: ")
            agenda[nombre] = numero
            print(f"Nuevo telefono registrado para {nombre}, {numero}\n")
            continue

        if nombre in agenda:
            print(f"Telefono de {nombre} es {agenda[nombre]}")
            numero = input(f"Ingrese el telefono para {nombre}: ")
            if numero == "":
                print()
                continue
            agenda[nombre] = numero
            print(f"Telefono actualizado para {nombre}, {numero}\n")
            continue

agenda()
