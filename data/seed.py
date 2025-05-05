from app import app
from app.models import db

with app.app_context():
    db.create_all()
    print("✅ DB 초기화 완료")
