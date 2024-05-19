# IN constructor es un metodo especial denomida __init__()
# compuesto por dos carcteres de subrayado '_'
# Este metodo se ejecuta automaticamente al instanciar una clase y, por lo general,
# se emeplea para inicializar los atributos.

# Constructor con Parametros
class Persona():
  nombres = ""
  edad = 0

  # Constructor
  def __init__(self): 
    self.nombres = "Carlos"
    self.edad = 20

  def imprimir(self): 
    print(f"Nombre: {self.nombres}; Edad: {self.edad}")

obj = Persona()
obj.imprimir()