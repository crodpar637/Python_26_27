def entrada_datos():
    l = [] 

    for _ in range(3):
        nombre = input("Nombre del equipo:")
        a_favor = int(input("Puntos a favor:"))
        en_contra = int(input("Puntos en contra:"))
        jugados = int(input("Partidos jugados:"))

        tupla_datos = (nombre, a_favor, en_contra, jugados)
        l.append(tupla_datos)

    print(l)

    return l

def calculo_estadistica(lista_datos):
    d = {}

    #for datos_equipo in lista_datos:
    #    diferencia = datos_equipo[1] - datos_equipo[2]
    #
    #    d[datos_equipo[0]] = ( diferencia ,  diferencia / datos_equipo[3])

    for ( nombre, a_favor, en_contra, jugados) in lista_datos:
        diferencia = a_favor - en_contra

        d[nombre] = ( diferencia , diferencia / jugados ) 
                     
    return d
        



# MAIN
# lista_datos = entrada_datos()
lista_datos = [('Quinto', 150, 99, 2), ('Cantely', 189, 90, 2), ('Mosqueo', 190, 289, 2)]

d = calculo_estadistica(lista_datos)

print(d)












