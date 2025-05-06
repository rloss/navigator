import sys
import os
from pathlib import Path

# 루트 경로 추가
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app
from app.models import db, Trend, Scenario, StrategyCard, User

with app.app_context():
    print("📦 DB 테이블 생성 시작...")
    db.drop_all()  # 💥 모든 기존 테이블 제거 (주의)
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
        db.session.flush()  # ID 참조 가능하게
        print("✅ 트렌드 생성")

    # ✅ 시나리오들
    scenario_list = [
        Scenario(id="s1", summary="디자이너가 직접 UI 안 만들고 GPT에게 요청", trend_id=trend.id),
        Scenario(id="s2", summary="기획자가 서비스 구조를 GPT에게 요약시키는 흐름", trend_id=trend.id),
        Scenario(id="s3", summary="개발자가 코드 베이스 구조화 없이 GPT로 문서화", trend_id=trend.id),
    ]
    db.session.add_all(scenario_list)
    print("✅ 시나리오 3개 생성")

    # ✅ 전략 카드들 (시나리오와 직접 연결 ❌)
    strategy_list = [
        StrategyCard(
            id="st1",
            title="1인 자동화 플로우 만들기",
            summary="GPT + Notion + Zapier 연계로 자동화",
            role_annotations={
                "디자이너": "이미지 생성 자동화",
                "기획자": "문서 작성 자동화"
            },
            trend_id=trend.id
        ),
        StrategyCard(
            id="st2",
            title="기획 문서 요약 자동화",
            summary="GPT를 통해 피그마/문서/코드 기반 내용을 자동 정리",
            role_annotations={
                "기획자": "컨셉 회의 요약",
                "개발자": "API 정의서 생성"
            },
            trend_id=trend.id
        ),
    ]
    db.session.add_all(strategy_list)
    print("✅ 전략 카드 2개 생성")

    db.session.commit()
    print("✅ 전체 DB 삽입 완료")
