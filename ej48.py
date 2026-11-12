import sqlite3

def get_connection():
    conn = sqlite3.connect("equipo.db")
    
    return conn

def altura_media():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT AVG(altura) FROM jugadores WHERE fecha_baja IS NOT null")

    row = cursor.fetchone()

    conn.close()

    print("Fila:", row)

    altura_media = row[0]

    return altura_media

def jugadores_altos():
    valor_altura_media = altura_media()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(f"SELECT dni FROM jugadores WHERE fecha_baja IS null AND altura >= {valor_altura_media}")

    rows = cursor.fetchall()

    conn.close()

    with open("jugadores.txt","wt") as f:
        for row in rows:
            f.write(row[0])
            f.write("\n")

    #el fichero se cierra solo al salir del bloque with


#MAIN
print("Altura media:", altura_media())
jugadores_altos()
