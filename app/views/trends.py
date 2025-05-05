from flask import Blueprint, render_template
from app.models import Trend

trends_bp = Blueprint("trends", __name__)

@trends_bp.route("/trends")
def trend_list():
    trends = Trend.query.all()
    return render_template("trend_list.html", trends=trends)

@trends_bp.route("/trend/<trend_id>")
def trend_detail(trend_id):
    trend = Trend.query.get(trend_id)
    if not trend:
        return "트렌드를 찾을 수 없습니다.", 404

    scenarios = trend.scenarios
    strategies = trend.strategies

    return render_template("trend_detail.html", trend=trend, scenarios=scenarios, strategies=strategies)
