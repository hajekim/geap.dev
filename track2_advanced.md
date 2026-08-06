# 🔵 Track 2. Advanced

<div class="track-slide-bar" style="border-color: var(--google-blue);">
  <span class="track-slide-label">📋 실습 교육 가이드</span>
  <a href="slide_track2.html" target="_blank" class="track-slide-btn" style="color: var(--google-blue);">📽️ 슬라이드로 강의 시작 →</a>
</div>

Gemini Notebook 팀 도서관 구축, Deep Research 자율 보고서, 에이전트 빌더를 활용한 맞춤형 AI로 업무 파이프라인을 직접 구성하는 실습입니다. Google Drive 커넥터 및 커스텀 에이전트 실습은 **Track 2 Plus**를 참고하세요.

<div class="download-card">
  <div class="download-card-left">
    <div class="download-icon-box" style="background: #e8f0fe; color: #1a73e8;">📦</div>
    <div class="download-text">
      <h4>Track 2 Gemini Notebook 실습 파일 다운로드</h4>
      <p>설명서 실습용 이미지 패키지 1종, 시네마틱 슬라이드 실습용 이미지 패키지 1종, Canvas 동영상 실습용 파일 2종 — 총 4종을 미리 다운로드합니다.</p>
    </div>
  </div>
  <div style="display: flex; gap: 8px; flex-wrap: wrap;">
    <a href="samples/data_agent.zip" download class="download-btn" style="background: #34a853; padding: 10px 16px; font-size: 0.9rem;">📦 data_agent.zip</a>
    <a href="samples/homestyle.zip" download class="download-btn" style="background: #e8710a; padding: 10px 16px; font-size: 0.9rem;">📦 homestyle.zip</a>
    <a href="samples/canvas.pdf" download class="download-btn" style="background: #9334e6; padding: 10px 16px; font-size: 0.9rem;">📄 canvas.pdf</a>
    <a href="samples/canvas.zip" download class="download-btn" style="background: #9334e6; padding: 10px 16px; font-size: 0.9rem;">📦 canvas.zip</a>
  </div>
</div>
<div class="verify-card" data-verify-id="track2-data">
  <div class="verify-checkbox"></div>
  <span>Track 2 전체 실습에 활용할 샘플 파일 4종(data_agent.zip, homestyle.zip, canvas.pdf, canvas.zip)을 내 컴퓨터에 다운로드하였습니다.</span>
</div>

---

## 2.1. Gemini Notebook Enterprise

업로드한 문서(PDF, 텍스트, 이미지) 범위 내에서 질의응답을 진행하고, Gemini Notebook으로 슬라이드, 인포그래픽, 튜토리얼 동영상을 자동 생성하는 실습입니다. 다음 5가지 과제를 순서대로 진행합니다.

Gemini Enterprise App 좌측 메뉴 Agents 아래에 Gemini Notebook이 있습니다. 처음 접속한다면 아래 화면을 참고해 진입하세요.

<img src="./img/notebooklm_000.webp" width="280" alt="Gemini Enterprise App 좌측 메뉴 — Agents > Gemini Notebook">

| 실습 | Gemini Notebook 기능 | 내용 |
|------|------|------|
| **실습 1** | **Infographic** | AI 인포그래픽 3종 스타일 변환 |
| **실습 2** | **Audio Overview** | AI 팟캐스트 자동 생성 |
| **실습 3** | **Slide Deck** | 제품 이미지 소스 → 시네마틱 슬라이드 생성 |
| **실습 4** | **Slide Deck + Reports** | 설명서 만들기 (Study guide · FAQ · Briefing doc) |
| **실습 5** | **Video Overview** | Canvas 기능 튜토리얼 동영상 자동 생성 |

### 🎨 실습 1: Infographic — AI 인포그래픽 생성

아래 3가지 Google 제품 소개 문서를 소스로 등록하고, **인포그래픽 3종**을 각각 다른 스타일로 만들어봅니다.

#### 노트북 준비

1. **새 노트북 생성**: Gemini Enterprise App 좌측 메뉴 **Agents → Gemini Notebook**에서 **새로만들기**를 클릭합니다.
2. **소스 타입 선택**: 소스 추가 패널에서 **텍스트 붙여넣기**를 선택합니다.

   <img src="./img/41.webp" width="600" alt="텍스트 붙여넣기 소스 추가">

