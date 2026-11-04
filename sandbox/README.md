# 샌드박스 구현 README

## 개요

이것은 **Relationship Manager Intelligence Experience** 아키텍처의 end-to-end 기능적 시안(Functional Prototype)입니다.

### 구현 범위
- ✅ 데이터 수집 및 검색 인덱싱
- ✅ 신원 관리 및 접근 통제 (OBO 토큰, ACL 필터링)
- ✅ API 오케스트레이션 (요청→근거 조립→LLM→응답)
- ✅ 감사 로깅 및 모니터링
- ✅ End-to-End 시나리오 검증

### 주요 성과
- **5개 End-to-End 시나리오 모두 성공**
- **권한 기반 접근 통제 검증**
- **감사 로그 불변성 확인**
- **인용(Citation) 기반 응답 생성**

---

## 아키텍처

```
┌─────────────────────────────────────────────────────────┐
│                  RM Query (M365 Copilot)                │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│           FastAPI (APIM 시뮬레이션)                      │
│     • 인증 (Bearer Token)                               │
│     • 상관ID 주입                                        │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│            Orchestrator (Main Logic)                    │
│  1. OBO 토큰 검증 (Identity Service)                    │
│  2. ACL 확인 (권한 없음 → 404)                          │
│  3. 근거 검색 (Search Service + ACL Filter)             │
│  4. 점수 계산 (Scoring Engine - 결정론)                 │
│  5. 텍스트 생성 (LLM Mock)                              │
│  6. 인용 검증 (미인용 문장 제거)                         │
│  7. 감사 로그 기록                                       │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
     [Search]   [Scoring]  [Audit]
      Index      Engine     Log
     (In-mem)    (Rules)    (JSON)
```

---

## 디렉토리 구조

```
sandbox/
├── data/
│   ├── accounts.json              # CRM 계정 4개 (ACME, TechVision, FinanceHub, RetailMax)
│   ├── transactions.json          # 거래 기록 7개
│   ├── emails.json                # 이메일 5개
│   ├── documents.json             # 지식 문서 5개
│   ├── account_acls.json          # 계정별 접근 권한
│   └── users.json                 # 테스트 사용자 5명
│
├── api/
│   ├── main.py                    # FastAPI 애플리케이션
│   ├── models.py                  # Pydantic 스키마
│   ├── orchestrator.py            # Main orchestration logic
│   ├── identity_service.py        # OBO, ACL 검증
│   ├── search_service.py          # In-memory 검색 + ACL 필터
│   ├── scoring.py                 # 위험/기회 점수 (결정론)
│   ├── llm_service.py             # LLM Mock (근거→문장화)
│   ├── audit_log.py               # 불변 감사 로그
│   └── requirements.txt
│
├── tests/
│   └── scenarios.py               # 5개 End-to-End 시나리오
│
└── README.md                       # 이 파일
```

---

## 테스트 사용자

| OID   | 이름 | 그룹 | 권한 |
|-------|------|------|------|
| user1 | Alice Chen | group-sales-east, group-finance | ACME001, FINANCE003 |
| user2 | Bob Johnson | group-sales-west, group-executive | TECH002 |
| user3 | Carol Martinez | group-finance, group-executive | FINANCE003 |
| user4 | David Lee | group-sales-south | RETAIL004 |
| user5 | Emma Wilson | group-sales-east, group-finance, group-executive | ACME001, FINANCE003 |

---

## 시나리오 설명

### Scenario 1: 권한 있는 사용자 (✅ PASSED)
```
User: user1 (Alice Chen)
Account: ACME001 (ACME Corporation)
Request: GET /accounts/ACME001/insights
Expected: 200 OK with risks, opportunities, citations

결과:
✅ 요청 성공
✅ 위험 분석: Engagement Decline (7.0/10) 감지
✅ 다음 단계: 긴급 비즈니스 리뷰 제안
```

### Scenario 2: 권한 없는 사용자 (✅ PASSED)
```
User: user4 (David Lee - group-sales-south 만 있음)
Account: ACME001 (requires: group-sales-east or group-finance)
Request: GET /accounts/ACME001/insights
Expected: 404 Not Found (권한 없음을 노출하지 않음)

결과:
✅ 404 반환 (권한 누설 없음)
✅ 감사 로그에 access_denied 기록
```

### Scenario 3: 감사 로깅 (✅ PASSED)
```
모든 요청과 접근 결정이 JSONL 형식으로 로그됨

로그 이벤트:
  • query_answered (성공한 쿼리)
  • access_denied (권한 거부)
  • search_executed (검색 실행)
  • auth_failed (인증 실패)
  • error (오류)
```

### Scenario 4: 인용 검증 (✅ PASSED)
```
모든 응답에는 sourceUri와 출처 정보가 포함됨
미인용 문장은 응답에서 제거됨

Citations:
  • sourceUri: 원본 문서 참조 ID
  • confidence: 0.0-1.0 신뢰도
  • source: email, transaction, document 등
```

