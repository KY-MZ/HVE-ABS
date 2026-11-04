---
type: role-analysis
role: Engineer
status: draft
evidence: documented
updated: 2026-11-03
---

# Engineer 역할 분석

## 책임 (Documented)
조사 → 계획 → 구현 → 리뷰 → 전달. 언어별 코딩 표준 자동 적용(C#, Python, Bash, Bicep, Terraform, GitHub Actions), Git 관리.

## 도구
`rpi-research`, `rpi-plan`, `rpi-implement`, `rpi-review`, RPI Agent, `code-review`, `hve-builder`, `git-commit` / `pull-request` / `git-merge`

## RPI 단계 정의
| 단계 | 핵심 | 산출물 |
|---|---|---|
| Research | 증거 부족 시에만. 읽기 전용. 생략 사유 기록 | `research/<date>/<task>-research.md` |
| Plan | 소스 변경 없음. `Pxx`/`Pxx-Txx`, 계획 비평 `Pass`/`Revise`/`Blocked` | 계획서, 비평 |
| Implement | 승인된 작업만. 체크박스는 증거가 있을 때만 | `changes/<date>/<task>-changes.md` |
| Review | 선택. 소스 수정 없음. `RV-xxx` + 심각도 | `reviews/logs/...` |

리뷰는 실행 상태(`Complete`/`Partial`/`Blocked`)와 결과(`Conformant`/`Defects found`/`Not accepted`)를 분리한다. 후속 라우팅: 결함→구현, 결정 격차→계획, 증거 격차→조사.

## 구현 단계 규칙
- 계획/PRD가 `Blocked`/`Not ready`면 `/rpi-implement` 금지
- 사람이 첫 P0 구현을 서면 승인
- 한 번에 한 작업, 테스트 동반
- 범위·아키텍처·보안·개인정보·RAI·가격·라이선스 변경 시 중단하고 계획으로 복귀
- RPI 단계 사이에는 `/clear`로 맥락 정리 (엔지니어 가이드 팁)
- 새 프로젝트/기존 프로젝트 경로(1A/1B): 검토·승인된 `.copilot-tracking/`만 복사

## 이 문서에서 확인되지 않은 것
- PM과의 인터페이스: engineer.md에 없음 (Unknown). 워크샵 문서 기준으로는 PM이 P0 승인을 진행하고 Engineer가 변경 기록을 남기는 구조.
- 엔지니어 역할의 상세 책임은 implementation.md에서도 간략하게만 서술됨.

---

## 추가 2026-11-03: Declarative agent + 백엔드 프로젝트에서의 Engineer 담당
상세 표는 [[RACI-Matrix]]. Engineer가 R인 주요 항목:
- **WP4 구현**: Entra 앱 등록, SSO(OBO)·동의 흐름. 동의 미충족 시 401 반환으로 프롬프트 유도, `identifierUris`와 허용 클라이언트 등록
- **WP5~WP8**: 플러그인(MCP 또는 OpenAPI) 구현, 평가 엔진, 관리 API 읽기 연동, 응답 요약기
- **WP9 패키징**: Agents Toolkit(VS Code, Node 20/22)로 Declarative agent·플러그인 패키지, Kiota 활용 가능
- **WP11 연동**: SaaS fulfillment/랜딩 페이지
- **WP13 테스트 구현**: Positive/Negative Path 자동화, 프롬프트 인젝션 시나리오
- **WP2 검증**: SME의 API/UI 커버리지 표 칸을 Microsoft Learn로 확인 (GA/Preview 구분)
- **P2**: UI 전용 증적 워커는 WP2에서 필요성이 입증된 항목만
- **규칙**: 승인된 P0 작업만, 한 번에 하나, 증거가 있을 때만 체크박스 완료. 작성한 코드의 승인은 Tech Lead
- 사이드로드 사전 조건: Custom App Upload Enabled, Copilot Access Enabled
