import sqlite3 as sql

conn = sql.connect('database.db')
cursor = conn.cursor()
cursor.execute('create table post (postName, postContent);')
conn.commit()
conn.close()
