class Empleado:
    def __init__(self,nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, valor):
        self.__salario_base = valor

    def calcular_salario(self,irpf):
        return self.salario_base * (100 - irpf)/100

    def __str__(self):
        return f"Nombre: {self.nombre} Salario base: {self.salario_base}"
        
class Vendedor(Empleado):
    def __init__(self, nombre, salario, lista_ventas):
        super().__init__(nombre, salario)
        self.__ventas_realizadas = lista_ventas #[100, 500, 1500]

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas[:]

    def calcular_salario(self):
        return self.salario_base + 0.1 * sum(self.ventas_realizadas)

    def agregar_venta(self, importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return super().__str__() + "- Ventas: " + str(self.ventas_realizadas) + " - Salario Total: " + str(self.calcular_salario())


# MAIN
e1 = Empleado("Pepe", "1200")
e2 = Empleado("María", "1250")

v1 = Vendedor("Juan", 1300, [50, 160, 180])
v2 = Vendedor("Antonio", 1100, [150, 60, 80])
print(e1)
print(e2)
print(v1)
print(v2)

e1.salario_base = 2000  # utiliza el setter 
v1.nombre = "Juanillo" # utiliza el setter 

v1.agregar_venta(100)
v1.agregar_venta(500)

print(e1)
print(e2)
print(v1)
print(v2)

    








        
        