import os

# 디렉토리 구조 생성
folders = [
    "app/views",
    "templates",
    "static/css",
    "static/js",
    "static/img",
    "data"
]

template_files = [
    "layout", "home",
    "trend_list", "trend_detail",
    "strategy_list", "strategy_detail",
    "mypage", "mypage_strategies", "mypage_edit",
    "login", "admin_dashboard", "admin_review"
]

files = {
    "run.py": "from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)\n",

    "config.py": "import os\n\nOPENAI_API_KEY = os.getenv('OPENAI_API_KEY')\nSUPABASE_URL = os.getenv('SUPABASE_URL')\nSUPABASE_KEY = os.getenv('SUPABASE_KEY')\n",

    "requirements.txt": "flask\nflask_sqlalchemy\nopenai\nsupabase\nrequests\nfeedparser\n",

    "README.md": "# 전략 내비게이터 MVP",

    "app/__init__.py": """from flask import Flask
from app.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strategy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 라우트 등록
from app.views import home, trends, strategies, strategy_select, mypage, my_strategies, mypage_edit, admin, auth
""",

    "app/db.py": "from flask_sqlalchemy import SQLAlchemy\ndb = SQLAlchemy()\n",

    "app/models.py": '''from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Trend(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    summary = db.Column(db.Text)
    scenarios = db.relationship('Scenario', backref='trend', lazy=True)
    strategies = db.relationship('StrategyCard', backref='trend', lazy=True)

class Scenario(db.Model):
    id = db.Column(db.String, primary_key=True)
    summary = db.Column(db.Text)
    trend_id = db.Column(db.String, db.ForeignKey('trend.id'))

class StrategyCard(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    summary = db.Column(db.Text)
    role_annotations = db.Column(db.JSON)
    trend_id = db.Column(db.String, db.ForeignKey('trend.id'))

class UserStrategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    strategy_id = db.Column(db.String)
    title = db.Column(db.String)
    summary = db.Column(db.Text)
    trend_title = db.Column(db.String)
    selected_at = db.Column(db.DateTime, default=datetime.utcnow)
'''
    ,

    "data/mock_trends.py": "# 여기에 목업 트렌드/시나리오/전략 카드 데이터 정의",

    "data/seed.py": '''from app import app
from app.models import db

with app.app_context():
    db.create_all()
    print("✅ DB 초기화 완료")
''',

    "static/css/main.css": "/* 커스텀 스타일 */",
    "static/js/filters.js": "// 전략 카드 필터링 스크립트",
}

def create_structure():
    # 폴더 생성
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # 템플릿 생성
    for name in template_files:
        path = f"templates/{name}.html"
        content = f"{{% extends 'layout.html' %}}\n{{% block content %}}\n<h2>{name.replace('_', ' ').title()}</h2>\n{{% endblock %}}"
        files[path] = content

    # 파일 생성
    for path, content in files.items():
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    print("✅ 전략 내비게이터 전체 폴더/파일 구조 생성 완료!")

if __name__ == "__main__":
    create_structure()
