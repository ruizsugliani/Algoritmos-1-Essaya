'''
Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:
>>> analisis2 = Materia("61.03", "Análisis 2", 8)
>>> fisica2 = Materia("62.01", "Física 2", 8)
>>> algo1 = Materia("75.40", "Algoritmos 1", 6)
>>> c = Carrera([analisis2, fisica2, algo1])
>>> str(c)
Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
>>> c.aprobar("95.14", 7)
ValueError: La materia 75.14 no es parte del plan de estudios
>>> c.aprobar("75.40", 10)
>>> c.aprobar("62.01", 7)
>>> str(c)
Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
75.40 Algoritmos 1 (10)
62.01 Física 2 (7)
'''
class Materia:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

class Carrera:
    def __init__(self, materias):
        self.materias = materias
        self.aprobadas = []
        self.notas = 0
        self.creditos = 0
        self.promedio = "N/A"

    def __str__(self):
        return f"Créditos: {self.creditos} -- Promedio: {self.promedio} -- Materias aprobadas:{self.mostrar_aprobadas()}"

    def aprobar(self, codigo, nota):
        materia_encontrada = False
        for materia in self.materias:
            if materia.codigo == codigo:
                materia_encontrada = True
                if 4 <= nota <= 10:
                    aprobada = f"{materia.codigo} {materia.nombre} ({nota})"
                    self.aprobadas.append(aprobada)
                    self.materias.remove(materia)
                    self.notas += nota
                    self.creditos += materia.creditos
                    self.promedio = self.notas / len(self.aprobadas)

        if not materia_encontrada:
            raise ValueError(f"La materia {codigo} no es parte del plan de estudios")

    def mostrar_aprobadas(self):
        aprobo = ""
        for materia in self.aprobadas:
            aprobo += f'\n{materia}'
        return aprobo
