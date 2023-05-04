class Cuerposcelestes:
    def __init__(self,nombre, distancia,diametro):
        self.nombre = nombre
        self.distancia = distancia
        self.diametro = diametro
    def tipo(self):
        print(f"este es un planeta y tiene de nombre: {self.nombre}, se encuentra a una distancia de la tierra de {self.distancia}")
class Estrellas(Cuerposcelestes):
    def tipo(self):
        print(f"esta es una estrella y lleva por nombre: {self.nombre} y tiene un diametro de {self.diametro}")
class Satelite(Cuerposcelestes):
    def tipo(self):
        print(f"este es un satelite y lleva el nombre: {self.nombre} y tiene un diametro de {self.diametro}")
marte = Cuerposcelestes("marte","54,6 millones de Km","6,779Km")
jupiter = Cuerposcelestes("jupiter","965,6 millones de Km","139,820Km")
luna = Satelite("Luna","384,400 km","3,474.8 Km")
Sol = Estrellas("sol","150.000.000 km","1.3927 millones de Km")
marte.tipo()
jupiter.tipo()
luna.tipo()
Sol.tipo()
