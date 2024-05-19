# super clase
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def reporte(self):
        return f"Soy {self.nombre} y mi apellido es {self.apellido}"
    
# subclase
class Estudiante(Persona):
    def __init__(self, nombre, apellido, codigo):
        super().__init__(nombre, apellido)
        self.codigo = codigo

    def reporte(self):
        return f"Soy {self.nombre}, mi apellido es {self.apellido} y mi codigo es {self.codigo}"
    

class Trabajador(Persona):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.salario = salario

    def reporte(self):
        return f"Soy {self.nombre}, mi apellido es {self.apellido} y mi salario es {self.salario}"
    

class Administrador(Persona):
    def __init__(self, nombre, apellido, area):
        super().__init__(nombre, apellido)
        self.area = area

    def reporte(self):
        return f"Soy {self.nombre}, mi apellido es {self.apellido} y soy responsable del área {self.area}"
    
# Crear objeto
e = Estudiante("Miguel", "Palacios", "u20234567")

print(e.reporte())

t = Trabajador("Dante", "Grande", 2300)
a = Administrador("Enid", "Huaman", "marketing")
print(t.reporte())
print(a.reporte())