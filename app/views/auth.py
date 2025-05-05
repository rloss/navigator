from flask import Blueprint, render_template, request, redirect, session, url_for

auth_bp = Blueprint("auth", __name__)

# 임시 사용자 정보 (DB 없이)
FAKE_USERS = {
    "minki": "1234",  # user_id: password
    "admin": "adminpass"
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        if user_id in FAKE_USERS and FAKE_USERS[user_id] == password:
            session["user_id"] = user_id
            return redirect(url_for("home.home"))  # 로그인 성공 → 홈으로
        else:
            return "❌ 로그인 실패: 아이디 또는 비밀번호가 틀렸습니다.", 401

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))
