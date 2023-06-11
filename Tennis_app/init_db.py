import os
import psycopg2


conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='postgres',
        password='**YOUR OWN PASSWORD**')

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS players CASCADE;')
cur.execute('CREATE TABLE players ( pid SERIAL PRIMARY KEY,'
            'pname varchar (50) NOT NULL,' 
            'country varchar (50) NOT NULL,' 
            'age integer NOT NULL,' 
            'ATP integer NOT NULL);'
            )

cur.execute('DROP TABLE IF EXISTS users CASCADE;')
cur.execute('CREATE TABLE users ( uid SERIAL PRIMARY KEY,'
            'username varchar (50) NOT NULL,' 
            'password varchar (255) NOT NULL);' 
            )
cur.execute('DROP TABLE IF EXISTS created;')
cur.execute('CREATE TABLE created(pid SERIAL REFERENCES players(pid) ON DELETE CASCADE,'
            'uid SERIAL REFERENCES users(uid),'
            'CONSTRAINT created_pk PRIMARY KEY(pid,uid) );'
            )

# Insert data into the table
cur.execute('TRUNCATE TABLE players CASCADE')
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