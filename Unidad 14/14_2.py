class Impresora:
    def __init__(self, nombre, max_tinta):
        self.nombre = nombre
        self.max_tinta = max_tinta
        self.documentos = Cola()

    def encolar(self, documento):
        self.documentos.encolar(documento)

    def imprimir(self):
        tinta = self.max_tinta - 1
        if len(self.documentos) == 0:
            print("No tengo documentos para imprimir.")

        else:
            if tinta >= 0:
                primer_documento = self.documentos.pop(0)
                print(f'{primer_documento} impreso.')

            else:
                print("No tengo tinta.")

    def cargar_tinta(self):
        return self.max_tinta

class Oficina:
    def __init__(self):
        self.impresora = str(impresora)
        self.impresoras = []

    def agregar_impresora(self, impresora):
        impresoras.append(impresora)

    def quitar_impresora(self, impresora):
        impresoras.remove(impresora)
