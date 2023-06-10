HOW TO RUN:

First make sure that Tennis_app is in a virtual environment 
if not, then create a virtual environment in the terminal 
and put Tennis_app inside the .venv folder
(Make sure that you have the newest version of python3!):
    On windows: py -3 -m venv .venv
    On Mac/Linux: python3 -m venv .venv

Activate virtual environment in FLASK_PROJECT:
    . .venv/bin/activate

Install Flask:
    pip install Flask

Install psycopg2 with the command: 
    pip install Flask psycopg2-binary

Open as psql terminal and log-in as 'postgres'-superuser

Create a database in psql:
    CREATE DATABASE flask_db;

Go to database:
    \c flask_db

Create a players table:
    CREATE TABLE players (
        pid serial PRIMARY KEY, 
        pname varchar (50) NOT NULL, 
        country varchar (50) NOT NULL, 
        age integer NOT NULL, 
        ATP integer NOT NULL
        );

In app.py and init_db.py:
replace "user='sammy'" and "password='password'" with "user='postgres'" and "password='**YOUR OWN PASSWORD**'"

In the vs code terminal (in virtual environment), 
navigate to the project directory (Tennis_app) and initialize database as follows:
    python init_db.py

In the vs code terminal from Tennis_app (in virtual environment), run flask app with:
    flask run

HOW TO INTERACT WITH THE WEBSITE:
Open a webbrowser and go to http://127.0.0.1:5000.
Our webiste shows the top tennis players in the world. 
You can press "Create" to create a new tennis player. 
Fill in the dataset and a press create.
A new tennis player should show up in the table ranked after ATP points. 

We have included two E/R diagrams: 

    * A small one (ER.jpg) that shows two entities - 'players' and 'users'. They are 
    connected via the relationship 'created'. If we had more time to build our app, 
    we would create a log-in functionality,  where a user can create new players for 
    the database. Only the user who created a player can delete the player. 

    * The diagram 'er_old.pgn' shows our old idea to show more complex data related 
    to tennis matches. 