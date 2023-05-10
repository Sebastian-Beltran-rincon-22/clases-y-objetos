class Human:
    def __init__(self, name, gender, age, city):
        self.__name = name
        self.gender = gender
        self.age = age
        self.city = city

    def get_name(self):
        return self.__name

class Occupation(Human):
    def __init__(self, name, gender, age, city, occupation):
        super().__init__(name, gender, age, city)
        self.occupation = occupation

name = input("Ingrese su nombre: ")
while not name:
    print("Datos incorrectos")
    name = input("Ingrese su nombre nuevamente: ")

gender = input("Ingrese su género (m: masculino, f: femenino, n: otro): ")
while gender not in ["m", "f", "n"]:
    print("Error")
    gender = input("Ingrese su género nuevamente: ")

age = int(input("Ingrese su edad: "))
while not (5 <= age <= 100):
    print("Edad inválida")
    age = int(input("Ingrese su edad nuevamente: "))

city = input("Ingrese su ciudad: ")
occupation = input("Ingrese su ocupación actual: ")

occupation_ins = Occupation(name, gender, age, city, occupation)

print("Nombre:", occupation_ins.get_name())
print("Género:", "Masculino" if occupation_ins.gender == "m" else "Femenino" if occupation_ins.gender == "f" else "otro")
print("Edad:", occupation_ins.age)
print("Ciudad:", occupation_ins.city)
print("Ocupación:", occupation_ins.occupation)
