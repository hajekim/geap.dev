# 🔵 Track 2. Advanced — Agentic Value

> [!NOTE]
> **트랙 개요**: Gemini Notebook 팀 도서관 구축, Deep Research 자율 보고서, 에이전트 빌더를 활용한 맞춤형 AI로 업무 파이프라인을 직접 구성하는 중급 실습 과정입니다. Google Drive 커넥터 및 프로코드 커스텀 에이전트 개발 실습은 [Track 2 Plus](track2plus.md)를 참고하세요.

> [!TIP]
> **실습 첨부파일 다운로드**
> - [📦 설명서 실습용 이미지 패키지 (data_agent.zip)](samples/data_agent.zip)
> - [📦 시네마틱 슬라이드 실습용 이미지 (homestyle.zip)](samples/homestyle.zip)
> - [📄 Canvas 가이드 문서 (canvas.pdf)](samples/canvas.pdf)
> - [📦 Canvas 튜토리얼 비디오 패키지 (canvas.zip)](samples/canvas.zip)
> - [📽️ Track 2 강의 슬라이드 열기](slide_track2.html)

---

## 2.1. Gemini Notebook Enterprise

업로드한 문서(PDF, 텍스트, 이미지) 범위 내에서 질의응답을 진행하고, Gemini Notebook으로 슬라이드, 인포그래픽, 튜토리얼 동영상을 자동 생성하는 실습입니다. 다음 5가지 과제를 순서대로 진행합니다.

Gemini Enterprise App 좌측 메뉴 **Agents > Gemini Notebook**에서 진입합니다.

![Gemini Enterprise App 좌측 메뉴 — Agents > Gemini Notebook](./img/notebooklm_000.webp)

| 실습 | Gemini Notebook 기능 | 내용 |
| :--- | :--- | :--- |
| **실습 1** | **Infographic** | AI 인포그래픽 3종 스타일 변환 (Overview, Sketchnote, Newspaper) |
| **실습 2** | **Audio Overview** | AI 팟캐스트 자동 생성 (AI 진행자 2인 대화) |
| **실습 3** | **Slide Deck** | 제품 이미지 소스 → 시네마틱 슬라이드 자동 완성 |
| **실습 4** | **Slide Deck + Reports** | BigQuery Data Agent 설명서 (Study Guide, FAQ, Briefing Doc) |
| **실습 5** | **Video Overview** | Canvas 기능 튜토리얼 동영상 자동 제작 |

---

### 🎨 실습 1: Infographic — AI 인포그래픽 생성

아래 3가지 Google 제품 소개 문서를 소스로 등록하고, **인포그래픽 3종**을 각각 다른 스타일로 만들어봅니다.

#### 1단계: 노트북 준비 및 소스 등록

1. **새 노트북 생성**: Gemini Enterprise App 좌측 메뉴 **Agents → Gemini Notebook**에서 **새로만들기**를 클릭합니다.
2. **소스 타입 선택**: 소스 추가 패널에서 **텍스트 붙여넣기**를 선택합니다.

   ![텍스트 붙여넣기 소스 추가](./img/41.webp)

3. 아래 3가지 Google 제품 소개 문서를 **각각 개별 소스로 붙여넣기**합니다.

   ![소스 텍스트 붙여넣기 완료 상태](./img/42.webp)

**[소스 A] Google Gemini**
```markdown
# Google Gemini — 기업용 AI 어시스턴트 및 전사 지식 플랫폼

Google Gemini는 텍스트, 코드, 고해상도 이미지, 오디오, 비디오를 동시에 이해하는 네이티브 멀티모달 대형 언어 모델입니다. 최대 200만 토큰에 달하는 긴 컨텍스트 윈도우를 지원하여 수백 페이지의 기술 문서, 사규집, 대규모 코드베이스를 한 번에 분석하고 핵심 인사이트를 도출합니다.

주요 기능으로 실시간 Google 검색과 연결된 웹 그라운딩(Web Grounding)과 수백 개 소스를 자율 탐색하는 Deep Research를 통해 최신 시장 동향 리포트를 자동 생성합니다. 또한 Google Drive 커넥터를 통해 사내 문서와 내규를 권한(ACL) 기반으로 검색하여 정확한 출처와 함께 답변을 제공합니다.

보안 측면에서는 고객의 프롬프트와 사내 데이터가 모델 학습에 절대 사용되지 않습니다. 기업 전용 VPC 환경에서 데이터 주권을 완벽히 유지하며, Model Armor를 통해 개인정보(PII) 유출과 악성 프롬프트를 인라인으로 차단합니다. SOC 1/2/3, ISO/IEC 27001 등 국제 보안 표준 인증을 모두 충족합니다.

비즈니스 실무자를 위한 No-Code Agent Designer부터 개발자를 위한 Vertex AI API 및 ADK까지 폭넓게 제공하여, 단순 챗봇을 넘어 전사 업무를 자동화하는 커스텀 AI 에이전트 생태계를 구축할 수 있습니다.
```

