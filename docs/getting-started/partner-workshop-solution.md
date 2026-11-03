---
title: 파트너 워크샵 솔루션
description: 역할별 결과물을 공유 솔루션 패키지, 백로그, 아키텍처 뷰, 게시 준비 계획으로 통합
sidebar_position: 10
author: Microsoft
ms.date: 2026-11-01
ms.topic: tutorial
keywords:
  - workshop solution
  - backlog
  - requirements traceability
  - Azure diagram
  - publication readiness
estimated_reading_time: 8
---

## 워크샵 일정

| 단계 | 활동                                                                                       | 시간   |
|------|-------------------------------------------------------------------------------------------|-------|
| 1    | [워크샵 개요](partner-workshop.md)                                                     | 30분 |
| 2    | [워크샵 환경 설정(로컬 VS Code)](partner-workshop-setup.md)                                            | 30분 |
| 3-1    | [역할별 트랙 Part1: 계획/비전/경험](partner-workshop-role-tracks.md)                      | 45분 |
| 3-2    | [역할별 트랙 Part2: 아키텍처 설계, 백로그](partner-workshop-role-tracks-2.md)                 | 45분 |
| 4    | [**검증 및 솔루션**](partner-workshop-solution.md)                                             | 30분 |
| 5    | [Microsoft Marketplace 및 Copilot Agent Store 준비](partner-workshop-publishing.md)       | 60분 |
| 6    | [구현 및 상용화로의 핸드오프](partner-workshop-implementation.md)                            | 30분 |

## 목표

비즈니스 컨텍스트, 요구사항, 사용자 경험, 백로그, 아키텍처 및 출시 준비 계획을 하나의 일관된 흐름으로 연결한 솔루션 초안을 작성합니다.

## 권장 솔루션 흐름

1. 각 역할은 2분 동안 자신의 결과물(artifact)을 요약하세요.
2. 아래의 프로덕션 아티팩트를 엽니다.
   `.copilot-tracking/research/`, `.copilot-tracking/prd-sessions/`,
   `.copilot-tracking/dt/`, `.copilot-tracking/plans/`,
   `.copilot-tracking/details/`, `.copilot-tracking/github-issues/` 
3. 파일 간의 용어를 비교하여 일관성을 확인하고, 서로 상충되는 내용을 조정합니다.
4. 도메인 용어와 비즈니스 규칙은 SME 컨텍스트 팩을 기준으로 합니다.
5. 각 사용자 스토리에 사용자, 요구사항, 기대하는 결과가 명확하게 포함되어 있는지 확인합니다. 
   (예: "누가 무엇을 원하는지", "어떤 결과를 원하는지")
6. 각 수락 기준이 확인 가능하고 테스트 가능한지 확인하세요.
7. 각 아키텍처 구성 요소가 최소 하나의 요구사항에 매핑되는지 확인하세요.
8. 중요한 요구사항과 주요 결정 사항이 실제 실행할 백로그 항목으로 연결되어 있는지 확인합니다.
9. 사용자 경험에 불확실한 상황, 사용자 피드백, 접근 실패, 
   그리고 사람의 개입이 필요한 경우가 모두 반영되어 있는지 확인합니다.
10. Publishing 워크샵에서 추가로 검토할 수 있도록, 아직 확정되지 않은 게시 관련 사항을 아키텍처 노트에 기록하세요.

## 추적성(Traceability) 검토

**RPI-Plan**을 선택하고 다음 프롬프트를 입력하세요:

```text
Review the production artifact set under `.copilot-tracking/research/`,
`.copilot-tracking/prd-sessions/`, `.copilot-tracking/dt/`,
`.copilot-tracking/plans/`, `.copilot-tracking/details/`, and
`.copilot-tracking/github-issues/` as one solution pack. Build a traceability
matrix from context facts and decisions to requirements, experience needs,
architecture components, backlog items, tests, and publication gates. Save
the matrix under `.copilot-tracking/details/`. Report missing links,
contradictions, unsupported claims, and unowned risks. Do not implement or
publish anything.
```

한글 프롬프트:

