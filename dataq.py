import psycopg2

db_name = "mwluqdpa"
db_user = "mwluqdpa"
db_pass = "QlKV9WhIJ2SF-v7GBjGYhJFZD5vkS-Ex"
db_host = "queenie.db.elephantsql.com"
db_port = "5432"



conn = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)


cur = conn.cursor()
cur.execute("SELECT ID, NAME, FACULTY FROM Students")

rows = cur.fetchall()

for data in rows:
    print("ID:", data[0])
    print("NAME:", data[1])
    print("FACULTY:", data[2])

conn.close()