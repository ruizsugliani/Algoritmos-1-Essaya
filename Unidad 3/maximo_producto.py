def maximo_producto(num_1, num_2, num_3, num_4):
    '''
    Recibe 4 números y devuelve el producto más grande que se puede
    obtener entre ellos.
    '''
    maximo_prod = max(num_1 * num_2, num_1 * num_3, num_1 * num_4, num_2 * num_1, num_2 * num_3, num_2 * num_4, num_3 * num_1, num_3 * num_2, num_3 * num_4, num_4 * num_1, num_4 * num_2, num_4 * num_3)
    #m2 = max(num_2 * num_1, num_2 * num_3, num_2 * num_4)
    #m3 = max(num_3 * num_1, num_3 * num_2, num_3 * num_4)
    #m4 = max(num_4 * num_1, num_4 * num_2, num_4 * num_3)
    #mf = max(m1, m2 , m3, m4)

    return maximo_prod

print(maximo_producto(1, 5, -2, -4))
