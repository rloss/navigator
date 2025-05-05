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
