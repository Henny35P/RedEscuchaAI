import psycopg2

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
for row in rows:
    print("COMENTARIO", row[0])

connect.close()
