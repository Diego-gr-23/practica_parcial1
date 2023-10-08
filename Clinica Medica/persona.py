import datetime


class Persona:

    def __init__(self,
                 nombre: str,
                 apellido: str,
                 dpi: int,
                 birthday: datetime.date,
                 telefono: str,
                 email: str):
        self.nombre = nombre
        self.apellido = apellido
        self.dpi = dpi
        self.birthday = birthday
        self.telefono = telefono
        self.email = email
