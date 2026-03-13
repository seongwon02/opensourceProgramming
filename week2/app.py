from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI(title="오픈소스 프로그래밍 아카이브")
tils = []

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
    
        <hr>
        <a href="/create"><button style="padding: 10px; margin-right: 10px; cursor: pointer;">학습내용 기록하기</button></a>
        <a href="/list"><button style="padding: 10px; cursor: pointer;">작성한 기록 보기</button></a>
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
    list_html = ""
    for i, til in enumerate(tils):
        list_html += f'<li><a href="/til/{i}">{til["title"]}</a></li>\n'
    
    if not tils:
        list_html = "<li>아직 작성된 글이 없습니다. 첫 글을 작성해보세요!</li>"

    return f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>TIL 목록</title>
    </head>
    <body>
        <h1>📚 내 글 목록</h1>
        <ul>
            {list_html}
        </ul>
        <br>
        <a href="/create">새 글 작성하기</a> | <a href="/home">홈으로 돌아가기</a>
    </body>
    </html>
    """

@app.get("/til/{til_id}", response_class=HTMLResponse)
async def detail_page(til_id: int):
    # 만약 없는 번호의 글을 요청하면 에러를 보여줍니다.
    if til_id < 0 or til_id >= len(tils):
        return HTMLResponse("<h1>해당 글을 찾을 수 없습니다.</h1><br><a href='/list'>목록으로</a>", status_code=404)
        
    til = tils[til_id]
    
    return f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>{til["title"]}</title>
    </head>
    <body>
        <h1>{til["title"]}</h1>
        <p style="white-space: pre-wrap;">{til["content"]}</p>
        <br>
        <hr>
        <a href="/list">목록으로 돌아가기</a>
    </body>
    </html>
    """
    
@app.post("/submit")
async def submit_til(title: str = Form(...), content: str = Form(...)):
    # 1. 넘어온 제목과 내용을 딕셔너리 형태로 리스트에 저장합니다.
    tils.append({"title": title, "content": content})
    
    # 2. 저장이 끝나면 글 목록 페이지(/list)로 사용자를 강제로 이동시킵니다.
    return RedirectResponse(url="/list", status_code=303)