**[소스 B] Google Workspace**
```markdown
# Google Workspace — AI 기반 차세대 스마트 협업 플랫폼

Google Workspace는 Gmail, Drive, Docs, Sheets, Slides, Meet, Calendar, Chat을 유기적으로 결합한 클라우드 업무 환경입니다. 모든 작업이 실시간으로 동기화되어 팀원들이 시공간 제약 없이 협업할 수 있습니다.

Gemini for Workspace는 개별 앱에 자연스럽게 녹아들어 업무 생산성을 극대화합니다. 각 앱 우측의 Gemini Side Panel을 통해 "지난주 회의록과 주고받은 메일을 종합하여 고객 제안서 초안을 작성해줘"와 같은 크로스 앱 멀티태스킹을 원클릭으로 수행합니다. Gmail과 Docs에서는 전문적인 비즈니스 문서를 빠르게 작성하고, Sheets에서는 자연어 질의만으로 복잡한 수식과 시각화 차트를 자동 생성합니다.

Google Meet은 38개 언어 실시간 통번역 자막과 스마트 회의록 생성을 지원하여 회의 직후 결정 사항과 액션 아이템을 자동 배포합니다. 또한 새로운 비디오 제작 툴인 Google Vids를 통해 기획서나 슬라이드 자료를 고품질 설명 영상으로 변환합니다.

기업 데이터 보호를 위해 클라이언트 측 암호화(CSE)와 엄격한 공유 정책을 제공하며, Google조차 고객의 암호화된 데이터에 접근할 수 없는 무신뢰(Zero-Trust) 보안 아키텍처를 실현합니다.
```

**[소스 C] Google Cloud**
```markdown
# Google Cloud — 엔터프라이즈 AI 혁신 및 인텔리전트 데이터 플랫폼

Google Cloud는 전 세계 40개 이상의 리전에서 확장성과 안정성을 보장하는 엔터프라이즈 인프라를 제공합니다. Google Kubernetes Engine(GKE)과 Cloud Run을 통해 컨테이너 기반 마이크로서비스와 AI 에이전트를 안정적으로 구동합니다.

Vertex AI는 기업용 생성형 AI 플랫폼입니다. Gemini 2.5를 비롯해 오픈소스 모델 등 150여 개 이상의 모델을 제공하는 Model Garden, 고정밀 사내 RAG 파이프라인, 그리고 오픈 에이전트 통신 규격인 A2A(Agent-to-Agent) 기반의 에이전트 빌더를 지원합니다. 커스텀 AI 가속기인 Cloud TPU v5e/v5p를 활용하여 대규모 AI 워크로드를 비용 효율적으로 운영합니다.

BigQuery는 페타바이트 규모의 데이터를 실시간 분석하는 서버리스 데이터 웨어하우스입니다. Conversational Analytics(CAA)를 통해 데이터 엔지니어가 아니더라도 자연어로 사내 원천 DB에 질의하여 정밀한 SQL 쿼리와 시각화 대시보드를 즉시 얻을 수 있습니다.

보안 체계는 Cloud Armor, Security Command Center, Chronicle SIEM으로 구성되어 다계층 위협 방어를 제공하며, VPC Service Controls(VPC-SC)를 통해 민감한 기업 데이터의 외부 유출 경로를 원천 차단합니다.
```

| 3개 소스 추가 완료 | 기본 질의응답 인터페이스 |
| :---: | :---: |
| ![총 세 개의 텍스트 소스](./img/notebooklm_003.webp) | ![기본 프롬프트](./img/notebooklm_001.webp) |

---

#### 2단계: 3종 스타일 인포그래픽 생성

