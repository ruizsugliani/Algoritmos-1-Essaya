#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "es_primo.c"
#include <string.h>

//204
/*
Escribir en C un programa que le pregunte al usuario por 5 números enteros y luego
los imprima de manera inversa al orden en que fueron ingresados.

int main() {
  int entradas[] = {0, 0, 0, 0, 0};
  char buffer[20];
  int entero;
  printf("%s\n", "Por favor ingrese 5 numeros enteros: ");
  for (int i = 4; i != -1; i--) {
    fgets(buffer, 20, stdin);
    entero = atoi(buffer);
    entradas[i] = entero;
  }
  printf("%s\n", "Estas son sus entradas al reves.");
  for (int j = 0; j != 5; j++) {
    printf("%d\n", entradas[j]);
  }

  return 0;
}
*/

//205
/*
Escribir en lenguaje C una función que recibe un arreglo de enteros y su longitud,
y devuelve la norma del arreglo. La norma se calcula como $\sqrt{\sum{{x_i}^2}}$.
Nota: la biblioteca math.h contiene las funciones double sqrt(double x) y double pow(double x, double y).

float norma(int arreglo[], int len) {
  int i = 0;
  int suma = 0;
  while (i < len) {
    suma += pow(arreglo[i], 2);
    i++;
  }
  return sqrt(suma);
}
*/

//206
/*
Escribir un programa en C que pida un número al usuario, imprima un mensaje
indicando si es primo o no, y repita lo mismo hasta que el usuario ingrese -1.

int main() {
  printf("%s\n", "Ingrese un numero para saber si es o no es primo (-1 para terminar)");
  char buffer[30];
  int entrada;
  fgets(buffer , 30, stdin);
  entrada = atoi(buffer);
  if (es_primo(entrada) == 1) {
    printf("%s\n", "Es primo.");
  } else {
     printf("%s\n", "No es primo.");
  }
  while (entrada != -1) {
    printf("%s\n", "Ingrese un numero para saber si es o no es primo (-1 para terminar)");
    fgets(buffer , 30, stdin);
    entrada = atoi(buffer);
    if (es_primo(entrada) == 1) {
      printf("%s\n", "Es primo.");
    } else {
      printf("%s\n", "No es primo.");
    }
  }
  return 0;

}
*/

//207
/*
Escribir en C un programa que pide al usuario un número n >= 1 (repitiendo hasta
que el número ingresado sea válido), y luego imprime un triángulo de altura n.
Ejemplo:
Ingrese la altura del triangulo: 3
*
**
***

void imprimir_triangulo(int n) {
  int i = 0;
    while(i < n) {
      for (int j = 0; j <= i; j++) {
        printf("%c", '*');
    }
    printf("%c", '\n');
    i++;
    }
}


int main() {
  printf("%s\n", "Ingrese un numero mayor o igual a 1 para continuar.");
  char buffer[30];
  fgets(buffer, 30, stdin);
  int n = atoi(buffer);
  while (n < 1) {
    printf("%s\n", "Ingrese un numero mayor o igual a 1 para continuar.");
    fgets(buffer, 30, stdin);
    n = atoi(buffer);
  }
  imprimir_triangulo(n);
  return 0;
}
*/

//208
/*
Escribir en C la función int obtener_valor(const int vector[], int len, int pos).
La función debe devolver el valor que se encuentra en vector[pos], interpretando
pos como en Python. Es decir, pos puede tomar valores entre -len y len - 1; y para
los valores negativos busca los elementos comenzando desde la última posición del vector.
Si pos no es válida, devolver la constante INT_MIN (asumir que la constante ya fue declarada).
*/
/*
Devuelve el elemento en la posicion pasada por parametro, la posicion puede tomar valores entre - len
y len - 1.
*/
#define INT_MIN -6
int obtener_valor(const int vector[], int len, int pos) {
  if (pos < -len || pos > len - 1) {
    return INT_MIN;
  }
  if (pos < 0) {
    return vector[pos + len];
  } else {
    return vector[pos];
  }
}

//209
/*
Escribir en C una función que reciba un número secreto n (de tipo int) y le pregunte
un número al usuario. Si el número ingresado es distinto a n, debe indicarle si
es mayor o menor y volver a pedirle otro número. Si es igual, debe felicitar al
usuario y mostrar en cuántos intentos adivinó.
*/
void adivinar(int secreto) {
  int contador = 0;
  printf("%s\n", "Ingrese un numero para intentar adivinar el numero secreto [1, 100]: ");
  char buffer[30];
  fgets(buffer, 30, stdin);
  int intento = atoi(buffer);
  while (intento <= 100 || intento >= 1) {
    if (intento < secreto) {
      printf("%s\n", "El secreto es mayor, ingrese un numero nuevamente: ");
      contador ++;
      fgets(buffer, 30, stdin);
      intento = atoi(buffer);
    }
    if (intento > secreto) {
      printf("%s\n", "El secreto es menor, ingrese un numero nuevamente: ");
      contador ++;
      fgets(buffer, 30, stdin);
      intento = atoi(buffer);
    }
    if (intento == secreto) {
      printf("%s", "ESE ES EL SECRETO, FELICITACIONES !, TUS INTENTOS: ");
      printf("%d\n", contador);
      break;
    }
  }
}

