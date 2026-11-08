from .piece import Piece


class Product:
    """A product composed of one or more pieces."""

    def __init__(self, id_product, name):
        self.id_product = id_product # it's calling the setter (validation)
        self.name = name
        self.__pieces = [] # no need for validation

    # gettter
    @property
    def id_product(self):
        return self.__id_product

    # setter
    @id_product.setter
    def id_product(self, value):
        if value is None or not str(value).strip():
            raise ValueError("id_product cannot be empty")
        self.__id_product = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # .strip() to avoid an empty String
        if value is None or not str(value).strip():
            raise ValueError("name cannot be empty")
        self.__name = value

    @property
    def pieces(self):
        return list(self.__pieces)

    def add_piece(self, piece) -> str:
        # optional
        if not isinstance(piece, Piece):
            raise TypeError(f"{piece} is not a Piece object")
        # required in the statement
        for piece_el in self.__pieces:
            if piece_el.id_piece == piece.id_piece:
                return "Repeated piece"
        self.__pieces.append(piece)
        return "Piece added successfully"

    def product_price(self) -> float:
        return sum(p.price for p in self.__pieces)

    def product_weight(self) -> int:
        return sum(p.weight for p in self.__pieces)

    def piece_listing(self) -> str:
        return "\n".join(str(p) for p in self.__pieces)