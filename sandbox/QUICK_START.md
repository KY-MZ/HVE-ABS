# 빠른 시작 가이드

## 🚀 5분 안에 시작하기

### 1단계: 환경 준비 (1분)
```bash
cd ~/Develop/hve-innovation-kr_megazone_2
cd sandbox

# 필요한 패키지 설치
pip install -r api/requirements.txt
```

### 2단계: 시나리오 실행 (2분)
```bash
# End-to-End 테스트 실행
python3 tests/scenarios.py
```

**예상 출력**:
```
================================================================================
RM INTELLIGENCE EXPERIENCE - END-TO-END SANDBOX SIMULATION
================================================================================

SCENARIO 1: Authorized User Viewing Account Insights
✅ REQUEST SUCCESSFUL
   Account: ACME001 (ACME Corporation)
   User: user1 (Alice Chen)
   ...

TEST SUMMARY
================================================================================
Scenario 1: Authorized User: ✅ PASSED
Scenario 2: Unauthorized User: ✅ PASSED
Scenario 3: Audit Logging: ✅ PASSED
Scenario 4: Citation Validation: ✅ PASSED
Scenario 5: Account Profiles: ✅ PASSED

Total: 5/5 scenarios passed ✅
```

### 3단계: API 서버 시작 (1분, 선택사항)
```bash
cd api
python3 main.py
```

**예상 출력**:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### 4단계: API 테스트 (1분, 선택사항)
```bash
# 다른 터미널에서 실행
curl -X POST http://localhost:8000/api/v1/accounts/ACME001/insights \
  -H "Authorization: Bearer user1" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the risks?", "detailLevel": "summary"}' | jq .
```

---

## 📚 주요 문서 가이드

| 문서 | 용도 | 읽어야 할 때 |
|------|------|-------------|
| [README.md](./README.md) | 전체 개요, 아키텍처, 시나리오 | 프로젝트 처음 접할 때 |
| [API_GUIDE.md](./API_GUIDE.md) | API 엔드포인트, 예제, 에러 처리 | API 호출할 때 |
| [sandbox-validation-report.md](../.copilot-tracking/sandbox-validation-report.md) | 요구사항 검증, 성능, 보안 | 아키텍처 검토할 때 |
| [sandbox-simulation-plan.md](../.copilot-tracking/sandbox-simulation-plan.md) | 구현 계획, 매핑, 성공 기준 | 디테일을 알고 싶을 때 |

---

## 🎯 시나리오별 테스트

### Scenario 1: 권한 있는 사용자
```bash
# 직접 실행 (scenarios.py에서)
# user1 (Alice Chen)이 ACME001 계정 조회
# 예상: ✅ 위험 분석 반환
```

### Scenario 2: 권한 없는 사용자
```bash
# user4 (David Lee)가 ACME001 조회 시도
# 예상: ✅ 404 반환 (권한 누설 없음)
```

### Scenario 3: 감시 로깅
```bash
# audit_log.jsonl 확인
cat ../.copilot-tracking/audit_log.jsonl
# 예상: ✅ 모든 쿼리와 접근 거부 기록됨
```

### Scenario 4: Citation 검증
```bash
# Scenario 1 응답에서 citations 필드 확인
# 예상: ✅ sourceUri와 confidence 포함
```

### Scenario 5: 계정 프로필
```bash
# 5개 계정의 다양한 점수 프로필 확인
# ACME001: 위험 (매출 감소)
# TECH002: 성장 (확장)
# FINANCE003: 전략 (파트너십)
# RETAIL004: 위험 (시장 포화)
```

---

## 🔧 자주 하는 질문

### Q1: "ModuleNotFoundError: No module named 'pydantic'"
```bash
pip install pydantic python-dateutil fastapi uvicorn pytest httpx
```

### Q2: "Connection refused" (API 서버에 연결 못함)
```bash
# 터미널 1: API 서버 시작
cd sandbox/api
python3 main.py

# 터미널 2: 다른 터미널에서 테스트
curl http://localhost:8000/health
```

