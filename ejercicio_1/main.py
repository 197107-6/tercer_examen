class Estacionamiento(object):
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        if self.horas > 0:
            if self.horas <= 2:
                tarifa = 15.00
            elif self.horas <= 5:
                tarifa = 12.00
            else:
                tarifa = 10.00
            return round(tarifa * self.horas, 2)
        else:
            return 0

    def mostrarRecibo(self):
        total = self.calcularPago()
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${total}")

if __name__ == "__main__":
    horas = int(input("Ingrese el número de horas: "))
    if horas > 0:
        estacionamiento = Estacionamiento(horas)
        estacionamiento.mostrarRecibo()
    else:
        print("Por favor, ingrese un número entero mayor que cero.")