### Scenario 5: 계정 프로필 분석 (✅ PASSED)
```
각 계정의 특성에 따른 다양한 인사이트:

ACME001:     위험 프로필 (매출 감소 추세)
TECH002:     성장 프로필 (확장 계획, 신규 채용)
FINANCE003:  전략 파트너십 (아시아 확장 논의)
```

---

## 실행 방법

### 1. 환경 준비
```bash
cd sandbox
pip install -r api/requirements.txt
```

### 2. End-to-End 시나리오 실행
```bash
python3 tests/scenarios.py
```

출력:
```
================================================================================
RM INTELLIGENCE EXPERIENCE - END-TO-END SANDBOX SIMULATION
================================================================================

SCENARIO 1: Authorized User Viewing Account Insights
✅ REQUEST SUCCESSFUL
...

TEST SUMMARY
================================================================================
Scenario 1: Authorized User: ✅ PASSED
Scenario 2: Unauthorized User: ✅ PASSED
Scenario 3: Audit Logging: ✅ PASSED
Scenario 4: Citation Validation: ✅ PASSED
Scenario 5: Account Profiles: ✅ PASSED

Total: 5/5 scenarios passed
```

### 3. API 서버 시작 (선택)
```bash
cd api
python3 main.py
```

서버가 `http://localhost:8000`에서 실행됨

### 4. API 테스트
```bash
# 디버그 엔드포인트: 사용자 목록 조회
curl http://localhost:8000/debug/users

# 디버그 엔드포인트: 계정 목록 조회
curl http://localhost:8000/debug/accounts

# Insight 요청
curl -X POST http://localhost:8000/api/v1/accounts/ACME001/insights \
  -H "Authorization: Bearer user1" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the risks?", "detailLevel": "summary"}'
```

---

## API 엔드포인트

### Insight 조회
```http
POST /api/v1/accounts/{accountId}/insights
Authorization: Bearer <user_oid>
X-Correlation-ID: <optional>

Request:
{
  "question": "What are the risks and opportunities?",
  "detailLevel": "summary"
}

Response 200:
{
  "accountId": "ACME001",
  "accountName": "ACME Corporation",
  "summary": "Account shows engagement decline...",
  "risks": [
    {"name": "Engagement Decline", "score": 7.0, "reason": "..."}
  ],
  "opportunities": [],
  "nextSteps": [
    {"action": "Schedule urgent review", "dueDate": "2026-11-10", ...}
  ],
  "citations": [
    {"text": "...", "sourceUri": "email_...", "confidence": 0.95, "source": "email"}
  ],
  "generatedAt": "2026-11-04T03:47:40Z"
}

Response 404:
{"error": "Not Found"}
```

### 검색
```http
GET /api/v1/search?q=revenue&accountId=ACME001&limit=10
Authorization: Bearer <user_oid>

Response:
{
  "query": "revenue",
  "results": [
    {
      "id": "...",
      "title": "...",
      "content": "...",
      "source": "transaction",
      "sourceUri": "...",
      "score": 0.95
    }
  ],
  "total": 5,
  "filtered_by_acl": true
}
```

### 감시 로그 (관리자)
```http
GET /api/v1/audit-logs?eventType=query_answered&limit=50
Authorization: Bearer <user_oid>

Response:
{
  "logs": [
    {
      "timestamp": "2026-11-04T03:47:40Z",
      "eventType": "query_answered",
      "userId": "user1",
      "accountId": "ACME001",
      "status": "success",
      "citationIds": ["email_...", "transaction_..."]
    }
  ],
  "total": 5,
  "filters": {...}
}
```

---

## 핵심 구현 특징

### 1. 신원 및 접근 통제 (Identity Service)
- **OBO (On-Behalf-Of)**: 사용자 토큰을 API 호출용으로 교환
- **ACL 검증**: 계정별 허용 사용자/그룹 확인
- **권한 누설 방지**: 권한 없을 때 404 반환 (계정 존재 여부 공개 안 함)

### 2. 검색 & 필터링 (Search Service)
- **In-memory 인덱스**: 4개 데이터 소스 통합 (계정, 거래, 이메일, 문서)
- **ACL 필터링**: 검색 결과를 사용자의 허용 계정만 반환
- **관련성 점수**: 간단한 키워드 매칭 + 최근성 부스트

### 3. 점수 계산 (Scoring Engine)
- **위험 지표**:
  - 매출 감소 (>15% 기준)
  - 소통 감소 (이메일 빈도, 우려 키워드)
  - 계정 상태 (At Risk 마크)
- **기회 지표**:
  - 성장 확장 (확장, 채용, 펀딩 언급)
  - 전략 파트너십 (파트너십, 지역 확장)
  - 서비스 강화 (지원 개선 기회)
- **결정론**: 모든 계산은 규칙 기반 (ML 모델 없음)

### 4. LLM Mock (LLM Service)
- **근거 기반**: 점수와 이유를 자연어로 변환
- **인용 추적**: 각 사실에 sourceUri 연결
- **다음 단계 생성**: 위험 수준에 따른 권장 조치

