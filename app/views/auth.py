from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import db, User

auth_bp = Blueprint("auth", __name__)

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


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))