3. 아래 3가지 Google 제품 소개 문서를 **각각 개별 소스로 붙여넣기**합니다.

   <img src="./img/42.webp" width="600" alt="소스 텍스트 붙여넣기 완료 상태">

   **[소스 A] Google Gemini**
   ```
   # Google Gemini — 기업용 AI 어시스턴트 소개

   Google Gemini는 멀티모달 대형 언어 모델을 기반으로 한 엔터프라이즈 AI 어시스턴트입니다. 텍스트, 이미지, 문서, 코드를 이해하고 업무 맥락에 맞는 결과물을 생성합니다.

   Gemini Enterprise는 Google Workspace와 통합되어 사용자의 캘린더, 이메일, 드라이브 데이터를 분석합니다. 개인화 컨텍스트(pContext)는 최근 30일의 Workspace 활동 데이터를 기반으로 자동 생성되며, 처음 사용 시 OAuth 인증으로 연동을 설정합니다.

   주요 기능으로 Deep Research, Agent Designer, Gemini Notebook, 실시간 웹 그라운딩, Canvas가 있습니다.

   Deep Research는 웹과 내부 문서를 자율적으로 탐색해 구조화된 보고서를 만듭니다. 표준 모드에서 약 80회, 최대 모드에서 최대 160회 검색을 수행하며 3~8분 안에 완료됩니다. Agent Designer는 코드 없이 단일 또는 멀티 에이전트 워크플로우를 구성합니다. Single-step 에이전트는 독립적으로 작업을 처리하고, Multi-step 에이전트는 여러 하위 에이전트를 조율합니다. Gemini Notebook은 업로드한 문서와 URL을 소스로 팟캐스트, 인포그래픽, 슬라이드, 보고서를 자동 생성합니다. Canvas는 문서와 코드를 실시간으로 함께 편집하는 협업 인터페이스입니다.

   보안 측면에서 Gemini Enterprise는 사용자의 입력 데이터를 모델 학습에 활용하지 않습니다. 어드민 콘솔에서 커넥터 활성화, 에이전트 등록, 사용자별 기능 접근 권한을 관리합니다. Google의 DLP(데이터 손실 방지) 정책과 엔터프라이즈 보안 규정을 준수합니다.
   ```

   **[소스 B] Google Workspace**
   ```
   # Google Workspace — 기업 협업 플랫폼 소개

   Google Workspace는 Gmail, Google Drive, Docs, Sheets, Slides, Meet, Calendar, Chat을 단일 플랫폼으로 통합한 클라우드 기반 업무 환경입니다. 모든 파일이 클라우드에 저장되어 팀원 여러 명이 동시에 같은 문서를 편집할 수 있습니다.

   Gemini for Workspace가 각 앱에 통합되면서 업무 방식이 달라집니다. Gmail에서는 긴 이메일 스레드를 한 문장으로 요약하고 회신 초안을 자동으로 작성합니다. Docs에서는 주제를 입력하면 초안을 생성하며, 작성된 문서의 개선 사항을 제안합니다. Sheets에서는 자연어로 데이터 분석을 요청하면 수식과 차트를 자동으로 만듭니다.

   Meet은 화상회의 중 실시간 자막과 38개 언어 번역을 지원합니다. 회의가 끝나면 핵심 내용과 결정 사항, 할 일 목록을 자동으로 정리합니다. 참석하지 못한 팀원도 요약본으로 내용을 빠르게 파악합니다.

   Drive의 공유 드라이브는 팀 단위로 파일을 관리하며, 구성원이 바뀌어도 파일 소유권이 유지됩니다. Gemini를 통해 드라이브 내 문서를 검색하고 내용에 대해 질문할 수 있습니다.

   관리자는 Admin Console에서 사용자별 앱 접근 권한, 외부 공유 정책, 데이터 보존 규칙을 설정합니다. Google Workspace Enterprise Plus는 SOC 2, ISO 27001, HIPAA 등 컴플라이언스 인증을 충족합니다.
   ```

   **[소스 C] Google Cloud**
   ```
   # Google Cloud — 클라우드 인프라 및 AI 플랫폼 소개

   Google Cloud는 전 세계 40개 이상의 리전에서 컴퓨팅, 스토리지, 네트워킹, 데이터베이스, AI/ML 서비스를 제공합니다. Compute Engine, Google Kubernetes Engine(GKE), Cloud Run을 통해 가상 머신, 컨테이너, 서버리스 워크로드를 배포합니다.

   Vertex AI는 Google Cloud의 통합 AI 플랫폼입니다. Gemini API를 포함한 생성형 AI 모델을 API로 제공하며, 기업 자체 데이터로 모델을 파인튜닝하거나 RAG(Retrieval-Augmented Generation) 파이프라인을 구성할 수 있습니다. Agent Builder로 대화형 에이전트와 검색 기반 애플리케이션을 구축합니다.

   BigQuery는 서버리스 데이터 웨어하우스로 페타바이트 규모 데이터를 SQL로 분석합니다. Gemini in BigQuery를 사용하면 자연어로 데이터를 조회하고 AI가 쿼리와 인사이트를 자동 생성합니다. Looker와 연동해 BI 대시보드도 구성합니다.

   보안 체계는 Cloud Armor(DDoS 방어), Security Command Center(위협 탐지), Chronicle SIEM(보안 이벤트 분석)으로 구성됩니다. VPC와 Private Service Connect로 네트워크를 격리하고, 저장 데이터와 전송 중 데이터를 기본으로 암호화합니다.

   Anthos와 Google Distributed Cloud로 온프레미스와 멀티 클라우드 환경을 단일 콘솔에서 관리합니다. 기존 인프라에 Google Cloud를 단계적으로 도입하는 하이브리드 전략을 지원합니다.
   ```

   <img src="./img/notebooklm_003.webp" width="600" alt="총 세 개의 텍스트 소스">

   Gemini Notebook은 입력한 소스를 기반으로 질문하고 답변을 받을 수 있습니다.
   <img src="./img/notebooklm_001.webp" width="600" alt="기본 프롬프트">

1. **기본 인포그래픽**: 우측에 Infograpgic 버튼의 점 세 개 메뉴를 클릭합니다.
   <img src="./img/notebooklm_004.webp" width="600" alt="Infographic 버튼">

    그 후 아래 프롬프트를 입력합니다.
   ```
   Google Workspace의 주요 앱과 각 앱에 통합된 Gemini AI 기능을 한눈에 정리한 인포그래픽을 만들어줘
   ```

   <img src="./img/notebooklm_005.webp" width="600" alt="인포그래픽 프롬프트 입력">
   <img src="./img/46.webp" width="600" alt="기본 인포그래픽 생성 결과">

   > [!TIP]
   > **화면 비율 안내**: 인포그래픽이 세로로 길게 보일 수 있습니다. **다운로드** 버튼으로 저장하면 16:9 가로 비율로 정상 출력됩니다.

2. **스케치노트 스타일**: 동일한 Infographic 생성 버튼을 눌러서 다른 프롬프트를 입력해봅니다.
   ```
   Google Gemini Enterprise의 핵심 기능과 실무 활용 시나리오를 스케치노트 스타일로 그려줘
   ```
   <img src="./img/notebooklm_006.webp" width="600" alt="인포그래픽 프롬프트 입력">

   <img src="./img/47.webp" width="600" alt="스케치노트 스타일 인포그래픽 결과">

3. **신문 1면 스타일**: 동일 소스에서 퍼블리싱 톤의 결과물을 뽑아봅니다.
   ```
   Google Cloud Vertex AI와 BigQuery 기반 기업 AI 혁신 현황을 신문 1면 기사 스타일 인포그래픽으로 만들어줘
   ```
   <img src="./img/notebooklm_007.webp" width="600" alt="인포그래픽 프롬프트 입력">
   <img src="./img/48.webp" width="600" alt="신문 1면 스타일 인포그래픽 결과">

