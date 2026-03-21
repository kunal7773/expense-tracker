import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("CREATE TABLE expenses (id INTEGER PRIMARY KEY, title TEXT, amount INTEGER)")
conn.close()

print("Database created!")