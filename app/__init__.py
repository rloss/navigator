from flask import Flask
from app.models import db
from app.views import register_blueprints

import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '../static')
)

# 🔐 세션을 위한 비밀 키 설정
app.secret_key = "supersecret"  # 반드시 나중에 .env로 대체해야 함

# DB 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strategy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 모든 라우트 블루프린트 등록
register_blueprints(app)
