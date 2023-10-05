from car import Car


class Suv(Car):
    def __init__(self,
                 marca: str,
                 linea: str,
                 modelo: int,
                 precio: float,
                 is_crashed: bool):
        super().__init__(marca, linea, modelo, precio)
        self.is_crashed = is_crashed

    def __str__(self):
        res = super().__str__()
        if self.is_crashed:
            res += ' - Chocada'
        else:
            res += ' - No chocada'

        return res

