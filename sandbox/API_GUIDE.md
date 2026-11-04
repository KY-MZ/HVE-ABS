# API 가이드

## 빠른 시작

### 1단계: 환경 설정
```bash
cd sandbox
pip install -r api/requirements.txt
```

### 2단계: 시나리오 실행
```bash
python3 tests/scenarios.py
```

### 3단계: API 서버 실행 (선택사항)
```bash
cd sandbox/api
python3 main.py
```

서버가 시작되면 `http://localhost:8000`에서 접근 가능합니다.

---

## API 엔드포인트 레퍼런스

### 1. Insight 조회 (핵심)

**요청**
```http
POST /api/v1/accounts/{accountId}/insights
Authorization: Bearer {user_oid}
X-Correlation-ID: {optional-uuid}
Content-Type: application/json

{
  "question": "What are the key risks and opportunities for this account?",
  "detailLevel": "summary"
}
```

**응답 200 OK**
```json
{
  "accountId": "ACME001",
  "accountName": "ACME Corporation",
  "summary": "ACME Corporation is showing signs of engagement decline with a 20% YoY revenue decrease and reduced communication frequency.",
  "risks": [
    {
      "name": "Engagement Decline",
      "score": 7.0,
      "severity": "high",
      "reason": "Email frequency decreased 30% in recent months; revenue trending downward",
      "detectedFrom": ["email", "transaction"]
    }
  ],
  "opportunities": [],
  "nextSteps": [
    {
      "action": "Schedule urgent business review with account stakeholders",
      "priority": "urgent",
      "dueDate": "2026-11-10",
      "estimatedEffort": "2 hours",
      "expectedOutcome": "Identify root causes and recovery plan"
    }
  ],
  "citations": [
    {
      "text": "Revenue declined 20% YoY",
      "sourceUri": "transaction_tx001_2024q3",
      "confidence": 0.95,
      "source": "transaction",
      "extractedAt": "2026-11-04T03:47:40Z"
    }
  ],
  "generatedAt": "2026-11-04T03:47:40Z",
  "correlationId": "550e8400-e29b-41d4-a716-446655440000"
}
```

**응답 404 Not Found**
```json
{
  "error": "Not Found"
}
```

**응답 400 Bad Request**
```json
{
  "error": "Invalid request",
  "details": "detailLevel must be 'summary' or 'detailed'"
}
```

**응답 500 Server Error**
```json
{
  "error": "Internal Server Error",
  "details": "...",
  "correlationId": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

### 2. 검색

**요청**
```http
GET /api/v1/search
Authorization: Bearer {user_oid}
X-Correlation-ID: {optional-uuid}

Query Parameters:
  q (required): Search query string
  accountId (optional): Filter to specific account
  sourceType (optional): email, transaction, document
  limit (optional): Max results, default 10, max 100
```

**예제**
```bash
curl "http://localhost:8000/api/v1/search?q=revenue&accountId=ACME001&limit=10" \
  -H "Authorization: Bearer user1"