1. **기본 인포그래픽 (Overview)**: 우측 Infographic 버튼의 점 세 개 메뉴를 클릭하고 프롬프트를 실행합니다.

   ![Infographic 버튼](./img/notebooklm_004.webp)

   ```markdown
   Google Workspace의 주요 앱과 각 앱에 통합된 Gemini AI 기능을 한눈에 정리한 인포그래픽을 만들어줘
   ```

   | 프롬프트 입력 | 생성 결과 |
   | :---: | :---: |
   | ![인포그래픽 프롬프트 입력](./img/notebooklm_005.webp) | ![기본 인포그래픽 생성 결과](./img/46.webp) |

   > [!TIP]
   > **화면 비율 안내**: 인포그래픽이 세로로 길게 보일 수 있습니다. **다운로드** 버튼으로 저장하면 16:9 가로 비율로 정상 출력됩니다.

2. **스케치노트 스타일 (Sketchnote)**: 동일한 생성 버튼을 눌러 다른 프롬프트를 입력합니다.

   ```markdown
   Google Gemini Enterprise의 핵심 기능과 실무 활용 시나리오를 스케치노트 스타일로 그려줘
   ```

   | 프롬프트 입력 | 스케치노트 스타일 결과 |
   | :---: | :---: |
   | ![인포그래픽 프롬프트 입력](./img/notebooklm_006.webp) | ![스케치노트 스타일 인포그래픽 결과](./img/47.webp) |

3. **신문 1면 스타일 (Newspaper Front-page)**: 퍼블리싱 톤의 결과물을 생성합니다.

   ```markdown
   Google Cloud Vertex AI와 BigQuery 기반 기업 AI 혁신 현황을 신문 1면 기사 스타일 인포그래픽으로 만들어줘
   ```

   | 프롬프트 입력 | 신문 1면 스타일 결과 |
   | :---: | :---: |
   | ![인포그래픽 프롬프트 입력](./img/notebooklm_007.webp) | ![신문 1면 스타일 인포그래픽 결과](./img/48.webp) |

---

### 🎙️ 실습 2: Audio Overview — AI 팟캐스트 자동 생성

동일 노트북 우측 **오디오 개요** 패널에서 **생성하기**를 클릭하면, AI 진행자 2인이 소스 문서 전체를 요약해 **5~8분 분량의 팟캐스트 오디오**를 자동 완성합니다.

| 오디오 패널 | 오디오 생성 결과 |
| :---: | :---: |
| ![Audio Overview](./img/notebooklm_008.webp) | ![Output: Audio Overview](./img/notebooklm_009.webp) |

> [!TIP]
> 팀 내 공유용으로 사용하거나, 이동 중 이어폰으로 문서 내용을 파악할 때 유용합니다. 생성된 오디오는 다운로드 후 사내 메신저나 이메일로 바로 배포할 수 있습니다.

---

### 🎬 실습 3: Slide Deck — 시네마틱 슬라이드 생성

제품 이미지만으로 Gemini Notebook이 영화 같은 시네마틱 슬라이드를 자동 생성합니다. 라이프스타일 브랜드 '홈스타일'의 신제품 이미지를 소스로 업로드하고, 브랜드 스토리를 붙여 시네마틱 슬라이드를 만듭니다.

#### 1단계: 실습 파일 준비
- [📥 homestyle.zip 받기](samples/homestyle.zip)
- 압축을 해제하면 `sofa.png`, `cushion.png`, `lighting.png`, `diffuser.png` 4장의 제품 이미지가 나옵니다.

![homestyle.zip](./img/notebooklm_010.webp)

#### 2단계: 새 노트북 생성 및 이미지 업로드
1. Gemini Enterprise App 좌측 메뉴 **Agents → Gemini Notebook**에서 **새로만들기**를 클릭합니다.
2. **소스 추가 → 파일 업로드**를 선택하고 이미지 4장을 한꺼번에 업로드합니다.

![Gemini Notebook 이미지 소스 4장 업로드 완료](./img/notebooklm_011.webp)

#### 3단계: 브랜드 스토리 텍스트 추가
**소스 추가 → 텍스트 붙여넣기**를 선택하고, 아래 텍스트를 복사해 붙여넣은 뒤 소스 이름을 **story**로 저장합니다.

