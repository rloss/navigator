import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app
from app.models import db, Trend, Scenario, StrategyCard, User

with app.app_context():
    print("📦 DB 테이블 생성 시작...")
    db.create_all()

    # ✅ 관리자 계정
    if not User.query.get("admin"):
        admin = User(id="admin", password="admin1234", is_admin=True)
        db.session.add(admin)
        print("✅ 관리자 계정 생성")

    # ✅ 트렌드
    trend = Trend.query.get("t1")
    if not trend:
        trend = Trend(
            id="t1",
            title="생성형 AI의 확산",
            summary="GPT와 같은 AI 도구들이 업무에 어떤 영향을 미치는가?"
        )
        db.session.add(trend)
        db.session.flush()  # trend.id 바로 사용 가능하게
        print("✅ 트렌드 생성")

    # ✅ 시나리오
    if not Scenario.query.get("s1"):
        scenario = Scenario(
            id="s1",
            summary="디자이너가 직접 UI 안 만들고 GPT에게 요청",
            trend_id=trend.id
        )
        db.session.add(scenario)
        print("✅ 시나리오 생성")

    # ✅ 전략 카드
    if not StrategyCard.query.get("st1"):
        strategy = StrategyCard(
            id="st1",
            title="1인 자동화 플로우 만들기",
            summary="GPT + Notion + Zapier 연계로 자동화",
            role_annotations={
                "디자이너": "이미지 생성 자동화",
                "기획자": "문서 작성 자동화"
            },
            trend_id=trend.id
        )
        db.session.add(strategy)
        print("✅ 전략 카드 생성")

    db.session.commit()
    print("✅ DB 테이블 + 데이터 삽입 완료")
