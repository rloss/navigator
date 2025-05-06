# 📁 프로젝트 구조

```
├── 📄 README.md
├── 📄 alembic.ini
├── 📁 app
│   ├── 📄 .env
│   ├── 📄 __init__.py
│   ├── 📄 db.py
│   ├── 📄 filters.py
│   ├── 📄 gpt_utils.py
│   ├── 📄 models.py
│   ├── 📄 rss_worker.py
│   ├── 📄 supabase_client.py
│   └── 📁 views
│       ├── 📄 __init__.py
│       ├── 📄 admin.py
│       ├── 📄 auth.py
│       ├── 📄 home.py
│       ├── 📄 my_strategies.py
│       ├── 📄 mypage.py
│       ├── 📄 mypage_edit.py
│       ├── 📄 strategies.py
│       ├── 📄 strategy_select.py
│       └── 📄 trends.py
├── 📄 config.py
├── 📁 data
│   ├── 📄 mock_trends.py
│   └── 📄 seed.py
├── 📁 instance
├── 📁 migrations
│   ├── 📄 README
│   ├── 📄 env.py
│   ├── 📄 script.py.mako
│   └── 📁 versions
├── 📄 navigator_백업.md
├── 📄 render.yaml
├── 📄 requirements.txt
├── 📄 run.py
├── 📄 setup.py
├── 📁 static
│   ├── 📁 css
│   │   └── 📄 main.css
│   ├── 📁 img
│   └── 📁 js
│       └── 📄 filters.js
└── 📁 templates
    ├── 📄 admin_create.html
    ├── 📄 admin_dashboard.html
    ├── 📄 admin_review.html
    ├── 📄 admin_trend_edit.html
    ├── 📄 home.html
    ├── 📄 layout.html
    ├── 📄 login.html
    ├── 📄 mypage.html
    ├── 📄 mypage_edit.html
    ├── 📄 mypage_strategies.html
    ├── 📄 signup.html
    ├── 📄 strategy_detail.html
    ├── 📄 strategy_list.html
    ├── 📄 trend_detail.html
    └── 📄 trend_list.html
```

## 📄 `alembic.ini`

```
# A generic, single database configuration.

[alembic]
# path to migration scripts
# Use forward slashes (/) also on windows to provide an os agnostic path
script_location = migrations

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python>=3.9 or backports.zoneinfo library and tzdata library.
# Any required deps can installed by adding `alembic[tz]` to the pip requirements
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to migrations/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:migrations/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
# version_path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
version_path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/.venv/bin/ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

```

## 📄 `config.py`

```python
import os

OPENAI_API_KEY = 
DATABASE_URL= postgresql://navigator_owner:npg_j9NHeIuoRW6G@ep-wild-cloud-a1gkpmtv-pooler.ap-southeast-1.aws.neon.tech/navigator?sslmode=require
SUPABASE_KEY = 

```

## 📄 `navigator_백업.md`

```markdown

```

## 📄 `README.md`

```markdown
# 전략 내비게이터 MVP
```

## 📄 `render.yaml`

```yaml
services:
  - type: web
    name: strategy-navigator
    env: python
    buildCommand: ""
    startCommand: gunicorn run:app
    plan: free
    autoDeploy: true
```

## 📄 `requirements.txt`

```
flask
flask_sqlalchemy
openai
supabase
requests
feedparser
gunicorn
python-dotenv
psycopg2-binary
```

## 📄 `run.py`

```python
import os
import sys
from pathlib import Path

# 모듈 경로 인식 보장
sys.path.append(str(Path(__file__).resolve().parent))

from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render가 제공하는 포트 사용
    app.run(host="0.0.0.0", port=port, debug=True)

```

## 📄 `setup.py`

```python
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

```

## 📄 `app\.env`

```
DATABASE_URL=postgresql://navigator_owner:npg_j9NHeIuoRW6G@ep-wild-cloud-a1gkpmtv-pooler.ap-southeast-1.aws.neon.tech/navigator?sslmode=require
SECRET_KEY=your_super_secret_key
```

## 📄 `app\db.py`

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```

## 📄 `app\filters.py`

```python

```

## 📄 `app\gpt_utils.py`

```python

