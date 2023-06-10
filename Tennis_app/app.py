import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

ids = [1,2,3,4,5,6,7,8,9,10]

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='sammy',
                            password='password')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    headers = ['Ranking', 'Name', 'Country', 'Age', 'ATP']
    cur.execute('SELECT * FROM players ORDER BY ATP DESC;')
    players = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('pages/index.html', headers=headers, players=players)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        #pid = int(request.form['pid'])
        pname = request.form['pname']
        country = request.form['country']
        age = int(request.form['age'])
        ATP = int(request.form['ATP'])
        
        ids.append(len(ids)+1)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
                    'VALUES (%s, %s, %s, %s, %s)',
                    (ids[-1], pname, country, age, ATP))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('pages/create.html')