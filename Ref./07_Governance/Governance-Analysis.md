---
type: governance
status: draft
evidence: documented+inference
updated: 2026-11-03
---

# 거버넌스 / 승인 게이트

## 팀 구성 (README, Documented)
스폰서, 퍼실리테이터, SME, 디자이너/리서처, 테크니컬 리드, 엔지니어. 보안·개인정보 등 전문가는 파트타임 리뷰어. 핵심 인원 4~6명.

## 승인 게이트 목록
| 게이트 | 승인자 | 근거 |
|---|---|---|
| GitHub Issue 생성 | 퍼실리테이터 + 저장소 권한 | solution |
| 생성 콘텐츠 초안 해제 | 책임자 검토 | solution |
| 첫 P0 구현 | 책임 담당자(제품/기술 리드/딜리버리)의 서면 승인 | implementation |
| PR/마일스톤 승인 | 사람 검토자 (체크박스 대리 완료 금지) | implementation |
| 가격/상업 조건 | PM, 재무 등 | publishing, implementation |
| 제출 전 | 보안, 개인정보, 접근성, 법무, 지원, 사업 담당자 승인 | publishing |
| 인증/게시/공동판매 상태 | 게시자(Partner Center)가 통제. 준비 상태와 분리 관리 | implementation |

## 변경 관리 (team-adoption, Documented)
- 지침·에이전트·스킬 변경은 PR 리뷰 필요, CODEOWNERS로 리뷰어 배정
- 지침 충돌 해소 순서: `copilot-instructions.md` 최우선 > 더 구체적인 `applyTo` > 소유자 PR 해소
- 폐기: 폐기 공지 → 마이그레이션 일정 → `.github/deprecated/` → 전환 기간 후 제거

## 리드 본인이 겸직할 때의 거버넌스 (Inference)
- 같은 사람이 작성자·검토자가 되는 게이트는 만들지 않는다. 최소한 다른 참가자의 확인 서명을 받는다.
- 열린 이슈는 모두 담당자·기한을 붙인다 (완료 기준과 직결).

---

## 추가 2026-11-03: 승인 배정 정리
- 첫 P0 구현 서면 승인: Tech Lead (PM은 진행만) — [[RACI-Matrix]]
- 제출 전 보안 승인: Security 파트타임 리뷰어 (WP4, WP10 협의 필수)
- ADR 수용: Tech Lead
- 가격·상용화 권장안: PM (재무·영업 검토 필요)
