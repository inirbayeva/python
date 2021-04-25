import psycopg2

db_name = "mwluqdpa"
db_user = "mwluqdpa"
db_pass = "QlKV9WhIJ2SF-v7GBjGYhJFZD5vkS-Ex"
db_host = "queenie.db.elephantsql.com"
db_port = "5432"



conn = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)


cur = conn.cursor()

cur.execute("INSERT INTO Student (ID, NAME, FACULTY) VALUES (1, 'Daniyar', 'FIT')")

conn.commit()
print(" Data have added!")

conn.close()