### Q3: 감시 로그 확인하고 싶은데?
```bash
# 감시 로그 파일 확인
cat .copilot-tracking/audit_log.jsonl

# 예쁘게 표시
python3 -m json.tool .copilot-tracking/audit_log.jsonl | head -50
```

### Q4: 특정 사용자의 권한 확인
```bash
# API 서버 실행 후
curl http://localhost:8000/debug/users | jq '.users[] | select(.oid=="user1")'
```

### Q5: 특정 계정의 ACL 확인
```bash
cat sandbox/data/account_acls.json | jq '.[] | select(.accountId=="ACME001")'
```

---

## 📊 데이터 구조

### 테스트 사용자
```json
{
  "oid": "user1",
  "name": "Alice Chen",
  "groups": ["group-sales-east", "group-finance"],
  "allowedAccounts": ["ACME001", "FINANCE003"]
}
```

### 테스트 계정
```json
{
  "id": "ACME001",
  "name": "ACME Corporation",
  "status": "at_risk",
  "revenue": 2500000,
  "yoyChange": -0.20
}
```

### 응답 구조
```json
{
  "accountId": "ACME001",
  "summary": "...",
  "risks": [{"name": "...", "score": 7.0, "reason": "..."}],
  "opportunities": [],
  "nextSteps": [{"action": "...", "priority": "urgent"}],
  "citations": [{"text": "...", "sourceUri": "...", "confidence": 0.95}]
}
```

---

## 🔐 보안 확인

### ACL 작동 확인
```python
# user4는 ACME001에 접근 불가
# 요청: POST /accounts/ACME001/insights with Bearer user4
# 결과: 404 Not Found (권한 누설 없음)
```

### 권한 누설 방지 확인
```bash
# 권한 있을 때: 200 OK + 데이터
# 권한 없을 때: 404 (권한 없는지 계정 없는지 알 수 없음)
```

### 감시 로그 불변성
```bash
# JSONL 형식: 각 줄이 JSON 객체
# append-only: 기존 라인 변경 불가
# 추적성: 모든 이벤트에 correlationId
```

---

## ⚡ 성능 확인

### 응답 시간 측정
```bash
# Insight 요청
time curl -X POST http://localhost:8000/api/v1/accounts/ACME001/insights \
  -H "Authorization: Bearer user1" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the risks?", "detailLevel": "summary"}'
# 예상: 200-500ms

# 검색 요청
time curl "http://localhost:8000/api/v1/search?q=revenue&accountId=ACME001" \
  -H "Authorization: Bearer user1"
# 예상: 50-100ms
```

---

## 📁 파일 구조 정리

```
hve-innovation-kr_megazone_2/
├── sandbox/                          # 핵심 구현
│   ├── README.md                     # 전체 개요 📄
│   ├── API_GUIDE.md                  # API 레퍼런스 📚
│   │
│   ├── data/
│   │   ├── accounts.json             # 4개 테스트 계정
│   │   ├── transactions.json         # 거래 기록
│   │   ├── emails.json               # 이메일 데이터
│   │   ├── documents.json            # 지식 문서
│   │   ├── account_acls.json         # 접근 권한
│   │   └── users.json                # 테스트 사용자
│   │
│   ├── api/
│   │   ├── main.py                   # FastAPI 앱
│   │   ├── models.py                 # Pydantic 스키마
│   │   ├── orchestrator.py           # 핵심 로직
│   │   ├── identity_service.py       # OBO & ACL
│   │   ├── search_service.py         # 검색 & 인덱싱
│   │   ├── scoring.py                # 점수 계산
│   │   ├── llm_service.py            # LLM Mock
│   │   ├── audit_log.py              # 감시 로깅
│   │   └── requirements.txt
│   │
│   └── tests/
│       └── scenarios.py              # End-to-End 테스트 (5개)
│
└── .copilot-tracking/
    ├── sandbox-simulation-plan.md    # 구현 계획
    └── sandbox-validation-report.md  # 검증 보고서
```

---

## ✅ 체크리스트

### 설정 확인
- [ ] Python 3.9+ 설치됨
- [ ] pip 또는 pip3 사용 가능
- [ ] Git repository 클론됨