```

## 📄 `app\models.py`

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# 🔹 트렌드 (1) → (다) 시나리오 / 전략카드
class Trend(db.Model):
    __tablename__ = "trend"
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    summary = db.Column(db.Text, nullable=False)

    # 관계
    scenarios = db.relationship("Scenario", backref="trend", cascade="all, delete-orphan", lazy=True)
    strategies = db.relationship("StrategyCard", backref="trend", cascade="all, delete-orphan", lazy=True)


# 🔹 시나리오 (다) → (1) 트렌드 / (1) → (다) 전략카드
class Scenario(db.Model):
    __tablename__ = "scenario"
    id = db.Column(db.String, primary_key=True)
    summary = db.Column(db.Text, nullable=False)

    trend_id = db.Column(db.String, db.ForeignKey("trend.id"), nullable=False)

    # 전략카드 연결 (선택적으로 활용)
    strategies = db.relationship("StrategyCard", backref="scenario", lazy=True)


# 🔹 전략 카드: 트렌드 + (선택적) 시나리오 연결
class StrategyCard(db.Model):
    __tablename__ = "strategy_card"
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    summary = db.Column(db.Text, nullable=False)

    # 역할 해석 (디자이너, 기획자 등)
    role_annotations = db.Column(db.JSON, nullable=True)

    # 연결 관계
    trend_id = db.Column(db.String, db.ForeignKey("trend.id"), nullable=False)
    scenario_id = db.Column(db.String, db.ForeignKey("scenario.id"), nullable=True)  # 시나리오 연결 (선택)


# 🔹 사용자별 선택한 전략 카드
class UserStrategy(db.Model):
    __tablename__ = "user_strategy"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    strategy_id = db.Column(db.String, nullable=False)

    title = db.Column(db.String)
    summary = db.Column(db.Text)
    trend_title = db.Column(db.String)

    selected_at = db.Column(db.DateTime, default=datetime.utcnow)


# 🔹 사용자 모델
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.String, primary_key=True)  # 로그인 ID
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

```

## 📄 `app\rss_worker.py`

```python

```

## 📄 `app\supabase_client.py`

```python

```

## 📄 `app\__init__.py`

```python
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


```

## 📄 `app\views\admin.py`

```python
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Trend, Scenario, StrategyCard

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/trend/<trend_id>/edit", methods=["GET", "POST"])
def edit_trend(trend_id):
    trend = Trend.query.get(trend_id)
    if not trend:
        return "해당 트렌드가 존재하지 않습니다.", 404

    # POST 요청 시 새로운 시나리오 또는 전략 등록 처리
    if request.method == "POST":
        form_type = request.form.get("form_type")

        if form_type == "scenario":
            summary = request.form.get("scenario_summary")
            scenario = Scenario(summary=summary, trend_id=trend_id)
            db.session.add(scenario)

        elif form_type == "strategy":
            title = request.form.get("strategy_title")
            summary = request.form.get("strategy_summary")
            scenario_id = request.form.get("strategy_scenario_id")
            strategy = StrategyCard(
                title=title,
                summary=summary,
                trend_id=trend_id,
                scenario_id=scenario_id,
                role_annotations={}  # 기본값 비워두기
            )
            db.session.add(strategy)

        db.session.commit()
        return redirect(url_for("admin.edit_trend", trend_id=trend_id))

    # GET 요청일 때 렌더링
    scenarios = Scenario.query.filter_by(trend_id=trend_id).all()
    strategies = StrategyCard.query.filter_by(trend_id=trend_id).all()

    return render_template(
        "admin_trend_edit.html",
        trend=trend,
        scenarios=scenarios,
        strategies=strategies
    )

@admin_bp.route("/admin/trends/new", methods=["GET", "POST"])
def create_trend():
    if request.method == "POST":
        title = request.form.get("title")
        summary = request.form.get("summary")

        new_id = f"t{Trend.query.count() + 1}"
        trend = Trend(id=new_id, title=title, summary=summary)
        db.session.add(trend)
        db.session.commit()

        return redirect(url_for("admin.edit_trend", trend_id=new_id))

    return render_template("admin_create.html")

```

## 📄 `app\views\auth.py`

```python
from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import db, User

auth_bp = Blueprint("auth", __name__)

# 🔑 로그인
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        user = User.query.filter_by(id=user_id).first()
        if user and user.password == password:
            session["user_id"] = user.id
            session["is_admin"] = user.is_admin
            return redirect(url_for("home.home"))
        else:
            return "❌ 로그인 실패: 아이디 또는 비밀번호가 틀렸습니다.", 401

    return render_template("login.html")

# 🆕 회원가입
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        # 중복 체크
        if User.query.get(user_id):
            return "이미 존재하는 아이디입니다.", 400

        # 사용자 생성
        new_user = User(id=user_id, password=password, is_admin=False)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("signup.html")

# 🚪 로그아웃
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))


```

## 📄 `app\views\home.py`

```python
from flask import Blueprint, render_template
from app.models import Trend, StrategyCard

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    trends = Trend.query.order_by(Trend.id.desc()).all()
    strategies = StrategyCard.query.order_by(StrategyCard.id.desc()).all()
    return render_template("home.html", trends=trends, strategies=strategies)

```

