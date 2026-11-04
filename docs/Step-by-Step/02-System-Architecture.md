# 02. 시스템 아키텍처

> 개념 아키텍처. 인프라 소스와 배포 검증 전까지 "개념적"으로 취급한다.

## 1. 논리 아키텍처

```mermaid
flowchart LR
  subgraph CH["Channel (고객 M365 테넌트)"]
    RM["Relationship Manager"]
    COP["M365 Copilot + Declarative agent"]
  end
  subgraph ID["Identity"]
    ENTRA["Entra ID (SSO, OBO, 그룹)"]
  end
  subgraph SUB["고객 Azure 구독: Managed Application"]
    APIM["API Management (인증, 쓰로틀)"]
    API["RM Insight API (Container Apps)"]
    ORCH["Orchestrator: 질의 계획, 근거 조립"]
    SCORE["Scoring Engine: 위험/기회 (결정론)"]
    AOAI["Azure OpenAI (고객 배포, 학습 미사용)"]
    SRCH["Azure AI Search (ACL 필터)"]
    SQL["Azure SQL / ADLS: 거래, 계정 ACL"]
    ING["Ingestion: Functions + Data Factory"]
    KV["Key Vault"]
    MON["Log Analytics + App Insights + 불변 Storage"]
  end
  subgraph SRC["Data Sources"]
    CRM["CRM (Dataverse)"]
    MAIL["Exchange (Graph)"]
    TXN["거래 시스템"]
    KB["내부 지식 (SharePoint/Blob)"]
  end
  subgraph PUB["퍼블리셔 (제어면)"]
    MKT["Marketplace + Managed App 정의"]
    OPS["Lighthouse/JIT 지원 접근"]
  end
  RM --> COP -->|"토큰"| ENTRA
  COP -->|"OpenAPI"| APIM --> API
  API -->|"OBO"| ENTRA
  API --> ORCH
  ORCH --> SRCH
  ORCH --> SQL
  ORCH --> SCORE
  ORCH --> AOAI
  CRM --> ING
  MAIL --> ING
  TXN --> ING
  KB --> ING
  ING --> SRCH
  ING --> SQL
  API --> KV
  API --> MON
  MKT -.->|"배포/업데이트"| SUB
  OPS -.->|"JIT, 승인, 감사"| SUB
```

## 2. 컴포넌트 책임

| 컴포넌트 | 책임 | 구현 기술 |
|---|---|---|
| Declarative agent | 지침, 대화 시작, API plugin 연결 | M365 Agents Toolkit |
| API Management | JWT 검증, 쿼터, 상관 ID 주입 | APIM Standard v2 |
| RM Insight API | 요청 검증, OBO, 응답 구성 | Python FastAPI 또는 .NET Minimal API |
| Orchestrator | 계정 해석, 허용 계정 집합 계산, 검색/조회, 근거 패키지 생성 | 앱 코드 |
| Scoring Engine | 위험/기회 점수 산출(규칙 + 통계), 산식 버전 | 앱 코드 (모델 호출 없음) |
| Azure OpenAI | 근거 패키지를 문장화, 인용 형식 준수 | gpt-4o 계열 배포 |
| AI Search | 하이브리드(키워드+벡터) 검색, ACL 필터 | 인덱스 + 인덱서/푸시 |
| Ingestion | 소스별 정규화, ACL 동기화, 청킹, 임베딩 | Functions, ADF |
| Monitoring | 요청 트레이스, 감사 이벤트, 알림 | Log Analytics, 진단 설정 |

## 3. 요청 흐름 (시퀀스)

```mermaid
sequenceDiagram
  participant RM
  participant COP as Copilot
  participant API as RM Insight API
  participant AAD as Entra
  participant ORC as Orchestrator
  participant S as AI Search
  participant DB as SQL
  participant LLM as Azure OpenAI
  participant LOG as Audit log
  RM->>COP: "ACME 계정 위험과 다음 조치는?"
  COP->>API: POST /accounts/insights (Bearer 사용자 토큰)
  API->>AAD: OBO 토큰 교환 + 그룹 조회
  API->>ORC: 사용자 컨텍스트 (oid, groups, correlationId)
  ORC->>DB: 허용 계정 ID 계산 (ACL)
  alt 계정 비허용
    ORC->>LOG: access_denied
    API-->>COP: 404 (존재 비공개)
  else 허용
    ORC->>S: 검색 + filter(accountId, aclGroups)
    ORC->>DB: 거래 집계 (허용 계정만)
    ORC->>ORC: 위험/기회 점수 (결정론)
    ORC->>LLM: 근거 패키지 + 인용 ID 지시
    LLM-->>ORC: 문장 + citation IDs
    ORC->>ORC: 인용 검증 (미인용 문장 제거)
    ORC->>LOG: query_answered (근거 ID 목록)
    API-->>COP: 요약 + citations[]
  end
  COP-->>RM: 답변 + 출처 링크
```

## 4. 배포 토폴로지

| 영역 | 소유 | 내용 |
|---|---|---|
| 고객 구독, 고객 RG | 고객 | 데이터 서비스(SQL, ADLS, Search), Key Vault, 네트워크 |
| 고객 구독, 관리 RG | 퍼블리셔(거부 할당으로 보호) | API, Orchestrator, APIM, 모니터링 구성 |
| 퍼블리셔 테넌트 | 퍼블리셔 | 이미지 레지스트리, Managed App 정의, 지원 도구 |

> 결정 필요: 데이터 서비스를 관리 RG(퍼블리셔 운영)에 둘지 고객 RG에 둘지는 [ADR-003](09-Review-and-ADR.md)에서 다룬다. 기본은 **데이터는 고객 RG, 컴퓨트는 관리 RG**.

## 5. 신뢰 경계

1. M365 테넌트 ↔ Azure 구독: Entra 토큰, APIM 검증.
2. 관리 RG ↔ 고객 RG: Managed Identity와 Private Endpoint만 허용.
3. 앱 ↔ 모델: 고객 구독 내 Azure OpenAI, 프롬프트는 **허용된 근거만** 포함.
4. 퍼블리셔 ↔ 고객: JIT 승인, 모든 작업은 고객 로그에 기록.
