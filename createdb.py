import sqlite3


conn = sqlite3.connect('vidyo.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE videos (id INTEGER PRIMARY KEY AUTOINCREMENT,filename VARCHAR(255) NOT NULL,username VARCHAR(255) NOT NULL,timestamp DATETIME NOT NULL,service_type VARCHAR(255) NOT NULL)')
print("Created table successfully!")

conn.close()