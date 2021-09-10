#include <stdio.h>
/*
Recibe un vector de enteros y la cantidad de elementos, y 
devuelve cuántos números del vector son menores al valor recibido.
*/
int contar_menores(int *vector, int len, int valor) {
    int res = 0;
    for (int i = 0; i < len; i++){
        if (vector[i] < valor) {
            res++;
        } else {
            continue;
        }
    }
    return res;
}

int main() {
    int vector[] = {2, 4, 1, 3, 2, 5};
    int r = contar_menores(vector, 6, 1);
    printf("%d\n", r);
    return 0;
}