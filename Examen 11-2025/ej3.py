import pymysql

def cargar_reservas_desde_csv():
    # Apertura del fichero
    f = open("reservas.csv", "rt", encoding="UTF-8")
    #Leemos el fichero completo como una lista de líneas
    lista_lineas = f.readlines()
    #Cerramos el fichero
    f.close()
    #Crear un diccionario vacío
    d = {}
    #Recorrer todas las líneas empezando en la primera con datos [1:]
    for linea in lista_lineas[1:]:
        # linea = 1,Ana García,611223344,2025-03-15,4,5
        # Dividimos en campos
        lista_campos = linea.split(",")
        # Creamos un elemento del diccionario
        d[int(lista_campos[0])] = { 'nombre': lista_campos[1] , 'telefono' : lista_campos[2], 'fecha': lista_campos[3], 'personas': int(lista_campos[4]) , 'mesa': int(lista_campos[5].strip()) }

    return d
    
def insertar_reservas_bbdd(reservas):

    conn = pymysql.connect(host='php-26-27-db-1',user='root',password='test',database='examen')

    cursor = conn.cursor()

    for reserva in reservas.items():
        #reserva.items  [ ( 1 , {'nombre': 'Ana García', 'telefono': '611223344', 'fecha': '2025-03-15', 'personas': 4, 'mesa': 5} ) , ( 2,  { ... } ) , ( 3 , { .... } ), .... ]
        sql = "INSERT INTO reserva(id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa) VALUES ( %s , %s , %s, %s , %s , %s )"

        cursor.execute(sql, ( reserva[0] ,  reserva[1]['nombre'] , reserva[1]['telefono'], reserva[1]['fecha'],reserva[1]['personas'], reserva[1]['mesa']) ) 

    conn.commit()

    conn.close()

def mostrar_reservas_fecha(fecha):

    conn = pymysql.connect(host='php-26-27-db-1',user='root',password='test',database='examen')
    cursor = conn.cursor()

    sql = "SELECT * FROM reserva WHERE fecha_reserva = %s"
    cursor.execute(sql, (fecha, ))
    
    rows = cursor.fetchall()  # Lista de tuplas, cada tupla es una fila de datos

    conn.close()

    listado = f"RESERVAS PARA {fecha}:\n"
    listado += "===========================\n"
    num_personas = 0
    num_reservas = 0
    for row in rows:
        listado += f"Mesa {row[5]}: {row[1]} ({row[4]} personas) - Tel: {row[2]}\n"
        num_reservas += 1
        num_personas += row[4]

    listado += f"Total {num_reservas} reservas, {num_personas} personas"

    return listado
    
# MAIN
reservas = cargar_reservas_desde_csv()
print(reservas)

# insertar_reservas_bbdd(reservas)

print(mostrar_reservas_fecha("2025-11-14"))
print(mostrar_reservas_fecha("2025-03-15"))



