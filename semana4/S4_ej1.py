class Persona(): 
    # atributos
    nombre = ""
    apellido = ""
    edad = 0

    # constructor
    def __init__(self):
        self.nombre = "Maruja"
        self.apellido = "Rios"
        self.edad = 21

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}"
    
obj = Persona()

print(obj)