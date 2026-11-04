---
type: role-analysis
role: Architect
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# Architect 담당 범위 (Declarative agent + 백엔드)

> HVE `roles/README`는 "Tech Lead / Architect"를 한 역할로 정의한다. 여기서는 효율을 위해 설계(Architect)와 전달·승인(Tech Lead)으로 분리한 제안이다. 분리 근거는 [[RACI-Matrix]].

## 핵심 질문
"이 시스템이 안전하고 심사 가능한 구조인가, 그리고 모든 구성 요소가 요구사항에 매핑되는가"

## 담당 산출물

| 산출물 | 내용 | 위치 |
|---|---|---|
| 솔루션 아키텍처 | 에이전트 셸과 백엔드 경계, 데이터 흐름 (개념도 표시) | `.copilot-tracking/details/` |
| 신뢰 경계·위협 모델 | 프롬프트 인젝션(도구 출력 경유), 테넌트 간 데이터 혼입, 과도한 위임 권한, 비밀 노출 | Security Planner 연계 |
| 인증·동의 설계 | Entra SSO(OBO), 위임 vs 애플리케이션 권한 선택, 최소 권한, 테넌트 관리자 승인 절차 | ADR |
| 플러그인 표면 설계 | 5개 이하 플러그인, 함수 10개 이하, 굵은 단위, 응답 크기 규칙 | ADR + OpenAPI 초안 |
| 증적 스키마 | "정책 존재 / 적용 / enforcement" 관찰 결과와 해석 분리, 증적 링크 | 스키마 문서 |
| 멀티테넌트 분리 모델 | 테넌트 키, 저장소 분리, 보존, 삭제 | ADR |
| 게시 가정 | 호스팅 위치, 데이터 상주, 테넌트 격리 | 게시 계획 입력 |

## 판단 기준 (Documented 제약에서 도출)
- 큰 증적은 Copilot에 직접 반환하지 않는다: 토큰 한도로 잘림 → 요약 + 증적 저장소 링크
- 함수는 굵게: 10개를 넘으면 품질 저하 가능
- 인증: MCP 플러그인은 API key 미지원, 익명은 개발용
- 개념도는 인프라 소스와 배포 검증이 없는 동안 "개념적"으로 표시 (HVE 통과 기준)

## 본인 경험과의 접점 (Inference)
Control Plane / Enforcement Plane / Evidence Plane 분리, Positive/Negative Path 검증, 규제·제한망 제약은 위 산출물 중 위협 모델, 증적 스키마, 인증 설계에서 직접 쓰인다.

## 인계
- 받는 것: PM의 BRD/PRD·AC·비목표 (H3), SME의 통제 카탈로그 (H1)
- 넘기는 것: 아키텍처·ADR·위협 모델 → Tech Lead (H4)
- 서명: ADR의 A는 Tech Lead. 본인이 Architect를 겸하면 다른 사람이 서명한다.

## HVE 도구
System Architecture Reviewer, Arch Diagram Builder, Security Planner, ADR Creation 에이전트 파일(`adr-creation.agent.md`)이 `.github/agents/project-planning/`에서 확인됨.

관련: [[Tech-Lead-Responsibilities]], [[Engineer-Role-Analysis]], [[Handoff-Interfaces]]
