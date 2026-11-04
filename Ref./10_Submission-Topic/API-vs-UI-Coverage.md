---
type: verification-table
status: template
evidence: unknown
updated: 2026-11-03
---

# 설정 항목별 API / UI 커버리지 표 (작성 대기)

목적: 솔루션 대상 설정 중 **API/PowerShell로 읽기·쓰기가 가능한 것**과 **화면(UI)으로만 가능한 것**을 분리한다. 이 표가 있어야 Playwright가 보조 수단인지 핵심 수단인지 판단할 수 있다.

> 이 표의 칸은 Microsoft Learn 등 공식 문서로 확인하기 전까지 `Unknown`이다. 추정으로 채우지 않는다.

| # | 설정 항목 | 읽기 API | 쓰기 API | PowerShell | UI만 가능 | 필요 권한 | 출처(Learn URL) | 상태 |
|---|---|---|---|---|---|---|---|---|
| 1 | `<항목>` | Unknown | Unknown | Unknown | Unknown | Unknown | | 미확인 |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

## 작성 방법
1. 솔루션 범위에 넣을 상위 10개 설정을 SME로서 선정
2. 항목마다 Microsoft Learn에서 Graph 리소스/cmdlet 존재 여부와 필요 권한 확인 (Preview/GA 구분)
3. 존재하지 않으면 `UI만 가능`으로 표시하고, 그 항목에 한해 브라우저 증적 사용
4. 결과를 [[Topic-Fit-Analysis]]의 3절 가설 검증에 반영