## 📄 `app\views\mypage.py`

```python
from flask import Blueprint, render_template, session

mypage_bp = Blueprint("mypage", __name__)

@mypage_bp.route("/mypage")
def mypage():
    user_id = session.get("user_id")
    is_admin = session.get("is_admin", False)

    if not user_id:
        return "로그인이 필요합니다", 401

    return render_template("mypage.html", user_id=user_id, is_admin=is_admin)

```

## 📄 `app\views\mypage_edit.py`

```python
from flask import Blueprint, render_template, session, request, redirect, url_for

mypage_edit_bp = Blueprint("mypage_edit", __name__)

@mypage_edit_bp.route("/mypage/edit", methods=["GET", "POST"])
def edit_profile():
    user_id = session.get("user_id")

    if not user_id:
        return "로그인이 필요합니다", 401

    if request.method == "POST":
        # 여기서 사용자 정보 수정 처리 (실제 DB 연동은 생략)
        return redirect(url_for("mypage.mypage"))

    return render_template("mypage_edit.html")

```

## 📄 `app\views\my_strategies.py`

```python
from flask import Blueprint, render_template, session
from app.models import UserStrategy

my_strategies_bp = Blueprint("my_strategies", __name__)

@my_strategies_bp.route("/mypage/strategies")
def mypage_strategies():
    user_id = session.get("user_id")

    if not user_id:
        return "로그인이 필요합니다", 401

    strategies = UserStrategy.query.filter_by(user_id=user_id).all()
    return render_template("mypage_strategies.html", strategies=strategies)

```

## 📄 `app\views\strategies.py`

```python
from flask import Blueprint, render_template, session
from app.models import StrategyCard, UserStrategy

strategies_bp = Blueprint("strategies", __name__)

@strategies_bp.route("/strategies")
def strategy_list():
    strategies = StrategyCard.query.all()
    return render_template("strategy_list.html", strategies=strategies)

@strategies_bp.route("/strategy/<strategy_id>")
def strategy_detail(strategy_id):
    strategy = StrategyCard.query.get(strategy_id)
    if not strategy:
        return "전략 카드를 찾을 수 없습니다.", 404

    user_id = session.get("user_id")
    already_selected = False

    if user_id:
        exists = UserStrategy.query.filter_by(user_id=user_id, strategy_id=strategy_id).first()
        already_selected = bool(exists)

    return render_template(
        "strategy_detail.html",
        strategy=strategy,
        already_selected=already_selected
    )
```

## 📄 `app\views\strategy_select.py`

```python
from flask import Blueprint, redirect, request, session, url_for
from app.models import db, StrategyCard, Trend, UserStrategy

strategy_select_bp = Blueprint("strategy_select", __name__)

@strategy_select_bp.route("/strategy/<strategy_id>/select", methods=["POST"])
def select_strategy(strategy_id):
    user_id = session.get("user_id")
    if not user_id:
        return "로그인이 필요합니다.", 401

    strategy = StrategyCard.query.get(strategy_id)
    if not strategy:
        return "전략 카드를 찾을 수 없습니다.", 404

    trend = strategy.trend  # 연결된 트렌드

    # 이미 선택했는지 확인
    exists = UserStrategy.query.filter_by(user_id=user_id, strategy_id=strategy_id).first()
    if exists:
        return redirect(url_for("my_strategies.mypage_strategies"))

    # 새로 추가
    new_strategy = UserStrategy(
        user_id=user_id,
        strategy_id=strategy_id,
        title=strategy.title,
        summary=strategy.summary,
        trend_title=trend.title
    )
    db.session.add(new_strategy)
    db.session.commit()

    return redirect(url_for("my_strategies.mypage_strategies"))

```

## 📄 `app\views\trends.py`

```python
from flask import Blueprint, render_template, request
from app.models import Trend

trends_bp = Blueprint("trends", __name__)

# 📄 트렌드 리스트
@trends_bp.route("/trends")
def trend_list():
    q = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()

    query = Trend.query.order_by(Trend.id.desc())

    # 🔍 검색 필터
    if q:
        query = query.filter(
            (Trend.title.ilike(f"%{q}%")) | 
            (Trend.summary.ilike(f"%{q}%"))
        )

    # ⛔ 카테고리 필터는 추후 확장
    trends = query.all()

    return render_template("trend_list.html", trends=trends)

# 📌 트렌드 상세 페이지
@trends_bp.route("/trend/<trend_id>")
def trend_detail(trend_id):
    trend = Trend.query.get(trend_id)
    if not trend:
        return "트렌드를 찾을 수 없습니다.", 404

    scenarios = trend.scenarios
    strategies = trend.strategies

    return render_template(
        "trend_detail.html",
        trend=trend,
        scenarios=scenarios,
        strategies=strategies
    )


```

