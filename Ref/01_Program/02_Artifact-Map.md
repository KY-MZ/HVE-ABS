---
type: artifact-map
status: draft
evidence: documented
updated: 2026-11-03
---

# 산출물 저장 위치 맵

| 경로 | 내용 | 주 소유 |
|---|---|---|
| `.copilot-tracking/research/YYYY-MM-DD/<session>-session-context.md` | 세션 컨텍스트 (주제, 증거 위치, 증거 경계, 출력 경로) | Tech 리드 + PM |
| `.copilot-tracking/research/workshop-input/` | 합성/공개 입력 자료, `leancanvas.md` | SME |
| `.copilot-tracking/research/.../<task>-research.md` | 리서치 | SME |
| `.copilot-tracking/brd-sessions/` | BRD | PM |
| `.copilot-tracking/prd-sessions/` | PRD | PM |
| `.copilot-tracking/dt/<project>/` | `user-research.md`, `journey-notes.md`, `experience-draft.md`, `screens/`, `wireframes/` | Design |
| `.copilot-tracking/plans/` | 구현 계획 (`Pxx`, `Pxx-Txx`) | PM |
| `.copilot-tracking/details/` | 아키텍처 노트, 추적 매트릭스, `YYYY-MM-DD/solution-monetization-plan.md` | Tech / PM |
| `.copilot-tracking/github-issues/` | 백로그 계획 | PM |
| `.copilot-tracking/changes/` | 구현 변경 기록 | Engineer |
| `.copilot-tracking/reviews/logs/` | `/rpi-review` 결과 (`RV-xxx`) | 리뷰어 |
| `docs/planning/adrs/` | 아키텍처 결정 기록 | Tech |

## 운영 규칙 (Documented)
- 워크샵 사례: 합성/공개 자료만 저장소에. 실제 사례는 SharePoint/OneDrive/접근통제 Blob 등 승인된 위치에 두고 경로만 참조
- 자격 증명, 개인 데이터, 고객 비밀, 프로덕션 콘텐츠는 프롬프트와 파일에 넣지 않는다
- 검토된 결과만 팀 브랜치(`workshop/<team-name>`)에 커밋
- 검토 전 산출물은 초안 표시

> 이 Obsidian Vault는 위 `.copilot-tracking/`을 대체하지 않는다. 분석과 판단을 위한 별도 노트다. 실제 워크샵 산출물은 워크샵 저장소에 만든다.
