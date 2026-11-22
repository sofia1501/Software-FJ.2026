from abc import ABC, abstractmethod

# Clase abstracta que representa una entidad general
class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass
      
