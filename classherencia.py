class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def saludar(self):
        print(f'Hola, soy {self.nombre}')
    def presentarse(self):
        print(f'Mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}')
class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion,materias):
        super().__init__(nombre, edad, profesion)
        self.materias = materias
    def materiasN(self, newmateria):
        self.materias = newmateria
        print(f"la nueva materia que va a ver es {self.materias}")
class PresentarEs(Estudiante):
    def __init__(self, nombre, edad, profesion, materias):
        super().__init__(nombre, edad, profesion, materias)
    def presentarse(self):
        print(f'Mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}. Actualmente estoy viendo la materia {self.materias}' )
class Cursando(PresentarEs):
    def __init__(self, nombre, edad, profesion, materias,aCursado):
        super().__init__(nombre, edad, profesion, materias)
        self.aCursado = aCursado
    def newcursado(self, newACursado):
        self.aCursado = newACursado
        print(f"el grado que actualmente va a cursar es {self.aCursado}")
persona1 = Persona('Juan', 30, 'programador')
persona2 = Persona('María', 25, 'médico')
persona1.saludar() 
persona2.presentarse()
estudiante1 = Estudiante("Sebastian", 14, "estudiante","español")
print(estudiante1.nombre,estudiante1.edad,estudiante1.profesion,estudiante1.materias)
estudiante1.materiasN("ciencias sociales")
estudiante2 = PresentarEs("Esteban",15,"estudiante","edu.fisica")
estudiante2.presentarse()
estudiante3 = Cursando("Maycol", 16,"estudiante","musica","decimo")
print(estudiante3.nombre,estudiante3.edad,estudiante3.profesion,estudiante3.materias,estudiante3.aCursado)
estudiante3.presentarse()