## 📄 `app\views\__init__.py`

```python
from app.views.home import home_bp
from app.views.trends import trends_bp
from app.views.strategies import strategies_bp
from app.views.mypage import mypage_bp
from app.views.mypage_edit import mypage_edit_bp
from app.views.my_strategies import my_strategies_bp
from app.views.auth import auth_bp
from app.views.admin import admin_bp
from app.views.strategy_select import strategy_select_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(trends_bp)
    app.register_blueprint(strategies_bp)
    app.register_blueprint(mypage_bp)
    app.register_blueprint(mypage_edit_bp)
    app.register_blueprint(my_strategies_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(strategy_select_bp)
```

## 📄 `data\mock_trends.py`

```python
# 여기에 목업 트렌드/시나리오/전략 카드 데이터 정의
```

## 📄 `data\seed.py`

```python
import sys
import os
from pathlib import Path

# 루트 경로 등록
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app
from app.models import db, User, Trend, Scenario, StrategyCard

with app.app_context():
    print("📦 DB 테이블 생성 시작...")
    db.create_all()

    # ✅ 관리자 계정
    if not User.query.get("admin"):
        admin = User(id="admin", password="admin1234", is_admin=True)
        db.session.add(admin)
        print("✅ 관리자 계정 생성")

    # ✅ 트렌드 생성
    trend = Trend.query.get("t1")
    if not trend:
        trend = Trend(
            id="t1",
            title="생성형 AI의 확산",
            summary="GPT, Copilot 등 생성형 AI가 업무를 어떻게 바꾸는가?"
        )
        db.session.add(trend)
        db.session.flush()
        print("✅ 트렌드 생성")
    else:
        print("✅ 트렌드 이미 존재")

    # ✅ 시나리오들 생성
    scenarios = [
        {"id": "s1", "summary": "디자이너가 GPT에게 프로토타입 설계를 맡김"},
        {"id": "s2", "summary": "PM이 기획안 초안을 GPT로 자동 작성"},
    ]
    for s in scenarios:
        if not Scenario.query.get(s["id"]):
            scenario = Scenario(id=s["id"], summary=s["summary"], trend_id=trend.id)
            db.session.add(scenario)
            print(f"✅ 시나리오 생성: {s['id']}")

    db.session.flush()  # 시나리오 id들 바로 참조 위해

    # ✅ 전략 카드들 생성
    strategies = [
        {
            "id": "st1",
            "title": "1인 프로덕트 자동화",
            "summary": "Notion + GPT + Zapier 연동으로 자동 워크플로우 구성",
            "role_annotations": {
                "디자이너": "UI 프로토타입 자동 생성",
                "기획자": "브레인스토밍 결과 자동 문서화"
            },
            "scenario_id": "s1"
        },
        {
            "id": "st2",
            "title": "자동화된 기획서 작성 플로우",
            "summary": "PM이 요구사항 정리 후 GPT가 문서 초안 생성",
            "role_annotations": {
                "PM": "기획안 작성 시간 단축",
                "디자이너": "요구사항 자동 변환"
            },
            "scenario_id": "s2"
        }
    ]

    for st in strategies:
        if not StrategyCard.query.get(st["id"]):
            strategy = StrategyCard(
                id=st["id"],
                title=st["title"],
                summary=st["summary"],
                role_annotations=st["role_annotations"],
                trend_id=trend.id,
                scenario_id=st["scenario_id"]
            )
            db.session.add(strategy)
            print(f"✅ 전략 카드 생성: {st['id']}")

    db.session.commit()
    print("🎉 모든 목업 데이터 삽입 완료!")

```

## 📄 `migrations\env.py`

```python
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

## 📄 `migrations\README`

```
Generic single-database configuration.
```

## 📄 `migrations\script.py.mako`

```
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade schema."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade schema."""
    ${downgrades if downgrades else "pass"}

```

## 📄 `static\css\main.css`

```css
/* main.css */

/* 기본 폰트 설정 */
body {
    font-family: 'Pretendard', 'SUIT', sans-serif;
    font-size: 16px;
    letter-spacing: -0.015em;
    line-height: 1.7;
    color: #1e293b;  /* 진회색 계열 */
    background-color: #f8fafc;
  }
  
  /* 제목 폰트 커스터마이징 */
  h1, h2, h3, h4 {
    font-weight: 600;
    color: #0f172a;
    letter-spacing: -0.03em;
  }
  
  h1 {
    font-size: 2rem;
  }
  h2 {
    font-size: 1.5rem;
  }
  h3 {
    font-size: 1.25rem;
  }
  
  a {
    transition: all 0.2s ease;
  }
  
  a:hover {
    color: #38bdf8;
  }
  
