class Cuenta:
    def __init__(self, prot, saldo, moneda):
        self.__propietario = prot
        self.__saldo = saldo
        self.__moneda = moneda
    #Getters (metodo Get)
    def get_propietario(self):
        return self.__propietario
    def get_saldo(self):
        return self.__saldo    
    def get_timoneda(self):
        return self.__moneda
    #Setters (metodo Set)
    def set_saldo(self,saldo):
        self.__saldo = saldo
    def set_moneda(self,moneda):
        self.__moneda= moneda
cuenta1 = Cuenta ("Johan Rincon", 20000,"Peso Colombiano")
print(cuenta1.get_propietario() , cuenta1.get_saldo(),cuenta1.get_timoneda())
cuenta1.set_saldo("50000")
cuenta1.set_moneda("Dolares")
#ejemplo imprimir una sola linea
print(cuenta1.get_propietario())
print(cuenta1.get_saldo())
print("su nuevo saldo es : ", cuenta1.get_saldo() , cuenta1.get_timoneda())
