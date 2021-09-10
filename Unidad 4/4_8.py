def signo_zodiacal(dia, mes):
    if  21 <= dia <= 31 and mes == 3 or 1 <= dia <= 20 and mes == 4:
        print("Aries")
    elif 21 <= dia <= 30 and mes == 4 or 1 <= dia <= 20 and mes == 5:
        print("Tauro")
    elif 21 <= dia <= 31 and mes == 5 or 1 <= dia <= 21 and mes == 6:
        print("Geminis")
    elif 22 <= dia <= 30 and mes == 6 or 1 <= dia <= 23 and mes == 7:
        print("Cancer")
    elif 24 <= dia <= 31 and mes == 7 or 1 <= dia <= 23 and mes == 8:
        print("Leo")
    elif 24 <= dia <= 31 and mes == 8 or 1 <= dia <= 23 and mes == 9:
        print("Virgo")
    elif 24 <= dia <= 30 and mes == 9 or 1 <= dia <= 22 and mes == 10:
        print("Libra")
    elif 23 <= dia <= 31 and mes == 10 or 1 <= dia <= 22 and mes == 11:
        print("Escorpio")
    elif 23 <= dia <= 30 and mes == 11 or 1 <= dia <= 21 and mes == 12:
        print("Sagitario")
    elif 22 <= dia <= 31 and mes == 12 or 1 <= dia <= 20 and mes  == 1:
        print("Capricornio")
    elif 21 <= dia <= 31 and mes == 1 or 1 <= dia <= 19 and mes == 2:
        print("Acuario")
    else:
        print("Piscis")

def main():
    """
    Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
    y el programa le debe decir a qué signo corresponde
    """
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    signo_zodiacal(dia, mes)
main()
