from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="나의 개발자 TIL 아카이브")

# 홈 페이지 라우팅
@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>오픈소스 프로그래밍 아카이브</title>
    </head>
    <body>
        <h1>오픈소스 프로그래밍 아카이브</h1>
        <p>오늘 수업에서 배운 내용들을 기록하는 공간입니다. (FastAPI 기반)</p>
    </body>
    </html>
    """

@app.get("/create", response_class=HTMLResponse)
async def create_page():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>학습 내용 작성</title>
    </head>
    <body>
        <h1>✏️ 새로 배운 내용 기록하기</h1>
        <form action="/submit" method="post">
            <input type="text" name="title" placeholder="오늘의 학습 내용" required><br><br>
            <textarea name="content" rows="5" cols="30" placeholder="내용을 입력하세요" required></textarea><br><br>
            <button type="submit">저장하기</button>
        </form>
        <br>
        <a href="/home">홈으로 돌아가기</a>
    </body>
    </html>
    """
    
# main.py 파일 맨 아래에 추가

@app.get("/list", response_class=HTMLResponse)
async def list_page():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>TIL 목록</title>
    </head>
    <body>
        <h1>📚 내 글 목록</h1>
        <ul>
            <li><a href="/til/0">첫 번째 TIL 테스트 글</a></li>
            <li><a href="/til/1">두 번째 TIL 테스트 글</a></li>
        </ul>
        <br>
        <a href="/home">홈으로 돌아가기</a>
    </body>
    </html>
    """

@app.get("/til/{til_id}", response_class=HTMLResponse)
async def detail_page(til_id: int):
    return f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>학습내용 상세 보기</title>
    </head>
    <body>
        <h1>학습 내용 상세 보기</h1>
        <h2>글 번호: {til_id}</h2>
        <p>열심히 공부한 내용이 이곳에 표시됩니다.</p>
        <br>
        <a href="/list">목록으로 돌아가기</a>
    </body>
    </html>
    """