# Clase padre (super clase)
class Persona:
    # constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # método de usuario
    def imprimir(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}")

    def mensaje_padre(self):
        print("Soy una super clase")

"""
per = Persona("Juana", "Perez", 25)
per.imprimir()
per.mensaje_padre()
"""


# Clase Hija (subclase)
class Alumno(Persona):
    # constructor
    def __init__(self, nombre, apellido, edad, nota1, nota2):
        super().__init__(nombre, apellido, edad)
        self.nota1 = nota1
        self.nota2 = nota2

    def mensaje_hija(self):
        print("soy una subclase")
    
    def promedio(self):
        return (self.nota1 + self.nota2)/2
    
    def __str__(self):
        return f"\nNota 1: {self.nota1}\nNota 2: {self.nota2}\nPromedio: {self.promedio()}"

a = Alumno("Luis", "Castro", 21, 18, 14)
a.imprimir()
print(a)

# Subclase hija 2
class Profesor(Persona): 
    # constructor heredado + nuevos atributos
    def __init__(self, nombre, apellido, edad, horas, tarifa):
        super().__init__(nombre, apellido, edad)
        self.horas = horas
        self.tarifa = tarifa

    # métodos de usuario
    def salario_bruto(self):
        return self.horas * self.tarifa
    
    def bono(self):
        return self.salario_bruto * 0.12
    
    def salario_neto(self):
        return self.salario_bruto() + self.bono()
    
    def reporte_pago(self):
        print(f"Horas trabajadas: {self.horas}\nTarifa x hora: {self.tarifa}\nSalario bruto: {self.salario_bruto}\nBonificación: {self.bono}\nSalario neto: {self.salario_neto}")

p = Profesor()