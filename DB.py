import mysql.connector

conn= mysql.connector.connect(host='localhost',username='root',password='')

my_cursor=conn.cursor()

query1="CREAT DATABASE new_database_python"
# query="SHOW DATABASES"

my_cursor.execute(query1)

# for database_name in my_cursor:
#     print(database_name)

conn.commit()
conn.close()