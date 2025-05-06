# 📄 reset_db.py

import sys
import os
from pathlib import Path

# 경로 설정
sys.path.append(str(Path(__file__).resolve().parent))

from app import app
from app.models import db

with app.app_context():
    print("⚠️ 모든 테이블 삭제 중... (기존 데이터 포함)")
    db.drop_all()
    print("✅ 테이블 삭제 완료.")

    print("📦 새로운 테이블 생성 중...")
    db.create_all()
    print("✅ DB 초기화 완료.")
