from functools import reduce

def leer_ventas_tapas():

    lista = []
    
    for _ in range(4):
        nombre_tapa = input("Nombre de la tapa:")
        precio = float(input("Precio de la tapa:"))
        unidades = int(input("Unidades vendidas:"))
        
        tupla = (nombre_tapa, precio, unidades)
        
        lista.append( tupla ) 

    return lista

def calcular_estadisticas_tapas(lista_tapas):
    d  = {} 
    
    for tapa in lista_tapas:
        # tapa  --> (nombre_tapa, precio, unidades) -- > ( tapa[0] , tapa[1] , tapa[2] ) 
        if tapa[2] > 25:
            popularidad = 'Alta'
        elif tapa[2] > 15: 
            popularidad = 'Media'
        else :
            popularidad = 'Baja'
            
        d[tapa[0]] = ( tapa[1] * tapa[2]   , tapa[1] * tapa[2] * 0.1 , popularidad)
        
    return d
"""
{'Serranito': (87.5, 8.75, 'Alta'),'Solomillo al whisky': (75.6, 7.56, 'Media'),
'Montadito de pringá': (89.6, 8.96, 'Alta'),
'Espinacas con garbanzos': (63.0, 6.3, 'Media') }

.items()
[  ( 'Serranito', (87.5, 8.75, 'Alta') ) ,  ( 'Solomillo al whisky' , (75.6, 7.56, 'Media') ) , ... ]
"""
def analizar_rendimiento_tapas(dicc_tapas):

    tapas_popularidad_alta = filter(lambda tapa : tapa[1][2] == 'Alta' , dicc_tapas.items() ) 

    promedio_iva  = sum(map( lambda tapa : tapa[1][1] , dicc_tapas.items() )) / len(dicc_tapas)

    tapa_mayor_importe = reduce(lambda t1,t2: t1 if t1[1][0] > t2[1][0] else t2, dicc_tapas.items())

    return ( list(tapas_popularidad_alta) , promedio_iva , tapa_mayor_importe[0] )    

# MAIN 
# datos = leer_ventas_tapas()
# print(datos)
datos = [('Serranito', 3.5, 25), ('Solomillo al whisky', 4.2, 18), ('Montadito de pringá', 2.8, 32), ('Espinacas con garbanzos', 3.0, 21)]

estadisticas = calcular_estadisticas_tapas(datos)
print(estadisticas)

resultado = analizar_rendimiento_tapas(estadisticas) 
print(resultado)


        