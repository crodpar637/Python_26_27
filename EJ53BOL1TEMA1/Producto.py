
class Producto:
    def __init__(self, idProducto: str, nombre: str):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__piezas = []

    @property
    def idProducto(self):
        return self.__idProducto

    @property
    def nombre(self):
        return self.__nombre

    def agregarPieza(self, oPieza):
        if oPieza in self.__piezas:
            return "Pieza repetida"
        else:
            self.__piezas.append(oPieza)
            return "Alta OK"

    def precioProducto(self):
        total = 0

        for i in self.__piezas:
            total = total + i.precio

        return total

    def pesoProducto(self):
        total = 0

        for i in self.__piezas:
            total = total + i.peso

        return total

    def listadoPiezas(self):
        listado = f"Producto: {self.nombre}\n"

        for pieza in self.__piezas:
            listado += str(pieza) + "\n"

        return listado
