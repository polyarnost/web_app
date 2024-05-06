from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
import os

secret_key = os.urandom(5)

app = Flask(__name__, template_folder='templates')

template_dir = Path(__file__).resolve().parent / 'templates'
app.template_folder = str(template_dir)

app.secret_key = secret_key

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes
from app.models import Student, Grade

