---
title: 파트너 워크샵 - 역할별 트랙 Part2- PM 및 기술 트랙
description: HVE 파트너 워크샵을 위한 프로젝트 관리 및 기술 역할 가이드
sidebar_position: 10
author: Microsoft
ms.date: 2026-11-01
ms.topic: tutorial
keywords:
  - Project Manager
  - System Architecture Reviewer
  - Security Planner
  - HVE technical track
estimated_reading_time: 10
---

## 워크샵 일정

| 단계 | 활동                                                                                       | 시간   |
|------|-------------------------------------------------------------------------------------------|-------|
| 1    | [워크샵 개요](partner-workshop.md)                                                     | 30분 |
| 2    | [로컬 VS Code 설정](partner-workshop-setup.md)                                            | 30분 |
| 3-1    | [역할별 트랙 Part1: 계획/비전/경험](partner-workshop-role-tracks.md)                      | 45분 |
| 3-2    | [**역할별 트랙 Part2: 백로그, 아키텍처 설계**](partner-workshop-role-tracks-2.md)                 | 45분 |
| 4    | [검증 및 솔루션](partner-workshop-solution.md)                                             | 30분 |
| 5    | [Microsoft Marketplace 및 Copilot Agent Store 준비](partner-workshop-publishing.md)       | 60분 |
| 6    | [구현 및 상용화로의 핸드오프](partner-workshop-implementation.md)                            | 30분 |

이 문서는 파트너 워크샵의 프로젝트 관리 및 기술 트랙을 다룹니다. 요구사항, 사용자 경험,
구현 계획을 검토한 뒤 솔루션 접근 방식, 아키텍처, 보안 및 게시 고려
사항을 구성하세요.

## 프로젝트 관리 (PM) 트랙

### 목표

비즈니스 컨텍스트와 사용자 경험을 요구사항, 우선순위, 구현 계획을 갖춘
백로그 초안으로 전환하세요.

### 단계

1. `.copilot-tracking/research/`, `.copilot-tracking/prd-sessions/`,
   `.copilot-tracking/brd-sessions/`, `.copilot-tracking/dt/`의
   컨텍스트 패키지를 검토하세요. 이를 비즈니스 결과, 측정 가능한 성공
   지표, 기능 및 비기능 요구사항, 사용자 스토리, 수락 기준, 범위 외
   항목, 미해결 가정과 정렬하세요.
2. **RPI Agent**를 선택하고 `/rpi-plan`을 실행하여 요구사항과
   컨텍스트를 단계와 단계별 세부 사항을 갖춘 구현 계획으로
   전환하세요. 예시:

   ```text
   /rpi-plan
   `.copilot-tracking/research/`, `.copilot-tracking/brd-sessions/`, `.copilot-tracking/dt/` 디렉토리를 읽고, 'relationship-manager-fsi'의 첫 번째 MVP를 위한 간소화된 구현 계획을 수립하십시오.
   계획에는 단계별 목표, 산출물, 요구사항, 의존성, 위험 요소, 수용 기준이 포함되어야 합니다.
   근거에 기반한 작업 하나를 계획하십시오. 여기에는 신뢰할 수 있는 답변, 출처 인용, 권한을 고려한 정보 검색, 불확실성에 대한 명확한 표시, 사람에게 에스컬레이션하는 절차, 외부 작업 수행 전 확인 단계가 포함되어야 합니다.
   Microsoft Marketplace 및 Microsoft 365 Copilot Agent Store 출시 준비 요건에 맞춰 계획을 수립하되, 실제 게시 가능 여부는 최신 Microsoft 지침, Partner Center 상태 및 테넌트별 구현 가능성을 확인하기 전까지는 잠정적인 것으로 간주하십시오.
   어떠한 구현이나 게시 작업도 수행하지 마십시오.
   ```

   이는 `.copilot-tracking/plans/`에 작성되며 요구사항과 디자인
   컨텍스트에 연결되는 영구 기록을 만듭니다.

3. `.copilot-tracking/plans/`에 생성된 계획을 검토하고 필요에 따라
   단계별 세부 사항을 다듬으세요.
