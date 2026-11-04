---
type: role-analysis
role: Tech-Lead
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# Tech Lead 담당 범위 (Declarative agent + 백엔드)

> `tech-lead.md` 가이드는 열람하지 못했다 (404, Unknown). 아래는 워크샵 문서와 RPI 문서에서 확인된 책임을 기반으로 한 제안이다.

## 핵심 질문
"승인된 설계를 계획대로, 검증 가능한 증거와 함께 구현·통과시킬 수 있는가"

## 문서에서 확인된 책임 (Documented)
- 환경 설정(2단계)의 기술 리드: 워크샵 브랜치 생성, 세션 컨텍스트 파일, 역할별 준비, 자료 취급 원칙 확인
- 솔루션 단계: 아키텍처 뷰와 게시 경로 발표
- 구현 단계: 첫 P0 작업의 서면 승인을 하는 책임 담당자 중 하나 (제품, 기술 리드, 딜리버리 담당자)
- 팀 도입 문서: 역할 진입점은 "아키텍처 결정 지침, 팀 표준 강제 리뷰 에이전트"

## 담당 산출물 (제안)

| 산출물 | 내용 |
|---|---|
| 기술 구현 계획 | `/rpi-plan`으로 `Pxx`/`Pxx-Txx`, 계획 비평 `Pass/Revise/Blocked` 관리 |
| 저장소·CI 구성 | 구조, 린트, 검증 명령, 브랜치 규칙 (`workshop/<team>`) |
| 개발 환경 | Copilot 라이선스 테넌트, 사이드로드 권한, Partner Center 등록 확인 (WP15) |
| 코드 리뷰 게이트 | PR 리뷰, 아키텍처 준수 확인, `/rpi-review` 결과의 라우팅 |
| P0 기술 승인 | 계획이 Blocked/Not ready가 아님을 확인하고 서면 승인 |
| 테스트 전략 | Positive/Negative Path, 프롬프트 인젝션 시나리오, 완료 정의 |
| 검증 통과 | 스토어 검증 가이드라인·RAI 점검의 기술 항목 수행 |
| 추적 매트릭스 유지 | 요구사항 → 구성요소 → 백로그 → 테스트 → 게시 게이트 |

## 결정권
- 기술 결정(ADR 수용, 스택, 구조)의 A.
- 범위·가격·라이선스 변경은 PM의 A. 이런 변경이 생기면 구현을 중단하고 계획으로 복귀시키는 것이 Tech Lead의 책임이다 (HVE 중단 조건).

## 겸직 주의
- Engineer를 겸하면 자기 코드의 승인자가 되므로 동료 리뷰 1인을 둔다.
- PM이 P0 승인자가 되지 않도록 한다 ([[RACI-Matrix]] 3절).

## HVE 도구
RPI Agent(`/rpi-plan`, `/rpi-challenger`, `/rpi-review`), `code-review`, `pull-request`.

관련: [[Architect-Responsibilities]], [[Engineer-Role-Analysis]], [[Handoff-Interfaces]]