```markdown
### **스토리**

**Scene 1. 햇살이 가득한 주말 오후**
* **배경:** 따뜻한 햇살이 큰 창을 통해 가득 들어오는, 밝고 화사한 톤의 모던한 거실.
* **오브젝트 배치:** 거실 중심에 브라운 가죽 소파인 sofa.png가 놓여 있고, 그 위로 창밖의 햇살이 부드럽게 내리쥡니다. 소파 위에는 화사한 오렌지색 기하학 패턴의 cushion.png들이 자연스럽게 놓여 있습니다. 소파 옆으로는 은은한 반투명 전등갓의 플로어 램프 lighting.png가 서 있고, 소파 앞 작은 테이블 위에는 영롱하게 빛나는 핑크색 디퓨저 diffuser.png가 놓여 있습니다.
* **스토리:** 주말 오후, 상쾌한 기분으로 주인공이 거실로 들어와 햇살을 받으며 소파 쪽으로 천천히 걸어갑니다.

**Scene 2. 포근한 소파에서의 시작 (sofa.png)**
* **배경:** 햇살이 가득 찬 화사한 거실.
* **오브젝트 배치:** 주인공이 햇살을 가득 머금은 sofa.png 브라운 가죽 소파에 몸을 포근하게 맡깁니다. 소파의 넓고 유연한 가죽 질감이 소파를 중심으로 거실 공간 전체와 자연스럽게 어우러져 화면에 담깁니다.
* **스토리:** 주인공이 소파에 기대어 편안한 표정으로 숨을 고릅니다. 소파는 거실의 중심에서 가장 따뜻하고 포근한 안식처의 역할을 합니다.

**Scene 3. 경쾌한 포인트 쿠션 (cushion.png)**
* **배경:** 소파에 앉아 편안히 휴식을 취하는 주인공의 모습.
* **오브젝트 배치:** 주인공이 포근한 소파 위에서 오렌지색 기하학 패턴의 cushion.png 쿠션을 가볍게 끌어안거나 기대고 있습니다.
* **스토리:** 주인공이 자연스럽게 옆에 있던 오렌지색 쿠션 하나를 품에 끌어안습니다. 선명한 패턴과 색감이 거실 분위기를 한층 더 감각적이고 상쾌하게 변화시킵니다.

**Scene 4. 공간을 채우는 부드러운 빛 (lighting.png)**
* **배경:** 턴을 넘기듯 자연스럽게 이어지는 거실 공간.
* **오브젝트 배치:** 주인공이 소파에 앉은 채로 손을 뻗어, 소파 옆에 자연스럽게 배치된 lighting.png 플로어 램프를 켭니다. 은은하고 부드러운 유백색 빛이 자연 채광과 섞여 거실 전체를 한층 더 아늑하게 감싸 안습니다.
* **스토리:** 조명의 따스한 불빛이 들어오면서 공간의 입체감이 살아나고, 거실 전체 인테리어가 더욱 세련되고 완성도 높게 연출됩니다.

**Scene 5. 감각을 깨우는 상쾌한 향기 (diffuser.png)**
* **배경:** 소파 앞 테이블과 거실 전체가 흐릿하게(아웃포커싱) 잡히는 구도.
* **오브젝트 배치:** 카메라 시선이 소파 앞 테이블 위에 놓인 diffuser.png 핑크색 디퓨저를 향합니다. 디퓨저는 햇살과 램프 빛을 동시에 받아 영롱하게 반짝이며 공간의 오브젝트들과 완벽한 톤앤매너를 이룹니다.
* **스토리:** 공기 중으로 디퓨저의 상쾌한 향이 은은하게 퍼지는 듯한 연출과 함께, 쿠션을 안고 소파에 기댄 주인공이 편안하게 눈을 감으며 주말의 완벽한 휴식을 만끽합니다.

**Scene 6. 완벽한 휴식의 공간 (엔딩)**
* **배경:** 모든 아이템이 조화롭게 어우러진 전체 거실 전경.
* **오브젝트 배치:** 카메라가 천천히 뒤로 물러나며(줌아웃), sofa.png 소파 위에 cushion.png 쿠션을 안고 햇살을 받으며 누운 주인공, 그 옆을 따뜻하게 비추는 lighting.png 램프와 상쾌한 무드를 더하는 diffuser.png까지 완벽하게 어우러진 화사한 거실의 전체 인테리어를 잡습니다.
* **스토리:** 잘 정돈된 아름다운 공간 속에서 오감으로 완성된 나만의 안식처를 보여주며 상쾌하게 마무리됩니다.
```

| 텍스트 소스 입력 | 소스 5개 등록 완료 |
| :---: | :---: |
| ![Gemini Notebook 텍스트 소스 입력](./img/notebooklm_012.webp) | ![Gemini Notebook 소스는 총 다섯개](./img/notebooklm_013.webp) |

