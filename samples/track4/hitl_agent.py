"""
Track 4.2: Human-in-the-Loop (HITL) ERP Expenditure Approval Agent
Google ADK 2.3.0 및 Gemini 3.6 Flash 기반 지출 결재 및 전결 거버넌스 에이전트

[배포 및 연동 대상]
- Vertex AI Agent Runtime (Reasoning Engine)
- Gemini Enterprise 사내 앱 (Agent Registry ADK Mode)
"""

import os
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

# 최신 Vertex AI 추론 모델 지정 (Gemini 3.6 Flash)
# ==============================================================================
# [엔터프라이즈 백엔드 설정: Google Cloud Vertex AI 연동]
# GOOGLE_GENAI_USE_VERTEXAI="TRUE" 설정을 통해 AI Studio API Key 대신
# Google Cloud ADC(gcloud auth) 인증 및 Vertex AI API(aiplatform.googleapis.com)를 호출합니다.
# 이를 통해 엔터프라이즈 보안 거버넌스(데이터 비학습, VPC-SC, IAM)가 자동 적용됩니다.
# ==============================================================================
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "TRUE")
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")

MODEL_NAME = "gemini-3.6-flash"


def check_department_budget(department: str) -> dict:
    """부서별 당월 잔여 예산 한도를 조회합니다.

    Args:
        department: 신청 부서명 (예: '마케팅팀', '개발1팀', '영업본부')

    Returns:
        총 배정 예산, 기집행액, 잔여 예산 정보
    """
    # 실제 환경에서는 SAP, Oracle 등 사내 ERP/DB API와 연동됩니다.
    budgets = {
        "마케팅팀": {"total": 50000000, "spent": 32000000, "remaining": 18000000},
        "개발1팀": {"total": 80000000, "spent": 45000000, "remaining": 35000000},
        "영업본부": {"total": 60000000, "spent": 58000000, "remaining": 2000000},
    }
    # 미등록 부서인 경우 기본 표준 예산 정보 반환
    return budgets.get(department, {"total": 30000000, "spent": 10000000, "remaining": 20000000})


def evaluate_and_request_approval(department: str, amount: int, item_name: str, reason: str) -> dict:
    """지출 결재를 요청하고 전결 규정에 따라 자동 승인 또는 인간 관리자(HITL) 결재 티켓을 발급합니다.

    Args:
        department: 신청 부서
        amount: 지출 요청 금액 (단위: KRW 원)
        item_name: 지출 항목명
        reason: 지출 사유

    Returns:
        결재 상태 (AUTO_APPROVED 또는 REQUIRES_HUMAN_APPROVAL) 및 승인 티켓 정보
    """
    # 전결 규정 기준 금액: 3,000,000 KRW (300만 원)
    APPROVAL_THRESHOLD = 3000000
    budget_info = check_department_budget(department)

    # 1. 잔여 예산 초과 검증 (Budget Guardrail)
    if amount > budget_info["remaining"]:
        return {
            "status": "REJECTED_BUDGET_EXCEEDED",
            "department": department,
            "request_amount_krw": amount,
            "remaining_budget_krw": budget_info["remaining"],
            "message": f"잔여 예산({budget_info['remaining']:,}원)을 초과하여 결재 신청이 자동 반려되었습니다.",
        }

    # 2. 전결 기준 금액 초과 시 Human-in-the-Loop 분기 (관리자 결재 티켓 생성)
    if amount > APPROVAL_THRESHOLD:
        ticket_id = f"APPR-2026-{abs(hash(item_name + reason)) % 10000:04d}"
        return {
            "status": "REQUIRES_HUMAN_APPROVAL",
            "ticket_id": ticket_id,
            "threshold_krw": APPROVAL_THRESHOLD,
            "request_amount_krw": amount,
            "message": f"지출 금액({amount:,}원)이 전결 기준({APPROVAL_THRESHOLD:,}원)을 초과하여 부서장 결재 티켓이 발급되었습니다.",
            "approval_link": f"https://erp.enterprise-corp.com/approvals/{ticket_id}"
        }

    # 3. 전결 기준 이하 시 자동 승인 (Auto-Approval)
    return {
        "status": "AUTO_APPROVED",
        "ticket_id": f"AUTO-{abs(hash(item_name)) % 10000:04d}",
        "request_amount_krw": amount,
        "message": f"{department}의 {item_name} 지출 건({amount:,}원)이 전결 규정에 따라 자동 승인되었습니다."
    }


# Google ADK Agent 정의
root_agent = Agent(
    name="erp_approval_bot",
    model=Gemini(
        model=MODEL_NAME,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""당신은 사내 전사적 자원 관리(ERP) 지출 결재를 총괄하는 거버넌스 에이전트입니다.
1. 사용자의 요청에서 부서, 품목, 금액, 사유를 정확히 추출하세요.
2. `check_department_budget` 도구를 호출하여 해당 부서의 예산 잔액을 먼저 확인하세요.
3. `evaluate_and_request_approval` 도구를 호출하여 전결 규정 준수 여부를 검토하고 결과를 안내하세요.
4. 관리자 승인이 필요한 경우 승인 링크와 티켓 번호를 강조하여 사용자에게 친절하게 브리핑하세요.""",
    tools=[check_department_budget, evaluate_and_request_approval],
)

# Agent App 래핑
app = App(root_agent=root_agent, name="erp_approval_app")

