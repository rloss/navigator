from flask import Blueprint, render_template, session

mypage_bp = Blueprint("mypage", __name__)

@mypage_bp.route("/mypage")
def mypage():
    user_id = session.get("user_id")

    if not user_id:
        return "로그인이 필요합니다", 401

    # 실제론 최근 전략 카드 몇 개만 보여줌
    return render_template("mypage.html", user_id=user_id)
