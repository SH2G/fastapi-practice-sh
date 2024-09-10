# 가상 환경 설정
## 가상 환경 생성
python -m venv venv

## 가상 환경 활성화 (Windows)
venv\Scripts\activate

## 가상 환경 활성화 (macOS/Linux)
source venv/bin/activate

## 패키지 설치
pip install fastapi uvicorn
pip install sqlalchemy

# 실행
uvicorn app.main:app --reload --port 8080