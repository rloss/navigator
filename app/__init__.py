from flask import Flask
from app.models import db
from app.views import register_blueprints
from dotenv import load_dotenv

import os

# 🔁 .env 파일 로드 (로컬에서만 적용됨)
load_dotenv()

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '../static')
)

# 🔐 세션 비밀키는 환경변수에서 가져옴
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")

# 📦 PostgreSQL 연동 (DATABASE_URL은 .env 또는 Render에서 설정)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB 초기화
db.init_app(app)

# 라우트 등록
register_blueprints(app)

