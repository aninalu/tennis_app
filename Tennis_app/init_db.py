import os
import psycopg2


conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='sammy',
        password='password')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
#cur.execute('DROP TABLE IF EXISTS books;')
#cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
#                                 'title varchar (150) NOT NULL,'
#                                 'author varchar (50) NOT NULL,'
#                                 'pages_num integer NOT NULL,'
#                                 'review text,'
#                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
#                                 )

# Insert data into the table
cur.execute('TRUNCATE TABLE players')
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            ' VALUES (%s, %s, %s, %s, %s)',
            (1, 'Carlos Alcaraz', 'Spain', 20, 6815))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            ' VALUES (%s, %s, %s, %s, %s)', 
            (2, 'Daniil Medvedev', 'Russia', 27, 6330))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',
            (3, 'Novak Djokovic', 'Serbia', 36, 5955))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',  
            (4, 'Casper Ruud', 'Norway', 24, 5955))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',
            (5, 'Stefanos Tsitsipas', 'Greece', 24, 4775))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',
            (6, 'Holger Rune', 'Denmark', 20, 4375))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',
            (7, 'Andrey Rublev', 'Russia', 25, 4375))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',
            (8, 'Taylor Fritz', 'USA', 25, 4270))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',
            (9, 'Jannik Sinner', 'Italy', 21, 3435))
cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
            'VALUES (%s, %s, %s, %s, %s)',
            (10, 'Felix Auger-Aliassime', 'Canada', 22, 3100))

conn.commit()

cur.close()
conn.close()