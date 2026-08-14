"""
Track 4.1: BigQuery Data & SQL Analytics Agent
Google ADK 2.3.0 및 Gemini 3.6 Flash 기반 엔터프라이즈 데이터 분석 커스텀 에이전트

[배포 및 연동 대상]
- Vertex AI Agent Runtime (Reasoning Engine)
- Gemini Enterprise 사내 앱 (Agent Registry ADK Mode)
"""

import os
from typing import Optional
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.cloud import bigquery
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


def get_table_schema(table_id: str) -> dict:
    """BigQuery 테이블의 컬럼 이름, 데이터 타입, 설명 등 스키마 메타데이터를 동적으로 조회합니다.

    Args:
        table_id: 완전한 BigQuery 테이블 ID
                  - 공개 데이터셋 예시: 'bigquery-public-data.thelook_ecommerce.orders'
                  - 사내 자체 테이블 예시: 'YOUR_PROJECT_ID.YOUR_DATASET.YOUR_TABLE'

    Returns:
        테이블의 총 행 수와 각 필드별 상세 스키마 딕셔너리
    """
    # 환경 변수에서 GCP Project ID 로드 (미설정 시 기본값 안내)
    # [고객 환경 설정]: gcloud config get-value project 로 확인한 프로젝트 ID를 주입하세요.
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "YOUR_GCP_PROJECT_ID")
    
    try:
        client = bigquery.Client(project=project_id)
        table = client.get_table(table_id.strip().strip("`"))
        fields = [
            {
                "name": field.name,
                "type": field.field_type,
                "mode": field.mode,
                "description": field.description or "설명 없음"
            }
            for field in table.schema
        ]
        return {
            "status": "SUCCESS",
            "table_id": table_id,
            "num_rows": table.num_rows,
            "fields": fields
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "message": f"테이블 스키마 조회 실패 ({table_id}): {str(e)}",
            "hint": "테이블 경로(프로젝트.데이터셋.테이블)와 IAM 권한(BigQuery Data Viewer)을 확인하세요."
        }


def query_bigquery_table(sql_query: str) -> dict:
    """읽기 전용 보안 가드레일을 통과한 표준 SQL을 BigQuery에서 실행하고 레코드를 반환합니다.

    Args:
        sql_query: 실행할 표준 GoogleSQL SELECT 쿼리문
                   (예: SELECT status, count(*) FROM `bigquery-public-data.thelook_ecommerce.orders` GROUP BY 1)

    Returns:
        조회된 실제 BigQuery 레코드 목록과 행 수
    """
    # 1. 엔터프라이즈 보안 가드레일: DML/DDL(UPDATE, DELETE, INSERT, DROP) 차단
    clean_sql = sql_query.strip().upper()
    if not clean_sql.startswith("SELECT") and not clean_sql.startswith("WITH"):
        return {"error": "보안 정책상 SELECT 및 WITH 읽기 전용 쿼리만 실행할 수 있습니다."}

    # 2. BigQuery 클라이언트 초기화 및 쿼리 실행
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "YOUR_GCP_PROJECT_ID")
    try:
        client = bigquery.Client(project=project_id)
        job = client.query(sql_query)
        # 네트워크/메모리 보호를 위해 최대 50건으로 레코드 제한
        rows = [dict(row) for row in job.result(max_results=50)]
        return {
            "status": "SUCCESS",
            "row_count": len(rows),
            "records": rows
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "error_detail": str(e),
            "guidance": "BigQuery 테이블 경로를 정확히 지정하거나 공개 데이터셋(`bigquery-public-data.thelook_ecommerce.orders`)을 질의하세요."
        }


# 3. Google ADK Agent 정의 및 도구 바인딩
root_agent = Agent(
    name="bigquery_data_analyst",
    model=Gemini(
        model=MODEL_NAME,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""당신은 Google Cloud BigQuery 기반의 엔터프라이즈 데이터 분석 전문가입니다.

[동작 원칙]
1. 테이블 스키마 파악: 특정 테이블에 대한 구체적인 분석 요청이 오면 먼저 `get_table_schema`를 호출하여 정확한 컬럼명과 타입을 확인하세요.
2. 표준 SQL 작성 및 실행: 스키마를 기반으로 표준 GoogleSQL(Standard SQL) SELECT 쿼리를 작성하여 `query_bigquery_table`을 호출하세요.
   - 공개 이커머스 데이터셋: `bigquery-public-data.thelook_ecommerce.orders`
   - 사내 자체 매출 데이터셋: `YOUR_GCP_PROJECT_ID.retail_data.sales_records`
3. 분석 및 시각화 브리핑: 반환된 실제 쿼리 레코드를 바탕으로 경영진이 직관적으로 이해할 수 있는 마크다운 표와 3줄 핵심 인사이트(Key Takeaways)를 작성하세요.
4. 보안 가드레일: 읽기 전용(SELECT/WITH) 쿼리만 생성하며 DDL/DML(UPDATE, DELETE 등)은 절대 실행하지 않습니다.""",
    tools=[get_table_schema, query_bigquery_table],
)

# 4. Agent App 래핑 (FastAPI 및 Agent Runtime 서빙 규격)
app = App(root_agent=root_agent, name="bigquery_analytics_app")


