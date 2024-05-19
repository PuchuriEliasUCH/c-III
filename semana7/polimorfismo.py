# superclase
class Animal:
    def hablar(self):
        pass

# subclases
class Perro(Animal):
    def hablar(self):
        print("El perro dice Guau guau!")

class Gato(Animal):
    def hablar(self):
        print("El perro dice miau miau!")

class Vaca(Animal):
    def hablar(self):
        print("La vaca dice muuu!")

# Crear Objetos
p = Perro()
p.hablar()

g = Gato()  
g.hablar()

v = Vaca()
v.hablar()