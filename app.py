import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="./templates", static_folder="./static")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:@postgres:5432/YU"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SECRET_KEY'] = 'super_secret_key'

db = SQLAlchemy(app)
# db = None

from routes import *

with app.app_context():
    db.session.commit()


