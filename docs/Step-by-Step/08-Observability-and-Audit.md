# 08. 관측성과 운영 감사 증거

## 1. 목표

고객 감사자가 "누가, 언제, 어떤 계정에 대해, 어떤 근거로 어떤 답을 받았나"와 "퍼블리셔가 무엇을 했나"를 고객 구독 안에서 재구성할 수 있어야 한다.

## 2. 이벤트 종류

| 이벤트 | 발생 시점 | 필수 필드 |
|---|---|---|
| `query_answered` | 응답 성공 | ts, correlationId, userOid, accountId, citationIds[], formulaVersion, modelDeployment, promptHash |
| `access_denied` | 계정 접근 거절 | ts, correlationId, userOid, accountId, reason |
| `citation_enforcement_failed` | 인용 검증 실패 | 위 + removedRatio |
| `acl_sync` | ACL 동기화 | ts, source, added, removed, status |
| `ingest_run` | 수집 실행 | ts, source, counts, failures |
| `admin_action` | 퍼블리셔/관리자 작업 | ts, actor, operation, justification, approver |
| `config_change` | 설정 변경 | ts, actor, resource, before/after 요약 |

**원문(질문 본문, 응답 본문, 이메일 내용)은 기본 저장하지 않는다.** 해시와 ID만 저장한다.

## 3. 로깅 코드

```python
import json, logging, hashlib
from datetime import datetime, timezone

audit_logger = logging.getLogger("audit")   # OpenTelemetry 로 Log Analytics 연결

def audit(event: str, ctx, **fields):
    audit_logger.info(json.dumps({
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "correlationId": ctx.correlation_id,
        "userOid": ctx.oid,
        "tenantId": ctx.tid,
        **fields,
    }, ensure_ascii=False))

def prompt_hash(prompt: str) -> str:
    return hashlib.sha256(prompt.encode()).hexdigest()
```

OpenTelemetry는 `azure-monitor-opentelemetry` 로 App Insights에 연결, 로그 테이블은 `AppTraces`/커스텀 테이블 `RmAudit_CL`.

## 4. 보존과 불변성

| 계층 | 설정 |
|---|---|
| Log Analytics | 보존 기간 고객 설정(기본 365일), 장기는 아카이브 |
| 불변 증거 | 진단 설정 → Storage Account, **불변 Blob 정책(WORM, 시간 기반)** |
| 접근 | 감사 저장소 읽기 전용 역할, 삭제 불가 |
| 리소스 로그 | Search, OpenAI, SQL, Key Vault, APIM 진단 설정 전부 활성 |

Bicep(발췌):

```bicep
resource audit 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = {
  name: '${stg.name}/default/audit-evidence'
  properties: {
    immutableStorageWithVersioning: { enabled: true }
  }
}
```

## 5. 샘플 KQL

권한 거절 급증:

```kusto
RmAudit_CL
| where event_s == "access_denied" and TimeGenerated > ago(1d)
| summarize denied=count() by userOid_s, bin(TimeGenerated, 1h)
| where denied > 20
```

특정 사용자의 계정별 조회 이력:

```kusto
RmAudit_CL
| where event_s == "query_answered" and userOid_s == "<oid>"
| project TimeGenerated, accountId_s, citationIds_s, correlationId_g
```

인용 강제 실패율:

```kusto
RmAudit_CL
| summarize failed=countif(event_s=="citation_enforcement_failed"), total=countif(event_s=="query_answered") by bin(TimeGenerated, 1d)
| extend rate = todouble(failed) / (failed + total)
```

## 6. 알림과 SLO

| 알림 | 조건 |
|---|---|
| ACL 동기화 지연 | 마지막 성공 > 30분 |
| 인용 실패율 | > 5%(일) |
| 접근 거절 급증 | 위 KQL |
| 5xx 비율 | > 2% 5분 |
| 수집 신선도 | 소스별 SLO 초과 |

## 7. 퍼블리셔 작업 증거

* 지원 접근은 JIT 승인 + 세션 기록. `admin_action`에 승인자와 사유 기록.
* Activity Log를 고객 Log Analytics에 연결해 퍼블리셔 계정의 ARM 작업을 고객이 조회 가능.

## 8. 증거 패키지 (고객 감사 제출용)

1. 기간별 `query_answered` 통계와 샘플 상관 ID 추적.
2. 접근 거절 통계.
3. 구성 증적: 공용 접근 비활성, 파인튜닝 금지 정책 준수, 불변 정책.
4. 퍼블리셔 작업 이력.

생성은 KQL 저장 쿼리 + 스크립트(`scripts/evidence-export`)로 자동화한다.

## 9. 리뷰 포인트

* 로그에 개인 정보나 원문이 들어가지 않는가(로그 스키마 린트).
* 모든 요청 경로에 correlationId 가 전파되는가.
