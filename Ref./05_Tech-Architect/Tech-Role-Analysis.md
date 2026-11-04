---
type: role-analysis
role: Tech-Architect
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# Tech / Architect 역할 분석

## 책임 경계
- 목표: 구현 계획에 맞춰 솔루션 접근, 아키텍처, 게시 고려 사항을 구성
- 입력: 구현 계획, PRD, 경험 초안
- 산출물: 아키텍처 노트(`.copilot-tracking/details/`), 다이어그램(Mermaid→이미지), 보안 위험/후속 조치, ADR(`docs/planning/adrs/`), 게시 계획 입력(잠정 제품 분할, 통합 경계, 제약, 미해결 결정)
- 환경 설정(2단계)의 기술 리드 담당: 워크샵 브랜치, 세션 컨텍스트 파일, 자료 취급 원칙 확인

## 에이전트
System Architecture Reviewer, Arch Diagram Builder, Security Planner, RPI Agent

## 게시 가정에 포함할 최소 항목 (Documented)
- SaaS 또는 Azure Managed Application 모델
- M365 에이전트가 보조 경험인지 여부
- 데이터 상주, 테넌트 격리
- 상세 Marketplace 평가는 별도 후속 워크샵

## 솔루션 단계의 아키텍처 리뷰 10단계 (Engineer 수행, Documented 요약)
요청 흐름, 콘텐츠 수집 경로, 권한 부여 지점, 비밀 저장 위치, 로깅 위치, 실패 경로(모델·검색·아이덴티티·의존성), 텔레메트리에 비밀/개인정보 유입 여부, 비용·운영 담당자 지정

## 통과 기준
- 모든 구성 요소가 최소 하나의 요구사항에 매핑
- 인프라 소스와 배포 검증이 없는 동안 다이어그램은 **개념적**으로 표시

## 문서의 Azure 전제
Azure로 한정한다는 명시는 없다. 다만 Well-Architected, CAF, Azure Managed Application, Azure 스타일 아이콘이 전제로 등장한다 (Inference: Azure 중심 설계로 보는 것이 자연스러움).

## 본인 경험과의 접점 (Inference)
| 워크샵 요구 | 매핑 가능한 경험 |
|---|---|
| 권한 부여 지점, 최소 권한 | Control Plane / Enforcement Plane 분리 |
| 실패 경로 | 인증·동기화 경로 분리 분석 |
| 감사 증적 | Evidence Plane 설계 |
| 개념도 표시 | 검증된 사실과 추론의 구분 |

## 겸직 리드 시 주의
PM/SME로서 요구사항을 쓰면서 동시에 아키텍처를 확정하면 문서의 역할 분리 취지(요구사항→구성요소 매핑 검증)가 약해진다. 아키텍처 결정은 ADR로 남기고 다른 참가자가 매핑 검토를 서명하도록 한다.

보강 필요: `tech-lead.md`, `security-architect.md` 미확인 ([[02_Evidence-Log]]).

---

## 추가 2026-11-03: Architect와 Tech Lead 분리
이 문서는 HVE 기술 트랙 전체를 다룬다. Declarative agent + 백엔드 프로젝트에서는 설계 책임과 전달·승인 책임을 나눠 다음 문서로 상세화했다.
- [[Architect-Responsibilities]]: 신뢰 경계, 인증·동의, 플러그인 표면, 증적 스키마, 위협 모델, ADR
- [[Tech-Lead-Responsibilities]]: 기술 계획, 환경, 리뷰 게이트, P0 기술 승인, 검증 통과
- 겸직 규칙은 [[RACI-Matrix]]
