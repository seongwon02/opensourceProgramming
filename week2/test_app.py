from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_create_page():
    # 1. /create 경로로 GET 요청을 보냅니다.
    response = client.get("/create")
    
    # 2. 응답 코드가 200(정상)인지 확인합니다.
    assert response.status_code == 200
    
    # 3. 응답 HTML 코드 안에 "TIL 작성"이라는 단어가 포함되어 있는지 확인합니다.
    assert "학습 내용 작성" in response.text