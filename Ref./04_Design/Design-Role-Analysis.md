---
type: role-analysis
role: Design
status: draft
evidence: documented
updated: 2026-11-03
---

# Design / 리서처 역할 분석

## 책임 경계
- 목표: 비즈니스 컨텍스트를 명확한 사용자 경험으로 구체화하고 문제에 대한 공통 이해를 만든다.
- 입력: SME 컨텍스트 패키지, 사용자 리서치, 스케치/와이어프레임
- 산출물: `.copilot-tracking/dt/<project>/` 아래 `user-research.md`, `journey-notes.md`, `experience-draft.md`, `screens/`, `wireframes/`
- 원칙: 디자인 결정은 "가정이 아닌 실제로 관찰된 사용자 요구"에 근거. 관찰과 가정을 구분

## 활동
1. Microsoft AI Discovery Cards 워크샵으로 에이전틱 AI 기능 브레인스토밍
2. 주 사용자 1명과 핵심 과제 1개 선정
3. 현재 여정과 Pain Point, 솔루션 적용 후 여정
4. 접근성(Accessibility Planner/Reviewer), 책임 있는 AI(RAI Planner/Reviewer) 요구사항 추가
5. UX UI Designer로 경험 개요, Design Thinking Coach / DT Learning Tutor로 퍼실리테이션
6. M365 Copilot Agent Store 적합성, Marketplace 패키징 방향 검토

## DT→RPI 인계 (Documented)
| 종료 지점 | DT 방법 | 인계 |
|---|---|---|
| 문제 정의 완료 | 1-3 | rpi-research |
| 컨셉 검증됨 | 4-6 | rpi-research |
| 구현 스펙 준비 | 7-9 | rpi-research |

인계 산출물 필드: `exit_point`, `dt_method`, `dt_space`, `handoff_target`, `date`, `artifacts`, `constraints`, `assumptions`. AI Discovery Cards 결과는 요구사항이 아니라 **DT 증거**로 취급한다.

## 제출 주제와의 관계 (Inference)
보안 구성 자동화 솔루션의 "사용자"는 일반 최종 사용자가 아니라 보안 관리자다. 그래서 핵심 여정은 "변경 전 영향 확인 → 승인 → 적용 → 검증 → 롤백"이고, 사람 개입 지점과 접근 실패 처리가 UX의 중심이 된다. solution 문서의 통과 기준(불확실성·피드백·접근 실패·사람 개입 반영)과 일치한다.

## 팀에 이 역할이 없을 때
리드를 맡는 본인이 대신 해야 한다면, 최소 산출물은 (1) 주 사용자 1명 정의, (2) 현재/목표 여정 각 1장, (3) 접근성·RAI 체크 결과 요약이다.
