def tiene_digito(digito, n):
    digitos = str(digito)
    for numero in digitos:
        if numero == n:
            return True
        return False
print(tiene_digito(9, 919))
