#include <stdio.h>
/*
Escribir una función que permita calcular el área de un rectángulo dada su base
y altura.
*/
float area_rectangulo(float base, float altura) {
  return base * altura;
}

int main(){
  printf("%f\n", area_rectangulo(3, 5));
  return 0;
}

/*
Recibe una cadena de texto y luego imprime la cadena enmarcada entre asteriscos (*).
*/
void imprimir_enmarcado(char mensaje[]) {
  int len = strlen(mensaje) + 4;
  int i = 0;
  int j = 0;
  while (i < len) {
    printf("%s", "*");
    i++;
  }
  printf("%s", "\n");
  printf("%s", "* ");
  printf("%s", mensaje);
  printf("%s\n", " *");
  while (j < len) {
    printf("%s", "*");
    j++;
  }
}

int main() {
  char mensaje[] = "Te extraño";
  imprimir_enmarcado(mensaje);
  return 0;
}

/*
Escribir una función que reciba un número entero n y calcule el factorial de n.
En forma iterativa y recursiva.
*/
int factorial_iterativa(int n) {
  int res = 1;
  for (int i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}

int main() {
  printf("%d\n", factorial_iterativa(5));
  return 0;
}

/*
Escribir una función que reciba un arreglo de números y la cantidad de elementos,
y devuelva el promedio.
*/
float promedio(float array[], int len) {
  float suma = 0;
  for (int i = 0; i < len; i++) {
    suma += array[i];
  }
  return suma / len;
}

int main() {
 float array[] = {1.6, 2.4, 3, 4.8, 5, 6.7};
  printf("%f\n", promedio(array, 6));
  return 0;
}

/*
Usando las funciones printf y sizeof, escribir un programa que imprima el
tamaño en bytes de cada uno de los siguientes tipos: bool, char, short, int, long, float, double,
bool*, char*, short*, int*, long*, float*, double*.
*/
int main() {
  printf("bool: %zd\n", sizeof(bool));
  printf("char: %zd\n", sizeof(char));
  printf("short: %zd\n", sizeof(short));
  printf("int: %zd\n", sizeof(int));
  printf("long: %zd\n", sizeof(long));
  printf("float: %zd\n", sizeof(float));
  printf("double: %zd\n", sizeof(double));
  printf("bool*: %zd\n", sizeof(bool*));
  printf("char*: %zd\n", sizeof(char*));
  printf("short*: %zd\n", sizeof(short*));
  printf("int*: %zd\n", sizeof(int*));
  printf("long*: %zd\n", sizeof(long*));
  printf("float*: %zd\n", sizeof(float*));
  printf("double*: %zd\n", sizeof(double*));
  return 0;
}

/*
Implementar la función unsigned int strlen(const char *s) que devuelve la
longitud de la cadena s (sin contar el último caracter '\0').
a) En forma iterativa.
b) En forma recursiva.
*/
#include <stdio.h>
unsigned int longitud(const char s[]) {
  int i = 0 ;
  while (s[i] != '\0'){
    i++;
  }
  return i;
}

int main() {
  const char s[] = "hola";
  printf("La longitud de la cadena es: %d\n", longitud(s));
  return 0;
}

/*
  Funcion que inverte la cadena ingresada por parametro in place.
*/
void invertir(char s[]) {
  int len = strlen(s);
  for (int i = 0; i < len / 2 ; i++) {
    s[i] = s[len-i-1];
  }
}

int main() {
  char s[] = "hola";
  printf("%c\n", invertir(s));
  return 0;
}

/*
Copia la cadena origen en la dirección de memoria apuntada por destino..
*/
void copiar(const char *origen[], char *destino[]) {
  for (int i = 0; origen[i] != '\0'; i++) {
    destino[i] = origen[i];
  }
}


int main () {
  char origen[] = "hola";
  char destino[10];
  copiar(origen, destino);
  printf("%s", destino);
  return 0;
}

/*
Recibe un arreglo de números y su longitud y lo
ordena mediante el algoritmo de ordenamiento por selección.
*/
int buscar_maximo(int numeros[], int len) {
  int maximo = 0;
  for(int i = 1; i < len; i++) {
    if(numeros[i] > numeros[maximo]) {
      maximo = i;
    }
  }
  return maximo;
}

void intercambiar(int *n1, int *n2) {
  int temp = *n1;
  *n1 = *n2;
  *n2 = temp;
}

void ordenar(int* numeros, int n) {
  for (int i = 0; i < n - 1; i++) {
    int mayor = buscar_maximo(numeros, n);
    if (numeros[i] > numeros[mayor]) {
      intercambiar(&numeros[i], &numeros[mayor]);
    }
  }
}


int main() {
  int* numeros[] = {1, 4, 5, 2, 3};
  printf("%d\n", buscar_maximo(numeros, 5));
  return 0;
}

/*
Recibe un mensaje y dos números enteros min y max. La función debe pedir al usuario que ingrese un número entero entre min y max (inclusive) y devolverlo. Si el usuario ingresa un valor inválido se le debe informar y pedir que ingrese un
nuevo valor, repitiendo hasta que ingrese un número válido.
*/
int pedir_entero(int min, int max, char mensaje[]) {
  printf("%s", mensaje);
  printf("%s", " [");
  printf("%d", min);
  printf("%s", "...");
  printf("%d", max);
  printf("%s\n", "]:");
  char buffer[30];
  fgets(buffer, 30, stdin);
  int n = atoi(buffer);
  while (n < min || n > max) {
    printf("%s", "Por favor ingresa un numero entre ");
    printf("%d", min);
    printf("%s", " y ");
    printf("%d", max);
    printf("%c\n", '.');
    printf("%s", mensaje);
    printf("%s", " [");
    printf("%d", min);
    printf("%s", "...");
    printf("%d", max);
    printf("%s\n", "]:");
    fgets(buffer, 30, stdin);
    n = atoi(buffer);
  }
  return n;
}

int main() {
  char mensaje[] = "¿Cual es tu numero favorito?";
  int min = -50;
  int max = 50;
  pedir_entero(min, max, mensaje);
  return 0;
}

/*
Escribir una función en C que le pida al usuario que ingrese números del 0 al 9.
Repetir este proceso hasta que el usuario ingresa -1.
Luego, mostrar por pantalla cuantas veces ingresó cada número.
Ayuda: usar un arreglo con las posiciones del 0 al 9 como diccionario.
*/
void vaciar_array(int numeros[], int len_n) {
  for (int i = 0; i < len_n; i++) {
    numeros[i] = 0;
  }
}

void mostrar_entradas(int entradas[]) {
  for (int i = 0; i < 10; i ++) {
    if (entradas[i] > 0) {
      printf("%d : %d\n", i, entradas[i]);
    }
  }
}

void cantidad_de_entradas() {
  int entradas[10];
  vaciar_array(entradas, 10);
  printf("Ingrese números del 0 al 9 (-1) para terminar: \n");
  char buffer[20];
  fgets(buffer, 20, stdin);
  int entrada = atoi(buffer);;
  while (entrada != -1) {
    char buffer[20];
    fgets(buffer, 20, stdin);
    int entrada = atoi(buffer);
    int numero = entrada;
    entradas[numero]++;
  }
  mostrar_entradas(entradas);
}


int main() {
  cantidad_de_entradas();
  return 0;
}
