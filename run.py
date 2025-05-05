import os
import sys
from pathlib import Path

# 모듈 경로 인식 보장
sys.path.append(str(Path(__file__).resolve().parent))

from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render가 제공하는 포트 사용
    app.run(host="0.0.0.0", port=port, debug=True)
