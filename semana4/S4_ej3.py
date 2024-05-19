class Empleado():
    # constructor (Parámetros)
    def __init__(self, codigo, nombre, tarifa, horas):
        self.codigo = codigo
        self.nombre = nombre
        self.tarifa = tarifa
        self.horas = horas

    # Métodos de usuario
    def salario_bruto(self):
        return self.tarifa * self.horas
    
    def bono(self):
        return 0.12 * self.salario_bruto() if self.salario_bruto() > 1000 else 0.10 * self.salario_bruto()
    
    def salario_neto(self):
        return self.salario_bruto() + self.bono()
    
    def imprimir(self): 
        print(f"Código: {self.codigo}\nEmpleado(a): {self.nombre}\nHoras trabajadas: {self.horas}\nSalario Bruto: S/{self.salario_bruto()}\nBonificación: S/{self.bono()}\nSalario Neto: S/{self.salario_neto()}")

oEmpleado = Empleado(1001, "Ruth", 25, 40)
oEmpleado.imprimir()