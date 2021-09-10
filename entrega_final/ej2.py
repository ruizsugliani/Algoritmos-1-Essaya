class RegistroDeDesplazamiento:
    def __init__(self, n):
        self.registro = [0 for _ in range(n)]

    def __str__(self):
        cadena = ""
        for n in self.registro:
            cadena += str(n)
        return f"{cadena}"

    def rshift(self, bit):
        valor_a_devolver = self.registro[-1]
        for i in range(len(self.registro) - 1, 0, -1):
            self.registro[i] = self.registro[i-1]
        self.registro[0] = bit
        return valor_a_devolver

    def lshift(self, bit):
        valor_a_devolver = self.registro[0]
        for i in range(0, len(self.registro)-1):
            if self.registro[i+1] != None:
                self.registro[i] = self.registro[i+1]
            else:
                self.registro[i] = 0
        self.registro[-1] = bit
        return valor_a_devolver

def pruebas():
    r = RegistroDeDesplazamiento(4)

    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'
    assert r.rshift(1) == 0
    assert str(r) == '1000'
    assert r.rshift(0) == 0
    assert str(r) == '0100'
    assert r.rshift(0) == 0
    assert str(r) == '0010'
    assert r.rshift(0) == 0
    assert str(r) == '0001'
    assert r.rshift(0) == 1
    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'

    # OPCIONAL: pruebas adicionales (ej: probar lshift)

    l = RegistroDeDesplazamiento(4)

    assert str(l) == '0000'
    assert l.lshift(0) == 0
    assert str(l) == '0000'
    assert l.lshift(1) == 0
    assert str(l) == '0001'
    assert l.lshift(0) == 0
    assert str(l) == '0010'
    assert l.lshift(0) == 0
    assert str(l) == '0100'
    assert l.lshift(0) == 0
    assert str(l) == '1000'
    assert l.lshift(0) == 1
    assert str(l) == '0000'
    assert l.lshift(0) == 0
    assert str(l) == '0000'

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
