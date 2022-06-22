import psycopg2


def abrirDatabase():
    hostname = "localhost"
    database = "redescucha"
    username = "postgres"
    pwd = "admin"
    port_id = 5432

    connect = psycopg2.connect(
        host=hostname, database=database, user=username, password=pwd, port=port_id
    )

    cur = connect.cursor()

    cur.execute("SELECT comentario from COMMENTS")

    rows = cur.fetchall()
    file = open("reclamos.txt", "w+")
    for row in rows:
        reclamo = row[0]
        file.write(reclamo + "\n")

    connect.close()
    file.close()


abrirDatabase()
