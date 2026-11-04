# 04. 아이덴티티와 계정별 접근 통제

## 1. 원칙

* RM의 Entra 신원이 Copilot → API → 데이터까지 전달된다(OBO).
* 접근 판단은 **서버에서 결정론적으로** 한다. 모델 프롬프트가 접근을 결정하지 않는다.
* 권한 없는 계정은 404로 응답해 존재 여부도 숨긴다.

## 2. 인증 흐름

1. Declarative agent의 API plugin이 Entra SSO(OAuth)로 사용자 토큰을 획득한다. 대상 audience = `api://<apiClientId>`.
2. APIM이 JWT(발급자, audience, 서명, 만료)를 검증한다.
3. API가 OBO로 하위 리소스 토큰(Graph 이메일 등)을 교환한다.
4. API는 `oid`, `tid`, 그룹 클레임(초과 시 Graph `getMemberObjects`)으로 사용자 컨텍스트를 만든다.

범위(scope) 예시: `Insights.Read`(필수). 쓰기 범위는 1차 릴리스에 없다.

## 3. 접근 모델

접근 가능 계정 = (CRM 계정 팀에 속함) ∪ (RM이 속한 Entra 그룹이 부여된 계정 포트폴리오)

ACL 테이블 (Azure SQL, 수집 파이프라인이 CRM에서 동기화):

```sql
CREATE TABLE dbo.AccountAcl (
  AccountId   NVARCHAR(64)  NOT NULL,
  PrincipalId UNIQUEIDENTIFIER NOT NULL,   -- user oid 또는 group objectId
  PrincipalType CHAR(1)     NOT NULL,      -- 'U' | 'G'
  SyncedAt    DATETIME2     NOT NULL,
  CONSTRAINT PK_AccountAcl PRIMARY KEY (AccountId, PrincipalId)
);
CREATE INDEX IX_AccountAcl_Principal ON dbo.AccountAcl (PrincipalId) INCLUDE (AccountId);
```

## 4. 코드: 사용자 컨텍스트와 허용 계정

```python
# app/auth.py
from dataclasses import dataclass
import jwt  # PyJWT

@dataclass(frozen=True)
class UserContext:
    oid: str
    tid: str
    groups: tuple[str, ...]
    correlation_id: str

def build_context(claims: dict, groups: list[str], correlation_id: str) -> UserContext:
    return UserContext(claims["oid"], claims["tid"], tuple(groups), correlation_id)
```

```python
# app/access.py
def allowed_account_ids(conn, ctx: UserContext, requested: list[str] | None = None) -> set[str]:
    principals = [ctx.oid, *ctx.groups]
    placeholders = ",".join("?" for _ in principals)
    sql = f"SELECT DISTINCT AccountId FROM dbo.AccountAcl WHERE PrincipalId IN ({placeholders})"
    rows = conn.execute(sql, principals).fetchall()  # 항상 매개변수화
    allowed = {r[0] for r in rows}
    return allowed if requested is None else allowed & set(requested)
```

## 5. 검색 보안 트리밍

인덱스에 `accountId`(filterable), `aclPrincipals`(Collection(Edm.String), filterable)를 둔다. 쿼리 시 항상 필터를 강제한다.

```python
def build_filter(account_ids: set[str], ctx: UserContext) -> str:
    acc = ",".join(sorted(account_ids))
    pr = ",".join([ctx.oid, *ctx.groups])
    return (f"search.in(accountId, '{acc}', ',') and "
            f"aclPrincipals/any(p: search.in(p, '{pr}', ','))")
```

* 계정 ID와 principal은 GUID/내부 ID 형식 검증 후 삽입(정규식 `^[A-Za-z0-9\-]{1,64}$`) → 필터 주입 방지.
* 허용 계정이 0건이면 검색을 호출하지 않고 404.
* 이메일처럼 개인 소유 문서는 `aclPrincipals`에 해당 사용자만 넣는다(계정 팀 전체 공유 금지, 정책으로 결정: ADR-005).

## 6. ACL 동기화

| 항목 | 규칙 |
|---|---|
| 주기 | 변경 이벤트 우선, 최소 15분 간격 전체 보정 |
| 삭제 | 권한 회수는 인덱스 문서 ACL 갱신을 **삭제보다 우선** 처리 |
| 지연 허용 | 목표 권한 반영 지연 ≤ 15분(고객 합의 필요) |
| 실패 | 동기화 실패 시 마지막 정상 시점 경과가 임계를 넘으면 **fail-closed** (응답 거절) |

## 7. 테넌트 앱 등록과 동의

* 퍼블리셔 멀티테넌트 앱 1개 또는 고객별 앱(Managed App 배포 시 생성). 기본 권고: **고객 테넌트 내 앱 등록**(고객 통제).
* 위임 권한만 사용, 최소 권한(`Mail.Read` 보다 가능하면 서버 측 수집 대신 `Mail.ReadBasic`/검색 범위 제한 검토).
* 관리자 동의 절차를 배포 전 체크리스트에 포함.

## 8. 테스트 (필수)

| 케이스 | 기대 |
|---|---|
| 팀 소속 RM이 계정 조회 | 200 + 인용 |
| 비소속 RM이 계정 조회 | 404, 감사 로그 `access_denied` |
| 그룹 제거 직후(동기화 전/후) | 전: 허용 지연 문서화, 후: 404 |
| 토큰 audience 불일치 | 401 |
| 필터 주입 문자열 | 400 |
| ACL 동기화 중단 임계 초과 | 503 fail-closed |

## 9. 리뷰 포인트

* 공용 서비스 계정으로 검색 키를 쓰는 경로가 없는가 (`disableLocalAuth` 확인).
* 모든 검색, SQL 호출이 `UserContext`를 필수 인자로 받는가(코드 리뷰 규칙: 컨텍스트 없는 데이터 접근 함수 금지).