#### 4단계: 시네마틱 슬라이드 생성 및 다운로드

노트북 우측 **슬라이드 자료** 패널에서 customize 옵션을 선택하고 프롬프트를 실행합니다.

```markdown
스토리에 맞는 시네마틱 슬라이드를 만들어줘, 타이틀, 텍스트, 자막, 설명 등은 포함하지 마
```

| 슬라이드 패널 | 프롬프트 입력 |
| :---: | :---: |
| ![슬라이드 자료](./img/notebooklm_014.webp) | ![슬라이드 생성 입력](./img/notebooklm_015.webp) |

| 생성 진행 중 | 슬라이드 완성 화면 |
| :---: | :---: |
| ![슬라이드 생성을 하는 중](./img/notebooklm_016.webp) | ![슬라이드 생성 완료](./img/notebooklm_017.webp) |

| 다운로드 옵션 선택 | PPTX 다운로드 |
| :---: | :---: |
| ![슬라이드 받을까 말까](./img/notebooklm_018.webp) | ![슬라이드 받을까 말까](./img/notebooklm_019.webp) |

- [📊 완성된 슬라이드 PPTX 다운로드 (Cinematic Sanctuary.pptx)](samples/Cinematic%20Sanctuary.pptx)
- [📄 완성된 슬라이드 PDF 다운로드 (Cinematic Sanctuary.pdf)](samples/Cinematic%20Sanctuary.pdf)

---

### 📖 실습 4: Slide Deck + Reports — 설명서 만들기

새로운 노트북을 생성하고 `data_agent.zip`의 이미지 10개를 소스로 업로드합니다. **슬라이드 Customize**로 가이드 문서를 생성하고, Studio의 **Reports** 기능으로 스터디 가이드, FAQ, 브리핑 문서를 제작합니다.

1. **소스 업로드**: `data_agent.zip` 압축 해제 후 이미지 10개를 소스에 추가합니다.

   ![10개의 파일을 업로드 완료](./img/notebooklm_020.webp)

2. **슬라이드 가이드 생성**: 슬라이드 Customize 버튼을 클릭하고 아래 프롬프트를 실행합니다.
   ```markdown
   BigQuery Data Agent를 생성하는 과정을 초보자도 쉽게 따라할 수 있도록 가이드 문서를 작성해줘
   ```

   | 프롬프트 입력 | 가이드 슬라이드 결과 |
   | :---: | :---: |
   | ![슬라이드 Customize 프롬프트 입력](./img/notebooklm_021.webp) | ![결과물](./img/notebooklm_022-a.webp) |

3. **3대 보고서 자동 생성 (Reports)**:

   ![Reports 메뉴](./img/notebooklm_029.webp)

   | 스터디 가이드 (Study Guide) | FAQ (자주 묻는 질문) | 브리핑 문서 (Briefing Doc) |
   | :---: | :---: | :---: |
   | ![Study guide](./img/notebooklm_030.webp) | ![FAQ](./img/notebooklm_031.webp) | ![Briefing doc](./img/notebooklm_032.webp) |

---

### 🎬 실습 5: Video Overview — Canvas 튜토리얼 동영상 제작

PDF 문서와 UI 스크린샷 이미지를 소스로 업로드하여 Canvas 사용법을 설명하는 튜토리얼 동영상을 자동 생성합니다.

#### 1단계: 실습 파일 준비
- [📄 Canvas 가이드 문서 (canvas.pdf)](samples/canvas.pdf)
- [📦 Canvas UI 스크린샷 이미지 모음 (canvas.zip)](samples/canvas.zip)

#### 2단계: 소스 업로드 및 비디오 생성
1. Gemini Notebook에서 `canvas.pdf`와 `canvas.zip` 내 스크린샷 이미지들을 한꺼번에 업로드합니다.

   ![canvas.pdf + 스크린샷 이미지 소스 추가 완료](./img/notebooklm_023.webp)

2. Video Overview의 **Customize** 버튼을 클릭하고 아래 프롬프트를 실행합니다.
   ```markdown
   Gemini Enterprise에서 Canvas를 사용하는 방법을 초보자도 따라가기 쉽게 차근차근 설명하는 동영상을 만들어줘
   ```

   | 영상 커스터마이즈 | 프롬프트 입력 |
   | :---: | :---: |
   | ![영상 커스터마이즈 생성](./img/notebooklm_024.webp) | ![영상 생성을 위한 프롬프트 입력](./img/notebooklm_025.webp) |

