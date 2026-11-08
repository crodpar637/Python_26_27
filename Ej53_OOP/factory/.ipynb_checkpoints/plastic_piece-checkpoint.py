from . import Piece # . is enough

class PlasticPiece(Piece):
    """A piece made of metal."""

    def __init__(self, id_piece, weight, price, manufacturer_url, resistance):
        super().__init__(id_piece, weight, price, manufacturer_url)
        self.resistance = resistance

    @property
    def resistance(self):
        return self.__resistance

    @resistance.setter
    def resistance(self, value):
        if value is None:
            raise ValueError("resistance cannot be None")
        if not isinstance(value, int):
            raise TypeError("resistance must be an integer")
        if value < 0:
            raise ValueError("resistance cannot be negative")
        self.__resistance = value

    def __str__(self):
        return f"{super().__str__()}; resistance: {self.resistance}"
            