4. 팀이 요구사항에서 구현으로 이동하는 데 도움이 될 때만 백로그
   개요를 만드세요. 필요하다면 첫 MVP를 위해 에픽, 기능, 스토리, 작업과
   같은 가벼운 계층 구조를 사용하세요.
5. 팀에 순서 신호가 필요한 경우에만 P0, P1, P2와 같은 간단한 레이블로
   첫 MVP의 우선순위를 지정하세요. 이를 경직된 Agile 프로세스로
   만들기보다는 가볍고 결과 중심으로 유지하세요.
6. Microsoft Marketplace와 Microsoft 365 Copilot Agent Store의 게시
   준비를 위해 요구사항과 백로그 아티팩트를 준비하세요.
   컨텍스트, 요구사항, 경험을 선택하고 **Functional Planner**에게
   프롬프트하세요:

   ```text
   /functional-planner
   `.copilot-tracking/prd-sessions/`에 있는 요구사항, `.copilot-tracking/research/`에 있는 컨텍스트, `.copilot-tracking/dt/` 에 있는 experience draft 를 검토하십시오.
   에픽(Epic), 기능(Feature), 스토리(Story), 태스크(Task)를 명확히 정의하여, 즉시 구현 가능한 수준의 MVP 백로그 계획을 `.copilot-tracking/github-issues/` 내에 생성하거나 다듬어 주십시오.
   또한, 작업 순서를 정하는 데 도움이 된다면 P0, P1, P2와 같은 간단한 라벨을 사용하여 MVP 항목들의 우선순위를 지정하십시오. 아울러 Microsoft Marketplace 에 게시할 준비가 되었는지도 평가해 주십시오.
   결과물은 간결하고 성과 중심적이며, 백로그를 구체화하는 데 유용하도록 작성해 주십시오.
   ```

1. GitHub Issues를 대상으로 한다면 Backlog Manager에게 워크플로우를
   조율하도록 요청하고 GitHub Backlog Executor가 초기 MVP를 위한 첫
   상위 이슈와 하위 이슈를 생성하도록 하세요. **Backlog Manager**는
   추적성을 위해 결과로 생성된 이슈 링크와 요약을
   `.copilot-tracking/github-issues/` 아래에 기록되도록 해야 합니다.

   GitHub 이슈 작성 활성화:

   * GitHub CLI 인증
     * 실행: gh auth login --web
     * 또는 필요하다면: gh auth refresh -h github.com -s repo
   * 인증 확인
     * 실행: gh auth status
   * 대상 저장소 확인
     * 실행: gh repo set-default [your git clone url]/hve-partner-workshop
   * GitHub 쓰기 도구가 노출된 세션에서 백로그 생성을 통해 GitHub
     Issues 생성
     * Copilot이나 에이전트 워크플로우를 사용한다면 세션이 GitHub MCP
       쓰기 도구에 접근할 수 있는지 확인하세요.
     * [Copilot Chat에서 GitHub MCP 서버 사용하기](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/using-the-github-mcp-server-from-copilot-chat)를
       참고하세요.
     * [IDE에서 GitHub MCP 서버 사용하기](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server)를
       참고하세요.

   프롬프트:

   ```text
   `.copilot-tracking/prd-sessions/`에 있는 승인된 요구사항과 `.copilot-tracking/github-issues/`에 있는 백로그 개요를 검토하세요.
   초기 MVP를 위한 첫 번째 상위 이슈(parent issue)와 하위 이슈(child issue)들을 생성하세요. 또한 추적 가능성을 위해 해당 이슈들의 링크와 요약 정보를 `.copilot-tracking/github-issues/`에 기록하세요.
   워크플로우에 도움이 되는 경우에 한해 P0, P1, P2, epic, feature, story, task와 같은 라벨을 사용하세요.
   백로그 계획을 업데이트하고 GitHub Issues에 백로그를 생성하세요.
   ```

1. 비즈니스 결과에서 요구사항, 백로그 항목까지의 추적성을 위해 이슈
   목록을 검토한 후, 최종 백로그 요약과 이슈 링크를
   `.copilot-tracking/github-issues/` 아래에 저장하세요.

