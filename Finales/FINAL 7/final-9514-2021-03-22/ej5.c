#include <stdio.h>
#include <assert.h>
#include <string.h>

/*
Escribir en lenguaje C la función void borrar_espacios_consecutivos(char s[]) que
elimina in-place los espacios consecutivos en la cadena s. Ejemplo:
char s[] = "A otro   perro con  ese hueso";
borrar_espacios_consecutivos(s);
// s contiene "A otro perro con ese hueso"
*/
void borrar_espacios_consecutivos(char s[]) {
  int j = 0;
  for (int i = 0; s[i] != '\0'; i++) {
    if (i == 0) {
      s[j] = s[i];
      j++;
    } else {
      if (s[j-1] != ' ') {
        s[j] = s[i];
        j++;
      } else if (s[j-1] == ' ' && s[i] != ' ') {
        s[j] = s[i];
        j++;
      }
    }
  }
  s[j] = '\0';
}

int main(void) {
    char s[] = "A otro    perro con   ese  hueso";
    char x[] = "  A otro    perro con   ese  hueso";
    char j[] = "           aguante  eee e bo  ki ta   a    ";
    borrar_espacios_consecutivos(s);
    borrar_espacios_consecutivos(x);
    borrar_espacios_consecutivos(j);
    printf("%s\n", s);
    printf("%s\n", x);
    printf("%s\n", j);

    return 0;
}