3. 완성된 튜토리얼 동영상을 확인합니다.

   | 씬 1 | 씬 2 | 씬 3 |
   | :---: | :---: | :---: |
   | ![결과 1](./img/notebooklm_026.webp) | ![결과 2](./img/notebooklm_027.webp) | ![결과 3](./img/notebooklm_028.webp) |

---

## 2.2. Deep Research Agent

복잡한 연구 주제를 하위 질문으로 분해하고, 웹과 기업 내부 문서를 다단계로 자율 탐색해 인용 출처가 명시된 종합 보고서를 만드는 에이전트입니다.

| 항목 | 내용 |
| :--- | :--- |
| **검색 횟수** | 표준 약 80회, Deep Research Max 최대 160회 |
| **소요 시간** | 일반적으로 3~8분 |
| **소스** | 웹, 기업 내부 앱 데이터, Drive, Gmail |
| **출력물** | 목차 및 인용 링크 포함 마스터 보고서 + 오디오 브리핑 요약 |

1. **에이전트 실행**: 좌측 메뉴에서 **Deep Research**를 클릭하고 프롬프트를 실행합니다.

   ![Deep Research 에이전트 진입](./img/34.webp)

   ```markdown
   현재 글로벌 스마트 오피스 IoT 및 디지털트윈 솔루션 시장의 기술 트렌드와 주요 경쟁사 동향을 종합적으로 분석해 줘. 넥스트 테크놀로지스가 속한 오피스 테크 산업의 핵심 경쟁 우위 요소를 도출하고 향후 직면할 기회와 위협 요인을 논리적으로 설명해 줘
   ```

2. **완성 보고서 검토**:

   | 보고서 목차 및 인용 링크 | 세부 분석 결과 |
   | :---: | :---: |
   | ![Deep Research 분석 보고서 생성 결과 1](./img/32.webp) | ![Deep Research 분석 보고서 생성 결과 2](./img/33.webp) |

---

## 2.3. Agent Designer

코드 없이 클릭 몇 번으로 업무에 특화된 AI 에이전트를 직접 만들고 팀원들과 공유합니다.

### 1) 에이전트 종류와 실무 활용 예시

- **No-Code 에이전트**: Agent Designer에서 자연어로 규칙과 대상을 설계하는 임직원용 간편 에이전트.
- **Low-Code 에이전트**: 시각적인 노드 기반 흐름 빌더(Flow Builder)와 트리거, 승인 단계 레이아웃을 통해 제작하는 업무 에이전트.
- **High-Code 에이전트**: 개발자 전용 프레임워크인 ADK(Agent Development Kit)를 사용해 Python 코드로 백엔드 API와 레거시 시스템 트랜잭션을 연동하는 고급 에이전트.

![Agent Designer 전체 UI 구조](./img/image9.webp)

---

### 2) 실전 실습: CRAFT 프롬프트 에이전트 만들기

1. **New Agent**를 클릭하고 Chat Pane에 아래 설계 요구 명세를 입력합니다.

   | Agents 메뉴 진입 | New Agent 클릭 |
   | :---: | :---: |
   | ![Agents 메뉴 진입](./img/agentdesigner-008.webp) | ![New Agent 버튼 클릭](./img/agentdesigner-001.webp) |

   ```markdown
   사용자가 작성한 프롬프트를 Gemini에 사용하기 좋도록 아래 CRAFT 프레임워크 기반으로 프롬프트를 재작성합니다. 작성하기 위해 너(Gemini)에게 어떤 정보가 필요한지 나에게 질문하여 얻습니다.

   ### [CRAFT 프레임워크]
   - Context (맥락): 상황을 파악할 수 있도록 배경지식, 목적, 비즈니스 환경을 제공합니다.
   - Role (역할): 구체적인 직업, 연차, 정체성을 부여하여 전문적인 페르소나를 활성화합니다.
   - Action (행동): 수행해야 할 핵심 작업이나 미션을 명확한 동사로 지시합니다.
   - Format (출력 형식): 보고서, 이메일, 표, 불릿포인트 등 원하는 결과물의 구조를 지정합니다.
   - Tone / Target (타겟 및 어조): 답변의 최종 소비자를 정의하고 전문적, 친근함 등의 톤앤매너를 설정합니다.
   ```

