---
title: HVE 파트너 워크샵
description: HVE Core로 요구사항, 컨텍스트, 백로그, Azure 아키텍처, 게시 계획을 만드는 파트너용 워크샵
sidebar_position: 7
author: Microsoft
ms.date: 2026-11-01
ms.topic: tutorial
keywords:
  - partner workshop
  - HVE Core
  - role-based learning
  - Azure architecture
  - Microsoft Marketplace
  - Copilot Agent Store
estimated_reading_time: 8
---

이 워크샵에서는 제품 아이디어를 실제 실행에 필요한 일련의 산출물로 구체화합니다. 참가자들은 하나의 공통 프로젝트에서 역할별 트랙으로 나누어 작업한 후, 각 결과물을 통합하여 요구사항 패키지, 우선순위가 지정된 백로그, Azure 아키텍처, 그리고 마켓플레이스 게시 준비 계획을 완성합니다.

이 워크샵의 목적은 반복해서 활용할 수 있는 체계적인 워크플로우를 익히는 것입니다. 운영 환경을 위한 보안 검토, Azure 배포 또는 Microsoft Marketplace 인증 과정을 하루 만에 완료하는 과정은 아닙니다.

## 워크샵 일정

| 단계 | 활동                                                                                       | 시간   |
|------|-------------------------------------------------------------------------------------------|-------|
| 1    | [**워크샵 개요**](partner-workshop.md)                                                     | 30분 |
| 2    | [워크샵 환경 설정(로컬 VS Code)](partner-workshop-setup.md)                                            | 30분 |
| 3-1    | [역할별 트랙 Part1: 계획/비전/경험](partner-workshop-role-tracks.md)                      | 45분 |
| 3-2    | [역할별 트랙 Part2: 아키텍처 설계, 백로그](partner-workshop-role-tracks-2.md)                 | 45분 |
| 4    | [검증 및 솔루션](partner-workshop-solution.md)                                             | 30분 |
| 5    | [Microsoft Marketplace 및 Copilot Agent Store 준비](partner-workshop-publishing.md)       | 60분 |
| 6    | [구현 및 상용화로의 핸드오프](partner-workshop-implementation.md)                            | 30분 |

## 결과물

본 워크샵이 끝나면 팀은 다음을 기대 할 수 있습니다:

* HVE Core가 기반이 되는 비즈니스, 사용자, 도메인, 디자인, 기술적 컨텍스트 제공
* 테스트 가능한 인수 기준 (Acceptance Criteria)을 포함한 비즈니스 및 사용자 요구사항 작성
* 요구사항을 우선 순위가 지정된 GitHub 백로그로 전환
* Azure 솔루션을 위한 Mermaid 아키텍처 다이어그램 생성 및 검토
* Microsoft Marketplace에서 Azure Managed Application 오퍼에 대한 단계와 승인 게이트 설명
* Microsoft 365 Copilot Agent Store로 지원되는 경로 설명

팀은 다음 결과물을 프로덕션 위치에 남겨야 합니다:

```text
.copilot-tracking/
|-- research/                 [rpi-research 결과물]
|-- brd-sessions/             [BRD 초안 및 세션 상태]
|-- prd-sessions/             requirements.md
|-- plans/                    [구현 계획 및 단계 세부 사항]
|-- details/                  [단계별 아키텍처 및 게시 (publication) 노트]
|-- dt/                       [design thinking 결과물]
`-- github-issues/            [백로그 계획]
docs/
`-- planning/
    `-- adrs/                 [아키텍처 결정 레코드]
