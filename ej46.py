# Abrir fichero
f = open("datos-ej46.txt","rt",encoding="UTF-8")

# Leo como lista de lineas
lineas = f.readlines()

# Cerrar fichero
f.close()

#Lista para almacenar todos los numeros
lista_numeros = []

#Recorrer las lineas de texto con numeros separados por ";"
for linea in lineas:
    # obtengo una lista de números reales (son cadenas de texto)
    numeros_string = linea.strip("\n").split(";")
    print(numeros_string)

    numeros_reales = map(lambda num_string: float(num_string), numeros_string)

    # Agregar los numeros reales a la lista que contiene todos los datos
    lista_numeros.extend(numeros_reales)

print(lista_numeros)
print("Máximo:", max(lista_numeros))
print("Mínimo:", min(lista_numeros))
print("Suma:", sum(lista_numeros))
print("Media:", sum(lista_numeros)/len(lista_numeros))


    
    
    



