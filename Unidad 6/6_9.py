def convertir_a_decimal(n_binario):
    res = 0
    for i in range(0, len(n_binario)):
        numero = int(n_binario[i])
        res += numero * 2 ** i
    return res * 2

print(convertir_a_decimal("1010"))
