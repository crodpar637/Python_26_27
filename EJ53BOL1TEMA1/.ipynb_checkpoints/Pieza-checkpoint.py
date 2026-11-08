
class Pieza:
    def __init__(self, idPieza: str, peso: int, precio: float, urlFabricante: str):
        self.__idPieza = idPieza
        self.__peso = peso
        self.__precio = precio
        self.__urlFabricante = urlFabricante

    @property
    def idPieza(self):
        return self.__idPieza

    @property
    def peso(self):
        return self.__peso

    @property
    def precio(self):
        return self.__precio

    @property
    def urlFabricante(self):
        return self.__urlFabricante

    def __str__(self):
        return (f"ID: {self.idPieza}, "
                f"Peso: {self.peso} g, "
                f"Precio: {self.precio} euros, "
                f"Fabricante: {self.urlFabricante}")
