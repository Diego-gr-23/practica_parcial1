import datetime

from doctor import Doctor
from paciente import Paciente

pacientes: list[Paciente] = []
doctores: list[Doctor] = []


def add_doctor():
    print('Ingrese un doctor \n')
    nombre = input('Ingrese el nombre: \n')
    apellido = input('ingrese el apellido: \n')
    dpi = int(input('Ingrese el DPI: \n'))
    day = int(input('Ingrese el dia de nacimiento: \n'))
    month = int(input('Ingrese el mes de nacimiento: \n'))
    year = int(input('Ingrese el anio de nacimiento: \n'))
    birthdate = datetime.date(year, month, day)
    phone = input('Ingrese el telefono: \n')
    email = input('Ingrese el correo electronico: \n')
    specialty = input('Ingrese la especialidad: \n')
    college_id = int(input('Ingrese el colegiado: \n'))
    sallary = float(input('Ingrese el salario: \n'))

    doctor = Doctor(
        nombre,
        apellido,
        dpi,
        birthdate,
        phone,
        email,
        specialty,
        college_id,
        sallary
    )

    doctores.append(doctor)


def add_paciente():
    print('Ingrese un paciente \n')
    nombre = input('Ingrese el nombre: \n')
    apellido = input('ingrese el apellido: \n')
    dpi = int(input('Ingrese el DPI: \n'))
    day = int(input('Ingrese el dia de nacimiento: \n'))
    month = int(input('Ingrese el mes de nacimiento: \n'))
    year = int(input('Ingrese el anio de nacimiento: \n'))
    birthdate = datetime.date(year, month, day)
    phone = input('Ingrese el telefono: \n')
    email = input('Ingrese el correo electronico: \n')
    peso = float(input('Ingrese el peso: \n'))
    altura = float(input('Ingrese la altura: \n'))
    gender = input('Ingrese el genero: \n')
    trigliceridos = int(input('Ingrese los trigliceridos: \n'))
    presion_sistolica = int(input('ingrese los trigliceridos: \n'))
    presion_diastolica = int(input('Ingrese presion diastolica: \n'))

    paciente = Paciente(
        nombre,
        apellido,
        dpi,
        birthdate,
        phone,
        email,
        peso,
        altura,
        gender,
        trigliceridos,
        presion_sistolica,
        presion_diastolica
    )
    pacientes.append(paciente)


def show_health(paciente: Paciente):
    print('Datos del paciente')
    print(paciente.nombre, paciente.apellido)
    print(paciente.get_imc())
    print(paciente.get_presion())
    print(paciente.get_trigliceridos())


def main():
    while True:
        print('Menu')
        print('1) Ingrese los medicos \n')
        print('2) Ingrese los pacientes \n')
        print('3) Ver estado del paciente \n')
        print('4) Ver pacientes de unn medico \n')
        print('5) Salir \n')
        option = int(input('Ingrese una opcion: \n'))

        if option == 1:
            add_doctor()
        elif option == 2:
            add_paciente()
        elif option == 3:
            dpi = int(input('Ingrese el DPI: \n'))
            for paciente in pacientes:
                if paciente.dpi == dpi:
                    show_health(paciente)
                    break
        elif option == 4:
            dpi = int(input('Ingrese el DPI: \n'))
            for doctor in doctores:
                if doctor.dpi == dpi:
                    for paciente in doctor.pacientes:
                        print(paciente)
        elif option == 5:
            break
        else:
            continue

main()