```

| 성과                 | 워크샵 아티팩트 위치                      | 워크샵 이후 경로        |
|---------------------|-----------------------------------|-------------------------------------------|
| 컨텍스트 및 리서치     | `.copilot-tracking/research/`     | 고객 검증 및 승인                         |
| 비즈니스 요구사항 (BRD)| `.copilot-tracking/brd-sessions/`    | 제품 계획 전에 비즈니스 범위 검증         |
| 요구사항 및 PRD       | `.copilot-tracking/prd-sessions/`    | 개발을 위해 PRD를 정제하고 확정          |
| 구현 계획             | `.copilot-tracking/plans/`           | 단계별로 팀 전달을 조율                 |
| 아키텍처 및 게시       | `.copilot-tracking/details/`         | 단계별 산출물 구현 및 검증              |
| 디자인 및 UX          | `.copilot-tracking/dt/`              | UI 구현 및 사용자 검증                 |
| 아키텍처 결정         | `docs/planning/adrs/`                | 인프라 구현 및 검증                      |
| GitHub 백로그         | `.copilot-tracking/github-issues/`   | 승인된 외부 작업 항목 생성               |
| 게시 계획             | `.copilot-tracking/[session-type]/`  | 마켓플레이스 및 에이전트 스토어 게시 실행   |

> [!IMPORTANT]
> HVE Core 커스텀 에이전트는 GitHub Copilot과 VS Code에서 실행됩니다. 이들은 Microsoft 365 Copilot 에이전트가 아니며 Agent Store에 직접 업로드할 수 없습니다. 팀은 지원되는 Microsoft 365 에이전트 도구로 고객 대면 에이전트를 구축하고, 패키징하고, 검증한 후 해당 조직의 카탈로그 또는 Partner Center 게시 경로를 따라야 합니다.

## 대상 및 역할

4~6명으로 다양한 분야의 구성원이 참여하는 팀을 구성합니다.

| 트랙                   | 제안되는 참가자                       | 주요 워크샵 결과물      |
|-----------------------|-------------------------------------|-------------------------------------|
| 프로젝트 관리           | PM, 프로그램 매니저, 제품 책임자        | 성과, 요구사항, 우선순위, 백로그 구조  |
| 주제 전문가(SME)        | 업계 SME, 컴플라이언스 리드, 운영 리드  | 도메인 컨텍스트, 용어, 제약, 증거 |
| 디자인                  | UX 디자이너, 서비스 디자이너, Design Thinking 진행자, 리서처   | 페르소나, 사용자 여정, 접근성, 책임 있는 AI, 에이전트 경험 |
| 기술                    | 아키텍트, 현장 배치 엔지니어, 보안, 플랫폼 리드 | Azure 설계, 다이어그램, 배포 및 게시 계획     |

워크샵 이후 진행 중인 역할별 워크플로우는 더 폭 넓은 [HVE 역할 가이드](../hve-guide/roles/)를 참고하세요.

### 샘플 시나리오

참가자가 프로젝트를 가져오지 않은 경우 이 시나리오를 사용하세요:

> 한 금융 서비스 파트너는 기업 고객에게 Relationship Manager Intelligence Experience를 제공하고자 합니다. Relationship Manager는 Microsoft 365 Copilot에> 질문하고 CRM 시스템, 이메일, 거래 내역, 내부 지식 소스로부터 통합된 계정 인사이트, 위험 지표, 성장 기회, 권장 다음 조치를 받습니다. 각 고객은 Azure Managed Application을 통해 자체 구독에 Azure 데이터, 검색, 모델, API, 아이덴티티, 모니터링 리소스를 배포합니다. 솔루션은 출처 인용을 보존하고, 계정별 사용자 접근 통제를 존중하고, 모델 학습에 고객 데이터를 사용하지 않으며, 운영 감사 증거를 제공해야 합니다.

워크샵 중에는 실제 고객 데이터를 사용하지 마세요. 합성 데이터 또는 공개 샘플 콘텐츠를 사용하세요.

## 참가자 흐름

1. [워크샵 개요](partner-workshop.md)를 검토하고, 시나리오를 선택하고, 워크샵 성과를 확인하세요.
2. [공유 설정](partner-workshop-setup.md)을 완료하고 공유 세션 컨텍스트를 만드세요.
3. [PM 역할 가이드](partner-workshop-role-tracks.md)와 [기술 트랙](partner-workshop-role-tracks-2.md)을 완료하세요.
4. 역할 결과물을 통합하고 검증하기 위해[역할 간 솔루션 가이드](partner-workshop-solution.md)를 완료하세요.
5. [게시 가이드](partner-workshop-publishing.md)를 완료하고 Marketplace와 Agent Store 준비에 필요한 후속 작업을 기록하세요.
6. 승인된 엔지니어링 및 상용화 후속 조치를 위해 [구현 핸드오프](partner-workshop-implementation.md)를 완료하세요.

## 완료 기준

워크샵은 팀이 여섯 가지 초안 아티팩트를 검토하고, 미해결 가정을 식별하고, 게시 후속 조치에 대한 담당자를 지정했을 때 완료됩니다. 진행자가 명시적으로 추가 시간을 제공하고 프로젝트 매니저가 환경을 승인하지 않는 한, 실제 Azure 배포, 상업적 Microsoft Marketplace 검증, Copilot Agent Store 가용성은 워크샵 이후의 마일스톤입니다.

## 관련 가이드

* [HVE Core 설치하기](install.md)
* [첫 전체 워크플로우](first-workflow.md)
* [Architecture Diagrams Skill](../agents/project-planning/arch-diagram-builder.md)
* [MCP 구성](mcp-configuration.md)

### 다음 단계
[**워크샵 환경 설정(로컬 VS Code)**](partner-workshop-setup.md)을 진행하세요.

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction, then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->