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
        <p>오늘 수업에서 배운 것을 기록하고 성장하는 공간입니다. (FastAPI 기반)</p>
    </body>
    </html>
    """