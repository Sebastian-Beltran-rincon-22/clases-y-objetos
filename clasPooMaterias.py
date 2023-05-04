class Materias:
    def __init__(self, nomMaterias, diaSemana, ):
        self.nomMaterias = nomMaterias
        self.diaSemana = diaSemana
    def estado_apro(self):
        print(f"{self.nomMaterias} se encuentra aprobadada")
    def estado_repro(self):
        print(f"{self.nomMaterias} se encuentra no aprobada")
    def cambio_Materia(self, newMateria):
        self.nomMaterias = newMateria
        print(f"Su nueva materia registrada es {self.nomMaterias}")
materia1 = Materias("matematicas", "lunes y jueves")
print (materia1.nomMaterias, materia1.diaSemana)
materia1.estado_apro()
materia2 = Materias ("español" ,"martes y miercoles")
print(materia2.nomMaterias, materia2.diaSemana)
materia2.estado_apro()
materia3 = Materias("musica" , "viernes")
print(materia3.nomMaterias, materia3.diaSemana)
materia3.estado_repro()
materia3.cambio_Materia("edu.fisica")
