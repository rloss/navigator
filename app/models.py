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
