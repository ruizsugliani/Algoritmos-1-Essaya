#include <stdio.h>
#include <assert.h>

#include <string.h>
/*
Implementar en C la función void join(char destino[], char delimitador, char
*cadenas[], int n), que a partir de un arreglo de cadenas guarda en destino la cadena
formada por todas las cadenas separadas por el delimitador. Asumir que destino tiene espacio
suficiente.
*/
void join(char destino[], char delimitador, char *cadenas[], int n) {
  int c = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; cadenas[i][j] != '\0'; j++) {
      if (cadenas[i][j+1] != '\0') {
        destino[c] = cadenas[i][j];
        c++;
      } else if (cadenas[i][j+1] == '\0') {
        destino[c] = cadenas[i][j];
        c++;
        destino[c] = delimitador;
        c++;
      }
    }
  }
  destino[c-1] = '\0';
}

int main(void) {
    char *cadenas[] = { "2021", "04", "05" };
    char s[16];

    char *cadenas1[] = {"hola", "mundo", "como", "esta", "?"};
    char s1[25];

    char *cadenas2[] = {"final", "de", "algoritmos", "1"};
    char s2[35];

    join(s, '-', cadenas, 3);
    assert(!strcmp(s, "2021-04-05"));

    join(s1, '-', cadenas1, 5);
    assert(!strcmp(s1, "hola-mundo-como-esta-?"));

    join(s2, '+', cadenas2, 4);
    assert(!strcmp(s2, "final+de+algoritmos+1"));


    printf("%s: OK\n", __FILE__);
    return 0;
}
