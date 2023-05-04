class Bebidas:
    def __init__(self, nombre, valor, tamaño):
        self.nombre = nombre
        self.valor = valor
        self.tamaño = tamaño
    def tipodeBebida (self):
        print(f"{self.nombre} este tipo de bebida es caliente, cuesta {self.valor} y viene en tamaño {self.tamaño}")
    def cambiarBebida(self,nuevaBebida):
        self.nombre = nuevaBebida
        print(f"su nueva bebida es: {self.nombre}")
class TiBebida(Bebidas):
    def tipodeBebida(self):
        print(f"{self.nombre} este tipo de bebida es fria, cuesta {self.valor} y viene en tamaño {self.tamaño}")
bebida1 =Bebidas("Cafe","2.000","pequeño")
print(bebida1.nombre, bebida1.valor,bebida1.tamaño)
bebida1.tipodeBebida()
bebida2 = TiBebida("Avena","3.000","grande")
bebida2.tipodeBebida()

