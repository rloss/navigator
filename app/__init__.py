from flask import Flask
from app.models import db
from app.views import register_blueprints

import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strategy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
register_blueprints(app)
