from car import Car


class Pickup(Car):
    def __init__(self,
                 marca: str,
                 linea: str,
                 modelo: int,
                 precio: float,
                 mileage: int):
        super().__init__(marca, linea, modelo, precio)
        self.mileage = mileage

    def __str__(self):
        res = super().__str__()
        res += f' - {self.mileage}'

        return res

