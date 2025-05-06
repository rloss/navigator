from flask import Blueprint, render_template, session
from app.models import db, User

mypage_bp = Blueprint("mypage", __name__)

@mypage_bp.route("/mypage")
def mypage():
    user_id = session.get("user_id")
    is_admin = session.get("is_admin", False)

    if not user_id:
        return "로그인이 필요합니다", 401

    return render_template("mypage.html", user_id=user_id, is_admin=is_admin)
