import psycopg2

db_name = "mwluqdpa"
db_user = "mwluqdpa"
db_pass = "QlKV9WhIJ2SF-v7GBjGYhJFZD5vkS-Ex"
db_host = "queenie.db.elephantsql.com"
db_port = "5432"

conn = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)

cur = conn.cursor()

cur.execute("""

CREATE TABLE Students

(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
FACULTY TEXT NOT NULL
)

""")

conn.commit()

print("Table created!")


