def convertir_a_decimal(n_binario):
    if n_binario == "0000":
        return 0
    elif n_binario == "0001":
        return 1
    elif n_binario == "0010":
        return 2
    elif n_binario == "0011":
        return 3
    elif n_binario == "0100":
        return 4
    elif n_binario == "0101":
        return 5
    elif n_binario == "0110":
        return 6
    elif n_binario == "0111":
        return 7
    elif n_binario == "1000":
        return 8
    elif n_binario == "1001":
        return 9
    else:
        return 10

print(convertir_a_decimal('1010'))
