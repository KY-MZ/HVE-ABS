# 05. 데이터 수집, 검색, 인용

## 1. 소스별 수집

| 소스 | 방식 | 단위 | ACL 출처 |
|---|---|---|---|
| CRM(Dataverse) | Change tracking + Functions | 계정, 연락, 활동, 기회 | 계정 팀 구성원 |
| 이메일(Graph) | 위임/앱 권한 델타 쿼리, 고객 승인된 사서함 범위 | 메시지 스레드 | 사서함 소유자 + (정책에 따라) 계정 팀 |
| 거래 내역 | ADF 증분 복사 → ADLS → SQL 집계 | 거래, 월별 집계 | 계정 ACL 테이블 |
| 내부 지식 | SharePoint/Blob 인덱서 | 문서 청크 | 문서 ACL(SharePoint 권한, Entra 그룹) |

수집 신원은 수집용 Managed Identity(읽기 전용, 소스별 최소 권한).

## 2. 정규화 문서 스키마 (인용의 기반)

모든 청크는 아래 필드를 필수로 가진다. 필수 필드가 없으면 색인하지 않는다.

| 필드 | 설명 |
|---|---|
| `id` | `{sourceType}:{sourceId}:{chunkNo}` 안정 키 |
| `accountId` | 계정 키 |
| `sourceType` | `crm` / `email` / `txn` / `kb` |
| `sourceId` | 원본 레코드/메시지/문서 ID |
| `sourceUri` | 사용자 열람 가능한 딥링크 |
| `title` | 표시 제목 |
| `sourceTimestamp` | 원본 최종 수정 시각 |
| `contentHash` | 변경 감지 |
| `aclPrincipals` | 허용 principal 목록 |
| `content` | 청크 텍스트 |
| `contentVector` | 임베딩(1536 등) |

## 3. 인덱스 정의

```json
{
  "name": "rm-insights-v1",
  "fields": [
    {"name": "id", "type": "Edm.String", "key": true},
    {"name": "accountId", "type": "Edm.String", "filterable": true},
    {"name": "sourceType", "type": "Edm.String", "filterable": true, "facetable": true},
    {"name": "sourceId", "type": "Edm.String", "filterable": true},
    {"name": "sourceUri", "type": "Edm.String", "retrievable": true},
    {"name": "title", "type": "Edm.String", "searchable": true},
    {"name": "sourceTimestamp", "type": "Edm.DateTimeOffset", "filterable": true, "sortable": true},
    {"name": "contentHash", "type": "Edm.String"},
    {"name": "aclPrincipals", "type": "Collection(Edm.String)", "filterable": true},
    {"name": "content", "type": "Edm.String", "searchable": true},
    {"name": "contentVector", "type": "Collection(Edm.Single)", "searchable": true,
     "dimensions": 1536, "vectorSearchProfile": "vp"}
  ]
}
```

## 4. 청킹과 인용 보존

* 청크 길이 500~800 토큰, 겹침 10%. 문서 구조(제목/문단) 경계 우선.
* 각 청크가 원본 위치(페이지, 메시지 ID, 레코드 필드)를 `sourceUri` 프래그먼트로 유지.
* 요약/재작성 청크를 만들지 않는다(요약은 인용 불가). 요약은 응답 시점에 생성.

```python
def chunk(text: str, size=700, overlap=70):
    words = text.split()
    step = size - overlap
    for i in range(0, len(words), step):
        yield " ".join(words[i:i + size])
```

## 5. 수집 파이프라인 규칙

1. **멱등**: `contentHash` 같으면 재색인하지 않음.
2. **삭제 전파**: 원본 삭제 → 인덱스 문서 삭제(툼스톤 24시간 내).
3. **ACL 먼저**: 권한 축소는 즉시 반영 우선순위.
4. **PII/민감 필드**: 색인 제외 목록(주민번호 등)을 설정으로 관리, 수집 단계에서 마스킹.
5. **데드레터**: 실패 항목은 큐에 보관하고 알림.

## 6. 질의 전략

하이브리드 검색(BM25 + 벡터) + 시맨틱 랭커, 항상 [04](04-Identity-and-Access.md)의 필터 적용.

```python
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

def retrieve(client: SearchClient, query: str, embedding: list[float], flt: str, k=12):
    vq = VectorizedQuery(vector=embedding, k_nearest_neighbors=k, fields="contentVector")
    results = client.search(search_text=query, vector_queries=[vq], filter=flt, top=k,
                            select=["id", "sourceType", "sourceId", "sourceUri",
                                    "title", "sourceTimestamp", "content"])
    return [dict(r) for r in results]
```

## 7. 검증

| 항목 | 기준 |
|---|---|
| 필수 필드 누락 색인 | 0건 |
| ACL 없는 문서 | 0건(없으면 색인 거부) |
| 삭제 전파 | 24시간 내 |
| 신선도 | 소스별 목표 SLO를 대시보드에 표시 |
