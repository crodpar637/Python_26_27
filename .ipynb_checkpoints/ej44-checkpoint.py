
nombre_fichero_entrada = input("Nombre del fichero de entrada:")

f = open(nombre_fichero_entrada, "rt")

todo = f.read()

f.close()

todo = todo.upper().replace(",", " ").replace(".", " ").replace(";", " ").replace("?", " ").replace("¿", " ").replace("!", " ").replace("¡", " ").replace(":", " ").replace(")", " ").replace("(", " ").replace("\n", " ")

lista_palabras = todo.split()
print(lista_palabras)

diccionario = {}
for palabra in lista_palabras:
    if palabra != ' ': #ignoro espacios

        # diccionario[palabra] = diccionario.get(palabra, 0) + 1
        
        if palabra in diccionario.keys():
             diccionario[palabra] = diccionario[palabra] + 1
        else:
             diccionario[palabra] = 1  # inserto en el diccionario

f2 = open("salida-ej44.txt", "wt")

for (clave, valor) in diccionario.items():
    salida = clave + ", " + str(valor) + "\n"
    
    f2.write(salida)

f2.close()













