class Ejemplo():
    a = 7 # Atributo de clase o estatico
    def __init__(self):
        self.b = 3 # Atributo de instancia


print (Ejemplo.a)
# print (Ejemplo.b) # Excepción, b no es atributo de clase

objeto = Ejemplo()
print(objeto.a) # Está definido en la clase --> 7
objeto.a = 9 # ¡¡ Cuidado, se crea un atributo dinámicamente !!
print("objeto.a:",objeto.a)
print("Ejemplo.a:", Ejemplo.a)

objeto2 = Ejemplo() # Creamos otra instancia
print(Ejemplo.a) #Atributo de clase --> 7
print(objeto.a) #Atributo de instancia --> 9
print(objeto2.a) #Atributo de clase --> 7