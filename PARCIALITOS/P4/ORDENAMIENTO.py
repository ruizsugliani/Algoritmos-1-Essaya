def merge(lista1, lista2, lista3):
    i, j, k = 0, 0, 0
    res = []
    while (i < len(lista1) and j < len(lista2) and k < len(lista3)):
        if (lista1[i] < lista2[j] and lista1[i] < lista3[k]):
            res.append(lista1[i])
            i += 1

        elif (lista2[j] < lista1[i] and lista2[j] < lista3[k]):
            res.append(lista2[j])
            j += 1

        else:
            res.append(lista3[k])
            k += 1

    res += lista1[i:]
    res += lista2[j:]
    res += lista3[k:]
    return res

def merge_sort_3(lista):
    if len(lista) < 2:
        return lista
    medio = len(lista) // 3
    izq = merge_sort_3(lista[:medio])
    mid = merge_sort_3([medio])
    der = merge_sort_3(lista[medio:])
    return merge(izq, mid, der)

print(merge_sort_3([6, 4, 7, -2, -1, 0, 8, 2]))
