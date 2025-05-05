from flask import Flask
from app.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strategy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 라우트 등록
from app.views import home, trends, strategies, strategy_select, mypage, my_strategies, mypage_edit, admin, auth
