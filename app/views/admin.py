from flask import Blueprint, render_template, request, redirect, url_for
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