2. **Flow Builder 확인 및 Preview 테스트**:

   | 명세 입력 | Flow Builder 편집 |
   | :---: | :---: |
   | ![설계 요구 명세 입력](./img/agentdesigner-002.webp) | ![Flow Builder 화면](./img/agentdesigner-003.webp) |

   | Preview 테스트 | Create 배포 |
   | :---: | :---: |
   | ![Preview 테스트](./img/agentdesigner-004.webp) | ![Create 배포](./img/agentdesigner-005.webp) |

   | 배포 후 옵션 | 배포된 에이전트 채팅 |
   | :---: | :---: |
   | ![배포 후 선택 화면](./img/agentdesigner-006.webp) | ![배포된 에이전트 채팅](./img/agentdesigner-007.webp) |

3. 생성된 에이전트는 **Your Agents** 목록에서 확인할 수 있습니다.

   ![Your Agents 목록](./img/agentdesigner-009.webp)

---

### 3) 실전 실습: 뉴스 링크 기반 SNS 마케팅 포스팅 자동 빌더

1. 에이전트 디자이너 왼쪽 대화창에 아래 프롬프트를 입력합니다.
   ```markdown
   뉴스 링크를 입력 받아서 Social Media 포스팅할 게시물 문구를 생성하는 에이전트를 만들어줘. 포스팅할 문구는 간략한 한줄 문장과 bullet point 5개를 생성하고 Hashtag도 추천해줘.
   ```

   ![에이전트 디자이너 프롬프트 입력](./img/image53.webp)

2. 우측 Flow를 검토한 뒤 **Create** 버튼을 클릭하여 적용합니다.

   ![디자이너 Flow 및 상세 설정](./img/image78.webp)

3. 프리뷰 테스트 창에 뉴스 기사 링크를 붙여넣어 결과를 테스트합니다.
   ```markdown
   이 뉴스 링크로 소셜 미디어 게시물을 만들어줘: https://news.next-tech.com/smart-office-iot-2026/
   ```

   | 프리뷰 테스트 | 출력 화면 |
   | :---: | :---: |
   | ![에이전트 프리뷰 뉴스 테스트](./img/image14.webp) | ![테스트 성공 출력화면](./img/image70.webp) |

4. **Agent Gallery**에 발행하여 사내 구성원들과 공유합니다.

   ![에이전트 공유 시작](./img/image23.webp)

---

## 2.4. Workflow Agent

엄격한 순서와 비즈니스 로직이 필요한 업무를 자동화하는 멀티 에이전트 워크플로우 실습입니다.

### 1) 실무 활용: 글로벌 시장 조사 에이전트

1. **New Agent > Workflow Agent**를 클릭합니다.

   ![Workflow Agent 생성 메뉴](./img/workflowagent-010.webp)

2. Chat Pane에 아래 설계 프롬프트를 입력합니다.
   ```markdown
   역할: 당신은 글로벌 시장 조사 및 경쟁 분석 전문 수석 전략 컨설턴트 에이전트입니다.
   목적: 사용자가 특정 산업군, 기업명 또는 기술 분야를 제시하면 내장된 Web Grounding 검색 기능을 활용하여 최신 동향을 수집하고, 단계별 분석을 거쳐 경영진 보고서 형태의 종합 리포트를 자동 작성합니다.

   작업 워크플로우 단계:
   Step 1. 정보 수집 및 검증 (Web Grounding)
     - 사용자가 제시한 주제 또는 기업에 대해 최신(최근 6개월 내) 시장 동향, 주요 기술 혁신, 경쟁 구도를 실시간 웹 검색을 통해 수집하세요.
   Step 2. 다각도 전략 분석 (Multi-angle Analysis)
     - 수집된 정보를 바탕으로 다음 4가지 핵심 영역을 분석하세요:
       1. 시장 성장 동인 및 주요 이슈 (Market Drivers & Key Trends)
       2. 주요 경쟁사별 핵심 전략 비교 (Competitor Comparison)
       3. SWOT 분석 (강점, 약점, 기회, 위협)
       4. 향후 1~3년 시장 전망 (Market Outlook)
   Step 3. 경영진 요약 및 시각적 리포트 작성 (Executive Reporting)
     - 아래 구성을 엄격히 준수하여 마크다운 표와 구조화된 개조식 문서로 응답하세요:
     - Executive Summary (3줄 요약)
     - 경쟁사 비교 분석표 (기업명, 핵심 기술/제품, 시장 점유율/강점, 최근 행보)
     - 시사점 및 대응 전략 제언 (3가지 액션 플랜)
   Step 4. 후속 질의 제안
     - 보고서 작성 완료 후, 사용자가 이어 질문할 수 있는 심층 후속 질문 3가지를 하단에 추천하세요.
   ```

   | 프롬프트 입력 | 워크플로우 자동 생성 완료 |
   | :---: | :---: |
   | ![시장 분석 에이전트 프롬프트 입력](./img/workflowagent-011.webp) | ![Workflow Agent 자동 생성 완료](./img/workflowagent-012.webp) |

