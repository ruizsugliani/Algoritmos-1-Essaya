def nombres_populares(archivo):
    nombres_por_anio = {}
    nombres_populares = {}
    with open(archivo) as file:
        for linea in file:
            linea = linea.rstrip('\n').split(';')
            if len(linea) == 3:
                if len(linea[0].split('-')) == 3:
                    anio, mes, dia = linea[0].split('-')
                    apellido = linea[1]
                    nombres = linea[2].split()

                    if anio not in nombres_por_anio:
                        nombres_por_anio[anio] = {}
                    for nombre in nombres:
                        nombre = nombre.lower()
                        if nombre not in nombres_por_anio[anio]:
                            nombres_por_anio[anio][nombre] = 0
                        nombres_por_anio[anio][nombre] += 1

    for anio in nombres_por_anio:
        if anio not in nombres_populares:
            nombres_populares[anio] = ''
        for nombre in nombres_por_anio[anio]:
            if nombres_por_anio[anio][nombre] == max(nombres_por_anio[anio].values()):
                nombres_populares[anio] = nombre

    return nombres_populares

print(nombres_populares('nacimientos.csv'))

def pruebas():

    # creamos un archivo de prueba nacimientos.csv
    with open('nacimientos.csv', 'w') as f:
        f.write('\n'.join([s.strip() for s in """
            1980-01-21;Browning;Lucille Kimora
            1980-12-20;Carey;Caitlyn
            1980-09-05;CHERRY;JANIAH CAITLYN
            1980-03-12;Graves;Serenity
            1980-04-07;Melendez;Essence
            1980-03-05;;
            1980-07-09;MOLINA SHAH;LUZ
            1981-04-25;Barron;Jacqueline
            1981-07-28;CARR;JANESSA
            ;Bryan;Evelin
            1981-08-15;Esparza;Linda Elise
            1981-07-15;Lucas;Chanel
            1981-10-13;mcdowell knight;jacqueline jordin
            1981-01-03;Pineda;Kinley
        """.split('\n')]))

    #
    # HACER: llamar a la función, y verificar con assert el valor devuelto
    # Los nombres más populares son: Caitlyn en 1980 y Jacqueline en 1981.
    #
    populares = nombres_populares('nacimientos.csv')
    assert populares['1980'] == 'caitlyn'
    assert populares['1981'] == 'jacqueline'

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
