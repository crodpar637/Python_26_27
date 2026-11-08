#import MySQLdb
import pymysql

def getConnection():
    db_host = 'db'
    usuario = 'root'
    clave = 'test'
    base_de_datos = 'equipo'
    #conn = MySQLdb.connect(host=db_host, user=usuario, passwd=clave, db=base_de_datos)
    conn = pymysql.connect(host=db_host, user=usuario, passwd=clave, db=base_de_datos)
    
    return conn

def altura_media():
     # Obtengo la conexión
    conn = getConnection()
    # Obtengo el objeto cursor
    cursor = conn.cursor()
    # Lanzó la ejecución de la sentencia SQL
    cursor.execute("SELECT avg(altura) FROM jugadores WHERE fecha_baja IS NULL")

    # Recupero una fila con el resultado
    fila = cursor.fetchone()

    # Cerrar la conexion
    conn.close()

    return fila[0]

    
def main():
    altura_resultado = altura_media()
    print("La altura media de los jugadores en activo es:", altura_resultado)

main()
    