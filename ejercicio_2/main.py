

class Operacion(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"Resultado de la suma: {resultado}")

class Resta(Operacion):
    def calcular(self):
        return self.numero1 - self.numero2

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"Resultado de la resta: {resultado}")

if __name__ == "__main__":
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))

    suma = Operacion(num1, num2)
    resta = Resta(num1, num2)

    suma.mostrarResultado()
    resta.mostrarResultado()