```

## 📄 `static\js\filters.js`

```javascript
// 전략 카드 필터링 스크립트
```

## 📄 `templates\admin_create.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2 class="text-2xl font-bold text-gray-800 mb-4">🆕 새 트렌드 등록</h2>

<form method="POST" class="space-y-4">
  <input type="text" name="title" placeholder="트렌드 제목" required
         class="w-full border rounded px-4 py-2 text-sm text-gray-800">
  <textarea name="summary" placeholder="트렌드 요약" required
            class="w-full border rounded px-4 py-2 text-sm text-gray-800"></textarea>

  <button type="submit" class="bg-blue-600 text-white px-5 py-2 rounded text-sm hover:bg-blue-700">
    ➕ 등록하기
  </button>
</form>
{% endblock %}

```

## 📄 `templates\admin_dashboard.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2>🗂️ 관리자 승인 대시보드</h2>
<p>여기에 향후 승인 대기 콘텐츠, 전략 카드, GPT 결과 등이 표시될 예정입니다.</p>
{% endblock %}

```

## 📄 `templates\admin_review.html`

```html
{% extends 'layout.html' %}
{% block content %}
<h2>Admin Review</h2>
{% endblock %}
```

## 📄 `templates\admin_trend_edit.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2 class="text-2xl font-bold text-gray-800 mb-4">{{ trend.title }} 편집</h2>
<p class="text-gray-600 mb-6">{{ trend.summary }}</p>

<!-- 🧩 시나리오 추가 -->
<section class="mb-10">
  <h3 class="text-xl font-semibold mb-2">📌 시나리오 추가</h3>
  <form method="POST" class="space-y-2">
    <input type="hidden" name="form_type" value="scenario">
    <input type="text" name="scenario_summary" placeholder="시나리오 요약" class="w-full border rounded px-3 py-2 text-sm">
    <button type="submit" class="bg-blue-600 text-white px-4 py-1 rounded text-sm">➕ 추가</button>
  </form>

  <ul class="mt-4 space-y-1 text-sm text-gray-700">
    {% for s in scenarios %}
      <li>🔹 {{ s.summary }}</li>
    {% endfor %}
  </ul>
</section>

<!-- 🧠 전략 카드 추가 -->
<section>
  <h3 class="text-xl font-semibold mb-2">🧠 전략 카드 추가</h3>
  <form method="POST" class="space-y-2">
    <input type="hidden" name="form_type" value="strategy">
    <input type="text" name="strategy_title" placeholder="전략 제목" class="w-full border rounded px-3 py-2 text-sm">
    <textarea name="strategy_summary" placeholder="전략 요약" class="w-full border rounded px-3 py-2 text-sm"></textarea>
    <select name="strategy_scenario_id" class="w-full border rounded px-3 py-2 text-sm">
      <option value="">연결할 시나리오 선택 (선택)</option>
      {% for s in scenarios %}
        <option value="{{ s.id }}">{{ s.summary }}</option>
      {% endfor %}
    </select>
    <button type="submit" class="bg-blue-600 text-white px-4 py-1 rounded text-sm">➕ 추가</button>
  </form>

  <ul class="mt-4 space-y-1 text-sm text-gray-700">
    {% for s in strategies %}
      <li>🧠 {{ s.title }} ({{ s.scenario.summary if s.scenario else '시나리오 없음' }})</li>
    {% endfor %}
  </ul>
</section>
{% endblock %}

```

## 📄 `templates\home.html`

```html
{% extends "layout.html" %}
{% block content %}

<!-- 💬 Hero Section -->
<section class="bg-white rounded-xl shadow p-8 mb-10">
  <h1 class="text-3xl font-bold text-gray-900">전략은 선택이다.</h1>
  <p class="text-gray-600 mt-2">빠르게 변하는 세상에서, 전략 내비게이터는 트렌드와 역할별 전략을 안내합니다.</p>
  <a href="/trends" class="mt-4 inline-block bg-blue-600 text-white px-5 py-2 rounded-md text-sm font-medium hover:bg-blue-700 transition">
    🔍 트렌드 탐색 시작하기
  </a>
</section>

<!-- 📊 인기 트렌드 -->
<section class="mb-14">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-bold text-gray-900">🔥 지금 주목받는 트렌드</h2>
      <a href="/trends" class="text-blue-600 text-sm hover:underline">전체 보기 →</a>
    </div>
  
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {% for trend in trends[:3] %}
        <div class="bg-white rounded-2xl p-6 shadow hover:shadow-xl transition min-h-[220px] flex flex-col justify-between">
          <div>
            <h3 class="text-xl font-semibold text-gray-900 mb-1">{{ trend.title }}</h3>
            <p class="text-sm text-gray-600">{{ trend.summary[:100] }}...</p>
          </div>
          <a href="/trend/{{ trend.id }}" class="mt-4 inline-block text-blue-600 hover:underline text-sm font-medium">
            자세히 보기 →
          </a>
        </div>
      {% endfor %}
      {% if not trends %}
        <p class="text-sm text-gray-500">등록된 트렌드가 없습니다.</p>
      {% endif %}
    </div>
  </section>
  

