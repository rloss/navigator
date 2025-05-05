import sys
import os
from pathlib import Path

# 현재 루트 경로를 PYTHONPATH에 넣기
sys.path.append(str(Path(__file__).resolve().parent))

from app import app

if __name__ == "__main__":
    app.run(debug=True)