3. **Preview** 탭에서 **Start manually**를 클릭하여 실행 흐름을 확인합니다.

   | 노드 클릭 세부 설정 | Start manually 실행 |
   | :---: | :---: |
   | ![세부 설정 확인](./img/workflowagent-013.webp) | ![Start manually](./img/workflowagent-014.webp) |

   | 단계별 실행 흐름 | Human-in-the-loop 대상 입력 |
   | :---: | :---: |
   | ![실행 흐름](./img/workflowagent-015.webp) | ![HITL 입력](./img/workflowagent-016.webp) |

   | 다음 단계 자동 진행 | 순차 노드 실행 중 |
   | :---: | :---: |
   | ![자동 진행](./img/workflowagent-017.webp) | ![노드 순차 실행](./img/workflowagent-018.webp) |

   ![모든 단계 완료 상태](./img/workflowagent-019.webp)

4. **실행 결과 검토**:

   | Executive Summary | 경쟁사 비교 분석표 |
   | :---: | :---: |
   | ![Executive Summary](./img/workflowagent-020.webp) | ![경쟁사 비교표](./img/workflowagent-021.webp) |

   | SWOT 분석표 | 시사점 및 후속 질의 |
   | :---: | :---: |
   | ![SWOT 분석](./img/workflowagent-022.webp) | ![시사점 및 후속 질의](./img/workflowagent-023.webp) |

---

### 2) 실무 시나리오: Price & Margin Optimization Agent

경쟁사 가격 변동에 대응하여 자동으로 마진을 분석하고 가격 정책 및 후속 마케팅을 처리하는 워크플로우입니다.

```mermaid
graph TD
    A["매시간 실행 트리거"] --> B{"Gmail 검색: Competitor Price Alert"}
    B -- "이메일 없음" --> C["워크플로우 즉시 중지"]
    B -- "이메일 발견" --> D["Drive 커넥터: 재고 및 원가 마진 조회"]
    D --> E{"마진 >= 10% & 재고 충분?"}
    E -- "No 거절" --> F["매칭 불가 PDF 보고서 생성"]
    F --> G["store-managers@ 이메일 발송"]
    E -- "Yes 승인" --> H["판매 20% 증가 가정 재고 보충 계획 수립"]
    H --> I["소셜 미디어 & 마케팅 이메일 초안 작성"]
    I --> J["가격 분석/재고/마케팅 요약 PDF 보고서 생성"]
    J --> K["store-managers@ 최종 결정 및 PDF 이메일 발송"]
```

#### 워크플로우 빌더 실습 단계
1. **에이전트 생성**: New Agent → Workflow Agent 선택 (`Price & Margin Optimizer`)
2. **트리거 설정**: Schedule Trigger (`Every 1 hour`)
3. **Gmail 검색 노드**: `subject:"Competitor Price Alert"`
4. **조건 분기**: Rules-based Branch (이메일 없음 → Stop Workflow)
5. **Drive 커넥터**: 재고/원가 마진 스프레드시트 연동
6. **마진 판단 노드**: Structured Output JSON 포맷 지정
   ```markdown
   제공된 재고 및 원가 마진 데이터를 분석하여, 마진이 10% 이상이고 재고가 충분한지 판단하라. JSON으로 {"approve": true/false, "margin_pct": 숫자, "stock_ok": true/false} 형태로만 응답하라.
   ```
7. **거절/승인 경로 분기 및 PDF/이메일 자동 발송**

> [!TIP]
> **Human-in-the-Loop(HITL) 설계 가이드**: 마케팅 이메일 초안 발송 전에 **Approval 노드**를 배치하면, 담당자가 직접 최종 내용을 검토하고 수정한 뒤 발송할 수 있어 안전합니다.
