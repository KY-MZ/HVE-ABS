---
type: raci
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# 역할별 담당 (RACI) – Architect / Tech Lead / Engineer / PM (+SME)

R = 수행, A = 최종 책임(행당 1명), C = 협의, I = 통보. 작성자와 승인자는 같은 사람이 아니도록 배정한다.

## 1. 역할 정의

| 역할 | 핵심 책임 | 하지 않는 것 |
|---|---|---|
| **PM** | 무엇을 왜 만들지: 범위, 요구사항, AC, 백로그, 가격·상용화, 게시 일정 | 설계 확정, 코드 승인 |
| **SME** | 통제 카탈로그, 기대값, 증적 기준, 규제·제한망 제약, 테스트 시나리오의 정답 | 요구사항 소유, 아키텍처 결정 |
| **Architect** | 어떻게 구성할지: 신뢰 경계, 인증·동의, 멀티테넌트, 증적 스키마, 플러그인 표면, 위협 모델, ADR | 일정·우선순위, 구현 |
| **Tech Lead** | 어떻게 만들고 통과시킬지: 기술 계획, 순서, 저장소·CI, 코드 리뷰 게이트, 아키텍처 준수 확인, P0 기술 승인, 환경 | 요구사항 범위 변경, 단독 설계 변경 |
| **Engineer** | 구현: 백엔드, 플러그인, 연동, 테스트, 변경 기록 | 범위·아키텍처 변경 결정 |
| **Security (파트타임)** | 위협 모델·권한·데이터 처리 검토, 제출 전 보안 승인 | 구현 |

HVE 문서(Documented)에서 Tech Lead와 Architect는 `roles/README`에 **"Tech Lead / Architect" 하나의 역할**로 묶여 있다. 워크샵 문서의 기술 트랙도 아키텍트, 현장 배치 엔지니어, 보안 담당, 플랫폼 리드를 한 트랙으로 둔다. 둘을 분리한 위 정의는 **본 Vault의 제안(Inference)**이다. `tech-lead.md`는 열람하지 못했다(Unknown).

## 2. 담당표

| WP / 활동 | PM | SME | Architect | Tech Lead | Engineer | Security |
|---|---|---|---|---|---|---|
| WP1 통제 카탈로그·베이스라인 | C | **A/R** | C | I | C | I |
| WP2 API/UI 커버리지 표 | I | **A**, R(초안) | C | C | R(검증) | I |
| BRD/PRD, AC | **A/R** | C | C | C | I | I |
| MVP 범위 결정 (D2) | **A/R** | C | C | C | I | C |
| WP3 아키텍처, ADR | I | C | R | **A** | C | C |
| WP4 인증·동의 설계 | I | C | R | **A** | C | **C(필수)** |
| WP4 앱 등록·동의 구현 | I | I | C | C | **R** | C |
| WP5 플러그인 표면(함수 10개 이하) | C | C | R | **A** | C | I |
| WP6 평가 엔진·증적 스키마 | I | C(규칙 정확성) | R(스키마) | **A** | **R(구현)** | I |
| WP7 관리 API 읽기 연동 | I | C | C | C | **A/R** | I |
| WP8 응답 요약기 | C | C | R(규칙) | **A** | R(구현) | I |
| WP9 에이전트 지침·가드레일 | **A**, R(의도) | R(용어·정확성) | C | C | R(패키징) | C |
| WP10 멀티테넌트·보존·로깅 | I | C | R | **A** | R | **C(필수)** |
| WP11 SaaS 오퍼·가격 | **A/R** | I | C | C | R(연동) | I |
| WP12 검증 가이드라인·RAI | **A** | C | C | R | R | **R** |
| WP13 테스트 (Positive/Negative, 프롬프트 인젝션) | C | R(시나리오) | C | **A** | **R** | C |
| WP14 리스팅·약관·설정 안내 | **A/R** | R(고객 설정 안내) | I | C | C | C |
| WP15 개발 환경·Partner Center | C | I | I | **A/R** | R | I |
| P0 구현 승인(서면) | R(진행) | I | C | **A** | I | I |
| 코드 리뷰 | I | I | C(준수) | **A** | R(작성) | C |

> A는 모든 행에서 1명이다. **P0 구현 승인**은 HVE 문서(Documented)에 따라 PM이 진행하고 책임 담당자(제품·기술 리드·딜리버리)가 서면 승인하므로, PM이 직접 승인하지 않고 Tech Lead를 A로 둔다.

## 3. 겸직 규칙 (소규모 팀 4~6명)

| 구성 | 허용 | 조건 |
|---|---|---|
| PM + SME 겸직 (본인) | 허용 | [[PM-SME-Dual-Hat-Controls]] 적용, 가격은 재무·영업 검토 |
| Architect + Tech Lead 겸직 | 조건부 | 인원이 부족하면 허용하되, Architect 산출물(ADR)은 다른 사람이 A 서명 |
| Tech Lead + Engineer 겸직 | 조건부 | 자기 코드를 자기가 승인하지 않도록 동료 리뷰 1인 필수 |
| Architect + Engineer 겸직 | 비권장 | 설계와 구현의 독립 검토가 사라짐 |
| PM이 P0 승인자 | **금지** | 작성·승인 분리 (HVE 구현 단계 규칙) |

## 4. 본인(리드)에게 권장하는 배치 (Inference)
- 본인 경험이 Architect에 가까워 **설계 입력(WP1, WP2, 위협 모델)**에서 가치가 크다. PM+SME를 맡으면서 이 입력을 Architect에게 넘기는 역할로 두면 역할 침범 없이 경험을 쓸 수 있다.
- Architect가 따로 없다면 본인이 ADR을 R로 작성하되, A는 Tech Lead가 서명한다.
- 가장 많은 병목: WP4(인증·동의), WP2(커버리지 표), WP15(환경). 이 셋은 워크샵 전에 사전 확인한다.

관련: [[Handoff-Interfaces]], [[Backend-Work-Breakdown]], [[01_Role-Boundary-Map]]

---

## 업데이트 2026-11-03: 제한 환경 대응 행 추가
| WP / 활동 | PM | SME | Architect | Tech Lead | Engineer | Security |
|---|---|---|---|---|---|---|
| WP18 제한 환경 카탈로그·관찰 사실 | C | **A/R** | C | I | I | C |
| WP19 운영 모드·ingress 설계 | I | C | R | **A** | C | **C(필수)** |
| WP19 정적 egress IP 추적 구현 | I | I | C | C | **A/R** | I |
| WP20 준비도 체크리스트·승인 패키지 | **A** | R | C | C | I | C |
| WP21 수집기 구현 | I | C | C | **A** | **R** | **C(필수)** |
