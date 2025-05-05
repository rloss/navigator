from app import app
from app.models import db, Trend, Scenario, StrategyCard

with app.app_context():
    db.create_all()

    # 트렌드 1개 생성
    trend = Trend(
        id="trend1",
        title="생성형 AI의 업무 재편",
        summary="GPT 등 AI 도구의 확산이 일하는 방식을 어떻게 바꾸는가?"
    )
    db.session.add(trend)

    # 시나리오 2개
    s1 = Scenario(id="sc1", summary="기획자들이 PPT를 직접 만들지 않는다", trend=trend)
    s2 = Scenario(id="sc2", summary="1인 업무 자동화 도구 세팅이 일반화됨", trend=trend)
    db.session.add_all([s1, s2])

    # 전략 카드 1개
    strategy = StrategyCard(
        id="st1",
        title="나만의 AI 워크플로우 세팅하기",
        summary="GPT + Notion + Zapier를 엮어 일의 흐름을 자동화한다",
        role_annotations={"기획자": "보고서 자동화", "디자이너": "이미지 자동 생성 연계"},
        trend=trend
    )
    db.session.add(strategy)

    db.session.commit()
    print("✅ 목업 데이터 삽입 완료")
