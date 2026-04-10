from fastapi.testclient import TestClient
from app.app import app

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
    client.post("/submit", data={"title": "테스트", "content": "내용"})
    
    response = client.get("/til/0")
    assert response.status_code == 200
    assert "테스트" in response.text
    assert "내용" in response.text

# Lab2-TDD
# create_page 함수에 대한 테스트 코드 - 띄어쓰기만 입력했을 때 400 에러 테스트
def test_submit_with_whitespace_title_and_content():
    """제목과 본문이 모두 띄어쓰기만 포함된 경우 - 400 Bad Request 에러"""
    response = client.post("/submit", data={"title": "   ", "content": "   "})
    assert response.status_code == 400
    assert "정상적인 입력이 아닙니다" in response.text

def test_submit_with_whitespace_title_only():
    """제목만 띄어쓰기로 이루어진 경우 - 400 Bad Request 에러"""
    response = client.post("/submit", data={"title": "  ", "content": "정상적인 내용"})
    assert response.status_code == 400
    assert "정상적인 입력이 아닙니다" in response.text

def test_submit_with_whitespace_content_only():
    """본문만 띄어쓰기로 이루어진 경우 - 400 Bad Request 에러"""
    response = client.post("/submit", data={"title": "정상적인 제목", "content": "\t\n   "})
    assert response.status_code == 400
    assert "정상적인 입력이 아닙니다" in response.text

def test_submit_with_valid_input():
    """제목과 본문이 모두 정상적으로 입력된 경우 - 성공"""
    response = client.post("/submit", data={"title": "FastAPI 학습", "content": "FastAPI를 사용하여 웹 애플리케이션을 만드는 방법을 배웠습니다."}, follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/list"