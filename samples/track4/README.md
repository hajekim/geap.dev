# Track 4 Custom Agent Solutions : Deployment & Sample Kit

Google ADK 2.3.0 및 Vertex AI Agent Runtime, Gemini Enterprise 연동을 위한 실전 커스텀 에이전트 소스코드 패키지입니다.

---

## 1. 엔터프라이즈 백엔드 연동 원리 (Vertex AI vs Google AI Studio)

본 샘플 코드는 **Google Cloud Vertex AI API (`aiplatform.googleapis.com`)**를 호출하도록 설계되어 있습니다.

- **Vertex AI 호출 메커니즘**:
  - `GOOGLE_GENAI_USE_VERTEXAI="TRUE"` 환경 변수 적용
  - Google Cloud Application Default Credentials (ADC) 인증 사용 (`gcloud auth login`)
  - **보안 및 거버넌스 보장**: 고객 입력 데이터의 모델 재학습 미사용, VPC Service Controls(VPC-SC) 지원, IAM 기반 세분화된 권한 제어.
- **AI Studio와의 차이점**:
  - AI Studio는 개별 `GEMINI_API_KEY`를 사용하는 개인/프로토타이핑 환경입니다.
  - 본 실습 코드는 전사 보안 규정을 준수하는 **Vertex AI 엔터프라이즈 추론 백엔드**를 호출합니다.

---

## 2. 패키지 구성 파일

- `data_agent.py`: BigQuery 데이터 스키마 탐색 및 안전한 SQL 조회 분석 에이전트 (4.1)
- `hitl_agent.py`: 전결 규정(300만 원) 기반 인간 관리자 승인(HITL) ERP 결재 에이전트 (4.2)
- `multi_agent.py`: 시장 조사 & 재무 CAGR 계산 서브 에이전트 및 수석 디렉터 오케스트레이션 파이프라인 (4.3)
- `deploy.sh`: Vertex AI Agent Runtime 배포 및 Gemini Enterprise 사내 앱 등록 자동화 스크립트 (4.4)
- `pyproject.toml` / `requirements.txt`: 의존성 정의 파일

---

## 3. 사전 준비 사항 (Prerequisites)

1. **Google Cloud CLI 및 인증**:
   ```bash
   gcloud auth login
   gcloud auth application-default login
   ```
2. **필수 GCP API 활성화**:
   ```bash
   gcloud services enable aiplatform.googleapis.com discoveryengine.googleapis.com bigquery.googleapis.com
   ```
3. **필수 패키지 설치**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. 환경 변수 설정 (Configuration)

본인의 GCP 프로젝트 및 Gemini Enterprise 환경에 맞추어 환경 변수를 설정합니다:

```bash
# 1. 대상 GCP 프로젝트 ID 설정
export GOOGLE_CLOUD_PROJECT="YOUR_GCP_PROJECT_ID"
export REGION="us-central1"

# 2. Vertex AI 백엔드 호출 플래그
export GOOGLE_GENAI_USE_VERTEXAI="TRUE"
export GOOGLE_CLOUD_LOCATION="global"

# 3. Gemini Enterprise App 리소스 ID 설정 (Console > Gemini Enterprise > 엔진 관리)
export GE_APP_ID="projects/YOUR_PROJECT_NUMBER/locations/global/collections/default_collection/engines/YOUR_APP_ID"
```

---

## 5. 로컬 테스트 실행 (Local Test)

```bash
# 4.1 BigQuery 데이터 분석 에이전트 실행
python data_agent.py

# 4.2 HITL ERP 결재 에이전트 실행
python hitl_agent.py

# 4.3 멀티 에이전트 협업 파이프라인 실행
python multi_agent.py
```

---

## 6. 클라우드 배포 및 사내 앱 등록 (Deploy & Publish)

```bash
chmod +x deploy.sh
./deploy.sh
```

배포 완료 후 Vertex AI Reasoning Engine 및 Gemini Enterprise 사내 앱 콘솔에서 등록 상태를 확인하세요.