<!-- 🧠 전략 카드 프리뷰 -->
<section class="mb-10">
  <h2 class="text-xl font-semibold text-gray-800 mb-4">최신 전략 카드</h2>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    {% for s in strategies[:2] %}
      <div class="bg-white rounded-xl p-5 shadow hover:shadow-lg transition">
        <h4 class="text-lg font-semibold text-gray-900">{{ s.title }}</h4>
        <p class="text-sm text-gray-600 mt-1">{{ s.summary[:100] }}...</p>
        <a href="/strategy/{{ s.id }}" class="mt-3 inline-block text-blue-600 hover:underline text-sm">카드 보기 →</a>
      </div>
    {% endfor %}
    {% if not strategies %}
      <p class="text-sm text-gray-500">전략 카드가 아직 없습니다.</p>
    {% endif %}
  </div>
</section>

<!-- 📌 내 전략 카드 (로그인 시) -->
{% if session.user_id %}
<section class="mb-10">
  <h2 class="text-xl font-semibold text-gray-800 mb-4">내 전략 카드</h2>
  <div class="bg-white rounded-lg p-5 text-sm text-gray-700">
    <p>내 전략 카드를 <a href="/mypage/strategies" class="text-blue-600 hover:underline">여기서 확인</a>하세요.</p>
  </div>
</section>
{% endif %}

<!-- 🛡️ 관리자 전용 안내 -->
{% if session.is_admin %}
<section class="mb-10">
  <h2 class="text-xl font-semibold text-gray-800 mb-4">🛡️ 관리자 권한</h2>
  <div class="bg-red-50 border border-red-200 rounded-lg p-5 text-sm text-red-700">
    <p>GPT가 자동 생성한 콘텐츠를 <a href="/admin" class="underline font-medium">검토하고 승인</a>해주세요.</p>
  </div>
</section>
{% endif %}

{% endblock %}

```

## 📄 `templates\layout.html`

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>전략 내비게이터</title>

  <!-- 메인 스타일 -->
  <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">

  <!-- 폰트 -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/suit-webfont@1.0.1/suit.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

  <!-- Tailwind -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Flowbite (선택사항) -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.5/flowbite.min.css" rel="stylesheet" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.5/flowbite.min.js"></script>

  <style>
    body {
      font-family: 'Inter', 'Pretendard', 'SUIT', sans-serif;
    }
  </style>
</head>
<body class="bg-[#0f172a] text-[#f8fafc] flex min-h-screen">

  <!-- ✅ 사이드바 -->
  <aside id="sidebar" class="w-64 bg-[#1e293b] p-6 flex flex-col gap-4 fixed h-full transition-transform duration-300">
    <h1 class="text-xl font-bold tracking-wide text-white">📍 NAVIGATOR</h1>
    <nav class="flex flex-col gap-3 text-sm mt-4">
      <a href="/" class="hover:text-blue-400">홈</a>
      <a href="/trends" class="hover:text-blue-400">트렌드</a>
      <a href="/strategies" class="hover:text-blue-400">전략 카드</a>
      <a href="/mypage" class="hover:text-blue-400">마이페이지</a>
      {% if session.is_admin %}
        <a href="/admin/trends/new" class="hover:text-blue-400">트렌드 등록</a>
      {% endif %}
    </nav>
  </aside>

  <!-- ✅ 사이드바 토글 버튼 -->
  <button id="toggleSidebar" class="fixed top-4 left-4 z-50 text-white bg-gray-800 hover:bg-gray-700 rounded-md p-2 focus:outline-none">
    ☰
  </button>

  <!-- ✅ 메인 콘텐츠 -->
  <main id="mainContent" class="ml-64 w-full p-10 relative bg-[#f5f5f5] text-[#1e293b] min-h-screen transition-all duration-300">
    <!-- 상단 사용자 정보 -->
    <div class="absolute top-6 right-10 space-x-4">
      {% if session.user_id %}
        <a href="/mypage" class="text-sm text-gray-700 hover:underline">👤 {{ session.user_id }}</a>
        <a href="/logout" class="text-sm text-gray-700 hover:underline">🔓 로그아웃</a>
      {% else %}
        <a href="/login" class="text-sm text-gray-700 hover:underline">🔐 로그인</a>
      {% endif %}
    </div>

    <!-- 페이지 내용 -->
    {% block content %}{% endblock %}
  </main>

  <!-- ✅ 토글 스크립트 -->
  <script>
    const toggleBtn = document.getElementById("toggleSidebar");
    const sidebar = document.getElementById("sidebar");
    const main = document.getElementById("mainContent");

    toggleBtn.addEventListener("click", () => {
      sidebar.classList.toggle("-translate-x-full");
      main.classList.toggle("ml-64");
    });

    // 초기화
    sidebar.classList.add("transition-transform", "duration-300");
    main.classList.add("transition-all", "duration-300");
  </script>
</body>
</html>





```

