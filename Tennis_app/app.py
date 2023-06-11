import os
import psycopg2
import psycopg2.extras
from flask import Flask, request, session, redirect, url_for, render_template, flash
import re 
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'hello_tennis_2023'

pids = [1,2,3,4,5,6,7,8,9,10]
uids = []

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='postgres',
                            password='**YOUR OWN PASSWORD**')
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
    if 'loggedin' in session:
        if request.method == 'POST':
            pname = request.form['pname']
            country = request.form['country']
            age = int(request.form['age'])
            ATP = int(request.form['ATP'])
            
            pids.append(len(pids)+1)
            newpid = pids[-1]

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO players (pid, pname, country, age, ATP)'
                        'VALUES (%s, %s, %s, %s, %s)',
                        (newpid, pname, country, age, ATP))
            cur.execute('INSERT INTO created (pid, uid)'
                        'VALUES (%s, %s)',
                        (newpid, session['uid']))

            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))
    else:
        flash('You need to log in')
        return redirect(url_for('login'))
    return render_template('pages/create.html' )

@app.route('/myplayers/', methods=('GET', 'POST'))
def myplayers():
    if 'loggedin' in session:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT * FROM players '
                        'INNER JOIN created ' 
                        'ON players.pid =created.pid '
                        'WHERE created.uid = %s;', 
                        (session['uid'],)) 
            
            players = cur.fetchall() 
            
            if len(players) == 0:
                flash('You haven\'t added any players')
                return redirect(url_for('create'))
            
            cur.close()
            conn.close()
    else:
        flash('You need to log in')
        return redirect(url_for('login'))
    return render_template('pages/myplayers.html', players=players)

@app.route('/delete/<int:id>', methods=('GET', 'POST'))
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM players WHERE pid = {0}'.format(id))
    conn.commit()
    flash('Player Removed Successfully')
    return redirect(url_for('index'))

@app.route('/register/', methods=('GET', 'POST'))
def register():
    if not 'loggedin' in session:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']   
            
            uids.append(len(uids)+1)
            _hashed_password = generate_password_hash(password)
            
            cur.execute('SELECT * FROM users WHERE username = %s', (username,))
            account = cur.fetchone()
            print(account)
            # If account exists show error and validation checks
            if account:
                flash('Account already exists!')
            elif not re.match(r'[A-Za-z0-9]+', username):
                flash('Username must contain only characters and numbers!')
            elif not username or not password:
                flash('Please fill out the form!')
            else:
                # Account doesnt exists and the form data is valid, now insert new account into users table
                cur.execute("INSERT INTO users (uid, username, password)" 
                            "VALUES (%s, %s,%s)", 
                            (uids[-1], username, _hashed_password))
                conn.commit()
                flash('You have successfully registered!')
                return redirect(url_for('login'))
        elif request.method == 'POST':
            # Form is empty... (no POST data)
            flash('Please fill out the form!')
        # Show registration form with message (if any)
    else:
        flash('You are already logged in - log out to register new user')
        return redirect(url_for('index'))    
    return render_template('pages/register.html')

@app.route('/login/', methods=('GET', 'POST'))
def login():
    if not 'loggedin' in session:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            print(password)
    
            # Check if account exists using MySQL
            cur.execute('SELECT * FROM users WHERE username = %s', (username,))
            # Fetch one record and return result
            account = cur.fetchone()
    
            if account:
                password_rs = account['password']
                print(password_rs)
                # If account exists in users table in out database
                if check_password_hash(password_rs, password):
                    # Create session data, we can access this data in other routes
                    session['loggedin'] = True
                    session['uid'] = account['uid']
                    session['username'] = account['username']
                    # Redirect to home page
                    flash('You were successfully logged in')
                    return redirect(url_for('index'))
                else:
                    # Account doesnt exist or username/password incorrect
                    flash('Username or password doesn\'t exist')
            else:
                # Account doesnt exist or username/password incorrect
                flash('Username or password doesn\'t exist - remember to register!')
                return redirect(url_for('register'))  
    else:
        flash('You are already logged in - log out to log in with another user')
        return redirect(url_for('index'))    
    return render_template('pages/login.html')

@app.route('/logout/')
def logout():
    if 'loggedin' in session:
        session.pop('loggedin', None)
        session.pop('uid', None)
        session.pop('username', None)
        flash('You logged out')
        # Redirect to login page
        return redirect(url_for('login'))
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(debug=True)