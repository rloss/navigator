import sys
import os
from pathlib import Path

# 현재 프로젝트 루트 경로를 import 경로에 추가
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app
from app.models import db, Trend, Scenario, StrategyCard

with app.app_context():
    print("📦 DB 테이블 생성 시작...")
    db.create_all()

    # ✅ 여기서 테스트용 더미 데이터 삽입
    trend = Trend(
        id="t1",
        title="생성형 AI의 확산",
        summary="GPT와 같은 AI 도구들이 업무에 어떤 영향을 미치는가?"
    )
    db.session.add(trend)

    scenario = Scenario(id="s1", summary="디자이너가 직접 UI 안 만들고 GPT에게 요청", trend=trend)
    strategy = StrategyCard(
        id="st1",
        title="1인 자동화 플로우 만들기",
        summary="GPT + Notion + Zapier 연계로 자동화",
        role_annotations={"디자이너": "이미지 생성", "기획자": "보고서 자동화"},
        trend=trend
    )
    db.session.add(scenario)
    db.session.add(strategy)

    db.session.commit()
    print("✅ DB 테이블 + 목업 데이터 삽입 완료")

from app.models import User

admin = User(id="admin", password="admin1234", is_admin=True)
db.session.add(admin)
