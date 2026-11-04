---
type: decision
status: accepted
decided-by: user
date: 2026-11-03
---

# 결정 001: Publishing 범주는 Microsoft 365 Copilot

- 맡은 역할(모자): 프로그램 리드 (PM+SME 겸직)
- 결정 내용: HVE 참여의 게시 범주를 Microsoft 365 Copilot 방향으로 확정한다.
- 근거: 사용자 지시. Microsoft Learn 확인 결과는 [[M365-Copilot-Path-Analysis]] 참조.
- 검토한 대안: Azure Managed Application 경로 (HVE 자료가 기본으로 예시하는 쪽)
- 영향 범위:
  - 제출 주제는 Declarative agent(+MCP/API 플러그인) 중심으로 재정의
  - "하네스 Wrapping 패키지"는 에이전트 뒤 백엔드로 재배치
  - HVE Part 2 기술 트랙의 Azure 중심 가정을 보정
- 되돌리는 방법: [[Publishing-Paths]]의 비교표로 복귀, Azure 경로 항목 재개
- 확인 서명자 (본인 외): 미지정 → 퍼실리테이터에게 확인 필요
- 후속 조치: D1~D4 결정, API/UI 커버리지 표 작성, 개발 테넌트 확보

## 아직 닫히지 않은 것
에이전트 유형(declarative / custom engine), MVP 범위(A / A+B), 백엔드 호스팅, 수익화 구조.