```text
경로에 있는 제작 산출물 세트를 하나의 솔루션 팩으로 검토하세요. 
컨텍스트의 사실과 결정사항부터 요구사항, 경험 요구, 아키텍처 구성 요소, 백로그 항목, 테스트, 
출판 게이트까지 추적 가능 매트릭스를 구축하세요. 
매트릭스를 `.copilot-tracking/details/` 경로에 저장하세요. 
누락된 연결고리, 모순, 근거 없는 주장, 소유자가 없는 위험 요소를 신고해 주세요. 
아무것도 구현하거나 배포하지 마세요.
```

실행 후 다음 단계를 완료하세요:

1. `.copilot-tracking/details/` 아래에 매트릭스 초안을 기록하세요.
2. 갭이 있는 곳에 담당자를 지정하세요.
3. 워크숍의 참고 자료를 바탕으로 해결할 수 있는 갭을 보완합니다.
4. 남아 있는 게시 관련 과제를 담당자와 함께 아키텍처 노트에 정리합니다.
5. 책임 있는 사람이 검토할 때까지 생성된 콘텐츠를 초안으로 표시하세요.

다음 워크숍에서 게시에 필요한 정보를 Microsoft Marketplace Coach에 전달하면, 이를 기반으로 공식 Marketplace 구현 계획이 `.copilot-tracking/plans/`에 생성됩니다. 따라서 이번 솔루션 검토 단계에서는 별도의 게시 준비 문서를 만들 필요가 없습니다.

### 프로젝트 매니저: GitHub Issues

1. **Backlog Manager**를 선택하세요.
2. `.copilot-tracking/github-issues/` 아래의 백로그 계획을 준비 상태와
   중복 여부를 기준으로 검사하도록 요청하세요.
3. 저장소, 레이블, 마일스톤, 담당자, 이슈 계층 구조를 확인하세요.
4. 변경 전에 드라이런(dry-run) 요약을 요청하세요.
5. 제안된 이슈 제목과 수락 기준을 검토하세요.
6. 퍼실리테이터의 승인과 저장소 권한이 있을 때만 이슈를 생성하세요.

### 프로젝트 매니저: Markdown 전용 대안

1. 백로그 계획은 `.copilot-tracking/github-issues/`에 특정 시스템에 종속되지 않는 공통 백로그로 관리합니다.
2. 대상 시스템, 담당자, 상태, 외부 ID를 위한 열을 추가하세요.
3. 워크샵 후 승인된 각 항목을 실제 시스템에 등록하거나 생성할 담당자를 지정하세요.

### 엔지니어: 아키텍처 리뷰

1. `.copilot-tracking/details/`에 있는 아키텍처 노트와 다이어그램을
   Markdown 미리보기로 여세요.
2. 사용자 요청이 Microsoft 365 Copilot에서 시작해서 Azure API, 
   정보 검색 계층(Retrieval Layer), AI 모델을 거쳐 최종 응답으로 
   돌아오기까지의 전체 흐름을 확인합니다.
3. 콘텐츠 수집 및 업데이트 경로를 별도로 따라가세요.
4. 권한 부여가 어디에서 적용되는지 확인하세요.
5. 비밀 정보와 키가 어디에 저장되는지 확인하세요.
6. 프롬프트, 검색된 콘텐츠, 응답, 피드백이 어디에서 기록(log)될 수 있는지
   확인하세요.
7. 텔레메트리 데이터에 비밀 정보나 불필요한 개인 데이터를 수집되지 않는지
   확인하세요.
8. 모델, 검색, 아이덴티티, 종속성 장애에 대한 실패 경로를 추가하세요.
9. 비용 담당자와 운영 담당자를 추가하세요.
10. 인프라 소스와 배포 검증이 존재할 때까지 다이어그램을 개념적인 것으로
    표시하세요.

## 10분 동안 팀 토론

1. PM이 결과, 요구사항, 첫 출시 범위를 발표합니다.
2. SME가 주요 제약과 미해결된 도메인 질문을 발표합니다.
3. 디자이너가 주요 여정과 사람이 검토해야할 포인트를 발표합니다.
4. 기술 리드가 아키텍처 뷰와 게시 경로를 발표합니다.
5. 팀에서 가장 중요한 3가지 위험 요소를 선정합니다.
6. 퍼실리테이터가 담당자와 다음 리뷰 일정을 확인합니다.

### 다음 단계
[**Microsoft Marketplace 및 Copilot Agent Store 준비**](partner-workshop-publishing.md)를 진행하세요.

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
