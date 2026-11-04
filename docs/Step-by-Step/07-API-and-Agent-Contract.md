# 07. API 계약과 Declarative Agent

## 1. 설계 규칙

* 함수는 5개 이하의 거칠은(coarse-grained) 연산. Copilot 토큰 한도 때문에 응답은 **요약 + 인용 링크**.
* 위임 권한만 사용(Entra SSO). API 키 방식 금지.
* 응답 항목마다 `citations[]`를 포함한다.

## 2. OpenAPI (발췌)

```yaml
openapi: 3.0.3
info: { title: RM Insight API, version: 1.0.0 }
servers: [ { url: https://<apim-host>/rm/v1 } ]
paths:
  /accounts/search:
    get:
      operationId: findAccounts
      summary: 접근 가능한 계정을 이름으로 찾기
      parameters:
        - { name: q, in: query, required: true, schema: { type: string, maxLength: 100 } }
      responses:
        '200': { description: ok, content: { application/json: { schema: { $ref: '#/components/schemas/AccountList' } } } }
  /accounts/{accountId}/insights:
    get:
      operationId: getAccountInsights
      summary: 계정 요약, 위험 지표, 성장 기회, 권장 조치
      parameters:
        - { name: accountId, in: path, required: true, schema: { type: string, pattern: '^[A-Za-z0-9\-]{1,64}$' } }
        - { name: focus, in: query, schema: { type: string, enum: [summary, risk, growth, actions] } }
      responses:
        '200': { description: ok, content: { application/json: { schema: { $ref: '#/components/schemas/Insights' } } } }
        '404': { description: not found or not permitted }
  /accounts/{accountId}/evidence:
    get:
      operationId: getEvidence
      summary: 인용 ID 의 원문 발췌와 링크
      parameters:
        - { name: accountId, in: path, required: true, schema: { type: string } }
        - { name: citationId, in: query, required: true, schema: { type: string } }
      responses:
        '200': { description: ok }
components:
  schemas:
    Citation:
      type: object
      required: [id, sourceType, title, uri, timestamp]
      properties:
        id: { type: string }
        sourceType: { type: string, enum: [crm, email, txn, kb] }
        title: { type: string }
        uri: { type: string, format: uri }
        timestamp: { type: string, format: date-time }
    Insights:
      type: object
      required: [accountId, summary, indicators, opportunities, nextActions, citations, correlationId]
      properties:
        accountId: { type: string }
        summary: { type: string }
        indicators:
          type: array
          items: { type: object, properties: { code: {type: string}, level: {type: string}, rationale: {type: string}, citationIds: {type: array, items: {type: string}} } }
        opportunities: { type: array, items: { type: object } }
        nextActions: { type: array, items: { type: object } }
        citations: { type: array, items: { $ref: '#/components/schemas/Citation' } }
        formulaVersion: { type: string }
        correlationId: { type: string }
```

`/accounts/{id}/evidence` 는 사용자 권한 재검증 후에만 원문을 반환한다.

## 3. 엔드포인트 구현 예 (FastAPI)

```python
from fastapi import FastAPI, Depends, HTTPException, Header
import uuid

app = FastAPI()

@app.get("/rm/v1/accounts/{account_id}/insights")
async def insights(account_id: str, focus: str = "summary",
                   ctx: UserContext = Depends(get_user_context)):
    allowed = allowed_account_ids(db(), ctx, [account_id])
    if account_id not in allowed:
        audit("access_denied", ctx, account=account_id)
        raise HTTPException(404)
    evidence = retrieve_for(account_id, ctx, focus)
    indicators = compute_indicators(account_id, ctx)
    draft = generate(evidence, indicators)
    text, used = enforce_citations(draft, {e["id"] for e in evidence})
    audit("query_answered", ctx, account=account_id, citations=used)
    return build_response(account_id, text, indicators, evidence, used, ctx)
```

오류 응답은 일관된 형식(`code`, `message`, `correlationId`)이며 내부 예외 메시지를 노출하지 않는다.

## 4. Declarative agent 매니페스트

`appPackage/declarativeAgent.json`:

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.5/schema.json",
  "version": "v1.5",
  "name": "RM Intelligence",
  "description": "계정 인사이트, 위험 지표, 성장 기회, 권장 조치를 출처 인용과 함께 제공합니다.",
  "instructions": "$[file('instruction.txt')]",
  "conversation_starters": [
    { "title": "계정 브리핑", "text": "ACME 계정 브리핑을 해줘" },
    { "title": "위험 점검", "text": "내 포트폴리오에서 위험 신호가 있는 계정은?" }
  ],
  "actions": [ { "id": "rmInsightApi", "file": "ai-plugin.json" } ]
}
```

`instruction.txt` 핵심: 답변마다 출처(citations) 목록 표시, 근거 없으면 모른다고 답함, 자동 실행 금지. (스키마 버전은 Agents Toolkit 최신에 맞춰 확인)

`ai-plugin.json`은 위 OpenAPI의 operationId를 함수로 노출하고 `auth`는 `OAuthPluginVault`(Entra SSO 등록 ID)로 설정한다.

## 5. 계약 테스트

* OpenAPI 스키마 대비 응답 검증(Schemathesis 또는 Dredd).
* 모든 `Insights` 응답에서 `citations`가 비어 있지 않음.
* 응답 크기 상한(예: 20KB) 초과 시 요약으로 절단.

## 6. 리뷰 포인트

| 항목 | 기대 |
|---|---|
| 함수 수 | ≤ 5 |
| 응답에 원문 장문 포함 | 없음(링크로 대체) |
| 404/403 구분 누출 | 둘 다 404 |
