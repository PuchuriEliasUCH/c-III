# primera super clase: Persona
class Persona:
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")

# segunda super clas: Trabajador
class Trabajador:
    def __init__(self, empresa, sueldo):
        self.empresa = empresa
        self.sueldo = sueldo

    def trabajar(self):
        print(f"\x1b[1;31mSoy empleado de la empresa {self.empresa} y mi sueldo basico es S/{self.sueldo}")

# subclase: Estudiante
class Estudiante(Persona, Trabajador):
    def __init__(self, nombre, edad, empresa, sueldo, escuela):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, empresa, sueldo)
        self.escuela = escuela

    def pension(self):
        if self.escuela == "Sistemas":
            return 750
        elif self.escuela == "Electrónica":
            return 700
        elif self.escuela == "Industrial":
            return 650
        elif self.escuela == "Ambiental":
            return 720
        else:
            return 0

    def imprimir(self):
        print(f"\x1b[1;36mMi escuela es {self.escuela} de la UCH y pago S/{self.pension()}")

# crear objeto de subclase
obj = Estudiante("Luisa", 25, "ALICORP SA", 1800, "Sistemas")
obj.presentarse()
obj.trabajar()
obj.imprimir()