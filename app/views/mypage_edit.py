from flask import Blueprint, render_template, session, request, redirect, url_for
from app.models import db, User

mypage_edit_bp = Blueprint("mypage_edit", __name__)

@mypage_edit_bp.route("/mypage/edit", methods=["GET", "POST"])
def edit_profile():
    user_id = session.get("user_id")
    if not user_id:
        return "로그인이 필요합니다", 401

    user = User.query.get(user_id)
    if not user:
        return "사용자를 찾을 수 없습니다", 404

    if request.method == "POST":
        user.role = request.form.get("role")
        user.interests = request.form.get("interests")
        user.situation = request.form.get("situation")
        db.session.commit()
        return redirect(url_for("mypage.mypage"))

    return render_template("mypage_edit.html", user=user)

