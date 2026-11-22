from entidad import Entidad

# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, nombre, documento, correo):

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        # Validar documento
        if not isinstance(documento, str) or not documento.strip():
            raise ValueError("El documento no puede estar vacío.")

        # Validar correo
        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ValueError("El correo electrónico no es válido.")

        # Encapsulación de datos
        self.__nombre = nombre.strip()
        self.__documento = documento.strip()
        self.__correo = correo.strip()

    # Mostrar información del cliente
    def mostrar_info(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo}"
        )

    # Consultar nombre
    @property
    def nombre(self):
        return self.__nombre

    # Consultar documento
    @property
    def documento(self):
        return self.__documento

    # Consultar correo
    @property
    def correo(self):
        return self.__correo
