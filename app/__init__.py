from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# FLASK_SECRET
app.config['SECRET_KEY'] = "flask" 

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql:12345@localhost:3306/testdb' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import Routes
from app import routes
