# import psycopg2
# import psycopg2.extras


# HOSTNAME = 'localhost'
# USERNAME = 'postgres'
# PASSWORD = '6LGbiIGH'
# DATABASE = 'actors'



# postgres_db_connection = psycopg2.connect(
#     host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE
# ) 



# cursor = postgres_db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


# query = "SELECT * FROM actors;"
# cursor.execute(query)

# results = cursor.fetchall()

# # print(results)
# # print(type(results))
# # print(type(results))

# print("--- Results from POstgres")
# for row in results:
#     print(row)


# postgres_db_connection.close()

import sqlite3
sqlite_db_connection = sqlite3.connect("jacobalexissubyushi.db")

cursor = sqlite_db_connection.cursor()

query = "CREATE TABLE IF NOT EXISTS pets ( \
   id INTEGER PRIMARY KEY AUTOINCREMENT, \
   name VARCHAR(255)   \
);"

cursor.execute(query)

query = "INSERT INTO pets (name) VALUES \
    ('Fido'), \
    ('Cookie'), \
    ('Caneller') \
;"

cursor.execute(query)

query = "SELECT * FROM pets;"
cursor.execute(query)
sqlite_db_connection.commit()

results = cursor.fetchall()

print(results)

sqlite_db_connection.close()