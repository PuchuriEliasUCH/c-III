class Cliente: 
    # Atributo público
    nombre = "Fer"

    # Atributo privado
    __apellido = "Rojas"

    # método público 
    def imprimir(self):
        print("soy un cliente")  


oCliente1 = Cliente()

print(oCliente1._Cliente__apellido)