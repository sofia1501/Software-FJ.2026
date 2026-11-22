
# main.py

from reserva import Reserva
from excepciones import ErrorReserva, ErrorOperacion


# Clase de prueba para simular un cliente
class ClientePrueba:

    def __str__(self):
        return "Cliente de prueba"


# Clase de prueba para simular un servicio
class ServicioPrueba:

    def calcular_costo(self, duracion):
        return 50000 * duracion

    def validar_disponibilidad(self, duracion):
        return True


# Servicio que no tiene disponibilidad
class ServicioNoDisponible:

    def calcular_costo(self, duracion):
        return 30000 * duracion

    def validar_disponibilidad(self, duracion):
        return False


# Crear objetos de prueba
cliente = ClientePrueba()
servicio = ServicioPrueba()

print("SISTEMA DE RESERVAS - SOFTWARE FJ")


# PRUEBA 1: Crear una reserva correctamente
print("\nPRUEBA 1: Crear reserva")

try:
    reserva = Reserva(cliente, servicio, 2)
    print("Reserva creada correctamente.")

except ErrorReserva as error:
    print("Error:", error)


# PRUEBA 2: Calcular el costo
print("\nPRUEBA 2: Calcular costo")

try:
    costo = reserva.calcular_costo(10, 19)
    print("Costo total:", costo)

except ErrorReserva as error:
    print("Error:", error)


# PRUEBA 3: Confirmar reserva
print("\nPRUEBA 3: Confirmar reserva")

try:
    reserva.confirmar()

except Exception as error:
    print("Error:", error)

else:
    print("Reserva confirmada correctamente.")


# PRUEBA 4: Consultar estado
print("\nPRUEBA 4: Consultar estado")

print("Estado:", reserva.obtener_estado())


# PRUEBA 5: Mostrar informacion
print("\nPRUEBA 5: Mostrar reserva")

reserva.mostrar_informacion()


# PRUEBA 6: Intentar crear una reserva sin cliente
print("\nPRUEBA 6: Cliente invalido")

try:
    reserva_invalida = Reserva(None, servicio, 2)

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 7: Intentar crear una reserva con duracion negativa
print("\nPRUEBA 7: Duracion incorrecta")

try:
    reserva_invalida = Reserva(cliente, servicio, -2)

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 8: Calcular costo con descuento incorrecto
print("\nPRUEBA 8: Descuento incorrecto")

try:
    reserva.calcular_costo(150, 19)

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 9: Servicio no disponible
print("\nPRUEBA 9: Servicio no disponible")

try:
    reserva_sin_servicio = Reserva(
        cliente,
        ServicioNoDisponible(),
        2
    )

    reserva_sin_servicio.confirmar()

except Exception as error:
    print("Error controlado:", error)


# PRUEBA 10: Cancelar reserva
print("\nPRUEBA 10: Cancelar reserva")

try:
    reserva.cancelar()
    print("Reserva cancelada correctamente.")

except ErrorOperacion as error:
    print("Error:", error)


print("\nTodas las pruebas finalizaron.")
print("El sistema continua funcionando.")
