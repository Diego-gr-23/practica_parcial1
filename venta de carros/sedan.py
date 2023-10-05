from car import Car


class Sedan(Car):
    def __init__(self,
                 marca: str,
                 linea: str,
                 modelo: int,
                 precio: float,
                 owner: str):
        super().__init__(marca, linea, modelo, precio)
        self.owner = owner

    def __str__(self):
        res = super().__str__()
        res += f' - {self.owner}'

        return res

