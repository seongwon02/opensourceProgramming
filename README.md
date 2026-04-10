# 📚 오픈소스 프로그래밍 아카이브 (Open Source Programming Archive)
> 수업에서 배운 내용을 체계적으로 기록하고 관리하는 FastAPI 기반 웹 애플리케이션

## 🖥️ Visual Demonstration
![alt text](image.png)
메인 페이지

![alt text](image-1.png)
학습내용 기록 페이지

![alt text](image-2.png)
학습내용 목록 페이지

![alt text](image-3.png)
학습내용 상세 페이지

## 🎯 Motivation & Problem
오픈소스 프로그래밍 수업에서 배운 다양한 개념(TDD, 리팩토링, 문서화)을 단순히 텍스트로 남기는 것을 넘어, 실제 동작하는 웹 애플리케이션에 적용하며 체득하기 위해 이 프로젝트를 시작했습니다. 단순한 하드코딩된 HTML 페이지에서 시작해, 점진적인 리팩토링을 거치며 지속 가능한 소프트웨어 구조가 무엇인지 탐구하고자 했습니다.

## 🛠️ Tech Stack & Rationale
* **Backend:** `FastAPI` (빠른 개발 속도와 Pydantic을 활용한 입력값 자동 검증 기능을 활용하기 위해 선택)
* **Template Engine:** `Jinja2` (비즈니스 로직과 UI 뷰를 분리하여 유지보수성을 높이기 위해 도입)
* **Testing:** `Pytest` (TDD 기반으로 견고한 애플리케이션을 작성하기 위해 사용)
* **Documentation:** `Sphinx` 및 `OpenAPI (Swagger)`

## ✨ Key Features
* **학습 내용 기록:** 오늘 배운 내용을 제목과 본문으로 나누어 저장 (공백 방지 등 입력 검증 적용)
* **기록 목록 조회:** 작성된 모든 학습 기록을 한눈에 볼 수 있는 리스트 제공
* **상세 보기 기능:** 각 항목을 클릭하여 자세한 내용 확인 가능
* **테스트 주도 개발(TDD):** 비정상적인 입력(공백 등)을 방어하는 꼼꼼한 테스트 코드 작성

## 🚀 Getting Started Guide
이 프로젝트를 로컬 환경에서 실행하는 방법입니다.

```bash
# 1. 저장소 클론
git clone [https://github.com/seongwon02/opensourceProgramming.git](https://github.com/seongwon02/opensourceProgramming.git)
cd opensourceProgramming/week6

# 2. 패키지 설치
pip install -r requirements.txt

# 3. 서버 실행
fastapi dev app/app.py
```

## 💡 Lessons Learned / Challenges
문제: 처음에는 단순히 사용자가 폼에 텍스트를 입력하면 무조건 리스트에 저장하도록 구현했습니다. 하지만 테스트 코드를 작성하는 과정(TDD)에서 사용자가 제목이나 본문에 '공백'만 입력하고 제출하는 엣지 케이스(Edge Case)를 발견하게 되었습니다.

해결 과정: 정상적인 기능 동작 여부만 확인하던 습관에서 벗어나, 실패하는 테스트 코드를 먼저 작성하고 이를 통과시키기 위해 .strip() 메서드를 활용한 입력 검증 로직과 400 Bad Request 예외 처리 로직을 추가했습니다. 이 과정을 통해 '코드가 돌아가는 것'에 만족하지 않고, '부서지지 않는 견고한 코드'를 짜는 사고방식을 기를 수 있었습니다.