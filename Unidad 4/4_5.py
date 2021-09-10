"""
Escribir funciones que resuelvan los siguientes problemas:
a) Dado un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
excepto que también sea divisible por 400.
b) Dado un mes y un año, devolver la cantidad de días correspondientes.
c) Dada una fecha (día, mes, año), indicar si es válida o no.
d) Dada una fecha, indicar los días que faltan hasta fin de mes.
e) Dada una fecha, indicar los días que faltan hasta fin de año.
f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
entre ambas, en años, meses y días.
"""

#a)
def bisiesto(anio):
    """ Recibe un anio y devuelve True si es bisiesto y False en caso contrario"""
    if anio % 4 == 0:
        if anio % 400 == 0:
            return True
        else:
            if anio % 100 == 0:
                return False
            else:
                return True
    else:
        return False
#b)
def dias_del_mes(mes, anio):
    """Dado un mes y un año, devuelve la cantidad de días correspondientes."""
    if bisiesto(anio) and mes == 2:
        return 29
    elif not bisiesto(anio) and mes == 2:
        return 28
    elif mes == 1:
        return 31
    elif mes == 3:
        return 31
    elif mes == 4:
        return 30
    elif mes == 5:
        return 31
    elif mes == 6:
        return 30
    elif mes == 7:
        return 31
    elif mes == 8:
        return 31
    elif mes == 9:
        return 30
    elif mes == 10:
        return 31
    elif mes == 11:
        return 30
    else:
        return 31
#c)
def fecha_valida(dia, mes, anio):
    """Indicar si es válida o no."""
    if dia <= dias_del_mes(mes, anio):
        return True
    return False

#d)
def dias_hasta_fin_de_mes(dia, mes, anio):
    

#e)
def dias_h_fin_de_anio(dia, mes ,anio):
    if 1 <= dia <= 365:
        return 365 - dia
