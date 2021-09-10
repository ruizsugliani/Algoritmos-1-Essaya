def duracion_a_segundos(h, m, s):
    '''
    Recibe horas , minutos y segundos para devolver la duración en segundos.
    '''
    return(3600 * h + 60 * m + s)

def segundos_a_hms(segundos):
    '''
    Recibe segundos y devuelve horas , minutos y segundos.
    '''

    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60

    return f"{h} horas {m} minutos {s} segundos"

def main():
    """
    Pida al usuario dos intervalos expresados en horas, minutos y segundos,
    sume sus duraciones, y muestre por pantalla la duración total en horas,
    minutos y segundos.
    """
    h1 = int(input("Ingrese horas del primer intervalo: "))
    m1 = int(input("Ingrese minutos del primer intervalo: "))
    s1 = int(input("Ingrese segundos del primer intervalo: "))

    h2 = int(input("Ingrese horas del segundo intervalo: "))
    m2 = int(input("Ingrese minutos del segundo intervalo: "))
    s2 = int(input("Ingrese segundos del segundo intervalo: "))

    duracion_segundos_1 = duracion_a_segundos(h1, m1, s1)
    duracion_segundos_2 = duracion_a_segundos(h2, m2, s2)

    duracion_final_segundos = duracion_segundos_1 + duracion_segundos_2
    print(segundos_a_hms(duracion_final_segundos))
main()
