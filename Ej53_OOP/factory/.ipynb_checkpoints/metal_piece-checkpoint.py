from . import Piece


class MetalPiece(Piece):
    """A piece made of metal."""

    def __init__(self, id_piece, weight, price, manufacturer_url, metal):
        super().__init__(id_piece, weight, price, manufacturer_url)
        self.metal = metal                      # goes through the setter

    @property
    def metal(self):
        return self.__metal

    @metal.setter
    def metal(self, value):
        if value is None or not isinstance(value, str) or not value.strip():
            raise ValueError("metal must be a non-empty string")
        self.__metal = value

    def __str__(self):
        return f"{super().__str__()}; metal: {self.metal}"