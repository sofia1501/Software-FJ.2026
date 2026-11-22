# excepciones.py

# Clase principal para los errores del sistema
class ErrorSistema(Exception):
    pass


# Error cuando los datos de una reserva son incorrectos
class ErrorReserva(ErrorSistema):
    pass


# Error cuando se intenta realizar una operación no permitida
class ErrorOperacion(ErrorSistema):
    pass


# Error cuando el servicio no está disponible
class ErrorServicioNoDisponible(ErrorSistema):
    pass
