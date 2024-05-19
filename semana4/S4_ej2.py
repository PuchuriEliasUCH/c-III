class Alumno:
    # atributos
    codigo = 0
    nombre = ""
    nota1 = ""
    nota2 = ""
    nota3 = ""

    # constructor (parámetros)
    def __init__(self, codigo, nombre, n1, n2, n3):
        self.codigo = codigo
        self.nombre = nombre
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3

    # métodos de usuario
    def promedio(self):
        return self.nota1 * 0.3 + self.nota2 * 0.3 + self.nota3 * 0.4
    
    def condicion(self):
        return "Aprovado" if self.promedio() >= 10.5 else "Desaprovado"
    
    def imprimir(self):
        print("Mi código es: {}\nMi nombre es: {}\nMis notas son: {}, {}, {}\nMi promedio es: {} y estoy {}".format(self.codigo, self.nombre, self.nota1, self.nota2, self.nota3, self.promedio(), self.condicion()))

obj = Alumno(112, "Daniel", 11, 5, 20)
obj2 = Alumno(113, "Nanda", 20, 19, 20)
obj.imprimir()
obj2.imprimir()