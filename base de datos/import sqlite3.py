import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')

cursor.close()
conn.close()