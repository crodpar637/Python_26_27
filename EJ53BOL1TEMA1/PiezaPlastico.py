
from Pieza import Pieza


class PiezaPlastico(Pieza):
    def __init__(self, idPieza: str, peso: int, precio: float,
                 urlFabricante: str, resistencia: int):
        super().__init__(idPieza, peso, precio, urlFabricante)
        self.__resistencia = resistencia

    @property
    def resistencia(self):
        return self.__resistencia

    def __str__(self):
        return super().__str__() + f", Resistencia: {self.resistencia}"
