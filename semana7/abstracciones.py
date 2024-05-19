# importar módulo ABC
from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class Televisor(Dispositivo):
    def encender(self):
        print("El televisor se está encendiendo")

    def apagar(self):
        print("El televisor se está apagando")