## 📄 `templates\login.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2>🔐 로그인</h2>
<form method="POST">
  <label>아이디</label><br>
  <input type="text" name="user_id" required><br><br>

  <label>비밀번호</label><br>
  <input type="password" name="password" required><br><br>

  <button type="submit">로그인</button>

<!-- 기존 login.html 하단에 추가 -->
<p class="mt-4 text-sm text-gray-500">계정이 없으신가요?
  <a href="/signup" class="text-blue-600 hover:underline">회원가입</a>
</p>

</form>
{% endblock %}

```

## 📄 `templates\mypage.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2>👤 마이페이지</h2>
<p>현재 로그인 중: {{ user_id }}</p>

{% if is_admin %}
  <p>🛡️ 관리자 계정입니다.</p>
  <p><a href="/admin">🗂️ 관리자 승인 페이지로 가기</a></p>
{% else %}
  <p><a href="/mypage/strategies">내 전략 카드 보기</a></p>
{% endif %}
{% endblock %}

```

## 📄 `templates\mypage_edit.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2>⚙️ 내 프로필 수정</h2>
<form method="POST">
  <label>내 역할/관심사/상황</label><br>
  <input type="text" name="profile_info"><br><br>
  <button type="submit">저장</button>
</form>
{% endblock %}

```

## 📄 `templates\mypage_strategies.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2>📌 내가 선택한 전략 카드</h2>
<ul>
  {% for s in strategies %}
    <li><strong>{{ s.title }}</strong> — {{ s.trend_title }}</li>
  {% else %}
    <li>선택한 전략 카드가 없습니다.</li>
  {% endfor %}
</ul>
{% endblock %}

```

## 📄 `templates\signup.html`

```html
{% extends "layout.html" %}
{% block content %}
<h2 class="text-xl font-bold text-gray-800 mb-4">🆕 회원가입</h2>

<form method="POST" class="space-y-4 max-w-sm">
  <div>
    <label class="block text-sm font-medium text-gray-700">아이디</label>
    <input type="text" name="user_id" required
           class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 text-sm" />
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700">비밀번호</label>
    <input type="password" name="password" required
           class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 text-sm" />
  </div>

  <button type="submit"
          class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm">
    회원가입 완료
  </button>
</form>

<p class="mt-4 text-sm text-gray-500">이미 계정이 있으신가요?
  <a href="/login" class="text-blue-600 hover:underline">로그인</a>
</p>
{% endblock %}

```

## 📄 `templates\strategy_detail.html`

```html
{% extends "layout.html" %}
{% block content %}

<!-- 🎯 전략 카드 요약 -->
<section class="bg-white rounded-xl shadow p-8 mb-10">
  <h2 class="text-2xl font-bold text-gray-900 mb-2">{{ strategy.title }}</h2>
  <p class="text-gray-700 text-sm">{{ strategy.summary }}</p>
</section>

<!-- 🧠 직군별 해석 -->
<section class="mb-12">
  <h3 class="text-xl font-semibold text-gray-800 mb-4">👥 직군별 해석</h3>

  {% if strategy.role_annotations %}
    <ul class="space-y-3">
      {% for role, comment in strategy.role_annotations.items() %}
        <li class="bg-gray-100 rounded-lg p-4 text-sm text-gray-700">
          <strong class="text-gray-900">{{ role }}</strong><br>
          <span>{{ comment }}</span>
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <p class="text-sm text-gray-500">📭 제공된 역할별 해석이 없습니다.</p>
  {% endif %}
</section>

<!-- ✅ 전략 선택 상태 확인 -->
<section class="mt-8">
  {% if session.user_id %}
    {% if already_selected %}
      <div class="flex items-center gap-2 bg-green-50 border border-green-300 text-green-700 px-4 py-3 rounded-md text-sm">
        ✅ 이 전략을 이미 선택했습니다.
      </div>
    {% else %}
      <form method="POST" action="/strategy/{{ strategy.id }}/select">
        <button type="submit"
                class="bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium px-6 py-2 rounded-md transition">
          ✅ 이 전략 선택하기
        </button>
      </form>
    {% endif %}
  {% else %}
    <p class="text-sm text-gray-500">
      🔐 전략 선택을 하려면 <a href="/login" class="text-blue-600 underline">로그인</a>하세요.
    </p>
  {% endif %}