```

**응답 200 OK**
```json
{
  "query": "revenue",
  "results": [
    {
      "id": "tx001_2024q3",
      "title": "Q3 2024 Revenue Report",
      "content": "Revenue declined 20% YoY due to market conditions",
      "source": "transaction",
      "sourceUri": "transaction_tx001_2024q3",
      "accountId": "ACME001",
      "score": 0.95,
      "extractedAt": "2026-11-04T03:47:40Z"
    }
  ],
  "total": 5,
  "returned": 1,
  "filtered_by_acl": true,
  "correlationId": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

### 3. 감시 로그 (관리자 권한 필요)

**요청**
```http
GET /api/v1/audit-logs
Authorization: Bearer {user_oid}

Query Parameters:
  eventType (optional): query_answered, access_denied, search_executed, etc.
  userId (optional): Filter by user OID
  accountId (optional): Filter by account
  status (optional): success, denied, error
  limit (optional): Max results, default 50, max 1000
```

**예제**
```bash
curl "http://localhost:8000/api/v1/audit-logs?eventType=query_answered&userId=user1&limit=10" \
  -H "Authorization: Bearer user1"
```

**응답 200 OK**
```json
{
  "logs": [
    {
      "timestamp": "2026-11-04T03:47:40Z",
      "eventType": "query_answered",
      "userId": "user1",
      "accountId": "ACME001",
      "status": "success",
      "correlationId": "550e8400-e29b-41d4-a716-446655440000",
      "details": {
        "question": "What are the risks?",
        "citationCount": 3
      }
    }
  ],
  "total": 5,
  "returned": 5,
  "filters_applied": {
    "eventType": "query_answered",
    "userId": "user1"
  }
}
```

---

### 4. 헬스 체크

**요청**
```http
GET /health
```

**응답 200 OK**
```json
{
  "status": "healthy",
  "timestamp": "2026-11-04T03:47:40Z",
  "version": "0.1.0"
}
```

---

### 5. 디버그 유틸리티

#### 5.1 사용자 목록 조회
```bash
curl http://localhost:8000/debug/users
```

**응답**
```json
{
  "users": [
    {
      "oid": "user1",
      "name": "Alice Chen",
      "groups": ["group-sales-east", "group-finance"],
      "allowedAccounts": ["ACME001", "FINANCE003"]
    }
  ]
}
```

#### 5.2 계정 목록 조회
```bash
curl http://localhost:8000/debug/accounts
```

**응답**
```json
{
  "accounts": [
    {
      "id": "ACME001",
      "name": "ACME Corporation",
      "status": "at_risk",
      "ownerGroup": "group-sales-east"
    }
  ]
}
```

#### 5.3 검색 인덱스 통계
```bash
curl http://localhost:8000/debug/search-stats
```

**응답**
```json
{
  "indexSize": 5,
  "indexedDocuments": [
    {
      "id": "doc_acme_q1_report",
      "title": "ACME Q1 Report",
      "source": "document"
    }
  ]
}
```

---

## 사용 예제

### Python (requests 라이브러리)

```python
import requests
import json

# 설정
BASE_URL = "http://localhost:8000"
USER_OID = "user1"
HEADERS = {
    "Authorization": f"Bearer {USER_OID}",
    "Content-Type": "application/json"
}

# 1. Insight 조회
response = requests.post(
    f"{BASE_URL}/api/v1/accounts/ACME001/insights",
    headers=HEADERS,
    json={
        "question": "What are the risks and opportunities?",
        "detailLevel": "summary"
    }
)

print(f"Status: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# 2. 검색
response = requests.get(
    f"{BASE_URL}/api/v1/search?q=revenue&accountId=ACME001&limit=10",
    headers=HEADERS
)

print(json.dumps(response.json(), indent=2))

# 3. 감시 로그 조회
response = requests.get(
    f"{BASE_URL}/api/v1/audit-logs?eventType=query_answered&limit=10",
    headers=HEADERS
)

print(json.dumps(response.json(), indent=2))
```

### cURL

```bash
#!/bin/bash

BASE_URL="http://localhost:8000"
USER_OID="user1"

# 1. Insight 요청
echo "=== Insight Request ==="
curl -X POST "$BASE_URL/api/v1/accounts/ACME001/insights" \
  -H "Authorization: Bearer $USER_OID" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the risks and opportunities?",
    "detailLevel": "summary"
  }' | jq .

# 2. 검색
echo -e "\n=== Search Query ==="
curl -X GET "$BASE_URL/api/v1/search?q=revenue&accountId=ACME001&limit=10" \
  -H "Authorization: Bearer $USER_OID" | jq .

# 3. 감시 로그
echo -e "\n=== Audit Logs ==="
curl -X GET "$BASE_URL/api/v1/audit-logs?eventType=query_answered&limit=10" \
  -H "Authorization: Bearer $USER_OID" | jq .
```

---

## 인증 & 권한

### Bearer Token 형식

```
Authorization: Bearer {user_oid}
```

**예제**
```
Authorization: Bearer user1
Authorization: Bearer user2
Authorization: Bearer user5
```

### ACL 모델

```
Account → Owner Group
          └─ Allowed Users: [user1, user2]
          └─ Allowed Groups: [group-sales-east, group-finance]
```

### 권한 확인 규칙

1. 사용자의 그룹이 계정의 `allowedGroups`에 포함되면 ✅ **허용**
2. 사용자가 계정의 `deniedUsers`에 포함되면 ❌ **거부**
3. 이외: ❌ **거부** (404로 반환)

**권한 누설 방지**
- 권한이 없어도 "권한 없음"이라고 알려주지 않음
- 대신 404 Not Found 반환
- 감시 로그에는 `access_denied` 이벤트 기록

---

## 데이터 모델

### Request Models

#### InsightRequest
```json
{
  "question": "string",           // 필수: 질문 내용
  "detailLevel": "summary"        // 선택: summary|detailed
}
```

#### SearchRequest (GET params)
```
q=string                          // 필수: 검색어
accountId=string                  // 선택: 계정 ID 필터
sourceType=string                 // 선택: email|transaction|document
limit=integer                     // 선택: 1-100, 기본값 10
```

### Response Models

#### InsightResponse
```json
{
  "accountId": "string",
  "accountName": "string",
  "summary": "string",
  "risks": [
    {
      "name": "string",
      "score": 0.0,
      "severity": "low|medium|high|critical",
      "reason": "string",
      "detectedFrom": ["string"]
    }
  ],
  "opportunities": [
    {
      "name": "string",
      "score": 0.0,
      "reason": "string",
      "potential": "string"
    }
  ],
  "nextSteps": [
    {
      "action": "string",
      "priority": "low|medium|high|urgent",
      "dueDate": "YYYY-MM-DD",
      "estimatedEffort": "string",
      "expectedOutcome": "string"
    }
  ],
  "citations": [
    {
      "text": "string",
      "sourceUri": "string",
      "confidence": 0.0,
      "source": "email|transaction|document|internal",
      "extractedAt": "ISO8601"
    }
  ],
  "generatedAt": "ISO8601",
  "correlationId": "UUID"
}
```

#### SearchResponse
```json
{
  "query": "string",
  "results": [
    {
      "id": "string",
      "title": "string",
      "content": "string",
      "source": "email|transaction|document",
      "sourceUri": "string",
      "accountId": "string",
      "score": 0.0,
      "extractedAt": "ISO8601"
    }
  ],
  "total": 0,
  "returned": 0,
  "filtered_by_acl": true,
  "correlationId": "UUID"
}
```

#### AuditLogResponse
```json
{
  "logs": [
    {
      "timestamp": "ISO8601",
      "eventType": "string",
      "userId": "string",
      "accountId": "string",
      "status": "success|denied|error",
      "correlationId": "UUID",
      "details": {}
    }
  ],
  "total": 0,
  "returned": 0,
  "filters_applied": {}
}
```

---

## 에러 처리

### HTTP 상태 코드

| 상태 | 설명 | 예제 |
|------|------|------|
| 200 | 성공 | 요청 완료 |
| 400 | 잘못된 요청 | detailLevel 값 오류 |
| 401 | 인증 실패 | Bearer token 누락 |
| 403 | 권한 거부 | 그룹 권한 없음 |
| 404 | 찾을 수 없음 | 계정 없음 또는 권한 없음 |
| 500 | 서버 오류 | 예측 불가 오류 |

### 에러 응답 형식

```json
{
  "error": "string",
  "details": "string",
  "correlationId": "UUID"
}
```

### 에러 처리 예제

```python
import requests

try:
    response = requests.post(
        "http://localhost:8000/api/v1/accounts/UNKNOWN/insights",
        headers={"Authorization": "Bearer user1"},
        json={"question": "What are the risks?", "detailLevel": "summary"}
    )
    
    if response.status_code == 404:
        print("Account not found or access denied")
    elif response.status_code == 400:
        print(f"Invalid request: {response.json()['details']}")
    else:
        data = response.json()
        print(f"Risks: {data['risks']}")
        
except requests.exceptions.ConnectionError:
    print("Server is not running")
```

---

## 성능 고려사항

### 타임아웃
- Insight 요청: ~2초 (mock LLM)
- 검색: ~500ms (in-memory index)
- 감시 로그: ~100ms (linear scan)

### 확장성 제한 (Sandbox)
- 메모리 기반 인덱스: ~10,000 문서까지 안정적
- 감시 로그: JSONL 파일 크기에 따라 성능 저하
- 동시 요청: 10-50개 권장 (uvicorn 기본 worker)

### 프로덕션으로 확장할 때
- Azure AI Search로 인덱싱 마이그레이션
- Azure Cosmos DB에 감시 로그 저장
- Azure OpenAI로 LLM 통합
- 로드 밸런싱 및 자동 스케일링 구성

---

## 테스트 및 검증

### 통합 테스트 실행
```bash
cd sandbox
python3 tests/scenarios.py
```

### 단위 테스트 (추가 작업)
```bash
# 아직 구현되지 않음
pytest sandbox/tests/unit/ -v
```

### 부하 테스트 (추가 작업)
```bash
# 아직 구현되지 않음
# 예: Apache JMeter, locust 등
```

---

## 문제 해결

### 문제 1: "Connection refused"
```
Error: Failed to connect to http://localhost:8000
```
**해결**
```bash
cd sandbox/api
python3 main.py
```

### 문제 2: "404 Access Denied"
```
Error: Not Found (but account exists)
```
**확인 사항**
1. 사용자가 그룹에 속해 있는가?
   ```bash
   curl http://localhost:8000/debug/users | grep {user_oid}
   ```

2. 그룹이 계정에 허용되어 있는가?
   ```bash
   cat sandbox/data/account_acls.json | grep {account_id}
   ```

### 문제 3: "ModuleNotFoundError"
```
Error: No module named 'pydantic'
```
**해결**
```bash
pip install -r sandbox/api/requirements.txt
```

### 문제 4: "Audit log not found"
```
Error: audit_log.jsonl does not exist
```
**해결**
```bash
mkdir -p .copilot-tracking
# API 서버 또는 시나리오 실행 시 자동 생성됨
```

---

## 모범 사례

### 1. Bearer Token 관리
```python
# ❌ 안 좋은 예
headers = {"Authorization": "Bearer user1"}

# ✅ 좋은 예
user_token = os.getenv("USER_TOKEN")
headers = {"Authorization": f"Bearer {user_token}"}
```

### 2. 상관 ID 추적
```python
import uuid

# 모든 요청에 상관 ID 포함
correlation_id = str(uuid.uuid4())
headers = {
    "Authorization": f"Bearer {user_token}",
    "X-Correlation-ID": correlation_id
}
```

### 3. 오류 재시도
```python
import time

max_retries = 3
for attempt in range(max_retries):
    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError:
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)
        else:
            raise
```

### 4. 응답 검증
```python
# ✅ 응답 필드 확인
if response.status_code == 200:
    data = response.json()
    assert "citations" in data
    assert len(data["citations"]) > 0
    for citation in data["citations"]:
        assert "sourceUri" in citation
        assert "confidence" in citation
```

---

## 다음 단계

1. **OpenAPI Spec 생성**
   ```bash
   # FastAPI 자동 생성
   curl http://localhost:8000/openapi.json
   ```

2. **Declarative Agent 매니페스트**
   - OpenAPI 스펙 기반 매니페스트 작성
   - M365 Copilot 채널 통합

3. **실제 배포**
   - Bicep 템플릿으로 Azure 리소스 배포
   - Azure OpenAI 통합
   - Azure AI Search 마이그레이션

---

**버전**: 0.1.0  
**마지막 업데이트**: 2026-11-04
