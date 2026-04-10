from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(
    title="오픈소스 프로그래밍 아카이브 API",
    description="TIL(Today I Learned)을 기록하고 관리하는 웹 애플리케이션의 자동화된 OpenAPI 문서입니다.",
    version="1.0.0",
    contact={
        "name": "Kim Seongwon"
    }
)

app = FastAPI(title="오픈소스 프로그래밍 아카이브 + TDD")
tils = []

templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))

# 홈 페이지 라우팅
@app.get("/", response_class=HTMLResponse, tags=["페이지 뷰"], summary="메인 홈 화면")
@app.get("/home", response_class=HTMLResponse, tags=["페이지 뷰"], include_in_schema=False)
async def home(request: Request):
    """
    사용자에게 메인 홈 화면을 렌더링하여 반환합니다.
    """
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/create", response_class=HTMLResponse, tags=["페이지 뷰"], summary="새 글 작성 화면")
async def create_page(request: Request):
    """
    새로운 학습 내용(TIL)을 기록할 수 있는 폼(Form) 페이지를 반환합니다.
    """
    return templates.TemplateResponse("create.html", {"request": request})
    
@app.get("/list", response_class=HTMLResponse, tags=["페이지 뷰"], summary="작성 글 목록 화면")
async def list_page(request: Request):
    """
    지금까지 작성된 모든 학습 기록의 목록을 렌더링합니다.
    """
    return templates.TemplateResponse("list.html", {"request": request, "tils": tils})

@app.get("/til/{til_id}", response_class=HTMLResponse, tags=["데이터 조회"], summary="개별 TIL 상세 조회")
async def detail_page(request: Request, til_id: int):
    """
    고유 ID(`til_id`)를 기반으로 특정 학습 기록의 상세 내용을 반환합니다.
    - 유효하지 않은 ID 요청 시 **404 에러** 페이지를 렌더링합니다.
    """
    if til_id < 0 or til_id >= len(tils):
        return HTMLResponse("<h1>해당 글을 찾을 수 없습니다.</h1><br><a href='/list'>목록으로</a>", status_code=404)

    til = tils[til_id]
    return templates.TemplateResponse("detail.html", {"request": request, "til": til})
    
# 3. 데이터 등록 API에 파라미터 설명 추가
@app.post("/submit", tags=["데이터 처리"], summary="새로운 TIL 저장 API")
async def submit_til(
    title: str = Form(..., description="학습 내용의 제목 (예: FastAPI 라우팅)"),
    content: str = Form(..., description="학습 내용의 상세 본문")
):
    """
    새로운 학습 기록을 메모리(리스트)에 저장합니다.
    
    - **title**: 빈 문자열이나 공백만 입력할 수 없습니다.
    - **content**: 상세 내용을 반드시 입력해야 합니다.
    - **에러**: 공백만 입력될 경우 400 Bad Request를 반환합니다.
    - **성공**: 처리가 완료되면 글 목록 페이지(`/list`)로 303 리다이렉트 됩니다.
    """
    if not title.strip() or not content.strip():
        raise HTTPException(status_code=400, detail="정상적인 입력이 아닙니다")

    tils.append({"title": title, "content": content})
    return RedirectResponse(url="/list", status_code=303)