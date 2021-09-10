import traceback
import random
import editor

def ejercicio_1():
    e = editor.Editor("\n")
    assert e.cantidad_lineas() == 1
    assert str(e) == "\n"

    e = editor.Editor("")
    assert e.cantidad_lineas() == 1
    assert str(e) == "\n"

    e = editor.Editor("linea 1\n")
    assert e.cantidad_lineas() == 1
    assert str(e) == "linea 1\n"

    e = editor.Editor("linea 1\nlinea 2")
    assert e.cantidad_lineas() == 2
    assert str(e) == "linea 1\nlinea 2\n"

    e = editor.leer_archivo('texto.txt')
    assert str(e) == contenido_archivo('texto.txt')

    e.escribir_archivo('texto2.txt')
    assert contenido_archivo('texto.txt') == contenido_archivo('texto2.txt')

def ejercicio_2():
    e = editor.Editor("hola\nmundo")
    assert e.cursor_pos() == (1, 1) # |hola
    assert e.cursor_caracter() == 'h'

    e.mover_derecha()
    assert e.cursor_pos() == (1, 2) # h|ola
    assert e.cursor_caracter() == 'o'
    e.mover_derecha()
    assert e.cursor_pos() == (1, 3) # ho|la
    assert e.cursor_caracter() == 'l'
    e.mover_derecha()
    assert e.cursor_pos() == (1, 4) # hol|a
    assert e.cursor_caracter() == 'a'
    e.mover_derecha()
    assert e.cursor_pos() == (1, 5) # hola|
    assert e.cursor_caracter() == '\n'
    e.mover_derecha()
    assert e.cursor_pos() == (2, 1) # |mundo  (pasamos a la siguiente línea)
    assert e.cursor_caracter() == 'm'
    e.mover_derecha()
    assert e.cursor_pos() == (2, 2) # m|undo
    assert e.cursor_caracter() == 'u'
    e.mover_derecha()
    e.mover_derecha()
    e.mover_derecha()
    assert e.cursor_pos() == (2, 5) # mund|o
    assert e.cursor_caracter() == 'o'
    e.mover_derecha()
    assert e.cursor_pos() == (2, 6) # mundo|
    assert e.cursor_caracter() == '\n'
    e.mover_derecha()
    assert e.cursor_pos() == (2, 6) # mundo|  (final del archivo)
    assert e.cursor_caracter() == '\n'

    e.mover_izquierda()
    assert e.cursor_pos() == (2, 5) # mund|o
    assert e.cursor_caracter() == 'o'
    e.mover_izquierda()
    assert e.cursor_pos() == (2, 4) # mun|do
    assert e.cursor_caracter() == 'd'
    e.mover_arriba()
    assert e.cursor_pos() == (1, 4) # hol|a
    assert e.cursor_caracter() == 'a'
    e.mover_arriba()
    assert e.cursor_pos() == (1, 4) # hol|a (no hay más líneas arriba)
    assert e.cursor_caracter() == 'a'
    e.mover_abajo()
    assert e.cursor_pos() == (2, 4) # mun|do
    assert e.cursor_caracter() == 'd'
    e.mover_abajo()
    assert e.cursor_pos() == (2, 4) # mun|do (no hay más líneas abajo)
    assert e.cursor_caracter() == 'd'

    e.mover_inicio_linea()
    assert e.cursor_pos() == (2, 1) # |mundo
    assert e.cursor_caracter() == 'm'
    e.mover_izquierda()
    assert e.cursor_pos() == (1, 5) # hola|  (pasamos a la línea anterior)
    assert e.cursor_caracter() == '\n'
    e.mover_inicio_linea()
    assert e.cursor_pos() == (1, 1) # |hola
    assert e.cursor_caracter() == 'h'
    e.mover_izquierda()
    assert e.cursor_pos() == (1, 1) # |hola  (inicio del archivo)
    assert e.cursor_caracter() == 'h'

    e.mover_abajo()
    assert e.cursor_pos() == (2, 1) # |mundo
    assert e.cursor_caracter() == 'm'
    e.mover_fin_linea()
    assert e.cursor_pos() == (2, 6) # mundo|
    assert e.cursor_caracter() == '\n'
    e.mover_arriba()
    assert e.cursor_pos() == (1, 5) # hola|  (la línea de arriba era más corta)
    assert e.cursor_caracter() == '\n'

    e.mover_a(1, 2)
    assert e.cursor_pos() == (1, 2) # h|ola
    assert e.cursor_caracter() == 'o'
    e.mover_a(1, 10)
    assert e.cursor_pos() == (1, 5) # hola|
    assert e.cursor_caracter() == '\n'
    e.mover_a(5, 2)
    assert e.cursor_pos() == (2, 2) # m|undo
    assert e.cursor_caracter() == 'u'

