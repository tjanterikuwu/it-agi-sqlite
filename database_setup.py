import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('it-agi.db')

# Create a cursor object
cursor = conn.cursor()

# Create the Test table with two columns
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Test (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print('Database and Test table created successfully.')
