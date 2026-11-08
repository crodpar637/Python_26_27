class Piece:
    """Base class for all pieces."""

    def __init__(self, id_piece, weight, price, manufacturer_url):
        # TODO: assign through the properties (self.weight = weight)
        # so the setter validation also runs in the constructor
        self.id_piece = id_piece # it's calling the setter (validation)
        self.weight = weight
        self.price = price
        self.manufacturer_url = manufacturer_url

    # --- id_piece (pattern to copy for the other attributes) ---
    @property
    def id_piece(self):
        return self.__id_piece

    @id_piece.setter
    def id_piece(self, value):
        # .strip() to avoid empty Strings (not same as None)
        if value is None or not str(value).strip():
            raise ValueError("id_piece cannot be empty")
        self.__id_piece = value

    # --- weight ---
    # TODO: @property + setter (integer, validate >= 0)
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value is None:
            raise ValueError("weight cannot be None")
        elif value < 0:
            raise ValueError("weight cannot be negative")
        self.__weight = value

    # --- price ---
    # TODO: @property + setter (float, validate >= 0)
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value is None:
            raise ValueError("price cannot be None")
        elif value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value
        
    # --- manufacturer_url ---
    # TODO: @property + setter (string)
    @property
    def manufacturer_url(self):
        return self.__manufacturer_url

    @manufacturer_url.setter
    def manufacturer_url(self, value):
        # if value is None:
        #     raise ValueError("manufacturer_url cannot be null")
        self.__manufacturer_url = value

    def __str__(self):
        return (f"Piece id: {self.id_piece}; weight: {self.weight}; "
                f"price: {self.price}; manufacturer_url: {self.manufacturer_url}")