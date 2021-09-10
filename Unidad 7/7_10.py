def sumar_matrices(m1, m2):
    '''
    Recibe dos matrices como listas de listas y devuelve la suma.
    Las matrices pueden ser de cualquier tamaño, pero ambas deben ser del mismo
    tamaño.
    '''
    res = []
    for fila1 in m1:
        for i in range(len(fila1)):
            res_fila = []
            num1 = fila1[i]
            for fila2 in m2:
                for i in range(len(fila2)):
                    num2 = fila2[i]
                    res_num = num1 + num2
                    res_fila.append(res_num)
                    res.append(res_fila)
    
    return res

print(sumar_matrices([[2, 3], [1, 9]], [[5, 7], [2, 1]]))
