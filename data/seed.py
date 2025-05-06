import sys
import os
from pathlib import Path

# 루트 경로 등록
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app
from app.models import db, User, Trend, Scenario, StrategyCard

with app.app_context():
    print("📦 DB 테이블 생성 시작...")
    db.create_all()

    # ✅ 관리자 계정
    if not User.query.get("admin"):
        admin = User(id="admin", password="admin1234", is_admin=True)
        db.session.add(admin)
        print("✅ 관리자 계정 생성")

    # ✅ 트렌드 생성
    trend = Trend.query.get("t1")
    if not trend:
        trend = Trend(
            id="t1",
            title="생성형 AI의 확산",
            summary="GPT, Copilot 등 생성형 AI가 업무를 어떻게 바꾸는가?"
        )
        db.session.add(trend)
        db.session.flush()
        print("✅ 트렌드 생성")
    else:
        print("✅ 트렌드 이미 존재")

    # ✅ 시나리오들 생성
    scenarios = [
        {"id": "s1", "summary": "디자이너가 GPT에게 프로토타입 설계를 맡김"},
        {"id": "s2", "summary": "PM이 기획안 초안을 GPT로 자동 작성"},
    ]
    for s in scenarios:
        if not Scenario.query.get(s["id"]):
            scenario = Scenario(id=s["id"], summary=s["summary"], trend_id=trend.id)
            db.session.add(scenario)
            print(f"✅ 시나리오 생성: {s['id']}")

    db.session.flush()  # 시나리오 id들 바로 참조 위해

    # ✅ 전략 카드들 생성
    strategies = [
        {
            "id": "st1",
            "title": "1인 프로덕트 자동화",
            "summary": "Notion + GPT + Zapier 연동으로 자동 워크플로우 구성",
            "role_annotations": {
                "디자이너": "UI 프로토타입 자동 생성",
                "기획자": "브레인스토밍 결과 자동 문서화"
            },
            "scenario_id": "s1"
        },
        {
            "id": "st2",
            "title": "자동화된 기획서 작성 플로우",
            "summary": "PM이 요구사항 정리 후 GPT가 문서 초안 생성",
            "role_annotations": {
                "PM": "기획안 작성 시간 단축",
                "디자이너": "요구사항 자동 변환"
            },
            "scenario_id": "s2"
        }
    ]

    for st in strategies:
        if not StrategyCard.query.get(st["id"]):
            strategy = StrategyCard(
                id=st["id"],
                title=st["title"],
                summary=st["summary"],
                role_annotations=st["role_annotations"],
                trend_id=trend.id,
                scenario_id=st["scenario_id"]
            )
            db.session.add(strategy)
            print(f"✅ 전략 카드 생성: {st['id']}")

    db.session.commit()
    print("🎉 모든 목업 데이터 삽입 완료!")