---

### 🎙️ 실습 2: Audio Overview — AI 팟캐스트 자동 생성

Gemini Notebook의 킬러 기능 중 하나입니다. 동일 노트북 우측 **오디오 개요** 패널에서 **생성하기**를 클릭하면, AI 진행자 2인이 소스 문서 전체를 요약해 **5~8분 분량의 팟캐스트 오디오**를 자동 완성합니다.

<img src="./img/notebooklm_008.webp" width="600" alt="Audio Overview">

오디오 생성은 소요시간이 꽤 걸리므로 다른 작업을 진행 후 이후에 확인해봅니다.

<img src="./img/notebooklm_009.webp" width="600" alt="Output: Audio Overview">


> [!TIP]
> 팀 내 공유용으로 사용하거나, 이동 중 이어폰으로 문서 내용을 파악할 때 매우 유용합니다. 생성된 오디오는 다운로드 후 사내 메신저나 이메일로 바로 배포할 수 있습니다.

---

### 🎬 실습 3: Slide Deck — 시네마틱 슬라이드 생성

텍스트 없이 **제품 이미지만으로** Gemini Notebook이 영화 같은 시네마틱 슬라이드를 자동 생성합니다. 라이프스타일 브랜드 '홈스타일'의 신제품 이미지를 소스로 업로드하고, 짧은 브랜드 스토리를 붙여 시네마틱 슬라이드를 만들어봅니다.

#### 1단계: 실습 파일 다운로드 및 압축 해제

아래 버튼을 클릭해 실습용 이미지가 포함된 압축파일 homestyle.zip을 로컬에 저장합니다.

<a href="./samples/homestyle.zip" download style="display:inline-flex;align-items:center;gap:6px;background:#1a73e8;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:500">📥 homestyle.zip 받기</a>

다운로드 후 압축을 해제하면 `sofa.png`, `cushion.png`, `lighting.png`, `diffuser.png` 4장의 제품 이미지가 나옵니다.

<img src="./img/notebooklm_010.webp" width="600" alt="homestyle.zip">

#### 2단계: 새 노트북 생성 및 이미지 소스 추가

1. Gemini Enterprise App 좌측 메뉴 **Agents → Gemini Notebook**에서 **새로만들기**를 클릭해 새 노트북을 엽니다.
2. **소스 추가** → **파일 업로드**를 선택하고 압축 해제된 이미지 4장(`sofa.png`, `cushion.png`, `lighting.png`, `diffuser.png`)을 **한꺼번에** 선택해 업로드합니다.

   <img src="./img/notebooklm_011.webp" width="600" alt="Gemini Notebook 이미지 소스 4장 업로드 완료">

#### 3단계: 브랜드 스토리 텍스트 추가

**소스 추가** → **텍스트 붙여넣기**를 선택하고, 아래 텍스트를 복사해 붙여넣기한 뒤 소스 이름을 **story** 로 저장합니다.

<img src="./img/notebooklm_012.webp" width="600" alt="Gemini Notebook 텍스트 소스 입력">

```markdown
### **스토리**

**Scene 1. 햇살이 가득한 주말 오후**

* **배경:** 따뜻한 햇살이 큰 창을 통해 가득 들어오는, 밝고 화사한 톤의 모던한 거실.
* **오브젝트 배치:** 거실 중심에 브라운 가죽 소파인 `sofa.png`가 놓여 있고, 그 위로 창밖의 햇살이 부드럽게 내리쥡니다. 소파 위에는 화사한 오렌지색 기하학 패턴의 `cushion.png`들이 자연스럽게 놓여 있습니다. 소파 옆으로는 은은한 반투명 전등갓의 플로어 램프 `lighting.png`가 서 있고, 소파 앞 작은 테이블 위에는 영롱하게 빛나는 핑크색 디퓨저 `diffuser.png`가 놓여 있습니다.
* **스토리:** 주말 오후, 상쾌한 기분으로 주인공이 거실로 들어와 햇살을 받으며 소파 쪽으로 천천히 걸어갑니다.

**Scene 2. 포근한 소파에서의 시작 (`sofa.png`)**

* **배경:** 햇살이 가득 찬 화사한 거실.
* **오브젝트 배치:** 주인공이 햇살을 가득 머금은 **`sofa.png`** 브라운 가죽 소파에 몸을 포근하게 맡깁니다. 소파의 넓고 유연한 가죽 질감이 소파를 중심으로 거실 공간 전체와 자연스럽게 어우러져 화면에 담깁니다.
* **스토리:** 주인공이 소파에 기대어 편안한 표정으로 숨을 고릅니다. 소파는 거실의 중심에서 가장 따뜻하고 포근한 안식처의 역할을 합니다.

**Scene 3. 온기를 더하는 화사한 포인트 (`cushion.png`)**

* **배경:** 소파와 그 주변 가구들이 함께 보이는 거실 전경.
* **오브젝트 배치:** 주인공이 앉은 자리 옆, **`sofa.png`** 위에 놓인 **`cushion.png`** 오렌지색 기하학 패턴 쿠션들이 선명하게 보입니다. 쿠션은 햇살 아래에서 한층 더 화사하고 생기 있게 빛납니다.
* **스토리:** 주인공이 자연스럽게 옆에 있던 오렌지색 쿠션 하나를 품에 끌어안습니다. 선명한 패턴과 색감이 거실 분위기를 한층 더 감각적이고 상쾌하게 변화시킵니다.

**Scene 4. 공간을 채우는 부드러운 빛 (`lighting.png`)**

* **배경:** 턴을 넘기듯 자연스럽게 이어지는 거실 공간.
* **오브젝트 배치:** 주인공이 소파에 앉은 채로 손을 뻗어, 소파 옆에 자연스럽게 배치된 **`lighting.png`** 플로어 램프를 켭니다. 은은하고 부드러운 유백색 빛이 자연 채광과 섞여 거실 전체를 한층 더 아늑하게 감싸 안습니다.
* **스토리:** 조명의 따스한 불빛이 들어오면서 공간의 입체감이 살아나고, 거실 전체 인테리어가 더욱 세련되고 완성도 높게 연출됩니다.

**Scene 5. 감각을 깨우는 상쾌한 향기 (`diffuser.png`)**

* **배경:** 소파 앞 테이블과 거실 전체가 흐릿하게(아웃포커싱) 잡히는 구도.
* **오브젝트 배치:** 카메라 시선이 소파 앞 테이블 위에 놓인 **`diffuser.png`** 핑크색 디퓨저를 향합니다. 디퓨저는 햇살과 램프 빛을 동시에 받아 영롱하게 반짝이며 공간의 오브젝트들과 완벽한 톤앤매너를 이룹니다.
* **스토리:** 공기 중으로 디퓨저의 상쾌한 향이 은은하게 퍼지는 듯한 연출과 함께, 쿠션을 안고 소파에 기댄 주인공이 편안하게 눈을 감으며 주말의 완벽한 휴식을 만끽합니다.

**Scene 6. 완벽한 휴식의 공간 (엔딩)**

* **배경:** 모든 아이템이 조화롭게 어우러진 전체 거실 전경.
* **오브젝트 배치:** 카메라가 천천히 뒤로 물러나며(줌아웃), **`sofa.png`** 소파 위에 **`cushion.png`** 쿠션을 안고 햇살을 받으며 누운 주인공, 그 옆을 따뜻하게 비추는 **`lighting.png`** 램프와 상쾌한 무드를 더하는 `diffuser.png`까지 완벽하게 어우러진 화사한 거실의 전체 인테리어를 잡습니다.
* **스토리:** 잘 정돈된 아름다운 공간 속에서 오감으로 완성된 나만의 안식처를 보여주며 상쾌하게 마무리됩니다.
```

