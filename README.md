# Gemini Enterprise 핸즈온 교육 포털 (Hands-on Class)

Google Gemini Enterprise를 활용한 실무 중심의 생성형 AI 핸즈온 교육 및 레퍼런스 가이드입니다. 

> [!TIP]
> **웹 포털로 실습하기**  
> 본 저장소는 순수 HTML/JS 기반의 독립 웹 애플리케이션을 제공합니다. [https://geap.dev](https://geap.dev)에 접속하거나 로컬 웹서버(`python3 -m http.server 8080`)를 실행하면 인터랙티브한 실습 환경(프롬프트 원클릭 복사, 이미지 줌 뷰어, 슬라이드 발표 모드)을 즉시 이용할 수 있습니다.

---

## 🧭 수준별 실습 교육 트랙

| 트랙 | 대상 및 난이도 | 주요 실습 주제 | MD 문서 | 웹 포털 실습 | 발표 슬라이드 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **🎯 오프닝 키노트** | 전사 임직원 · 리더십 | 전사 AI 도입 비전 및 4단계 성숙도 로드맵 | - | [🌐 geap.dev](https://geap.dev) | [📽️ Keynote 슬라이드](https://geap.dev/slide_v2.html) |
| **🟢 Track 1. Day 1 Value** | 전사 임직원 · 기획/마케팅 실무진<br>`입문 (No-Code)` | 웹 검색 그라운딩, 이미지/영상 생성, 엑셀/PPT 파일 분석, Canvas 슬라이드, CRAFT 프롬프트 | [📖 Track 1 가이드](track1_day1_value.md) | [🌐 Track 1 포털](https://geap.dev/track1.html) | [📽️ 슬라이드](https://geap.dev/slide_track1_v2.html) |
| **🔵 Track 2. Agentic Value** | 비즈니스 파워 유저 · 기획 리더<br>`중급 (No-Code Agent)` | Gemini Notebook(3종 인포그래픽, 팟캐스트, 시네마틱 슬라이드), Deep Research, Agent Designer, Workflow Agent | [📖 Track 2 가이드](track2_advanced.md) | [🌐 Track 2 포털](https://geap.dev/track2.html) | [📽️ 슬라이드](https://geap.dev/slide_track2_v2.html) |
| **🟣 Track 3. Knowledge & Connectors** | 클라우드 엔지니어 · 백엔드 개발자<br>`고급 (Pro-Code)` | Google Drive/Workspace 커넥터 연동, 사내 내규 RAG 검색, Python ADK 에이전트 개발, Cloud Run 배포 및 A2A 등록 | [📖 Track 3 가이드](track3_pro_code.md) | [🌐 Track 3 포털](https://geap.dev/track3.html) | [📽️ 슬라이드](https://geap.dev/slide_track3_v2.html) |
| **🔴 Track 4. Admin & Security** | IT 관리자 · CISO · 보안 조직<br>`고급 (Admin & Security)` | GCP 이중화 배포, Cloud Identity (WIF), 전사 제어판 튜닝, Model Armor 7대 보안 테스트, Cloud Audit Logs SQL 감사, Chrome 옴니바 연동 및 ROI | [📖 Track 4 가이드](track4_admin.md) | [🌐 Track 4 포털](https://geap.dev/track4.html) | [📽️ 슬라이드](https://geap.dev/slide_track4_v2.html) |

---

## 🚀 프롬프트 엔지니어링 프레임워크

업무 목적과 완성도에 따라 최적화된 프롬프트 작성 프레임워크를 활용합니다.

| 프레임워크 | 핵심 구성 요소 | 추천 활용 상황 |
| :--- | :--- | :--- |
| **C.R.A.F.T** | Context(맥락), Role(역할), Action(행동), Format(형식), Target(대상) | 복합 기획서, 대외 공식 커뮤니케이션, 상세 분석 보고서 |
| **A.P.E** | Action(지시), Purpose(목적), Expectation(기대수준) | 일상 업무, 빠른 초안 작성, 1회성 요약 요청 |
| **CO-STAR** | Context, Objective, Style, Tone, Audience, Response | 마케팅 카피, C-Level 보고, SNS 브랜드 포스팅 |

> [!NOTE]
> 상세 템플릿과 4대 실무 시나리오(제안 기획, CS 클레임, 보도자료, IT 장애 보고)는 [Track 1 프롬프트 가이드](track1_day1_value.md#18-프롬프트-작성법)에서 확인할 수 있습니다.

---

## 🏢 산업별 실무 시나리오

다양한 산업군의 실제 업무 문제를 해결하는 실습 시나리오가 각 트랙에 포함되어 있습니다.

- **🚗 자동차/모빌리티**: 글로벌 전기차 정책 변화를 실시간 검색하여 전략적 SWOT 분석 매트릭스 도출
- **🤖 로보틱스/제조**: 최신 기술 컨퍼런스 동향을 분석하여 경쟁사 대비 핵심 마케팅 메시지 수립
- **📢 마케팅/광고**: 브랜드 캠페인 포스터 이미지 생성 및 시네마틱 루프 영상 제작
- **☕ 소비재/유통**: 글로벌 커피 원두 매출 데이터를 다각도로 분석하고 시계열 트렌드 예측
- **☁️ IT/클라우드**: 대규모 기능 업데이트 문서를 요약하고 실무 적용 로드맵으로 구조화
- **🎓 교육/공공**: 플립러닝 수업 설계 및 국책 사업 기획안 자동 작성
- **🎮 게임/엔터**: 시즌 이벤트 콘텐츠 기획 및 퀘스트 시나리오 작성
- **🏢 엔터프라이즈 범용**: 뉴스 링크 입력만으로 SNS 게시물과 해시태그를 자동 생산하는 전용 에이전트 빌딩

---

## 📂 저장소 구조

```text
├── index.html               # 메인 교육 포털 홈 웹 애플리케이션 (https://geap.dev)
├── track1.html              # Track 1 웹 인터랙티브 가이드 (https://geap.dev/track1.html)
├── track2.html              # Track 2 웹 인터랙티브 가이드 (https://geap.dev/track2.html)
├── track3.html              # Track 3 웹 인터랙티브 가이드 (https://geap.dev/track3.html)
├── track4.html              # Track 4 웹 인터랙티브 가이드 (https://geap.dev/track4.html)
├── track1_day1_value.md     # Track 1 마크다운 원본 문서
├── track2_advanced.md       # Track 2 마크다운 원본 문서
├── track3_pro_code.md       # Track 3 마크다운 원본 문서
├── track4_admin.md          # Track 4 마크다운 원본 문서
├── img/                     # 전체 실습 스크린샷 및 UI 에셋
└── samples/                 # 실습용 샘플 파일 (엑셀, PPTX, PDF, Zip, CSV)
```

---

## 💻 로컬 실행 방법

별도의 빌드 도구 없이 Python 기본 웹서버로 즉시 실행할 수 있습니다.

```bash
# 1. 저장소 디렉토리로 이동
cd geap.dev

# 2. 로컬 웹 서버 실행
python3 -m http.server 8080

# 3. 브라우저에서 접속
# http://localhost:8080
```
