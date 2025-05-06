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

