import datetime

from persona import Persona
from paciente import Paciente


class Doctor(Persona):
    def __init__(self,
                 nombre: str,
                 apellido: str,
                 dpi: int,
                 birthday: datetime.date,
                 telefono: str,
                 email: str,
                 especialidad: str,
                 no_colegiado: int,
                 salario: float):
        super().__init__(nombre, apellido, dpi, birthday, telefono, email)
        self.especialidad = especialidad
        self.no_colegiado = no_colegiado
        self.salario = salario
        self.paciente: list[Paciente] = []

    def add_paciente(self, paciente: Paciente):
        self.paciente.append(paciente)
