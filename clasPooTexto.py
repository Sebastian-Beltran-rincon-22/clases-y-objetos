class Texto:
    def __init__(self, xtexto):
        self.xtexto = xtexto

    def invertir(self):
        return self.xtexto[::-1]

    def contarPalabras(self):
        print("la cantidad de palabras son: ")
        return len(self.xtexto.split())

    def convertirMayusculas(self):
        return self.xtexto.upper()
texto_ejemplo = Texto("El problema del hombre no esta en la bomba atomica. sino en su corazon.")
print(texto_ejemplo.xtexto)
print(texto_ejemplo.invertir())
print(texto_ejemplo.contarPalabras())
print(texto_ejemplo.convertirMayusculas())