### 5. 감사 로깅 (Audit Logger)
- **불변 기록**: JSONL 형식 append-only
- **포괄적 이벤트**:
  - query_answered: 질의 응답
  - access_denied: 권한 거부
  - search_executed: 검색 실행
  - auth_failed: 인증 실패
  - error: 오류 발생
- **추적 가능성**: correlationId로 전체 요청 추적

---

## 데이터 모델

### Mock 데이터셋 구성

| 엔티티 | 개수 | 용도 |
|--------|------|------|
| Accounts | 4 | CRM 계정: ACME, TechVision, FinanceHub, RetailMax |
| Transactions | 7 | 거래 기록 (매출 추세 분석용) |
| Emails | 5 | 소통 기록 (소통 빈도, 우려 신호 분석용) |
| Documents | 5 | 내부 지식 (위험, 기회 분석 근거) |
| ACLs | 4 | 계정별 접근 권한 |
| Users | 5 | 테스트 사용자 |

### 검색 인덱스 스키마
```json
{
  "id": "doc_acme_q1_report",
  "accountId": "ACME001",
  "title": "ACME Q3 2024 Performance Report",
  "content": "Revenue declined 20% YoY...",
  "category": "financial_report",
  "source": "document",
  "sourceUri": "document_doc_acme_q1_report",
  "aclGroups": ["group-sales-east", "group-finance"],
  "score": 0.95
}
```

---

## 감사 로그 분석

### 로그 파일 위치
```
.copilot-tracking/audit_log.jsonl
```

### 로그 통계 확인
```python
from sandbox.api.audit_log import AuditLogger

logger = AuditLogger()
stats = logger.get_statistics()
print(stats)
# {
#   'total_events': 10,
#   'by_type': {'query_answered': 5, 'access_denied': 3, 'search_executed': 2},
#   'by_user': {'user1': 6, 'user4': 3, 'unknown': 1},
#   'by_status': {'success': 7, 'denied': 3}
# }
```

### 로그 조회
```python
logs = logger.get_logs(
    event_type="query_answered",
    user_id="user1",
    limit=10
)
```

---

## 성공 기준 검증

| 기준 | 검증 방법 | 결과 |
|------|---------|------|
| End-to-end 요청 처리 | POST /accounts/ACME001/insights | ✅ 200 OK |
| ACL 필터링 작동 | 권한 없는 사용자 요청 | ✅ 404 |
| 인용 검증 | Response citations 확인 | ✅ sourceUri 포함 |
| 감사 로깅 | audit_log.jsonl 확인 | ✅ 모든 이벤트 기록 |
| 접근 통제 | 권한 없는 계정 검색 제외 | ✅ 필터됨 |

---

## 향후 확장

### Phase 2: 실제 배포
- [ ] Bicep 템플릿 컴파일 및 배포
- [ ] Azure OpenAI 통합 (Mock 대체)
- [ ] Azure AI Search 통합 (벡터 임베딩)
- [ ] Managed Application 패키징

### Phase 3: 성능 & 보안
- [ ] 부하 테스트 (목표: p95 10초)
- [ ] 보안 위협 모델링 (STRIDE)
- [ ] 암호화 (Key Vault, Private Endpoints)
- [ ] 규정 준수 검증

### Phase 4: Declarative Agent 통합
- [ ] OpenAPI 스펙 생성 및 검증
- [ ] Agent 매니페스트 작성
- [ ] M365 Copilot 채널 통합
- [ ] 사용자 수용 테스트 (UAT)

---

## 참고 문서

| 단계 | 문서 | 매핑 |
|------|------|------|
| 개요 | Step-by-Step/00-Overview.md | 범위, 원칙, 가정 |
| 요구사항 | Step-by-Step/01-Context-and-Requirements.md | FR/NFR |
| 아키텍처 | Step-by-Step/02-System-Architecture.md | 논리/배포 다이어그램 |
| 신원 | Step-by-Step/04-Identity-and-Access.md | OBO, ACL 구현 |
| 검색 | Step-by-Step/05-Data-and-Search.md | 인덱싱, 필터링 |
| LLM | Step-by-Step/06-AI-Safeguards.md | 근거 강제, 인용 |
| API | Step-by-Step/07-API-and-Agent-Contract.md | OpenAPI 스펙 |
| 감시 | Step-by-Step/08-Observability-and-Audit.md | 로그 스키마 |

---

## 문제 해결

### "ModuleNotFoundError: No module named 'pydantic'"
```bash
pip install pydantic python-dateutil fastapi uvicorn
```

### "Access Denied but should pass"
- ACL 확인: `data/account_acls.json` 에서 사용자 그룹이 계정에 포함되어 있는지 확인
- 사용자 그룹 확인: `data/users.json` 에서 사용자의 그룹 목록 확인

### "Audit log file not found"
```bash
mkdir -p .copilot-tracking
```

---

## 라이선스 & 기여

이 구현은 Step-by-Step 가이드(00-11)를 기반으로 합니다.
기여하려면 PR을 제출해주세요.

---

**생성일**: 2026-11-04  
**버전**: 0.1.0 (Functional Prototype)  
**상태**: 모든 시나리오 성공 ✅
