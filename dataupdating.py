import psycopg2

db_name = "mwluqdpa"
db_user = "mwluqdpa"
db_pass = "QlKV9WhIJ2SF-v7GBjGYhJFZD5vkS-Ex"
db_host = "queenie.db.elephantsql.com"
db_port = "5432"


conn = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)


cur = conn.cursor()

cur.execute("UPDATE Students set FACULTY = 'BS' WHERE ID = 1")

conn.commit()

print("Data Uodated!")