//210
/*
Escribir en C la función contar_menores, que recibe un vector de enteros y la
cantidad de elementos, y devuelve cuántos números del vector son menores al valor
recibido.
*/
int contar_menores(int numeros[], int len, int valor) {
  int suma = 0;
  for (int i = 0; i < len; i++) {
    if (numeros[i] < valor) {
      suma++;
    }
  }
  return suma;
}

//211
/*
Implementar en C una función que reciba dos arreglos de enteros (y sus respectivos
tamaños), y que imprima los números del primer arreglo que no están presentes en el
segundo. Ejemplo:

int numeros[] = {1, 2, 7, 2, 3, 5};
int ignorar[] = {2, 3};
imprimir(numeros, 6, ignorar, 2);
// Salida:
1
7
5
*/
void imprimir(int arr1[], int len1, int arr2[], int len2) {
  int i, j;
  for (i = 0; i < len1; i++) {
    for (j = 0; j < len2; j++) {
      if (arr1[i] == arr2[j]) {
        break;
      }
    }
    if (j == len2) {
      printf("%d\n", arr1[i]);
    }
  }
}
//212
/*
Escribir en lenguaje C un programa que pida al usuario un número n e imprima un
cuadrado de lado n formado por asteriscos.
Ejemplo:
Ingrese un numero: 4
****
*  *
*  *
****

int main() {
  printf("%s\n", "Ingrese un numero positivo: ");
  char buffer[30];
  fgets(buffer, 30, stdin);
  int entrada = atoi(buffer);
  while (entrada < 1) {
    printf("%s\n", "Ingrese un numero positivo: ");
    fgets(buffer, 30, stdin);
    entrada = atoi(buffer);
  }
  //Imprime el techo
  for (int i = 0; i < entrada; i++) {
    printf("*");
  }
  printf("\n");

  //Imprime los bordes;
  for (int i = 0; i < (entrada - 2); i++) {
    for (int j = 0; j <= entrada; j++) {
      if (j == 0 || j == entrada - 2) {
        printf("*");
      }
      if (j == entrada) {
        printf("\n");
      } else {
        printf(" ");
      }
    }
  }

  //Imprime el piso
  for (int i = 0; i < entrada; i++) {
    printf("*");
  }
  printf("\n");
}
*/

//213
/*
Escribir en lenguaje C una función que recibe una cadena de caracteres e imprime
la cantidad de apariciones de cada caracter. Ejemplo: caracteres("Barbara")
a: 3
b: 1
r: 2
B: 1
Ayuda: recordar que cada caracter (char) es un número entre 0 y 255. Usar un arreglo de 255 posiciones para contar la cantidad de ocurrencias de cada caracter.

void vaciar_array(int numeros[], int len_n) {
  for (int i = 0; i < len_n; i++) {
    numeros[i] = 0;
  }
}

void contar_caracteres(char cadena[], int numeros[]) {
  for (int i = 0; i < strlen(cadena); i++) {
    char c = cadena[i];
    numeros[c]++;
  }
}

void imprimir_caracteres(int numeros[], int len_n) {
  for (int i = 0; i < len_n; i ++) {
    if (numeros[i] > 0) {
      printf("%c : %d\n", i, numeros[i]);
    }
  }
}

int main() {
  char cadena[] = "Santuito";
  int numeros[256];
  vaciar_array(numeros, 256);
  contar_caracteres(cadena, numeros);
  imprimir_caracteres(numeros, 256);
  return 0;
}
*/
//214
/*
Escribir en C una función que pida al usuario que ingrese un número natural e
imprima por pantalla los primeros n números primos. Se debe implementar una función
auxiliar es_primo que recibe un número y devuelve true o false dependiendo si el
número es primo o no. Por ej, si el usuario ingresa 4, debe imprimir 2,3,5,7.
*/
int es_primo(int n){
  int i;
  for (i = 2; i < n; i++) {
    if (n % i == 0) {
      return 0;
    }
  }
  return 1;
}

void imprimir_primeros_pares() {
  int contador = 0;
  printf("Ingrese un numero natural: ");
  char buffer[20];
  fgets(buffer, 20, stdin);
  int n = atoi(buffer);
  for (int i = 2; contador < n ; i++) {
    if (es_primo(i) == 1) {
      printf ("%d\n", i);
      contador ++;
    }
  }
}

