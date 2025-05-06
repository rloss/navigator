from flask import Blueprint, render_template, request
from app.models import Trend

trends_bp = Blueprint("trends", __name__)

# 📄 트렌드 리스트
@trends_bp.route("/trends")
def trend_list():
    q = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()

    query = Trend.query.order_by(Trend.id.desc())

    # 🔍 검색 필터
    if q:
        query = query.filter(
            (Trend.title.ilike(f"%{q}%")) | 
            (Trend.summary.ilike(f"%{q}%"))
        )

    # ⛔ 카테고리 필터는 추후 확장
    trends = query.all()

    return render_template("trend_list.html", trends=trends)

# 📌 트렌드 상세 페이지
@trends_bp.route("/trend/<trend_id>")
def trend_detail(trend_id):
    trend = Trend.query.get(trend_id)
    if not trend:
        return "트렌드를 찾을 수 없습니다.", 404

    scenarios = trend.scenarios
    strategies = trend.strategies

    return render_template(
        "trend_detail.html",
        trend=trend,
        scenarios=scenarios,
        strategies=strategies
    )