<img src="./img/notebooklm_012.webp" width="600" alt="Gemini Notebook 텍스트 소스 붙여넣기">

<img src="./img/notebooklm_013.webp" width="600" alt="Gemini Notebook 소스는 총 다섯개">

#### 4단계: 시네마틱 슬라이드 생성

소스가 모두 준비되면, 노트북 우측 **슬라이드 자료** 패널에서 customize 옵션을 선택합니다.

<img src="./img/notebooklm_014.webp" width="600" alt="슬라이드 자료">

아래 프롬프트를 복사하여 붙여넣습니다.

```markdown
스토리에 맞는 시네마틱 슬라이드를 만들어줘, 타이틀, 텍스트, 자막, 설명 등은 포함하지 마
```

<img src="./img/notebooklm_015.webp" width="600" alt="슬라이드 생성 입력">

생성하는 데 시간이 걸립니다.

<img src="./img/notebooklm_016.webp" width="600" alt="슬라이드 생성을 하는 중">

완성된 슬라이드를 볼 수 있습니다.

<img src="./img/notebooklm_017.webp" width="600" alt="슬라이드 생성 완료">

다운로드도 할 수 있습니다.

<img src="./img/notebooklm_018.webp" width="600" alt="슬라이드 받을까 말까">

pptx 파일로 다운로드하였습니다.

<img src="./img/notebooklm_019.webp" width="600" alt="슬라이드 받을까 말까">

결과물은 직접 보실 수 있습니다.

- [📊 Cinematic Sanctuary.pptx](/samples/Cinematic%20Sanctuary.pptx)
- [📄 Cinematic Sanctuary.pdf](/samples/Cinematic%20Sanctuary.pdf)


> [!TIP]
> 시네마틱 슬라이드는 이미지 소스가 있어야 생성됩니다. 텍스트만 있을 경우 일반 슬라이드 자료로 안내될 수 있습니다. 이미지 품질이 높을수록 결과물의 완성도도 높아집니다.

---

### 📖 실습 4: Slide Deck + Reports — 설명서 만들기

새로운 노트북을 하나 생성합니다. 상단 다운로드 카드에서 받은 `data_agent.zip`을 로컬에서 압축 해제한 뒤, 파일 업로드로 이미지 10개를 소스에 추가합니다. **슬라이드 Customize**로 가이드 문서를 생성하고, Studio의 **Reports** 기능으로 스터디 가이드·FAQ·브리핑 문서를 차례로 만들어봅니다.

**생성 방법:**

1. Gemini Enterprise App 좌측 메뉴 **Agents → Gemini Notebook**에서 **새로만들기**를 클릭합니다. **소스 추가** → **파일 업로드**를 선택한 뒤, 상단에서 다운로드한 `data_agent.zip`의 압축을 해제하고 이미지 10개를 소스에 추가합니다.

   <img src="./img/notebooklm_020.webp" width="600" alt="10개의 파일을 업로드 완료">

2. 우측 **Studio** 패널에서 **슬라이드** 의 Customize 버튼을 클릭합니다.

   <img src="./img/notebooklm_014.webp" width="600" alt="슬라이드 자료">

3. 그 후 아래 텍스트를 복사하여 붙여넣습니다.
   ```
   BigQuery Data Agent를 생성하는 과정을 초보자도 쉽게 따라할 수 있도록 가이드 문서를 작성해줘
   ```

   <img src="./img/notebooklm_021.webp" width="600" alt="슬라이드 Customize 프롬프트 입력">

4. 완성되면 아래처럼 출력됩니다.

   <img src="./img/notebooklm_022-a.webp" width="600" alt="결과물">
   <img src="./img/notebooklm_022-b.webp" width="600" alt="결과물">

5. Studio 섹션에서 Reports 에서 Study guide, FAQ, Briefing doc을 차례대로 클릭해봅니다.
   <img src="./img/notebooklm_029.webp" width="600" alt="결과물">

6. Study guide 결과입니다.
<img src="./img/notebooklm_030.webp" width="600" alt="결과물">

7. FAQ 결과입니다.
<img src="./img/notebooklm_031.webp" width="600" alt="결과물">

8. Briefing doc 결과입니다.
<img src="./img/notebooklm_032.webp" width="600" alt="결과물">

> [!TIP]
> 스터디 가이드는 기술 개념 학습용으로, FAQ는 팀 온보딩 자료로, 브리핑 문서는 임원 보고서로 바로 활용할 수 있습니다.

---

### 🎬 실습 5: Video Overview — 동영상 만들기

