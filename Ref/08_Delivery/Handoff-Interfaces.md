---
type: interface-spec
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# 역할 간 인계 인터페이스 (RPI 기준)

각 경계에서 **무엇을 넘기고, 무엇이 충족돼야 넘길 수 있는가**를 정의한다. HVE 에이전트·명령은 Documented, 필드·조건은 제안(Inference)이다.

| # | 보내는 쪽 → 받는 쪽 | 넘기는 산출물 | 통과 조건 (Exit criteria) | HVE 도구 |
|---|---|---|---|---|
| H1 | SME → PM | 통제 카탈로그, 베이스라인, 증적 기준, 제약 | 모든 항목에 `validated/assumed/unknown/conflicting` 표시, 출처 | `/rpi-research` |
| H2 | SME → Engineer (WP2) | API/UI 커버리지 표 초안 | 칸이 `Unknown`이면 Learn 확인 전까지 채우지 않음 | `/rpi-research` |
| H3 | PM → Architect | BRD/PRD, AC, 비목표(쓰기 제외) | AC가 테스트 가능, MVP 범위 확정 | BRD/PRD Builder |
| H4 | Architect → Tech Lead | 아키텍처 노트, ADR, 위협 모델, 플러그인 표면 | 모든 구성 요소가 요구사항에 매핑, 개념도 표시 | System Architecture Reviewer, Arch Diagram Builder, Security Planner |
| H5 | Tech Lead → Engineer | 구현 계획(Pxx/Pxx-Txx), 환경, 리뷰 규칙 | 계획 비평 `Pass`, Blocked/Not ready 없음 | `/rpi-plan` |
| H6 | PM → Tech Lead | 첫 P0 승인 요청 | 책임 담당자 서면 승인 | (사람) |
| H7 | Engineer → Tech Lead | 변경 기록, 테스트 증거, PR | 증거가 있는 체크박스만 완료 | `/rpi-implement`, `git-commit`, `pull-request` |
| H8 | Tech Lead → PM / SME | 리뷰 결과(`RV-xxx`), 라우팅 | 결함→구현, 결정 격차→계획, 증거 격차→조사 | `/rpi-review` |
| H9 | Engineer/Tech Lead → Security | 데이터 흐름, 권한 목록, 로깅 | 비밀·개인정보가 텔레메트리에 없음 | Security Planner |
| H10 | PM → 게시 | 가격 권장안, 리스팅 초안, 미해결 게이트 | 승인 공백 목록과 담당자 | Marketplace Coach, Copilot Agent Store Coach |

## 인계 산출물 공통 필드 제안 (HVE 린터 호환 미확인)

```yaml
hve_role: sme | pm | architect | tech-lead | engineer | security
owner: <name>
rpi_phase: research | plan | implement | review
status: draft | in-review | approved | blocked    # approved는 사람만 설정
evidence: validated | assumed | unknown | conflicting
upstream: [<path>]
downstream: [<path>]
gate:
  approver_role: tech-lead | pm | security | facilitator
  approved: false
```

## 라우팅 규칙 (RPI Review 결과 → 담당)
| 발견 유형 | 돌아가는 곳 | 담당 |
|---|---|---|
| 결함 | 구현 | Engineer |
| 결정 격차 | 계획 | Tech Lead (설계 영향 시 Architect) |
| 증거 격차 | 조사 | SME |
| 범위·가격·라이선스 변경 | 계획 + 구현 중단 | PM (A), Tech Lead (승인) |

관련: [[RACI-Matrix]], [[Backend-Work-Breakdown]]

---

## 업데이트 2026-11-03: 인터페이스 확장
H11~H15(Security 판정, SME 제한 환경 입력, Architect 타당성 피드백, 퍼실리테이터 승인 요청/확인)가 추가되었다. 전체 구조도와 컴포넌트 경계별 소유는 [[Interface-Structure-Map]].
