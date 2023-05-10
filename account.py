class User:
    def __init__(self,name, age,civil_estatus):
        self.name = name
        self.age = age
        self.civil_estatus = civil_estatus
    def cash_mont(self, cash):
        self.cash = cash
class Mont_cash(User):
    def __init__(self, name, age, civil_estatus):
        super().__init__(name, age, civil_estatus)
    def cash_mont(self, cash):
        return super().cash_mont(cash)
print("datos recopilados ")
name = input("ingrese su nombre de usuario:  ")
while not name:
    print("Error casilla vacia")
    name = input("ingrese nuevamente los datos:  ")
age = int(input("ingrese su edad:  "))
while True:
    if age >= 18 and age <=70:
        print("edad registrada")
        break
    elif age <= 17 or age >=99:
        print("la edad no cumple los requisitos")
        age = int(input("ingrese una edad entre 18 y 70:  "))
    else:
        print("edad invalida")
        age = int(input("ingrese nuevamente la edad:  "))
civil_estatus = input("ingrese su estado civil(soltero, casado, divorciado, union libre): ")
while civil_estatus not in ["soltero","casado","divorciado","union libre"]:
    print("Error")
    civil_estatus = input("ingrese nuevamente su estado civil: ")
cash = int (input("ingrese la cantidad de dinero en su cuenta: "))
while not (1000 <= cash ):
    print("monto invalido")
    cash = input("ingresar nuevamente el monto:  ")
user1 = Mont_cash(name , age , civil_estatus)
print("nombre: ", user1.name)
print("edad: ", user1.age)
print("estado civil: ", user1.civil_estatus)
user1.cash_mont = print("nuevo valor en cuenta: ", "5000")

