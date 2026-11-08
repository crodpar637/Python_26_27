from functools import reduce

diccionario = { ("ferry",1) : [ 2500 ,350 ], # [ carga, pasajeros ]
                ("mercante",2) : [ 1200000, 6500 ], # [ carga, autonomía ]
                ("mercante",3) : [ 200000, 3200 ], # [ carga, pasajeros ]
                ("ferry",4) : [ 3520 , 420] , # [ carga, pasajeros ]
                ("mercante",4) : [ 200000, 3200 ], # [ carga, pasajeros ]
                ("mercante",5) : [ 200000, 3200 ], # [ carga, pasajeros ]
                ("mercante",6) : [ 11200000, 3200 ], # [ carga, pasajeros ]
                ("mercante",7) : [ 200000, 3200 ], # [ carga, pasajeros ]
}

"""
a) Escriba una función obtenerPasajeros(diccionario), que tomando como parámetro de entrada el diccionario anterior, devuelva una tupla con los pasajeros de cada ferry. --> (350, 420) """

def obtenerPasajeros(d):
    # Filtrado para quedarme con los ferrys
    ferrys = filter(lambda item_barco : item_barco[0][0] == "ferry"  , d.items())

    # Obtener el numero de pasajeros 
    # Entrada : [ ( ("ferry",1) , [ 2500 ,350 ] ) ,  ( ("ferry",4) , [ 3520 , 420] ) ]
    pasajeros = map(lambda item_barco : item_barco[1][1] , ferrys)

    return tuple(pasajeros)
"""
Escribir una función mayorCarga(diccionario), que tomando como parámetro de entrada el diccionario anterior, obtenga en una lista de un único elemento el id_barco del mercante con mayor carga.
Para el diccionario dado el resultado sería: [ 3 ] """

def mayorCarga(d):
    # Filtrado para quedarme con los mercantes
    mercantes = filter(lambda item_barco : item_barco[0][0] == "mercante"  , d.items())

    # max_carga = reduce(lambda num , mercante : max(num, mercante)       ,mercantes, 0)
    mercante_max_carga = reduce(lambda m1, m2 :  m1 if m1[1][0] > m2[1][0] else m2 ,mercantes)

    return [mercante_max_carga[0][1]]


# Main
resultado = obtenerPasajeros(diccionario)
print(resultado)
resultado = mayorCarga(diccionario)
print(resultado)



