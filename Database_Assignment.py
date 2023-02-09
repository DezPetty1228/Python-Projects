
import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('files.db')

# Create a cursor
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )''')

# Insert the data into the table
fileList = ['information.docx', 'Hello.txt', 'myImage.png',
            'myMovie.mpg', 'World.txtdata.pdf', 'myPhoto.jpg']
for file in fileList:
    if file.endswith('.txt'):
        cursor.execute('''INSERT INTO files (name)
                          VALUES (?)''', (file,))

# Commit the changes
conn.commit()

# Query the database for text files
cursor.execute('''SELECT * FROM files WHERE name LIKE '%.txt' ''')

# Fetch and print the results
results = cursor.fetchall()
for result in results:
    print(result[1])

# Close the connection
conn.close()
