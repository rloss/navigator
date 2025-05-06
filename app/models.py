from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Trend(db.Model):
    __tablename__ = "trend"
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    summary = db.Column(db.Text)
    scenarios = db.relationship("Scenario", backref="trend", lazy=True)
    strategies = db.relationship("StrategyCard", backref="trend", lazy=True)

class Scenario(db.Model):
    __tablename__ = "scenario"
    id = db.Column(db.String, primary_key=True)
    summary = db.Column(db.Text)
    trend_id = db.Column(db.String, db.ForeignKey("trend.id"))

class StrategyCard(db.Model):
    __tablename__ = "strategy_card"
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    summary = db.Column(db.Text)
    role_annotations = db.Column(db.JSON)
    trend_id = db.Column(db.String, db.ForeignKey("trend.id"))

class UserStrategy(db.Model):
    __tablename__ = "user_strategy"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    strategy_id = db.Column(db.String)
    title = db.Column(db.String)
    summary = db.Column(db.Text)
    trend_title = db.Column(db.String)
    selected_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.String, primary_key=True)  # 로그인용 ID
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