### 결과물

1. **구현 계획**(`.copilot-tracking/plans/`): 각 단계의 목표,
   결과물, 수락 기준을 갖춘 단계별 구현 계획.
2. **GitHub 백로그**(`.copilot-tracking/github-issues/`): 비즈니스
   결과를 추적 가능한 작업 항목으로 전환하기 위한 기능, 스토리, 작업의
   백로그로, 구현 계획에 연결되어 있습니다.

## 기술 트랙

### 목표

구현 계획에 맞춰 솔루션 접근 방식, 아키텍처, 게시 고려 사항을
구성하세요.

### 단계

1. `.copilot-tracking/brd-sessions/`, `copilot-tracking/prd-sessions/`
   아래의 요구사항, `.copilot-tracking/dt/` 아래의 경험 초안,
   `.copilot-tracking/plans/`의 구현 계획을 검토하세요.
2. 단계별 계획을 뒷받침하는 핵심 서비스, 데이터 소스, 통합 지점을
   식별하세요.
3. 계획의 각 단계와 정렬되는 간단한 솔루션 접근 방식, 주요
   트레이드오프, 아키텍처 노트를 구성하기 위해
   **System Architecture Reviewer**를 선택하세요:

   * 배포, 보안, 운영 고려 사항을 기록하세요.
   * Well-Architected 설계와 Cloud Adoption Framework 가이드에
     비추어 초안을 검토하세요.
   * 패키징, 발견 가능성, 지원 가능성, 통합 기대치를 포함하여
     Microsoft Marketplace와 Microsoft 365 Copilot Agent Store 준비를
     위한 게시 요구사항을 포착하세요.

   ```text
   `.copilot-tracking/plans/`에 있는 구현 계획, `.copilot-tracking/prd-sessions/`에 있는 요구사항, 그리고 `.copilot-tracking/dt/`에 있는 경험 초안을 검토하십시오.
   `.copilot-tracking/details/`에 아키텍처 노트를 작성하십시오.
   이 노트에는 각 단계별 간단한 해결 방안, 주요 트레이드오프(상충 관계), 클라우드 아키텍처, 'Well-Architected(잘 설계된 아키텍처)' 관련 고려 사항, 게시 요구사항, Microsoft IQ, 그리고 Mermaid 형식의 아키텍처 다이어그램이 포함되어야 합니다.
   작성한 아키텍처 노트를 구현 계획의 각 단계와 연결하십시오.
   ```
   * **Arch Diagram Builder**를 선택하여 간단한 Mermaid 아키텍처
     다이어그램을 만드세요.
     
   ```text
   현재 솔루션의 Implementation Plan, PRD, Experience Draft 및 Architecture Notes를 검토하고, 핵심 서비스, 데이터 소스, 사용자 경험 계층 및 통합 지점을 포함하는 첫 번째 MVP의 간단한 Mermaid 아키텍처 다이어그램을 생성해 주세요.
   ```

   Mermaid 아키텍처 다이어그램을 이미지 파일로 생성하세요
     
   ```text
   작성한 mermaid 아키텍처 다이어그램을 이미지로 생성해서 details 폴더에 추가해 주세요.
   ```

4. 각 단계에 맞춰 준비 상태를 검토하고 후속 작업을 드러내기 위해
   **Security Planner**를 사용하세요.

   ```text
   이 솔루션 초안을 검토하여 보안 위험 요소, 배포 시 고려 사항, 그리고 구현 계획의 각 단계별로 필요한 후속 조치를 확인하십시오.
   보안 관련 작업은 모두 해당 단계와 연결해 주십시오.
   ```

