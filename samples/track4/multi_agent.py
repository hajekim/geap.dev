"""
Track 4.3: Multi-Agent Collaboration Pipeline (A2A Multi-Agent System)
Google ADK 2.3.0 및 Gemini 3.6 Flash 기반 멀티 에이전트 협업 파이프라인

[아키텍처 구조]
1. Market Researcher (서브 에이전트): 산업별 트렌드 및 기회 요인 분석
2. Financial Analyst (서브 에이전트): calculate_cagr 툴을 활용한 연평균 성장률 및 ROI 산출
3. Strategy Director (총괄 수석 에이전트): 하위 에이전트들의 산출물을 오케스트레이션하여 C-Level 보고서 합성
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


def calculate_cagr(start_val: float, end_val: float, years: int) -> float:
    """초기값, 최종값, 경과 연수를 받아 연평균 복합 성장률(CAGR)을 수학적으로 계산합니다.

    Args:
        start_val: 기준 연도 시장 규모 (단위: 억 원 또는 백만 달러)
        end_val: 목표 연도 시장 규모 (단위: 억 원 또는 백만 달러)
        years: 경과 연수 (단위: 년)

    Returns:
        백분율(%) 형태의 CAGR 값 (소수점 둘째 자리 반올림)
    """
    if start_val <= 0 or years <= 0:
        return 0.0
    cagr = ((end_val / start_val) ** (1.0 / years) - 1.0) * 100.0
    return round(cagr, 2)


# 1. 시장 조사 전문 서브 에이전트 (Market Researcher)
researcher = Agent(
    name="market_researcher",
    model=Gemini(model=MODEL_NAME),
    instruction="""당신은 글로벌 IT 및 클라우드 시장 조사 전문 애널리스트입니다.
주요 산업별 AI 도입 동향, 경쟁 구도, 기회 요인을 구조화된 개조식으로 요약하여 제공하세요.""",
    description="글로벌 시장 및 기술 트렌드 조사를 전담하는 서브 에이전트",
)

# 2. 재무 및 비즈니스 타당성 분석 전문 서브 에이전트 (Financial Analyst)
financial_analyst = Agent(
    name="financial_analyst",
    model=Gemini(model=MODEL_NAME),
    instruction="""당신은 기업 재무 및 신사업 타당성 분석 전문가입니다.
시장 규모 데이터와 `calculate_cagr` 툴을 활용하여 연평균 성장률(CAGR)과 예상 매출 ROI를 산출하세요.""",
    tools=[calculate_cagr],
    description="재무 지표, CAGR 계산, ROI 분석을 전담하는 서브 에이전트",
)

# 3. 최상위 조율 총괄 디렉터 (Supervisor Agent)
strategy_director = Agent(
    name="strategy_director",
    model=Gemini(
        model=MODEL_NAME,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""당신은 신사업 전략 기획 총괄 수석 디렉터입니다.
사용자로부터 특정 산업 분야의 신사업 전략 보고서 요청이 들어오면:
1. 먼저 `market_researcher` 서브 에이전트를 호출하여 시장 기회와 트렌드를 파악하세요.
2. 그 다음 `financial_analyst` 서브 에이전트를 호출하여 성장률(CAGR)과 재무 지표를 계산하세요.
3. 두 서브 에이전트의 산출물을 종합하여 C-Level 경영진 보고용 '1-Page Strategy Blueprint'를 마크다운 표와 실행 로드맵으로 작성하세요.""",
    sub_agents=[researcher, financial_analyst],
)

# Agent App 래핑 (멀티 에이전트 통합 서빙)
app = App(root_agent=strategy_director, name="strategy_orchestrator_app")

