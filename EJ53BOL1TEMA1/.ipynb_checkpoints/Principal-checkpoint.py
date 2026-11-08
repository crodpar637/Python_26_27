
from PiezaMetalica import PiezaMetalica
from PiezaPlastico import PiezaPlastico
from Producto import Producto


def main():
    p1 = PiezaMetalica("P001", 500, 12.5, "www.metal.com", "Acero")
    p2 = PiezaMetalica("P002", 300, 8.0, "www.metal.com", "Hierro")

    p3 = PiezaPlastico("P003", 100, 2.5, "www.plastico.com", 80)
    p4 = PiezaPlastico("P004", 200, 4.0, "www.plastico.com", 100)

    producto = Producto("PROD01", "Bicicleta")

    print(producto.agregarPieza(p1))
    print(producto.agregarPieza(p2))
    print(producto.agregarPieza(p3))
    print(producto.agregarPieza(p4))

    # Intentar añadir una pieza repetida
    print(producto.agregarPieza(p1))

    print(f"Precio total: {producto.precioProducto()} euros")
    print(f"Peso total: {producto.pesoProducto()} gramos")

    print(producto.listadoPiezas())


if __name__ == "__main__":
    main()
