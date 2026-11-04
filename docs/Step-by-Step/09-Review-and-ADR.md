# 09. 아키텍처 리뷰와 ADR

## 1. 리뷰 범위

시스템 유형: AI 에이전트 + 데이터 검색(RAG), 고객 구독 배포(Managed App). 가장 영향이 큰 영역 3개를 선정한다.

1. **Security**: 계정별 접근 통제, 퍼블리셔/고객 경계
2. **Reliability**: ACL 동기화, 모델 장애 저하
3. **Operational Excellence**: 감사 증거, 업데이트 배포

> 범위는 사용자 확인 전 초안이다.

## 2. Well-Architected 리뷰

| 필라 | 평가 | 상태 | 조치 |
|---|---|---|---|
| Security | OBO, 서버측 ACL, Private Endpoint, 키 없는 인증 | 설계 충족 | 간접 프롬프트 주입 테스트 필수 |
| Security | 퍼블리셔 지원 접근 | 위험 | JIT + 승인 + 로그, 데이터 평면 권한 배제 |
| Reliability | 모델 장애 | 부분 | 인용 있는 원문 목록(생성 없이)로 저하 응답 |
| Reliability | ACL 동기화 지연 | 위험 | fail-closed + 알림 |
| Cost | 모델/검색 상시 비용 | 주의 | 소형 모델 분류, 캐시(권한 키 포함), Search SKU 사이징 |
| Operations | 버전 업데이트 | 주의 | Managed App 버전 + 카나리 고객, 롤백 계획 |
| Performance | 질의 p95 | 미검증 | 부하 테스트로 확정 |

## 3. 위협 모델 요약 (STRIDE)

| 위협 | 시나리오 | 완화 |
|---|---|---|
| Spoofing | 위조 토큰 | APIM JWT 검증, audience 고정 |
| Tampering | ACL 테이블 변조 | 수집 ID만 쓰기, 변경 로그 |
| Repudiation | 조회 부인 | 불변 감사 로그 |
| Information disclosure | 타 계정 데이터 노출 | 서버 ACL + 검색 필터 + 404, 교차 계정 테스트 |
| Information disclosure | 프롬프트 주입으로 데이터 유출 | 근거 격리, 인용 검증, 도구 없음(읽기 전용) |
| DoS | 과다 호출 | APIM 쿼터, 사용자별 레이트 |
| Elevation | 퍼블리셔 과다 권한 | 거부 할당, JIT |

보안 전반은 `security-planner` 에이전트로 에스컬레이션하여 TM 를 정식화한다.

## 4. ADR 목록

ADR 템플릿(`docs/templates/adr-template-solutions.md`)이 이 저장소에 없으므로 아래 요약 형식을 사용하고, 확정 시 정식 ADR로 옮긴다. 저장 위치: `docs/decisions/` (생성 예정).

### ADR-001 에이전트 채널: Declarative agent + API plugin

* 맥락: M365 Copilot에서 질문, 고객 API 호출.
* 옵션: Declarative agent / Custom engine agent / Copilot connectors(Graph 커넥터).
* 결정: Declarative agent + API plugin. 근거: 빠른 구현, 고객 테넌트 거버넌스.
* 결과: 오케스트레이션은 Copilot 소유, 복잡한 워크플로 제어가 제한됨. 필요 시 custom engine 재평가.

### ADR-002 검색: Azure AI Search(하이브리드 + 보안 트리밍)

* 옵션: AI Search / Cosmos DB 벡터 / Copilot 커넥터 인덱스.
* 결정: AI Search. 근거: 필터 기반 ACL, 하이브리드 검색, 고객 구독 내 배치.
* 결과: ACL 동기화 책임이 우리에게 있음.

### ADR-003 데이터 평면 배치: 데이터는 고객 RG, 컴퓨트는 관리 RG

* 옵션: 전부 관리 RG / 전부 고객 RG / 분리.
* 결정: 분리. 근거: 퍼블리셔 데이터 접근 차단 + 운영 가능성.
* 결과: 관리 RG 앱이 고객 RG 데이터에 접근하려면 Managed Identity 역할 할당 필요, 배포 복잡도 증가.

### ADR-004 접근 판단: 서버 결정론 + 404 비공개

* 근거: 모델에 위임 시 누출 위험. 결과: 항상 ACL 계산 비용(캐시 키에 사용자 포함, TTL 5분 이하).

### ADR-005 이메일 ACL: 사서함 소유자 한정 기본

* 옵션: 계정 팀 공유 / 소유자 한정.
* 결정: 기본 소유자 한정, 고객이 정책으로 확장. 결과: 팀 인사이트가 줄어드나 프라이버시 위험 최소.

### ADR-006 컴퓨트: Azure Container Apps

* 옵션: Container Apps / AKS / Functions.
* 결정: Container Apps. 근거: 낮은 운영 부담, VNet 통합, 스케일. 결과: 매우 큰 확장 시 AKS 재평가.

## 5. 에스컬레이션 필요 항목

| 항목 | 이유 | 대상 |
|---|---|---|
| 남용 모니터링 옵트아웃 | 규제 고객, 승인 절차 | 고객 컴플라이언스, Microsoft 신청 |
| 이메일 수집 범위/ACL | 개인정보, 법무 | 고객 법무 |
| 금융 규제(감독 규정) 매핑 | 해석 불명확 | 컴플라이언스 |
| 비용 상한 | Search/OpenAI 상시 비용 | 사업 책임자 |

## 6. 구현 리뷰 체크리스트 (PR 게이트)

- [ ] 모든 데이터 접근 함수가 `UserContext`를 요구
- [ ] 검색 호출에 필터 강제(없으면 예외)
- [ ] 응답에 `citations` 비어 있지 않음, 인용 검증 통과
- [ ] 로그에 원문/PII 없음
- [ ] `disableLocalAuth`, Private Endpoint, 공용 접근 비활성 확인
- [ ] 교차 계정 부정 테스트 통과
- [ ] 프롬프트 주입 평가 통과
- [ ] Bicep what-if 검토 및 정책 준수
- [ ] 인적 검토 체크박스는 사람이 확인 (에이전트가 표시하지 않음)

## 7. 이 리뷰의 한계

* 실제 CRM 종류, 거래 데이터 구조, 규제 요건이 확정되지 않았다(가정 [Q1~Q5](00-Overview.md)).
* 성능, 비용 수치는 측정 전 추정이다.