### 설치 확인
- [ ] `pip install -r api/requirements.txt` 성공
- [ ] `import pydantic` 성공
- [ ] `import fastapi` 성공

### 실행 확인
- [ ] `python3 tests/scenarios.py` 5/5 PASSED
- [ ] API 서버 시작 (CTRL+C로 종료)
- [ ] `curl http://localhost:8000/health` 200 OK

### 기능 확인
- [ ] Scenario 1: 권한 있는 사용자 ✅
- [ ] Scenario 2: 권한 없는 사용자 (404) ✅
- [ ] Scenario 3: 감시 로그 기록 ✅
- [ ] Scenario 4: Citation 포함 ✅
- [ ] Scenario 5: 다양한 프로필 ✅

### 문서 확인
- [ ] README.md 읽음
- [ ] API_GUIDE.md 읽음
- [ ] 검증 보고서 읽음

---

## 🎓 학습 순서

### 초급 (이 문서)
1. 빠른 시작 (5분)
2. 시나리오 실행 (2분)
3. FAQ 읽기 (3분)

### 중급 (README.md)
1. 전체 아키텍처 이해
2. 각 컴포넌트의 역할 파악
3. 데이터 흐름 이해

### 고급 (API_GUIDE.md + 코드)
1. API 엔드포인트 상세 학습
2. 요청/응답 스키마 분석
3. 에러 처리 패턴 이해
4. 소스 코드 리뷰

### 심화 (검증 보고서 + 계획)
1. 요구사항 대비 구현 검증
2. 보안 설계 리뷰
3. 성능 특성 분석
4. 향후 개선 방안 검토

---

## 🚀 다음 단계

### Phase 1: Sandbox 완성 (✅ 완료)
- [x] End-to-End 구현
- [x] 5개 시나리오 테스트
- [x] 문서화

### Phase 2: 검증 (⏳ 진행 중)
- [ ] OpenAPI Spec 생성
- [ ] 보안 위협 모델링 (STRIDE)
- [ ] 성능 기준선 설정

### Phase 3: 배포 준비 (📋 계획 중)
- [ ] Bicep 템플릿 작성
- [ ] Azure 개발 환경 구성
- [ ] 배포 테스트

### Phase 4: 프로덕션 (🎯 목표)
- [ ] Azure OpenAI 통합
- [ ] Azure AI Search 마이그레이션
- [ ] 부하 테스트 & 최적화
- [ ] Marketplace 출시

---

## 📞 문제 해결

### 문제: Python 찾을 수 없음
```bash
# 수정
python3 --version  # 3.9+인지 확인
```

### 문제: 패키지 설치 실패
```bash
# 수정
pip3 install --upgrade pip
pip3 install -r api/requirements.txt -v
```

### 문제: 포트 8000 이미 사용 중
```bash
# 수정: 다른 포트 사용
# main.py의 uvicorn.run() 파라미터 변경
uvicorn.run(app, host="127.0.0.1", port=8001)
```

### 문제: 감시 로그 파일 없음
```bash
# 수정: 디렉토리 생성
mkdir -p .copilot-tracking
# 시나리오 또는 API 서버 실행 시 자동 생성
```

---

## 📞 지원

### 문서
- 📄 [README.md](./README.md) - 전체 개요
- 📚 [API_GUIDE.md](./API_GUIDE.md) - API 레퍼런스
- 📋 [검증 보고서](.copilot-tracking/sandbox-validation-report.md)
- 📝 [구현 계획](.copilot-tracking/sandbox-simulation-plan.md)

### 소스 코드
- 🔧 [orchestrator.py](./api/orchestrator.py) - 핵심 로직
- 🔐 [identity_service.py](./api/identity_service.py) - 권한 관리
- 🔍 [search_service.py](./api/search_service.py) - 검색 엔진
- 📊 [scoring.py](./api/scoring.py) - 점수 계산

---

**생성일**: 2026-11-04  
**상태**: ✅ 모든 시나리오 통과  
**다음 단계**: OpenAPI Spec 생성 & Bicep 템플릿 작성
