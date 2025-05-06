from flask import Blueprint, render_template, session
from app.models import StrategyCard, UserStrategy

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

    user_id = session.get("user_id")
    already_selected = False

    if user_id:
        exists = UserStrategy.query.filter_by(user_id=user_id, strategy_id=strategy_id).first()
        already_selected = bool(exists)

    return render_template(
        "strategy_detail.html",
        strategy=strategy,
        already_selected=already_selected
    )