class Animales:
    def __init__(self,nombre,grupo):
        self.nombre = nombre
        self.grupo = grupo
    def tipo(self):
        pass
        print(f"{self.nombre}, Este animal no es salvaje y pertenece a los {self.grupo}")
class Salvaje(Animales):
    def tipo(self):
        print(f"{self.nombre}, Este animal es salvaje y pertenece a los {self.grupo}")

leon = Salvaje("leon","mamiferos")
ballena = Animales("ballena","mamiferos")
perro = Animales("perro","mamiferos")
araña = Salvaje("araña","Artropodos")
leon.tipo()
ballena.tipo()
perro.tipo()
araña.tipo()

