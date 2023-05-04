class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def saludar(self):
        print(f'Hola, soy {self.nombre}')
    def presentarse(self):
        print(f'Mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}')
persona1 = Persona('Juan', 30, 'programador')
persona2 = Persona('María', 25, 'médico')
persona1.saludar() 
persona2.presentarse() 