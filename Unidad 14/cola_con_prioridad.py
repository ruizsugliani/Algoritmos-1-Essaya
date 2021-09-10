from cola import Cola

class ColaConPrioridad:
    def __init__(self):
        self.normales = Cola()
        self.prioritarios = Cola()

    def encolar_normal(self, elemento):
        self.normales.encolar(elemento)

    def encolar_prioritarios(self, elementos):
        self.prioritarios.encolar(elemento)

    def desencolar(self):
        if self.prioritarios.esta_vacia():
            return self.normales.desencolar()
        return self.prioritarios.desencolar()

    def __str__(self):
        return f"Prioritarios: {self.prioritarios}, Normales: {self.normales}"

c = ColaConPrioridad
c.encolar_normal('N1')
c.encolar_prioritarios('P1')
c.encolar_normal('N2')
c.encolar_normal('N3')
c.encolar_prioritarios('P2')
