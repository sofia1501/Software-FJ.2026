

from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, disponible = True):
        self._disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion):
        """Método abstracto para calcular el costo del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        """Método abstracto para validar los parametros del servicio."""
        pass

    @abstractmethod
    def describir(self):
        """Metodo que devuelve la descripción del servicio."""
        pass

    def validar_disponibilidad(self, duracion):
        """Metodo que comprueba si el servicio está disponible."""
        self.validar_parametros(duracion)
        return self._disponible

    def __str__(self):
        return self.describir()

#Reserva de salas
class ReservaSala(Servicio):
    def __init__(self, disponible = True):
        super().__init__(disponible)

    #Validación de parámetros
    def validar_parametros(self, duracion):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser numérica.")

        if duracion <= 0:
            raise ValueError("Las horas de reserva deben ser mayores a cero.")
    
    #Costo por hora
    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        #Tarifa de 100 por hora de reserva
        return duracion * 100

    #Descripción del servicio
    def describir(self):
        return "Reserva de salas por horas"


#Alquiler de equipos
class AlquilerEquipos(Servicio):

    def __init__(self, disponible = True):
        super().__init__(disponible)

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser numérica.")

        if duracion <= 0:
            raise ValueError("Los días de alquiler deben ser mayores a cero.")

    #costo por dia
    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)

        # Tarifa por día de alquiler
        return duracion * 50

    def describir(self):
        return "Alquiler de equipos por días"

# Asesorias especializadas.
class Asesoria(Servicio):
    def __init__(self, disponible = True):
        super().__init__(disponible)

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser numérica.")

        if duracion <= 0:
            raise ValueError("Las horas de asesoría deben ser mayores a cero.")
    # Costo por hora de asesoria
    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        # Tarifa por hora de asesoría
        return duracion * 150

    def describir(self):
        return "Asesorías especializadas por horas"