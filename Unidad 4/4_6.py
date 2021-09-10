"""
Suponiendo que el primer día del año fue lunes, escribir una función que reciba
un número con el día del año n (de 1 a 366) y devuelva el día de la semana
que le toca.
"""
#Recibe un numero con el dia del año
#Devuelve el dia de la semana que le toca

def dia_semana(n):
    clave = n % 7
    if clave == 0:
        return "domingo"
    elif clave == 1:
        return "lunes"
    elif clave == 2:
        return "martes"
    elif clave == 3:
        return "miércoles"
    elif clave == 4:
        return "jueves"
    elif clave == 5:
        return "viernes"
    elif clave == 6:
        return "sábado"

print(dia_semana(3))
