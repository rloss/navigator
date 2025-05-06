from flask import Blueprint, render_template
from app.models import Trend, StrategyCard

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    trends = Trend.query.order_by(Trend.id.desc()).all()
    strategies = StrategyCard.query.order_by(StrategyCard.id.desc()).all()
    return render_template("home.html", trends=trends, strategies=strategies)
