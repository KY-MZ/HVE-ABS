---
type: role-analysis
role: PM
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# PM 역할 분석

## 책임 경계
| 항목 | 내용 | 증거 |
|---|---|---|
| 핵심 | SME 컨텍스트를 요구사항, 우선순위, 백로그로 전환 | documented |
| 소유 | BRD/PRD 초안 | documented |
| 계획 | `/rpi-plan` 구현 계획, MVP 백로그 | documented |
| 가격 | 재무·엔지니어링·영업과 함께 소유. 결과는 "승인된 가격표가 아니라 검토용 권장안" | documented |
| 구현 승인 | 첫 P0 작업의 서면 승인 진행 | documented |
| 의사결정 권한 | BPM 가이드에 명시 없음. 다만 "자문 없이 우선순위 결정 금지" 권고 | documented |
| 하지 않는 것 | 근거 생성(SME), 아키텍처 확정(Tech), 사람 검토 체크박스 대리 완료 | documented |

> 주의: HVE 역할 가이드의 **Business Program Manager는 베타**이며 TPM과 구분된다. BPM = 비즈니스 수준 요구사항·이해관계자·성과 추적, TPM = 기술 스펙·작업 항목 분해. 워크샵 문서의 "PM"이 둘 중 어느 쪽에 가까운지는 명시되어 있지 않다 (Unknown).

## 사용 에이전트 / 프롬프트
| 대상 | 도구 |
|---|---|
| BRD | BRD Builder (`brd-builder`) |
| PRD | PRD Builder (`prd-builder`) |
| 계획 | `/rpi-plan` (RPI Agent) |
| 백로그 구조 | Functional Planner |
| 이슈 | Backlog Manager (드라이런·중복 검사), GitHub Backlog Executor |
| 조사 | `/rpi-research` |

## 워크샵 시간대별 행동
| 단계 | PM 행동 | Exit criteria |
|---|---|---|
| 개요 | 성과, 시나리오, 첫 출시 범위, 역할 합의 | 성과 문장 1개, 범위 외 항목 목록 |
| Part 1 | BRD/PRD 초안: 문제, 이해관계자, 측정 가능한 결과, 범위/비목표, 제약, 위험, 가정 | AC가 테스트 가능 |
| Part 2 | 계획 + 백로그. P0/P1/P2는 순서가 필요할 때만 | 결과→백로그 추적 가능 |
| 솔루션 | 결과·요구사항·첫 출시 범위 발표. 백로그 준비 상태/중복 검사 | 담당자 없는 갭 0 |
| 게시 | MVP 가격안 (공개/비공개, 고정/사용자당). 에이전트 요금과 백엔드 요금 이중 청구 방지 | 승인 공백 목록 |
| 핸드오프 | P0 서면 승인 진행 | `Blocked`/`Not ready` 없음 |

## 통과 기준 (solution 문서)
- 각 스토리에 사용자·요구사항·기대 결과
- 각 AC 확인 가능/테스트 가능
- 핵심 요구사항·결정이 백로그와 연결
- 이슈는 퍼실리테이터 승인 + 저장소 권한이 있을 때만 생성

## 전문가 위임이 필요한 항목
Marketplace Coach / Agent Store Coach 에이전트는 세무·법률·재무 조언을 하지 않는다. 법인·관할·계약 의존 질문은 전문가에게 넘기고 작업 항목으로 기록한다.

## 위험
- 가격 소유자가 주제 제안자와 같으면 낙관 편향 → 재무/영업 검토를 일정에 포함
- 에이전트 생성 백로그의 과잉 분해 → "필요할 때만 개요를 만든다"는 문서 지침을 따른다

관련: [[PM-SME-Dual-Hat-Controls]], [[Publishing-Paths]]

---

## 추가 2026-11-03: Declarative agent + 백엔드 프로젝트에서의 PM 담당
상세 표는 [[RACI-Matrix]]. PM이 A인 항목:
- **MVP 범위(D2)**: 읽기 전용(안 A)을 P0로, 쓰기(안 B)는 비목표로 BRD/PRD에 명시
- **AC 작성**: "정책 존재 / 적용 / enforcement"를 분리한 테스트 가능한 AC, Positive/Negative Path를 각각 AC로
- **WP9 에이전트 지침의 의도**: 페르소나, 하지 않는 일(변경 수행 금지), 증거 없이 단정하지 않는 규칙. 구현은 Engineer
- **WP11 SaaS 오퍼·가격 권장안**: 에이전트 요금과 백엔드 요금의 이중 청구 방지, 승인 공백 목록
- **WP12 검증 총괄**, **WP14 리스팅·약관·고객 설정 안내**
- **P0 승인 진행** (승인은 Tech Lead가 서면으로)
- **하지 않는 것**: 아키텍처 확정, 코드 승인