def ejercicio_3():
    e = editor.Editor("")

    e.insertar("holamundo")
    assert str(e) == "holamundo\n"
    assert e.cursor_pos() == (1, 10) # holamundo|
    assert e.cantidad_lineas() == 1

    e.mover_a(0, 5)                  # hola|mundo
    assert e.cursor_caracter() == 'm'

    e.insertar(" ")
    assert e.cursor_pos() == (1, 6)  # hola |mundo
    assert e.cursor_caracter() == 'm'
    assert e.cantidad_lineas() == 1
    assert str(e) == "hola mundo\n"

    e = editor.Editor("")
    e.insertar("\n")
    assert str(e) == "\n\n"
    assert e.cantidad_lineas() == 2
    e.insertar("hola\n")
    assert e.cursor_pos() == (3, 1)
    assert e.cursor_caracter() == '\n'
    assert e.cantidad_lineas() == 3
    assert str(e) == "\nhola\n\n"

    e = editor.Editor("1111\n2222\n3333\n")
    e.mover_a(2, 3) # 22|22
    e.insertar("44\n55")
    assert e.cursor_pos() == (3, 3)  # 55|22
    assert e.cursor_caracter() == '2'
    assert e.cantidad_lineas() == 4
    assert str(e) == "1111\n2244\n5522\n3333\n"

def ejercicio_4():
    e = editor.Editor(contenido_archivo('texto.txt'))

    f = e.palabras_mas_frecuentes()
    assert len(f) == 780 # hay 780 palabras únicas en el texto
    f = f[:10]           # me quedo con las primeras 10
    assert_iguales('palabras_mas_frecuentes() (primeras 10)', f, [('║', 30), ('⠹⠑', 9), ('and', 8), ('in', 8), ('the', 8), ('•', 7), ('τὴν', 7), ('καὶ', 7), ('of', 6), ('a', 6)])

def ejercicio_5():
    e = editor.Editor(contenido_archivo('texto.txt'))
    r = e.buscar('and')
    assert_iguales('buscar("and")', r, [(7, 50), (8, 41), (11, 46), (13, 13), (21, 13), (34, 18), (38, 28), (123, 65), (155, 15), (155, 52), (156, 34)])


def assert_iguales(k, v1, v2):
    k1 = f"Resultado de {k}"
    k2 = f"Resultado esperado"
    n = max(len(k1), len(k2))
    assert v1 == v2, f"\n  {k1:<{n}}: {v1}\n  {k2:<{n}}: {v2}"

def contenido_archivo(ruta):
    with open(ruta, encoding='utf8') as f:
        return f.read()

def main():
    ejercicios = [
        ejercicio_1,
        ejercicio_2,
        ejercicio_3,
        ejercicio_4,
        ejercicio_5,
    ]

    ejercicios_ok = 0

    for i, ejercicio in enumerate(ejercicios):
        try:
            random.seed(0)
            ejercicio()
            resultado = 'OK'
            ejercicios_ok += 1
        except:
            print()
            traceback.print_exc()
            print()
            resultado = 'FAIL'
        print(f"{ejercicio.__name__}: {resultado}")

    print(f"Cantidad de ejercicios OK: {ejercicios_ok}")

main()
