from flask import Blueprint, render_template, session

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):
        return "접근 권한이 없습니다", 403

    return render_template("admin_dashboard.html")
