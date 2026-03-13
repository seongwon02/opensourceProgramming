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
    
def test_read_list_page():
    # /list 경로에 접속했을 때 200 정상 코드가 뜨고, "내 글 목록" 이라는 글자가 있어야 함
    response = client.get("/list")
    assert response.status_code == 200
    assert "내 글 목록" in response.text

def test_read_detail_page():
    # /til/0 경로(0번 글 상세)에 접속했을 때 "상세 보기" 라는 글자가 있어야 함
    response = client.get("/til/0")
    assert response.status_code == 200
    assert "상세 보기" in response.text