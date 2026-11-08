def mi_funcion():
    return "Un saludo"

class mi_clase:
    def __init__(self):
        self.__numero = 7

    def __str__(self):
        return str(self.__numero)

if __name__ == "__main__":
    print("Ejecutado desde modulo.py")