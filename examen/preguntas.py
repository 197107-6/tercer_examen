#1. ¿Cuál es el nombre de la clase? 
#Producto

#2. ¿Cuáles son sus propiedades? 
#nombre, precio, total
    
#3. ¿Cuáles son sus métodos? 
#calcularTotal, mostrarTotal

#4. ¿Qué función cumple __init__? 
#Inicializa las propiedades del objeto.

#5. ¿Para qué se utiliza self? 
#Se utiliza para referirse a las propiedades y métodos del objeto actual.

#6. ¿En qué instrucción se crea un objeto? 
#producto1 = Producto("Cuaderno", 35)

#7. ¿Cuál es el nombre del objeto? 
#producto1

#8. ¿Cómo se llama a calcularTotal()? 
#producto1.calcularTotal()

#9. ¿Qué valores recibe el constructor cuando se crea el objeto? 
#"Cuaderno", 35

#10. ¿Qué resultado mostrará el programa? 
#Producto: Cuaderno y Total: $105.00

# Actividad 2. Completar código


class Rectangulo(object): 
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def mostrarArea(self):
        print(f"El área del rectángulo es: {self.calcularArea()}")

        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def mostrarArea(self):
        print(f"El área del rectángulo es: {self.calcularArea()}")


rectangulo1 = Rectangulo(8, 5)

rectangulo1.mostrarArea()

# Actividad 3. Interpretar herencia 

#1. ¿Cuál es la clase padre? 
#Operacion

#2. ¿Cuál es la clase hija? 
#Multiplicacion

#3. ¿Cómo se indica la herencia? 
#Se indica colocando el nombre de la clase padre entre paréntesis en la definición de la clase hija.

#4. ¿Qué propiedades utiliza la clase hija? 
#numero1, numero2

#5. ¿Por qué puede utilizarlas sin definir su propio __init__? 
#Porque hereda el __init__ de la clase padre.

#6. ¿Por qué los métodos calcular() tienen resultados distintos? 
#Porque la clase hija sobrescribe el método calcular() para proporcionar una implementación diferente.

#7. ¿Qué valores se imprimen? 
#12
#32

#8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion? 
#Se utilizaría el método calcular() de la clase padre, Operacion.