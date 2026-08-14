#!/usr/bin/env bash
# ==============================================================================
# Track 4: Custom Agent Deployment & Gemini Enterprise Registration Script
# Google ADK 2.3.0 & Vertex AI Agent Runtime 원클릭 배포 및 등록 스크립트
# ==============================================================================

set -euo pipefail

# ------------------------------------------------------------------------------
# [고객 환경 설정 안내]
# 실습 및 고객 프로젝트 환경에 맞추어 아래 환경 변수를 입력하세요.
# 터미널에서 export GOOGLE_CLOUD_PROJECT="내-프로젝트-ID" 형태로 미리 설정할 수도 있습니다.
# ------------------------------------------------------------------------------
PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-YOUR_GCP_PROJECT_ID}"
REGION="${GOOGLE_CLOUD_REGION:-us-central1}"

# Gemini Enterprise App 전체 리소스 ID
# 확인 경로: Cloud Console > Gemini Enterprise > 앱 선택 > 엔진 설정
# 형식: projects/{PROJECT_NUMBER}/locations/global/collections/default_collection/engines/{APP_ID}
GE_APP_ID="${GEMINI_ENTERPRISE_APP_ID:-projects/YOUR_PROJECT_NUMBER/locations/global/collections/default_collection/engines/YOUR_APP_ID}"

echo "=========================================================="
echo "🚀 1. Google Cloud 환경 및 프로젝트 설정"
echo "   - Project ID: ${PROJECT_ID}"
echo "   - Region:     ${REGION}"
echo "   - GE App ID:  ${GE_APP_ID}"
echo "=========================================================="

if [[ "${PROJECT_ID}" == "YOUR_GCP_PROJECT_ID" ]]; then
  echo "⚠️ [주의] PROJECT_ID를 고객 환경의 실제 GCP 프로젝트 ID로 변경하세요."
  echo "   예: export GOOGLE_CLOUD_PROJECT=\"my-company-ai-project\""
fi

gcloud config set project "${PROJECT_ID}"
export GOOGLE_CLOUD_PROJECT="${PROJECT_ID}"
export GOOGLE_CLOUD_LOCATION="global"
export GOOGLE_GENAI_USE_VERTEXAI="TRUE"

echo "=========================================================="
echo "📦 2. Agent Runtime (Vertex AI Reasoning Engine) 배포"
echo "=========================================================="
# agents-cli를 활용하여 Agent Runtime으로 컨테이너 배포 수행
# 배포 완료 후 출력되는 Reasoning Engine 리소스 ID를 확인하세요.
agents-cli deploy \
  --project="${PROJECT_ID}" \
  --region="${REGION}" \
  --deployment-target=agent_runtime \
  --service-name="track4-custom-agent" \
  --no-confirm-project

echo "=========================================================="
echo "🏢 3. Gemini Enterprise 커스텀 에이전트 등록"
echo "=========================================================="
# Gemini Enterprise 사내 앱에 ADK 네이티브 연동(StreamQuery IAM) 모드로 등록
agents-cli publish gemini-enterprise \
  --gemini-enterprise-app-id="${GE_APP_ID}" \
  --display-name="Track 4 Custom Agent" \
  --description="BigQuery 분석, HITL ERP 결재, Multi-Agent 협업 전담 커스텀 에이전트" \
  --tool-description="BigQuery 데이터 분석, ERP 결재 승인, CAGR 성장률 계산" \
  --registration-type=adk

echo "=========================================================="
echo "✅ 배포 및 Gemini Enterprise 등록 완료!"
echo "   사내 Gemini Enterprise 채팅창에서 커스텀 에이전트를 테스트하세요."
echo "=========================================================="