**Gemini Enterprise Canvas** 기능 사용법을 설명하는 튜토리얼 동영상을 Gemini Notebook이 자동 생성합니다. PDF 문서와 스크린샷 이미지를 소스로 제공하면, 별도 편집 도구 없이 단계별 설명 영상이 완성됩니다.

#### 1단계: 실습 파일 준비

아래 버튼을 클릭해 실습 파일 2종을 로컬에 저장합니다.

<a href="./samples/canvas.pdf" download style="display:inline-flex;align-items:center;gap:6px;background:#1a73e8;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:500;margin-right:8px">📥 canvas.pdf 받기</a>
<a href="./samples/canvas.zip" download style="display:inline-flex;align-items:center;gap:6px;background:#1a73e8;color:#fff;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:500">📥 canvas.zip 받기</a>

- `canvas.pdf` — Canvas 기능 소개 및 사용 가이드 문서
- `canvas.zip` — Canvas UI 스크린샷 이미지 모음 (압축 해제 후 사용)

#### 2단계: 새 노트북 생성 및 소스 추가

1. Gemini Enterprise App 좌측 메뉴 **Agents → Gemini Notebook**에서 **새로만들기**를 클릭합니다.
2. **소스 추가** → **파일 업로드**에서 `canvas.pdf`를 추가합니다.
3. `canvas.zip` 압축을 해제한 뒤, 이미지 파일 전체를 한꺼번에 소스로 업로드합니다.

<img src="./img/notebooklm_023.webp" width="600" alt="canvas.pdf + 스크린샷 이미지 소스 추가 완료">

#### 3단계: 동영상 생성 프롬프트 입력

소스 업로드가 완료되면 Video Overview의 Customize 버튼을 클릭합니다.

<img src="./img/notebooklm_024.webp" width="600" alt="영상 커스터마이즈 생성">

```markdown
Gemini Enterprise에서 Canvas를 사용하는 방법을 초보자도 따라가기 쉽게 차근차근 설명하는 동영상을 만들어줘
```

<img src="./img/notebooklm_025.webp" width="600" alt="영상 생성을 위한 프롬프트 입력">

잠시 후 Canvas 기능 소개 튜토리얼 영상이 자동 완성됩니다.

<img src="./img/notebooklm_026.webp" width="600" alt="Gemini Enterprise Canvas 튜토리얼 동영상 생성 결과 1">
<img src="./img/notebooklm_027.webp" width="600" alt="Gemini Enterprise Canvas 튜토리얼 동영상 생성 결과 2">
<img src="./img/notebooklm_028.webp" width="600" alt="Gemini Enterprise Canvas 튜토리얼 동영상 생성 결과 3">

