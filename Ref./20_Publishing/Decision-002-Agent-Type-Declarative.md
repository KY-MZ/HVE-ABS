---
type: decision
status: accepted
decided-by: user
date: 2026-11-03
supersedes: D1 (open)
---

# 결정 002: 에이전트 유형은 Declarative agent로 시작

- 맡은 역할(모자): 프로그램 리드
- 결정 내용: MVP는 Declarative agent(+MCP/API 플러그인 액션)로 시작한다. 가치의 본체는 공통 백엔드에 둔다.
- 근거: 사용자 판단 ("M365 Copilot의 MW 팀 취지에 맞음"). 비교 근거는 [[Agent-Type-Decision-D1]].
- 검토한 대안: Custom engine agent (선제 알림·오케스트레이션이 MVP에 필수일 때 재검토)
- 영향 범위:
  - 호스팅: 오케스트레이터 호스팅 불필요, 백엔드(MCP/API 서버)만 ISV가 호스팅
  - RAI·컴플라이언스: M365 표준 상속, 백엔드 데이터 처리는 직접 책임
  - 기능 제약: 사용자 시작형만. 선제 알림, 정기 점검 푸시는 MVP 비목표
  - 설계 제약: 플러그인 5개 이하, 함수·도구 10개 이하 권장, 큰 응답은 토큰 한도로 잘림
- 되돌리는 방법: 공통 백엔드는 유지하고 Agents SDK 기반 Custom engine 셸을 추가 (전환 경로 자체는 문서에 명시 없음)
- 확인 서명자 (본인 외): 미지정
- 재검토 트리거: 선제 알림/정기 점검/채널 단위 협업이 MVP 필수로 바뀌는 경우

## 이 결정으로 닫힌 것과 남은 것
- 닫힘: D1 (에이전트 유형)
- 남음: D2 MVP 범위(A 읽기 전용 vs 일부 쓰기), D3 백엔드 호스팅(ISV 호스팅 vs 고객 구독), D4 수익화(연결 SaaS 오퍼 vs BYOL)

역할별 담당은 [[RACI-Matrix]], 작업 분해는 [[Backend-Work-Breakdown]].
