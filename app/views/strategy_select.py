from flask import Blueprint, redirect, request, session, url_for
from app.models import db, StrategyCard, Trend, UserStrategy

strategy_select_bp = Blueprint("strategy_select", __name__)

@strategy_select_bp.route("/strategy/<strategy_id>/select", methods=["POST"])
def select_strategy(strategy_id):
    user_id = session.get("user_id")
    if not user_id:
        return "로그인이 필요합니다.", 401

    strategy = StrategyCard.query.get(strategy_id)
    if not strategy:
        return "전략 카드를 찾을 수 없습니다.", 404

    trend = strategy.trend  # 연결된 트렌드

    # 이미 선택했는지 확인
    exists = UserStrategy.query.filter_by(user_id=user_id, strategy_id=strategy_id).first()
    if exists:
        return redirect(url_for("my_strategies.mypage_strategies"))

    # 새로 추가
    new_strategy = UserStrategy(
        user_id=user_id,
        strategy_id=strategy_id,
        title=strategy.title,
        summary=strategy.summary,
        trend_title=trend.title
    )
    db.session.add(new_strategy)
    db.session.commit()

    return redirect(url_for("my_strategies.mypage_strategies"))
