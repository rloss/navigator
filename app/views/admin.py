from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import db, Trend, Scenario, StrategyCard
import uuid

admin_bp = Blueprint("admin", __name__)

# 관리자 대시보드
@admin_bp.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):
        return "접근 권한이 없습니다", 403
    return render_template("admin_dashboard.html")

# ✍️ 트렌드 작성 폼
@admin_bp.route("/admin/create", methods=["GET", "POST"])
def admin_create():
    if not session.get("is_admin"):
        return "접근 권한이 없습니다", 403

    if request.method == "POST":
        trend_title = request.form.get("title")
        trend_summary = request.form.get("summary")
        scenario_summary = request.form.get("scenario")
        strategy_title = request.form.get("strategy_title")
        strategy_summary = request.form.get("strategy_summary")
        role_annotations = {
            "디자이너": request.form.get("designer_note"),
            "기획자": request.form.get("planner_note")
        }

        # 트렌드 저장
        trend_id = "t_" + uuid.uuid4().hex[:6]
        trend = Trend(id=trend_id, title=trend_title, summary=trend_summary)
        db.session.add(trend)
        db.session.flush()  # trend.id 사용 가능

        # 시나리오 저장
        scenario = Scenario(
            id="s_" + uuid.uuid4().hex[:6],
            summary=scenario_summary,
            trend_id=trend.id
        )
        db.session.add(scenario)

        # 전략 카드 저장
        strategy = StrategyCard(
            id="st_" + uuid.uuid4().hex[:6],
            title=strategy_title,
            summary=strategy_summary,
            role_annotations=role_annotations,
            trend_id=trend.id
        )
        db.session.add(strategy)

        db.session.commit()
        return redirect(url_for("admin.admin_dashboard"))

    return render_template("admin_create.html")
