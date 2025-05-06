from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import db, Trend, Scenario, StrategyCard

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/trend/<trend_id>/edit", methods=["GET", "POST"])
def edit_trend(trend_id):
    trend = Trend.query.get(trend_id)
    if not trend:
        return "해당 트렌드가 존재하지 않습니다.", 404

    # POST 요청 시 새로운 시나리오 또는 전략 등록 처리
    if request.method == "POST":
        form_type = request.form.get("form_type")

        if form_type == "scenario":
            summary = request.form.get("scenario_summary")
            scenario = Scenario(summary=summary, trend_id=trend_id)
            db.session.add(scenario)

        elif form_type == "strategy":
            title = request.form.get("strategy_title")
            summary = request.form.get("strategy_summary")
            strategy = StrategyCard(
                title=title,
                summary=summary,
                trend_id=trend_id,
                role_annotations={}  # 기본값 비워두기
            )
            db.session.add(strategy)

        db.session.commit()
        return redirect(url_for("admin.edit_trend", trend_id=trend_id))

    # GET 요청일 때 렌더링
    scenarios = Scenario.query.filter_by(trend_id=trend_id).all()
    strategies = StrategyCard.query.filter_by(trend_id=trend_id).all()

    return render_template(
        "admin_trend_edit.html",
        trend=trend,
        scenarios=scenarios,
        strategies=strategies
    )

@admin_bp.route("/admin/trends/new", methods=["GET", "POST"])
def create_trend():
    if request.method == "POST":
        title = request.form.get("title")
        summary = request.form.get("summary")

        new_id = f"t{Trend.query.count() + 1}"
        trend = Trend(id=new_id, title=title, summary=summary)
        db.session.add(trend)
        db.session.commit()

        return redirect(url_for("admin.edit_trend", trend_id=new_id))

    return render_template("admin_create.html")

# admin.py (일부 추가)

# --- 트렌드 삭제 ---
@admin_bp.route("/admin/trend/<trend_id>/delete", methods=["POST"])
def delete_trend(trend_id):
    trend = Trend.query.get(trend_id)
    if not trend:
        return "해당 트렌드가 존재하지 않습니다.", 404

    db.session.delete(trend)
    db.session.commit()
    return redirect(url_for("trends.trend_list"))


# --- 시나리오 수정 ---
@admin_bp.route("/admin/scenario/<scenario_id>/edit", methods=["POST"])
def edit_scenario(scenario_id):
    scenario = Scenario.query.get(scenario_id)
    if not scenario:
        return "시나리오가 없습니다", 404

    new_summary = request.form.get("new_summary", "").strip()
    scenario.summary = new_summary
    db.session.commit()
    return redirect(url_for("admin.edit_trend", trend_id=scenario.trend_id))


# --- 시나리오 삭제 ---
@admin_bp.route("/admin/scenario/<scenario_id>/delete", methods=["POST"])
def delete_scenario(scenario_id):
    scenario = Scenario.query.get(scenario_id)
    if not scenario:
        return "시나리오가 없습니다", 404

    trend_id = scenario.trend_id
    db.session.delete(scenario)
    db.session.commit()
    return redirect(url_for("admin.edit_trend", trend_id=trend_id))


# --- 전략카드 삭제 ---
@admin_bp.route("/admin/strategy/<strategy_id>/delete", methods=["POST"])
def delete_strategy(strategy_id):
    strategy = StrategyCard.query.get(strategy_id)
    if not strategy:
        return "전략카드가 없습니다", 404

    trend_id = strategy.trend_id
    db.session.delete(strategy)
    db.session.commit()
    return redirect(url_for("admin.edit_trend", trend_id=trend_id))

@admin_bp.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):
        return "접근 권한이 없습니다", 403

    trends = Trend.query.all()
    strategies = StrategyCard.query.all()

    return render_template(
        "admin_dashboard.html",
        trends=trends,
        strategies=strategies
    )
