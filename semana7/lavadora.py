
from .abstracciones import Dispositivo
class Lavadora(Dispositivo):
    def encender(self):
        print("La lavadora se está encendiendo")

    def apagar(self):
        print("La lavadora se está apagando")