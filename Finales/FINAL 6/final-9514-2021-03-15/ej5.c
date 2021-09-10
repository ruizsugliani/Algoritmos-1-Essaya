#include <stdio.h>
#include <assert.h>
#include <string.h>

/*
Escribir en C la función void intercalar(const char *s1, const char *s2, char
*dest) que guarda en dest el resultado de intercalar caracter a caracter las cadenas s1 y s2.
Asumir que dest tiene espacio suficiente para guardar el resultado.
Ejemplo: para las cadenas "Hola" y "mundo!" el resultado en dest sería "Hmoulnado!"
*/
void intercalar(const char *s1, const char *s2, char *dest) {
  int c = 0;
  int len1 = strlen(s1);
  int len2 = strlen(s2);
  for (int i; i < (len1 + len2); i++) {
    if (i < strlen(s1)) {
      dest[c] = s1[i];
      c++;
    }
    if (i < strlen(s2)) {
      dest[c] = s2[i];
      c++;
    }
  }
  dest[c] = '\0';
}

int main(void) {
    char dest[30];
    intercalar("Hola", "mundo!", dest);

    assert(strcmp(dest, "Hmoulnado!") == 0);

    // OPCIONAL: Pruebas adicionales. Sugerencias:
    // - una cadena vacía
    // - ambas cadenas vacías

    printf("%s: OK\n", __FILE__);
    return 0;
}