5. Mermaid 다이어그램을 검토하고 자연어로 다듬으세요.
6. (선택 사항) GitHub Copilot 대신 **Microsoft 365 Copilot**을 사용하여
   이미지를 만드세요. M365 Copilot에서 구현 계획을 첨부하고, Azure와
   Copilot 스타일 아이콘을 사용해 첫 MVP의 핵심 서비스, 데이터 소스,
   사용자 경험 계층, 통합을 나타내는 아키텍처 이미지를 Mermaid
   다이어그램에서 만드세요.

   Copilot 프롬프트에 relationship-manager-fsi-mvp-plan.md 파일을 추가하고 아래 프롬프트를 추가하세요.

   ```text
   이 솔루션의 Mermaid 다이어그램을 바탕으로 아키텍처 이미지를 생성해 주세요. 첫 번째 MVP를 위한 핵심 서비스, 데이터 소스, 사용자 경험 계층, 그리고 통합 요소들을 Azure 및 Copilot 스타일의 아이콘으로 표현해 주세요.
   ```
   검토된 이미지를 `.copilot-tracking/details/` 아래에 저장하거나 참조하세요.

8. 솔루션 검토에 필요한 게시 가정만 아키텍처 노트에 포착하고 구현
   계획에 링크하세요.

   * SaaS 또는 Azure Managed Application을 선호하는 Marketplace
     모델로 선택하고 Microsoft 365 에이전트를 잠재적인 컴패니언
     경험으로 선택하세요.
   * Managed Application: 구성 요소가 무엇을 배포하는지, 에이전트가
     사용자에게 무엇을 보여주는지, 각 제품 경계가 어디서 시작되고
     끝나는지 명시하세요.
   * 두 제품 간 API, 아이덴티티, 권한, 데이터 계약을 요약하세요.
   * 데이터 상주, 테넌트 격리, 고객 통제 인프라, 최소 권한 접근을
     포함하여 솔루션에 영향을 미치는 아키텍처 제약을 기록하세요.
   * 담당자와 함께 미해결 게시 가정을 나열하세요. 역할 실습 중에
     상업적 또는 제출 세부 사항을 해결하지 마세요.

   **RPI Agent**를 선택하세요.

   ```text
   `.copilot-tracking/plans/`의 구현 계획, `.copilot-tracking/prd-sessions/`의 요구사항, `.copilot-tracking/dt/`의 경험 초안, 그리고 `.copilot-tracking/details/`의 아키텍처 노트를 검토하십시오.
   솔루션 검토에 필요한 게시 관련 가정 사항만을 아키텍처 노트에 업데이트하십시오.
   선호하는 마켓플레이스 모델과 잠재적인 보조 경험으로서의 Microsoft 365 에이전트를 기록하십시오.
   제품 범위를 정의하고, 제품 간의 API, ID, 권한 및 데이터 계약을 요약하십시오.
   솔루션 통합에 필요한 아키텍처 제약 사항, 가정, 미결정 사항 및 담당자만을 기록하십시오.
   이러한 입력 항목들을 구현 계획과 연결하십시오.
   마켓플레이스 구현 계획, 오퍼 검증, 가격 책정, 수익화, 파트너 센터(Partner Center) 구성, 패키지 준비, 인증 및 출시 계획은 '파트너 워크숍 게시 후속 단계(Partner Workshop Publishing Follow-Up)'에서 다루도록 미뤄두십시오.
   ```

   [파트너 워크샵 게시 후속 작업](partner-workshop-publishing)에서 상세한
   준비 상태 평가를 완료하세요.

9. 나머지 팀과 결과를 공유하세요.

### 결과물

1. **아키텍처 노트**(`.copilot-tracking/details/`): 위험, 트레이드오프,
   통합 요구사항, 솔루션 검토에 필요한 최소한의 게시 가정을 포함하여
   구현 계획의 각 단계에 맞춘 아키텍처 설계 노트.
2. 게시 계획 입력: 잠정적인 제품 분할, 통합 경계, 아키텍처 제약,
   게시 워크샵을 위해 아키텍처 노트 안에 기록된 미해결 결정 사항.

## 작업 세션 알림

결과물을 간결하고 실행 지향적으로 유지하세요. 완벽한 정보를 기다리지
마세요. 목표는 팀이 워크샵 이후 다듬을 수 있는 검토된 초안을 만드는
것입니다.

## 다음 단계
[**검증 및 솔루션**](partner-workshop-solution.md)을 진행하세요.

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
