from flask import Blueprint, render_template, session, request, redirect, url_for

mypage_edit_bp = Blueprint("mypage_edit", __name__)

@mypage_edit_bp.route("/mypage/edit", methods=["GET", "POST"])
def edit_profile():
    user_id = session.get("user_id")

    if not user_id:
        return "로그인이 필요합니다", 401

    if request.method == "POST":
        # 여기서 사용자 정보 수정 처리 (실제 DB 연동은 생략)
        return redirect(url_for("mypage.mypage"))

    return render_template("mypage_edit.html")