//215
/*
Dado un arreglo de enteros y su longitud, escribir en lenguaje C una función que
devuelva el mayor elemento del arreglo.
*/
int encontar_mayor_elemento(int arreglo[], int len) {
  int mayor = arreglo[0];
  for (int i = 1; i < len; i ++) {
    if (arreglo [i] > mayor) {
      mayor = arreglo[i];
    }
  }
  return mayor;
}

//216
/*
Implementar en C la función potencia(), que recibe la base (número entero) y el
exponente (número entero no negativo) y devuelva el resultado de elevar la base
al exponente. Nota: no pueden incluir bibliotecas para resolver la potencia, por
lo que la funcion math.pow no está disponible para usar.
*/
float potencia(int base, int exponente) {
  int i = 1;
  int res = base;
  while (i != exponente) {
    res *= base;
    i++;
  }
  return res;
}

//217
/*
Escribir un programa en C que le pida al usuario que ingrese una cadena y luego
muestre por pantalla esa cadena pero reemplazando cada vocal por un *.

int main() {
  printf("Ingrese una cadena: ");
  char buffer[30];
  fgets(buffer, 30, stdin);
  for (int i = 0; buffer[i] != '\0'; i++) {
    if (buffer[i] == 'a' || buffer[i] == 'e' || buffer[i] == 'i' || buffer[i] == 'o' || buffer[i] == 'u') {
      printf("%c", '*');
    } else {
      printf("%c", buffer[i]);
    }
  }
  printf("\n");
  return 0;
}
*/

//218
/*
Implementar en C la función invertir_arreglo(int arreglo[], unsigned int n), que
invierte el arreglo de números in-place.
*/
void invertir_arreglo(int arreglo[], unsigned int n) {
  int temp;
  for (int i = 0; i < n / 2; i++) {
    temp = arreglo[i];
    arreglo[i] = arreglo[n-i-1];
    arreglo[n-i-1] = temp;
  }
}

//219
/*
Implementar en C una función que reciba un número entero positivo n e imprima
una flecha hacia la derecha de longitud n. Por ejemplo, para n = 4:

*
 *
  *
****
  *
 *
*
*/
void imprimir_flecha(int n) {
  //Imprime la parte superior de la flecha
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0;j < n - 1; j++) {
      if (j == i) {
        printf("*\n");
        break;
      } else {
        printf(" ");
      }
    }
  }

  //Imprime el medio de la flecha
  for (int i = 0; i != n; i++) {
    printf("*");
  }
  printf("\n");

  //Imprime la parte inferior de la flecha
  for (int i = n - 2; i >= 0; i--) {
    for (int j = 0; j < n - 1; j++) {
      if (j == i) {
        printf("*\n");
        break;
      } else {
        printf(" ");
      }
    }
  }
}

//221
/*
Implementar en C una función que reciba una cadena e imprima la cantidad de
letras, números y espacios presentes en la misma. Usar las funciones de la
biblioteca: int isalpha(char), int isdigit(char), isspace(char).

void contar_caracteres(char cadena[]) {
  int c_letras = 0;
  int c_numeros = 0;
  int c_espacios = 0;
  int len = strlen(cadena);
  for (int i =0; i < len; i++) {
    if (isalpha(cadena[i])) {
      c_letras ++;
    } else if (isdigit(cadena[i])) {
      c_numeros ++;
    } else if (isspace(cadena[i])) {
      c_espacios ++;
    }
  }
  printf("%s %d\n", "Letras:", c_letras);
  printf("%s %d\n", "Numeros:", c_numeros);
  printf("%s %d\n", "Espacios:", c_espacios);
}
*/

//222
/*
Escribir en C un programa que pida al usuario dos palabras. El programa debe
imprimir ambas palabras en una línea, separadas por una secuencia de puntos de
forma tal que la longitud total de la línea sea de 30 caracteres. Ejemplo:

Primera palabra: Hola
Segunda palabra: Mundo
Hola.....................Mundo

#define max 200

void quitar_salto(char *palabra) {
  palabra[strlen(palabra)-1] = '\0';
}

int main() {
  printf("%s\n", "Primera palabra:");
  char buffer1[max];
  fgets(buffer1, max, stdin);
  quitar_salto(buffer1+1);

  printf("%s\n", "Segunda palabra:");
  char buffer2[max];
  fgets(buffer2, max, stdin);
  quitar_salto(buffer2+1);


  int len = 30 - (strlen(buffer1) + strlen(buffer2));
  char separadores[30];
    for (int i = 0; i < len; i++) {
        separadores[i] = '.';
    }
    separadores[len] = '\0';

  printf("%s", buffer1);
  printf("%s", separadores);
  printf("%s\n", buffer2);
  return 0;
}
*/

