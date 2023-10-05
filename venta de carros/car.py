class Car:
    def __init__(self,
                 marca: str,
                 linea: str,
                 modelo: int,
                 precio: float):
        self.marca = marca
        self.linea = linea
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.linea}'
