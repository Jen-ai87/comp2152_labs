import sqlite3

import function

db_connection = sqlite3.connect('sqlite.db')
print("Opened database successfully")
print(db_connection)

db_cursor = db_connection.cursor()
print(db_cursor)

query_1 = "SELECT * FROM demo"
db_cursor.execute(query_1)
row = db_cursor.fetchone()
print(" ")
print("-------------------------------")
print("Reading one row")
print("-------------------------------")
print(" ")
print(row)

row_many = db_cursor.fetchmany(2)
print(" ")
print("-------------------------------")
print("Reading 2 rows")
print("-------------------------------")
print(" ")
# for each_row in row_many:
#     print(each_row)
function.query_responder(db_cursor, "fetchmany", 2)

rows = db_cursor.fetchall()
print(" ")
print("-------------------------------")
print("Reading all remaining rows")
print("-------------------------------")
print(" ")
# for each_row in rows:
#     print(each_row)
function.query_responder(db_cursor, "fetchall")
print(" ")

query_2 = "INSERT INTO demo (Name, Hint) VALUES ('Jen Henry', 'Student at George Brown College')"
db_cursor.execute(query_2)
# db_connection.commit()

id = int(input("Insert ID: "))
query_3 = f"SELECT * FROM demo WHERE ID > ?"
db_cursor.execute(query_3, (id,))
row = db_cursor.fetchone()
function.query_responder(db_cursor, "fetchall")