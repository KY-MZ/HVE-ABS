---
type: index
status: draft
updated: 2026-11-03
---

# HVE Vault – 사용 안내

**Vault Root (사용자 환경)**: `D:\OneDrive - Megazone Cloud Corporation\Study\HVE`
이 폴더 전체를 위 경로에 복사한 뒤 Obsidian에서 해당 폴더를 Vault로 엽니다.

## 목적
HVE 파트너 워크샵을 리드하기 위해 **역할별 경계**, **산출물 소유권**, **인계(Handoff) 조건**, **제출 주제 적합성**을 증거 기반으로 정리한다.

## 폴더 구조

| 폴더 | 내용 | 역할 경계 |
|---|---|---|
| `00_Index` | 사용 안내, 역할 경계 맵, 증거 로그 | 전 역할 공통 |
| `01_Program` | 프로그램 개요, 산출물 맵 | 전 역할 공통 |
| `02_SME` | 산업 전문가 분석 | 컨텍스트 원천 |
| `03_PM` | PM 분석 | 요구사항·백로그·가격 |
| `04_Design` | 디자인/리서치 분석 | 사용자 경험 |
| `05_Tech-Architect` | 기술/아키텍트 분석 | 아키텍처·게시 계획 |
| `06_Engineer` | 엔지니어 분석 | 구현·검증 |
| `07_Governance` | 스폰서·퍼실리테이터·승인 게이트 | 승인·감독 |
| `08_Delivery` | 작업 분해, 담당표(RACI), 인계 인터페이스 | 전달 계획 |
| `10_Submission-Topic` | 제출 주제 적합성, API/UI 커버리지 | 주제 소유자 |
| `20_Publishing` | 게시 경로 비교 | PM + Tech |
| `30_Dual-Hat` | PM+SME 겸직 통제, 경험 매핑 | 본인 |
| `40_Regulated-Environment` | 제한 환경(금융권) 대응 전략, 관찰 사실, 준비도 | SME |
| `90_Sources` | 출처 인덱스 | – |
| `99_Templates` | 템플릿 | – |

## 읽는 순서
1. [[01_Role-Boundary-Map]] → 2. [[01_Program-Overview]] → 3. 각 역할 분석 → 4. [[Topic-Fit-Analysis]] → 5. [[PM-SME-Dual-Hat-Controls]]

## 문서 규칙
- 모든 문서는 YAML frontmatter에 `type`, `status`, `evidence`를 둔다.
- 증거 등급: `documented`(README/하위 문서에 명시), `inference`(추론), `unknown`(미확인), `hypothesis`(가설).
- 사실/가정/결정/미해결 질문은 항상 분리한다 (워크샵 문서 자체의 원칙).
- 고객명, Tenant ID, 계정, IP, 토큰은 기록하지 않고 `<TenantId>` 같은 placeholder를 쓴다.
- 이 Vault의 내용은 **초안**이며, 문서 지적대로 책임자 검토 전에는 승인된 것으로 표시하지 않는다.

## 한계
- 아래 `90_Sources`에 적힌 문서만 읽었다. 읽지 않은 문서는 [[02_Evidence-Log]]의 "미확인" 표에 있다.
- 읽은 내용은 웹 페치 요약본이다. 가격·게시 요건·정책은 원문과 Partner Center로 재확인한다.
