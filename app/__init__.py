from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "flask" # FLASK_SECRET

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql:12345@localhost:3306/testdb' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes
