---
type: role-analysis
role: SME
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# SME (산업 전문가) 역할 분석

## 책임 경계
| 항목 | 내용 | 증거 |
|---|---|---|
| 목표 | 설계·구축 전에 비즈니스 진실을 포착 | documented |
| 위치 | 팀 공통 컨텍스트의 출발점. 작업 순서상 첫 번째 | documented |
| 제공 | 비즈니스 사실, 규칙, 제약, 증거, 용어 | documented |
| 기준 권한 | 도메인 용어·비즈니스 규칙의 모순은 SME 컨텍스트 팩 기준으로 해소 | documented |
| 하지 않는 것 | BRD/PRD 소유(PM), 아키텍처 결정(Tech), 가격 소유(PM) | documented |

## 활동
1. 증거 수집: 정책, SOP, 프로세스 다이어그램, 메모, PDF, 스크린샷
2. 워크샵 사례는 `workshop-input/`에 합성·공개 자료만 정리
3. 실제 사례는 승인된 저장소에 두고 경로만 `/rpi-research`에 제공. 저장소에 고객·규제·기밀 증거를 복사하지 않는다
4. **Marketplace Lean Canvas** 작성: 문제, 고객 세그먼트, 가치 제안, 솔루션, 채널, 수익 모델, 비용, 지표, 경쟁 우위. 모르는 항목은 `Unknown`과 출처/필요 결정 메모
5. `/rpi-research` 실행: 사실, 영향받는 사용자, 규칙, 제약, 실패 사례, AI 가드레일, 미해결 질문
6. 사실 / 가정 / 결정 / 미해결 질문 분리 기록

## 산출물과 Exit criteria
| 산출물 | Exit criteria (Technical inference) |
|---|---|
| 컨텍스트 패키지 | 모든 주장에 출처 또는 `assumed` 표시 |
| Lean Canvas | `Unknown` 항목에 담당자 |
| 리서치 | 증거 경계(어디까지가 실측/문서/추정)가 명시됨 |

## 컨텍스트 패키지 신뢰도 표시 (DT-RPI 문서의 정의 재사용)
| 표시 | 의미 | 후속 처리 |
|---|---|---|
| validated | 다중 출처 확인 | 신뢰 입력 |
| assumed | 미검증 추정 | 검증 단계 포함 |
| unknown | 정보 격차 | 우선 조사 |
| conflicting | 증거 상충 | 작업 전 해결 |

## 규제 산업 SME가 추가로 제공할 수 있는 컨텍스트 (Inference)
- 제한망/Proxy/TLS 검사 환경의 egress 제약
- 감사 증적 보존, 관리 분리, 최소 권한 요건
- 데이터 상주, 테넌트 격리 요건
- "기능 존재 / 정책 설정 / 대상 적용 / 실제 enforcement"의 구분이 요구되는 검증 기준

## 위험
- 본인이 PM을 겸하면 자기 컨텍스트를 자기가 BRD로 옮기게 된다 → [[PM-SME-Dual-Hat-Controls]]
- HVE 가이드(roles/README)에는 SME 정의가 없다. 정의는 워크샵 문서에만 있다. 역할 기대치를 퍼실리테이터와 맞춘다.

관련: [[Role-Analysis-Template]], [[01_Role-Boundary-Map]]

---

## 추가 2026-11-03: Declarative agent + 백엔드 프로젝트에서의 SME 담당
- **WP1 통제 카탈로그 (A/R)**: 범위에 넣을 Tenant MW 보안 설정, 기대값, 증적 정의. "기능 존재 / 정책 설정 / 대상 적용 / 실제 enforcement" 4단계 중 어떤 증적이 어느 단계를 입증하는지 명시
- **WP2 API/UI 커버리지 표 초안 (A)**: 칸 확인은 Engineer가 Learn으로 검증. 확인 전에는 Unknown 유지
- **WP13 테스트 시나리오의 정답**: Positive/Negative 기대 결과, 프롬프트 인젝션 시나리오의 위험 정의
- **WP14 고객 설정 안내**: 라이선스, 권한, 동의, 제한망 egress 허용 목록 등 고객 측 준비 사항
- **용어·정확성**: 에이전트 지침과 응답이 설정 존재를 enforcement로 단정하지 않는지 검토
- 상세: [[RACI-Matrix]], [[Backend-Work-Breakdown]]
