from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f865b53623b121fd34ee5426c792e5c33af8c227'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'employees_db'

mysql = MySQL()
mysql.init_app(app)
