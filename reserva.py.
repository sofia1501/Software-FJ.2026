
# reserva.py

from excepciones import (
    ErrorReserva,
    ErrorOperacion,
    ErrorServicioNoDisponible
)

from logs import registrar_evento, registrar_error


# Clase encargada de gestionar las reservas
class Reserva:

    def __init__(self, cliente, servicio, duracion):

        try:
            # Validar los datos recibidos
            if cliente is None:
                raise ErrorReserva("Debe seleccionar un cliente.")

            if servicio is None:
                raise ErrorReserva("Debe seleccionar un servicio.")

            if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
                raise ErrorReserva("La duracion debe ser numerica.")

            if duracion <= 0:
                raise ErrorReserva("La duracion debe ser mayor que cero.")

            # Guardar los datos de forma privada
            self.__cliente = cliente
            self.__servicio = servicio
            self.__duracion = duracion
            self.__estado = "Pendiente"
            self.__costo = 0

            registrar_evento("Reserva creada correctamente.")

        except ErrorReserva as error:
            registrar_error(str(error))
            raise

    # Consultar el estado
    def obtener_estado(self):
        return self.__estado

    # Consultar la duracion
    def obtener_duracion(self):
        return self.__duracion

    # Calcular el costo con descuento e impuesto
    def calcular_costo(self, descuento=0, impuesto=0):

        try:
            if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
                raise ErrorReserva("Descuento invalido.")

            if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
                raise ErrorReserva("Impuesto invalido.")

            if not 0 <= descuento <= 100:
                raise ErrorReserva("El descuento debe estar entre 0 y 100.")

            if not 0 <= impuesto <= 100:
                raise ErrorReserva("El impuesto debe estar entre 0 y 100.")

            # Obtener el costo del servicio
            costo_base = self.__servicio.calcular_costo(self.__duracion)

            if isinstance(costo_base, bool) or not isinstance(costo_base, (int, float)) or costo_base < 0:
                raise ErrorReserva("El costo del servicio no es valido.")

            subtotal = costo_base - (costo_base * descuento / 100)
            self.__costo = subtotal + (subtotal * impuesto / 100)

            registrar_evento("Costo calculado correctamente.")

            return self.__costo

        except ErrorReserva as error:
            registrar_error(str(error))
            raise

        except Exception as error:
            registrar_error("Error al calcular el costo: " + str(error))
            raise ErrorReserva("No fue posible calcular el costo.") from error

    # Confirmar una reserva
    def confirmar(self):

        try:
            if self.__estado != "Pendiente":
                raise ErrorOperacion("La reserva no esta pendiente.")

            if hasattr(self.__servicio, "validar_disponibilidad"):
                disponible = self.__servicio.validar_disponibilidad(
                    self.__duracion
                )

                if not disponible:
                    raise ErrorServicioNoDisponible(
                        "El servicio no esta disponible."
                    )

            self.__estado = "Confirmada"

            registrar_evento("Reserva confirmada correctamente.")

            return True

        except (ErrorOperacion, ErrorServicioNoDisponible) as error:
            registrar_error(str(error))
            raise

        except Exception as error:
            registrar_error(str(error))
            raise ErrorReserva("Error al confirmar la reserva.") from error

    # Cancelar una reserva
    def cancelar(self):

        try:
            if self.__estado not in ("Pendiente", "Confirmada"):
                raise ErrorOperacion("No se puede cancelar esta reserva.")

            self.__estado = "Cancelada"

            registrar_evento("Reserva cancelada correctamente.")

            return True

        except ErrorOperacion as error:
            registrar_error(str(error))
            raise

        finally:
            print("Proceso de cancelacion finalizado.")

    # Mostrar los datos de la reserva
    def mostrar_informacion(self):

        print("\n--- INFORMACION DE LA RESERVA ---")
        print("Cliente:", self.__cliente)
        print("Servicio:", self.__servicio)
        print("Duracion:", self.__duracion)
        print("Estado:", self.__estado)
        print("Costo:", self.__costo)
        print("--------------------------------")
