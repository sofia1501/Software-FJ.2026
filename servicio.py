

from abc import ABC, abstractmenthod

class Servicio(ABC):
    @abstractmenthod
    def calcular_costo(self):
        """Método abstracto para calcular el costo del servicio."""
        pass

@abstractmenthod
def validar_parametros(self):
    """Metodo abstracto para validar los parametros del servicio."""
    pass

#Reserva de salas
    class ReservaSala(Servicio):
        def __init__(self,horas):
         self.horas = horas
         slef.validar_parametros()

        #Costo por hora
        def calcular_costo(self):
            return self.horas * 100

def validar_parametros(self):
    if self.horas <= 0:
      raise ValueError("Las horas deben ser mayores a cero.")

      #Alquiler de equipos
      class AlquilerEquipos(Servicio):
        def __init__(self, dias):
            self.dias = dias
            self.validar_parametros()

            #costo por dia
        def calcular_costo(self):
            return self.dias * 50

        def validar_parametros(self):
            if self.dias <=0:
                raise ValueError("Los dias deben ser mayores a cero.")

# Asesorias especializadas.
class Asesoria(Servicio):
    def __init__(self, horas):
      self.horas = horas
      slef.validar_parametros()

# Costo por hora de asesoria
def calcular_costo(self):
    return self.horas * 150

def validar_parametros(self):
    if self.horas <= 0:
       raise ValueError("Las horas deben ser mayores a cero.")
