import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO prompts (prompt, msg) VALUES ('This is a test prompt.', 'This is a test message.')")

connection.commit()
connection.close()