> [!NOTE]
> 참고 영상: [YouTube — Gemini Enterprise Canvas 데모](https://www.youtube.com/watch?v=4-5qeh4IXVY)
> 동영상 생성 기능은 Gemini Notebook의 소스 내용을 기반으로 하므로, 소스 품질이 높을수록 더 정확한 튜토리얼 영상이 만들어집니다.

## 2.2. Deep Research Agent

Google이 직접 만들고 관리하는 **"Made by Google" 에이전트**입니다. Deep Research Agent로 수백 개 소스를 자율 탐색해 인용 출처가 명시된 종합 보고서를 만들어봅니다.

### 🔍 Deep Research Agent

복잡한 연구 주제를 하위 질문으로 분해하고, 웹·기업 내부 문서를 다단계로 자율 탐색해 인용 출처가 명시된 종합 보고서를 만들어주는 에이전트입니다. 질의 분해 → 플랜 생성 → 자율 탐색 → 반복 추론 → 보고서 완성의 **5단계 에이전틱 워크플로우**로 작동합니다.

| 항목 | 내용 |
|---|---|
| **검색 횟수** | 표준 약 80회, Deep Research Max 최대 160회 |
| **소요 시간** | 일반적으로 3~8분 |
| **소스** | 웹, 기업 내부 앱 데이터, Drive, Gmail |
| **출력물** | 목차·인용 링크 포함 보고서 + 1~2분 오디오 요약 |

- **실습 진입**: 화면 좌측 또는 하단 메뉴에서 **Deep Research** 아이콘을 클릭합니다.

  <img src="./img/34.webp" width="600" alt="Deep Research 에이전트 진입">

- **리서치 프롬프트 복사 및 실행**:
  대화창에 아래 프롬프트를 입력하여 실습을 진행합니다.
  ```markdown
  현재 글로벌 스마트 오피스 IoT 및 디지털트윈 솔루션 시장의 기술 트렌드와 주요 경쟁사 동향을 종합적으로 분석해 줘. 넥스트 테크놀로지스가 속한 오피스 테크 산업의 핵심 경쟁 우위 요소를 도출하고 향후 직면할 기회와 위협 요인을 논리적으로 설명해 줘
  ```
  에이전트가 시작되면 수집·심층 검색 단계가 비주얼 대시보드에 표시됩니다. 완료되면 목차(TOC)와 풍부한 인용 링크가 달린 마스터 보고서와 팟캐스트 형태의 오디오 요약본을 받을 수 있습니다. 보통 **3~8분** 걸립니다.

  <img src="./img/32.webp" width="600" alt="Deep Research 분석 보고서 생성 결과 1">
  <img src="./img/33.webp" width="600" alt="Deep Research 분석 보고서 생성 결과 2">

## 2.3. Agent Designer

코드 없이 클릭 몇 번으로, 내 업무에 특화된 AI 에이전트를 직접 만들고 팀원들과 공유해봅니다.

### 1) 에이전트 종류와 실무 활용 예시

#### 에이전트 종류
- **No-Code 에이전트**: Agent Designer에서 말하듯 대화하며 자연어로 규칙과 대상을 설계하는 임직원용 간편 에이전트.
- **Low-Code 에이전트**: 시각적인 노드 기반 흐름 빌더(Flow Builder)와 트리거, 승인 단계 레이아웃을 통해 제작하는 업무 에이전트.
- **High-Code 에이전트**: 개발자 전용 프레임워크인 ADK(Agent Development Kit)를 사용해 파이썬이나 고(Go) 언어 소스로 복잡한 백엔드 API와 레거시 시스템 트랜잭션을 연동해 구축하는 최고 수준의 지능형 에이전트.

#### 에이전트 실무 활용 예시
1. **비즈니스 프로세스/SOP 자동화**: AI의 판단력과 사내 업무 규칙을 결합하여 송장 처리 및 비용 정산 등 반복적인 기업의 업무 과정을 자동화.
2. **복잡한 작업 산출물 생성**: 대화를 주고받으며 PRD(제품 요구사항 정의서), RFP(제안요청서) 같은 결과물을 반복적으로 초안 작성 및 수정.
3. **기존 프로세스용 채팅 인터페이스**: IT 헬프데스크 에이전트처럼 사용자의 IT 문제를 해결하거나 시스템에 SOP 요청을 직접 등록.
4. **데이터 및 문서 기반 질의**: 기업 전략 문서, 복리후생 내규, 재무 데이터 등 특정 구조화/비구조화 사내 자산에 대한 RAG 질의응답.
5. **개인 생산성 ("비서실장" 역할)**: 수신함, 캘린더를 모니터링하여 회의 시작 전 참가자와의 지난 대화 및 안건 요약 등 선제적으로 업무를 지원.

### 2) Agent Designer
에이전트를 생성·관리·배포하는 **노코드/로우코드 인터랙티브 플랫폼**입니다. 자연어 대화로 에이전트를 즉시 만들거나, 시각적 캔버스에서 직접 워크플로우를 조립할 수 있습니다. **특정 작업을 독립 수행**하는 Single-step 에이전트와 **메인 에이전트가 서브에이전트를 단계별 조율**하는 Multi-step 에이전트, 두 가지 유형을 지원합니다.

| 유형 | 설명 | 적합한 작업 |
|---|---|---|
| **Single-step** | 특정 작업을 독립적으로 완수하는 에이전트 | 명확하게 정의된 단일 목적 작업 |
| **Multi-step** | 메인 에이전트가 하나 이상의 서브에이전트를 조율해 복합 작업을 처리하는 에이전트 | 순차적 단계로 분해 가능한 복합 업무 |

<img src="./img/image9.webp" width="800" alt="Agent Designer 전체 UI 구조">

- **Chat Pane**: 자연어로 에이전트를 생성하고 수정하는 노코드 대화 인터페이스. "이메일 알리미 만들어줘"라고 요청하면 역할·권한·규칙이 자동으로 구성됩니다.
- **Designer Pane**:
  - `Flow`: 에이전트 노드와 서브에이전트를 시각적 캔버스에서 직접 구성하는 로우코드 편집기.
  - `Schedule`: 특정 요일·주기·외부 트리거 기반의 자동 실행 구성.
  - `Preview`: 배포 전 실시간으로 에이전트 동작을 테스트하는 샌드박스.
- **Create(배포)**: 에이전트를 조직 전체 또는 특정 사용자에게 공유. 미배포 상태는 Draft로 저장됩니다.

> [!TIP]
> **💡 에이전트 디자이너 지시문(Instructions) 작성 베스트 프랙티스**
>
> * **명확한 목표 정의**: 모호한 요청 대신 충분한 배경 컨텍스트와 기대 동작을 명확히 제시하세요.
>   - ❌ *Not Recommended*: "영업 이메일용 에이전트를 만들어줘."
>   - ⭕ *Recommended*: "내 CRM의 새로운 영업 리드에게 보낼 후속 이메일 초안을 작성하는 에이전트를 만들어줘. 연락처의 회사를 검색하고, 비즈니스를 요약하며, 우리 제품이 그들에게 어떻게 도움이 될 수 있는지 제안해야 해."
> * **출력 경계 및 제한 설정**: 에이전트가 해야 할 일과 절대 하지 말아야 할 일(분량, 어조, 포함/배제 요소 등 경계)을 명확히 정의하세요.
> * **Gemini가 역질문하도록 유도**: 누락된 세부 정보를 수집할 수 있도록, 작업 실행 전 사용자에게 확인 질문을 던지도록 규칙에 포함하세요.

### 3) 💻 실전 실습: CRAFT 프롬프트 에이전트 만들기
1. 상단 **Agents** 메뉴를 클릭합니다.

<img src="./img/agentdesigner-008.webp" width="600" alt="Agents 메뉴 진입">

2. **New Agent**를 클릭합니다.

<img src="./img/agentdesigner-001.webp" width="600" alt="New Agent 버튼 클릭">

3. Chat Pane(왼쪽 대화창)에 아래 설계 요구 명세를 입력합니다.

```markdown
사용자가 러프하게 작성한 프롬프트를 Gemini에 사용하기 좋도록 아래 CRAFT 프레임워크 기반으로 프롬프트를 재작성합니다. 작성하기 위해 너(Gemini)에게 어떤 정보가 필요한지 나에게 질문하여 얻습니다.

### [CRAFT 프레임워크]

**Context / 맥락:** 상황을 파악할 수 있도록 배경지식, 목적, 비즈니스 환경을 제공합니다.

**Role / 역할:** 구체적인 직업, 연차, 정체성을 부여하여 전문적인 역할/페르소나를 활성화합니다.

**Action / 행동:** 수행해야 할 핵심 작업이나 미션을 명확한 동사로 지시합니다.

**Format / 출력 형식:** 보고서, 이메일, 표, 불릿포인트 등 원하는 결과물의 구조를 지정합니다.

**Tone / Target (타겟 및 어조):** 답변의 최종 소비자가 누구인지 정의하고 전문적, 친근함 등의 톤앤매너를 설정합니다.
```

<img src="./img/agentdesigner-002.webp" width="600" alt="Chat Pane에 설계 요구 명세 입력">

4. 에이전트가 생성되면 편집 화면으로 자동 이동합니다. 왼쪽 **Chat Pane**에서 대화로 에이전트를 수정하고, 오른쪽 **Flow Builder**에서 캔버스 세부 설정을 조정합니다.

<img src="./img/agentdesigner-003.webp" width="600" alt="Chat Pane과 Flow Builder 편집 화면">

5. **Preview** 탭에서 생성된 에이전트를 직접 테스트합니다.

<img src="./img/agentdesigner-004.webp" width="600" alt="Preview 탭에서 에이전트 테스트">

6. 테스트가 완료되면 **Create** 버튼을 눌러 에이전트를 배포합니다.

<img src="./img/agentdesigner-005.webp" width="600" alt="Create 버튼으로 에이전트 배포">

배포 후 에이전트를 계속 수정하거나 채팅으로 바로 사용할 수 있습니다.

<img src="./img/agentdesigner-006.webp" width="600" alt="배포 후 수정 또는 채팅 선택 화면">
<img src="./img/agentdesigner-007.webp" width="600" alt="배포된 에이전트 채팅 화면">

7. 좌측 **Agents** 목록 → **Your Agents**에서 생성된 에이전트를 확인합니다.

<img src="./img/agentdesigner-009.webp" width="600" alt="Your Agents 목록에서 생성된 에이전트 확인">



### 4) 💻 실전 실습: 뉴스 링크 기반 SNS 마케팅 포스팅 자동 빌더 에이전트 구축
1. **에이전트 목록** 메뉴에서 <b>새 에이전트 생성(New Agent)</b>을 클릭합니다.
2. 에이전트 디자이너가 켜지면 왼쪽 대화창에 아래의 설계 요구 명세 프롬프트를 입력합니다.
   ```markdown
   뉴스 링크를 입력 받아서 Social Media 포스팅할 게시물 문구를 생성하는 에이전트를 만들어줘 포스팅할 문구는 간략한 한줄 문장과 bullet point 5개를 생성하고 Hashtag도 추천
   ```

   <img src="./img/image53.webp" width="700" alt="에이전트 디자이너 프롬프트 입력">

3. 시스템이 자동으로 뼈대를 잡으면, 우측 상세 Flow를 최종 검토한 뒤 상단의 **Create(생성)** 또는 **Publish** 버튼을 클릭하여 적용합니다.

   <img src="./img/image78.webp" width="800" alt="디자이너 Flow 및 상세 설정">

   4. 프리뷰 테스트 창에 아래 뉴스 기사 링크를 복사해 붙여넣어 에이전트가 요약 포스팅을 제대로 만들어내는지 테스트합니다.
      ```markdown
      이 뉴스 링크로 소셜 미디어 게시물을 만들어줘: https://news.next-tech.com/smart-office-iot-2026/
      ```

   <img src="./img/image14.webp" width="800" alt="에이전트 프리뷰 뉴스 테스트">
   <img src="./img/image70.webp" width="800" alt="테스트 성공 출력화면">

5. 에이전트가 완성되었다면 사내 <b>Agent Gallery</b>에 발행하여 전사 공유합니다. 우측 상단의 `Share` 클릭 후, `Add People` 지정 대신 `Done`을 누르면 사내 공용 채널인 'Low Code Agents'에 갤러리 형태로 자동으로 등록됩니다.

<img src="./img/image23.webp" width="800" alt="에이전트 공유 시작">

---

## 2.4. Workflow Agent

정밀한 비즈니스 로직과 단계를 순서대로 실행하는 방식을 구현하여 엄격한 업무 규칙을 자동화하는 **Workflow Agent** 실습입니다.

### 1) Workflow Agent
복잡한 업무를 순차적 단계로 분해하고, 각 단계를 전담 서브에이전트가 실행하는 멀티 에이전트 오케스트레이션 방식입니다. Single-step 에이전트가 단일 프롬프트로 즉시 응답하는 방식이라면, Multi-step 에이전트(Workflow Agent)는 Flow Builder 캔버스에서 노드를 연결해 "정보 수집 → 분석 → 보고서 작성"처럼 엄격한 순서가 필요한 업무를 자동화합니다.

- 각 노드는 독립적인 Instruction·Knowledge·Tools·Model 설정을 가집니다.
- **스케줄러 트리거**로 정해진 시간에 자동 실행하거나, 사람의 **승인(Human-in-the-loop)** 단계를 중간에 삽입할 수 있습니다.
- Preview 탭에서 단계별 실행 흐름을 실시간으로 모니터링하고 수정할 수 있습니다.

> [!NOTE]
> Workflow Agent는 Preview(미리 보기) 신청을 통해 활성화된 환경에서 사용할 수 있습니다.

#### Workflow Agent 구성 요소
- **트리거 (Trigger)**: 지정된 일정(Schedule Event)이나 이메일 수신 등 특정 이벤트 발생 시 기동되는 시작 조건.
- **Gemini 에이전트 노드**: 유연한 판단 및 대화 수행. Structured Outputs, 프롬프트 내 변수 참조, 도구/지식 소스 연동 지원.
- **커넥터 (Connector)**: Google Workspace(Gmail, Calendar, Drive), Office 365, ServiceNow, Confluence, Jira 등 실시간 연동.
- **플로우 컨트롤 (Flow Control)**: 조건 분기(Rules-based), 목록 내 항목 일괄 반복 처리(For 루프), 데이터 필터 등 규칙 기반 제어 노드.
- **Human-in-the-Loop (HITL)**: 자산 손실이나 오작동 위험을 통제하기 위해, 사람의 추가 정보 입력, 최종 승인, 답변 초안 검토/수정 단계를 중간 블록에 장착.
- **통합 및 연동**: 기존 사내 IT 시스템 및 BYO-MCP(Model Context Protocol) 노드 연동.

### 2) Workflow Agent 실무 활용 예시: 글로벌 시장 조사 에이전트

좌측 **Agents**에서 **New Agent > Workflow Agent**를 클릭합니다.

<img src="./img/workflowagent-010.webp" width="600" alt="Workflow Agent 생성 메뉴">

Chat Pane에 아래 프롬프트를 입력합니다.
```
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

출력 규칙:
 - 항상 객관적 데이터와 구체적인 사례를 바탕으로 작성하세요.
 - 텍스트는 명확하고 가독성 높은 한국어 마크다운 포맷으로 전달하세요.
```

<img src="./img/workflowagent-011.webp" width="600" alt="Chat Pane에 시장 분석 에이전트 프롬프트 입력">

입력한 프롬프트를 기반으로 Workflow Agent가 자동 생성됩니다.

<img src="./img/workflowagent-012.webp" width="600" alt="Workflow Agent 자동 생성 완료">

생성된 에이전트는 순차 실행되는 멀티 에이전트 구조로 구성됩니다. 각 Gemini 노드를 클릭하면 Instruction·Knowledge·Tools·Output·Model 등 세부 설정을 확인하고 수정할 수 있습니다.

<img src="./img/workflowagent-013.webp" width="600" alt="노드 클릭 시 세부 설정 확인">

**Preview** 탭에서 **Start manually**를 클릭해 실행합니다. 각 단계가 순서대로 실행되는 흐름을 실시간으로 확인하고 수정할 수 있습니다.

<img src="./img/workflowagent-014.webp" width="600" alt="Preview 탭 Start manually 버튼">

<img src="./img/workflowagent-015.webp" width="600" alt="단계별 실행 흐름 실시간 확인">

첫 번째 노드는 스케줄러 트리거, 두 번째 노드는 **Human-in-the-loop** 승인 단계입니다. 분석할 산업군 또는 기업명을 입력합니다.

<img src="./img/workflowagent-016.webp" width="600" alt="Human-in-the-loop 단계에서 분석 대상 입력">

입력이 완료되면 다음 단계로 자동 진행됩니다.

<img src="./img/workflowagent-017.webp" width="600" alt="다음 단계로 자동 진행">

세 번째·네 번째 노드가 순서대로 실행됩니다.

<img src="./img/workflowagent-018.webp" width="600" alt="세 번째·네 번째 노드 순차 실행 중">

모든 단계가 성공적으로 완료됩니다.

<img src="./img/workflowagent-019.webp" width="600" alt="모든 단계 완료 상태">

실행 결과를 확인합니다.

<img src="./img/workflowagent-020.webp" width="600" alt="시장 분석 결과 - Executive Summary">
<img src="./img/workflowagent-021.webp" width="600" alt="시장 분석 결과 - 경쟁사 비교 분석표">
<img src="./img/workflowagent-022.webp" width="600" alt="시장 분석 결과 - SWOT 분석">
<img src="./img/workflowagent-023.webp" width="600" alt="시장 분석 결과 - 시사점 및 후속 질의 제안">  

### 3) 🏭 실무 활용 대표 예시: Price & Margin Optimization Agent
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
    
    style E fill:#e8f0fe,stroke:#1a73e8,stroke-width:2px
```

#### 🛠️ 워크플로우 에이전트 빌더 실습 체크리스트

다이어그램을 보며 아래 순서대로 Gemini Enterprise **Workflow Agent**에서 워크플로우를 직접 조립해봅니다.

- [ ] **① 워크플로우 에이전트 생성**: **New Agent** → 유형을 **Workflow Agent** 선택 → 이름: `Price & Margin Optimizer`
- [ ] **② 트리거 설정**: 좌측 노드 패널에서 **Schedule Trigger** 드래그 → 실행 주기 `Every 1 hour` 설정
- [ ] **③ Gmail 검색 노드 추가**: Connector 패널 → **Gmail** 검색 노드 추가 → 검색 조건: `subject:"Competitor Price Alert"` 입력
- [ ] **④ 조건 분기 추가**: Flow Control → **Rules-based Branch** 노드 추가
  - `이메일 없음` 경로 → **Stop Workflow** 연결
  - `이메일 발견` 경로 → 다음 단계 연결
- [ ] **⑤ Drive 커넥터 추가**: Connector → **Google Drive** 노드 추가 → 파일 ID 또는 공유 폴더 경로 지정 (재고·원가 마진 스프레드시트)
- [ ] **⑥ 마진 판단 에이전트 노드 추가**: Gemini Agent 노드 추가 → 프롬프트 입력:
  ```
  제공된 재고 및 원가 마진 데이터를 분석하여, 마진이 10% 이상이고 재고가 충분한지 판단하라. JSON으로 {"approve": true/false, "margin_pct": 숫자, "stock_ok": true/false} 형태로만 응답하라.
  ```
  → **Structured Output** 활성화
- [ ] **⑦ 두 번째 조건 분기**: `approve: false` → PDF 보고서 생성 → Gmail 발송 노드 연결 (`store-managers@`)
- [ ] **⑧ 승인 경로 노드 추가**: `approve: true` 경로에 Gemini Agent 노드 → 재고 보충 계획 및 마케팅 이메일 초안 생성
- [ ] **⑨ 최종 PDF 보고서 생성 및 발송**: 보고서 생성 노드 → Gmail 발송 노드 (`store-managers@`) 연결
- [ ] **⑩ 테스트 실행**: 상단 **Test Run** 클릭 → 각 노드 실행 결과 로그 확인 → 정상 동작 여부 검토

> [!TIP]
> **HITL(Human-in-the-Loop) 적용 팁**: ⑧ 단계의 마케팅 초안 발송 전에 **Approval** 노드를 삽입하면, 담당자가 내용을 검토·수정한 뒤 최종 발송하는 안전한 워크플로우를 구성할 수 있습니다.

### 4) 🌐 글로벌 비즈니스 확장 시나리오
1. **공급망 리스크 선제 대응**:
   글로벌 공급망(SCM) 뉴스와 컨테이너 선적 상태를 실시간으로 웹 검색 ➡️ 항만 파업 감지 시 리스크 수준(High/Medium) AI 판단 ➡️ 대체 운송 루트 제안서 자동 생성 ➡️ SCM 파트장 결재 및 메일 발송 승인 대기 (**Human-in-the-loop**) ➡️ 긴급 대체 노선 예약 메일 발송.
2. **글로벌 고객 VoC 피드백 개선 루프**:
   해외 법인 다국어 오디오/이메일 클레임 수집 ➡️ 현지 언어 번역 및 주요 페인포인트 분류 ➡️ AI가 핵심 부서 배정 제안 ➡️ 제품 책임자 승인 ➡️ 즉시 Jira 티켓 생성 및 협업.



---