</section>

{% endblock %}




```

## 📄 `templates\strategy_list.html`

```html
{% extends "layout.html" %}
{% block content %}

<h2 class="text-2xl font-bold text-gray-800 mb-6">전체 전략 카드</h2>

<!-- 🔍 필터링 영역 (선택 사항) -->
<!-- 추후 여기에 직군/상황별 필터 추가 가능 -->

<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
  {% for s in strategies %}
    <div class="bg-white p-6 rounded-xl shadow hover:shadow-lg transition">
      <h3 class="text-xl font-semibold text-gray-900">{{ s.title }}</h3>
      <p class="text-sm text-gray-600 mt-1">{{ s.summary[:100] }}...</p>
      <a href="/strategy/{{ s.id }}" class="mt-3 inline-block text-blue-600 hover:underline text-sm">카드 보기 →</a>
    </div>
  {% else %}
    <p class="text-sm text-gray-500">전략 카드가 없습니다.</p>
  {% endfor %}
</div>

{% endblock %}



```

## 📄 `templates\trend_detail.html`

```html
{% extends "layout.html" %}
{% block content %}

<!-- 🔷 트렌드 요약 -->
<section class="bg-white rounded-xl p-6 shadow-md mb-8">
  <h2 class="text-2xl font-bold text-gray-900">{{ trend.title }}</h2>
  <p class="mt-2 text-gray-600">{{ trend.summary }}</p>
</section>

<!-- 🧩 시나리오 목록 -->
<section class="mb-10">
  <h3 class="text-xl font-semibold text-gray-800 mb-3">시나리오</h3>
  <ul class="space-y-2">
    {% for s in scenarios %}
      <li class="bg-gray-100 rounded-md px-4 py-2 text-sm text-gray-700">
        {{ s.summary }}
      </li>
    {% else %}
      <li class="text-sm text-gray-500">시나리오 없음</li>
    {% endfor %}
  </ul>
</section>

<!-- 🧠 전략 카드 목록 -->
<section>
  <h3 class="text-xl font-semibold text-gray-800 mb-4">관련 전략 카드</h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
    {% for card in strategies %}
      <div class="bg-white rounded-xl p-5 shadow hover:shadow-lg transition">
        <h4 class="text-lg font-semibold text-gray-900">{{ card.title }}</h4>
        <p class="text-sm text-gray-600 mt-2">{{ card.summary }}</p>
        <a href="/strategy/{{ card.id }}" class="mt-4 inline-block text-blue-600 hover:underline text-sm font-medium">자세히 보기 →</a>
      </div>
    {% else %}
      <p class="text-sm text-gray-500">전략 카드 없음</p>
    {% endfor %}
  </div>
</section>

{% endblock %}



```

## 📄 `templates\trend_list.html`

```html
{% extends "layout.html" %}
{% block content %}

<h2 class="text-2xl font-bold text-gray-800 mb-6">📊 트렌드 리스트</h2>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
  {% for trend in trends %}
    <div class="bg-white p-6 rounded-xl shadow hover:shadow-lg transition">
      <h3 class="text-xl font-semibold text-gray-900">{{ trend.title }}</h3>
      <p class="text-sm text-gray-600 mt-1">{{ trend.summary[:100] }}...</p>
      <a href="/trend/{{ trend.id }}" class="mt-3 inline-block text-blue-600 hover:underline text-sm">자세히 보기 →</a>
    </div>
  {% else %}
    <p class="text-sm text-gray-500">등록된 트렌드가 없습니다.</p>
  {% endfor %}
</div>

<!-- 📌 탐색 툴바 -->
<form method="GET" action="/trends" class="mb-6 flex flex-col sm:flex-row sm:items-center gap-3">
  <input type="text" name="q" value="{{ request.args.get('q', '') }}" placeholder="트렌드를 검색하세요..."
         class="w-full sm:w-1/3 px-4 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" />

  <!-- 카테고리 필터 (향후 확장용) -->
  <select name="category" class="px-3 py-2 border border-gray-300 rounded-md text-sm">
    <option value="">전체 카테고리</option>
    <option value="ai">AI</option>
    <option value="design">디자인</option>
    <option value="automation">자동화</option>
    <!-- 향후 DB 기반 태그 연동 -->
  </select>

  <button type="submit" class="px-4 py-2 bg-blue-600 text-white text-sm rounded-md hover:bg-blue-700 transition">
    🔍 검색
  </button>
</form>

{% endblock %}

```

