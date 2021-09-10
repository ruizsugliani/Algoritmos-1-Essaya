def duracion_a_segundos(h, m, s):
    '''
    Recibe horas , minutos y segundos para devolver la duración en segundos.
    '''
    return(3600 * h + 60 * m + s)

def segundos_a_hms(segundos):
    '''
    Recibe segundos y devuelve horas , minutos y segundos.
    '''

    h = 3600 / segundos
    m = 60 / segundos
    s = segundos

    return (h, m, s)

def main():
    """
    Recibe dos intervalos en horas, minutos y segundos, suma sus duraciones e
    imprime la duracion total en horas, minutos y segundos.
    """
    h1 = int(input("Ingrese horas del primer intervalo: "))
    m1 = int(input("Ingrese minutos del primer intervalo: "))
    s1 = int(input("Ingrese segundos del primer intervalo: "))

    h2 = int(input("Ingrese horas del segundo intervalo: "))
    m2 = int(input("Ingrese minutos del segundo intervalo: "))
    s2 = int(input("Ingrese segundos del segundo intervalo: "))

    i1 = duracion_a_segundos(h1, m1, s1)
    i2 = duracion_a_segundos(h2, m2, s2)

    (hf1, mf1, sf1) = segundos_a_hms(i1)
    (hf2, mf2, sf2) = segundos_a_hms(i2)

    print(hf1 + hf2, "horas", mf1 + mf2, "minutos", sf1 + sf2, "segundos")
main()
