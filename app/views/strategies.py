from flask import Blueprint, render_template
from app.models import StrategyCard

strategies_bp = Blueprint("strategies", __name__)

@strategies_bp.route("/strategies")
def strategy_list():
    strategies = StrategyCard.query.all()
    return render_template("strategy_list.html", strategies=strategies)

@strategies_bp.route("/strategy/<strategy_id>")
def strategy_detail(strategy_id):
    strategy = StrategyCard.query.get(strategy_id)
    if not strategy:
        return "전략 카드를 찾을 수 없습니다.", 404
    return render_template("strategy_detail.html", strategy=strategy)
