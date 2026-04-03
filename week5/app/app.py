from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(title="오픈소스 프로그래밍 아카이브 + TDD")
tils = []

templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))

# 홈 페이지 라우팅
@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/create", response_class=HTMLResponse)
async def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})
    
@app.get("/list", response_class=HTMLResponse)
async def list_page(request: Request):
    return templates.TemplateResponse("list.html", {"request": request, "tils": tils})

@app.get("/til/{til_id}", response_class=HTMLResponse)
async def detail_page(request: Request, til_id: int):
    if til_id < 0 or til_id >= len(tils):
        return HTMLResponse("<h1>해당 글을 찾을 수 없습니다.</h1><br><a href='/list'>목록으로</a>", status_code=404)

    til = tils[til_id]
    return templates.TemplateResponse("detail.html", {"request": request, "til": til})
    
@app.post("/submit")
async def submit_til(title: str = Form(...), content: str = Form(...)):
    if not title.strip() or not content.strip():
        raise HTTPException(status_code=400, detail="정상적인 입력이 아닙니다")

    tils.append({"title": title, "content": content})
    return RedirectResponse(url="/list", status_code=303)