//223
/*
Escribir una función en C que reciba un arreglo de enteros, su largo, y un número
y devuelva la cantidad de veces que aparece ese número en el arreglo. Mostrar su
correcto funcionamiento escribiendo un programa (un main) que permita probarla
pidiéndole un entero al usuario para buscar en un arreglo predefinido.

int apariciones(int arr[], int len, int n) {
  int res = 0;
  for (int i = 0; i < len; i ++) {
    if (arr[i] == n) {
      res ++;
    }
  }
  return res;
}

int main() {
  int arr[] = {1, 2, 3, 4, 5, 6, 7, 5, 5, 5};
  printf("Ingrese un numero a buscar en el arreglo: ");
  char buffer[20];
  fgets(buffer, 20, stdin);
  int n  = atoi(buffer);
  printf("%s %d\n", "El cantidad de apariciones: ", apariciones(arr, 10, n));
  return 0;
}
*/

//224
/*
Escribir en C la funcion void intercalar(const char *s1, const char *s2, char *dest)
que guarda en dest el resultado de intercalar caracter a caracter las cadenas s1 y s2.
Asumir que dest tiene espacio suficiente para guardar el resultado.
*/
void intercalar(const char *s1, const char *s2, char *dest) {
  int len1 = strlen(s1);
  int len2 = strlen(s2);
  int c = 0;
  for (int i = 0; i < (len1 + len2); i++) {
    if (i < len1) {
      dest[c] = s1[i];
      c++;
    }
    if (i < len2) {
      dest[c] = s2[i];
      c++;
    }
  }
  dest[c] = '\0';
}

int main() {
  const char s1[] = "Hola";
  const char s2[] = "mundo!";
  char dest[20];
  intercalar(s1, s2, dest);
  printf("%s\n", dest);
  return 0;
}

//225
/*
Escribir en C una funcion que pida al usuario que ingrese una cadena y la imprima
invertida.
*/
void invertir_cadena_ingresada() {
  printf("Ingrese una cadena: ");
  char buffer[20];
  fgets(buffer, 20, stdin);
  int len = strlen(buffer);

  for (int i = len - 1; i > -1; i--) {
    printf("%c", buffer[i]);
  }
  printf("\n");
}

//226
/*
Escribir en C un programa que pida al usuario un valor mnimo, un valor maximo y un
numero n, e imprima una tabla con los cuadrados de los numeros entre mnimo y maximo cada
n numeros. Por ejemplo (mnimo = 0, maximo = 17, n = 5) debe mostrar:
0 0
5 25
10 100
15 225

int main() {
  //Ingresa el minimo
  printf("Ingrese un minimo: ");
  char buffer1[20];
  fgets(buffer1, 20, stdin);
  int minimo = atoi(buffer1);

  //Ingresa el maximo
  printf("Ingrese un maximo: ");
  char buffer2[20];
  fgets(buffer2, 20, stdin);
  int maximo = atoi(buffer2);

  //Ingresa n
  printf("Ingrese un numero: ");
  char buffer3[20];
  fgets(buffer3, 20, stdin);
  int n = atoi(buffer3);

  for (int i = 0; i < maximo; i += n) {
    printf("%d %d\n", i, i * i);
  }

  return 0;
}
*/

//227
/*
Escribir en C un programa que pida al usuario que ingrese 10 numeros enteros e imprima
el mnimo, el maximo y el promedio.

int main() {
  int entrada[10];
  printf("Ingrese 10 numeros:\n");
  //Agrega los numeros ingresados al arreglo.
  for (int i = 0; i < 10; i++) {
    char buffer[20];
    fgets(buffer, 20, stdin);
    int n = atoi(buffer);
    entrada[i] = n;
  }

  //Busca el minimo
  int min = 0;
  for (int i = 1; i < 10; i ++) {
    if (entrada[min] > entrada[i]) {
      min = i;
    }
  }
  printf("El minimo es : %d\n", entrada[min]);

  //Busca el maximo
  int max = 0;
  for (int i = 1; i < 10; i ++) {
    if (entrada[i] > entrada[max]) {
      max = i;
    }
  }
  printf("El maximo es:  %d\n", entrada[max]);

  //Busca el promedio
  int suma = 0;
  for (int i = 0; i < 10; i++) {
    suma += entrada[i];
  }
  float promedio = suma /10;
  printf("El promedio es : %f\n", promedio);
  return 0;
}
*/

//228
/*
Escribir en lenguaje C un programa que reciba un número entero positivo n e imprima un triángulo equilátero de esa base y altura. Por ejemplo, para n = 4:

   *
  * *
 * * *
* * * *
*/
void imprimir_triangulo(int n){

  for(int k = 1; k <= n; k++){
    for (int i = n - k; i > 0; i--){
      printf(" ");
    }
    for (int j = 0; j < k; j++){
      printf("* ");
    }
    printf("\n");
  }
}
