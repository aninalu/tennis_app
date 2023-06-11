# tennis_app

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

Create a database called flask_db in postgreSQL as postgres user. 
If you call it something else, remember to change database name in app.py and init_db.py.

In app.py and init_db.py:
Insert you own password into "password='**YOUR OWN PASSWORD**'"

In the vs code terminal (in virtual environment), 
navigate to the project directory (Tennis_app) and initialize database as follows:
    python init_db.py

In the vs code terminal from Tennis_app (in virtual environment), run flask app with:
    flask run

HOW TO INTERACT WITH THE WEBSITE:
Open a webbrowser and go to http://127.0.0.1:5000.
Our website shows the top tennis players in the world. 
You can register as a user, log-in and log out. 
You can press "Create" to create a new tennis player. 
Add in you data and press "Submit".
A new tennis player should show up in the table ranked after ATP points. 
If you press "Your players", you can see the players you have added and delete them.
You need to log in to create and delete players. You can only delete your own players.

If there are issues with creating new users or players due to duplicate primary key, 
then it is a good idea to restart the database and run the project again. 


We have included two E/R diagrams: 

    * A small one (ER.jpg) that shows two entities - 'players' and 'users'. They are 
    connected via the relationship 'created'. This is our model for the current app.

    * The diagram 'er_old.pgn' shows our old idea to show more complex data related 
    to tennis matches. 