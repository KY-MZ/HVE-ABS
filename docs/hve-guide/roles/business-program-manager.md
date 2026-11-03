---
title: Business Program Manager 가이드
description: 이해관계자 정렬, 비즈니스 성과, 프로그램 조율을 이끄는 비즈니스 프로그램 매니저를 위한 HVE Core 지원
sidebar_position: 6
author: Microsoft
ms.date: 2026-10-31
ms.topic: how-to
keywords:
  - BPM
  - program management
  - business requirements
  - stakeholder alignment
estimated_reading_time: 10
---

> [!IMPORTANT]
> BPM 역할 가이드는 베타 상태입니다. BPM 전용 도구는 TPM 및 project-planning 자산에서 파생되었습니다. 전용 BPM 워크플로가 성숙해짐에 따라 이 가이드는 더 정교한 에이전트 상호작용과 맞춤형 프롬프트로 업데이트될 예정입니다.

비즈니스 성과를 정의하고, 이해관계자 정렬을 관리하고, 팀 간 프로그램을 조율하거나, 비즈니스 전략을 기술적 전달과 연결하는 분이라면 이 가이드가 적합합니다. 비즈니스 프로그램 매니저는 TPM과 많은 도구를 공유하지만, 기술 구현 세부 사항보다 비즈니스 수준의 요구사항, 이해관계자 커뮤니케이션, 성과 추적에 초점을 맞춥니다.

## 기능 그룹

> [!TIP]
> VS Code 마켓플레이스에서 [HVE Core 확장](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core)을 설치하면 구성 없이 완전한 활성 컴포넌트 세트를 사용할 수 있습니다.
>
> 선택적 클론 방식을 사용하려면, 프로그램에 맞는 비즈니스 요구사항, 제품 자문, 애자일 코칭, 리서치 컴포넌트를 선택하세요. 기능 그룹은 관련 컴포넌트를 찾는 데 도움을 주는 것이며, 독립적으로 설치 가능한 제품이 아닙니다. [설치 가이드](../../getting-started/install.md)를 참고하세요.

## HVE Core가 제공하는 것

1. 이해관계자 대화와 전략 입력으로부터 비즈니스 요구사항 문서(BRD)를 생성합니다
2. 우선순위 결정과 go-to-market 의사결정을 위한 제품 관리 자문 안내를 제공합니다
3. 테스트 가능한 수용 기준을 갖춘 사용자 스토리 작성 및 정제를 코칭합니다
4. 경쟁 분석, 시장 조사, 비즈니스 케이스 개발을 위한 리서치 워크플로를 지원합니다

## BPM vs TPM

BPM과 TPM 역할은 도구를 공유하지만 다르게 적용합니다:

| 측면            | BPM 초점                                                               | TPM 초점                                                 |
|-------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 주요 산출물 | 비즈니스 요구사항, 성과 정의                                              | 기술 요구사항, 작업 항목 계층 구조                             |
| 이해관계자 범위 | 비즈니스 리더, 고객, 조직 간 파트너                                         | 엔지니어링 팀, 기술 이해관계자                                 |
| 측정       | 비즈니스 성과, ROI, 고객 영향                                                 | 스프린트 속도, 전달 마일스톤, 기술 품질   |
| 라이프사이클 단계  | Stage 2: Discovery, Stage 3: Product Definition, Stage 4: Decomposition | Stage 2부터 Stage 8까지 더 깊은 기술적 관여 |

기술 백로그 관리, Azure DevOps 통합, GitHub 이슈 워크플로에 대해서는 [TPM 가이드](tpm.md)를 참고하세요.

## 당신의 라이프사이클 단계

> [!NOTE]
> BPM은 주로 다음 라이프사이클 단계에서 활동합니다:
>
> [Stage 2: Discovery](../lifecycle/discovery.md): 비즈니스 요구사항, 경쟁 환경, 시장 맥락 조사
> [Stage 3: Product Definition](../lifecycle/product-definition.md): 비즈니스 요구사항과 성과 스펙 정의
> [Stage 4: Decomposition](../lifecycle/decomposition.md): 비즈니스 목표를 프로그램 마일스톤으로 분해
> [Stage 5: Sprint Planning](../lifecycle/sprint-planning.md): 팀 간 계획과 마일스톤 정렬 조율

## 단계별 안내

1. Stage 2: Discovery. `/rpi-research`를 사용하여 비즈니스 맥락, 경쟁 환경, 이해관계자 니즈를 조사하세요.
2. Stage 3: Product Definition. **brd-builder** 에이전트를 실행하여 이해관계자 대화와 전략 입력으로부터 비즈니스 요구사항 문서를 작성하세요.
3. Stage 3: Advisory. `requirements-author` 스킬을 적용하는 **brd-builder** 및 **prd-builder** 에이전트에서 우선순위 프레이밍, go-to-market 고려사항, 제품 포지셔닝을 이어서 진행하세요.
4. Stage 4: Decomposition. 비즈니스 목표를 프로그램 마일스톤으로 나누고 팀 간 종속성을 조율하세요.
5. Stage 5: Planning. **backlog-manager** 에이전트를 사용하여 프로그램 작업 항목에 대해 명확한 수용 기준을 가진 사용자 스토리를 생성하거나 정제하세요. 이 에이전트는 `backlog-management` 스킬의 스토리 품질 참조에 있는 작업 항목 품질 지침을 적용합니다.

## 시작 프롬프트

### 비즈니스 요구사항

**brd-builder** 에이전트 선택:

```text
Create a business requirements document for the customer onboarding portal.
Target enterprise customers with 500+ seats, with the objective of reducing
onboarding time from 2 weeks to 3 days. Include integration requirements
for existing SSO and billing systems and SOC 2 Type II compliance constraints.
```

이전 세션을 재개하려면, **brd-builder** 에이전트 선택:

```text
Continue my claims automation BRD. Pick up where we left off
and focus on completing the data and reporting requirements section.
```

명시적인 RFI, RFP, 입찰, 설문지의 경우, BRD Builder는 전체 시퀀스를 처리할 수 있습니다: 질문 세트를 분석하고, 승인된 비즈니스 성과, 이해관계자 역할, 제약사항, 위험을 기여한 다음 초안을 작성합니다. 각 주장이 기억된 텍스트가 아니라 승인된 BRD를 인용하도록 BRD 이름을 지정하세요. 결과 응답 증거는 내부 검토용이며 외부 사용 권한을 부여하지 않습니다. [제안서 응답 워크플로](../../agents/project-planning/brd-prd-builders#proposal-response-workflow)를 참고하세요.

### 제품 요구사항 발견

**prd-builder** 에이전트 선택:

```text
We're building a webhook notification system for our API platform. Walk me
through requirements discovery: identify who the target users are, what
pain points exist with the current polling approach, and what measurable
outcomes would indicate success. Three enterprise customers provided
interview feedback we can reference.
```

기능 우선순위를 위해서는 `requirements-author` 스킬을 사용하세요:

```text
Advise on prioritization for the identity and access management product
area. We have 12 open feature requests and 5 bugs. Revenue impact and
customer escalation status should weigh highest. Budget constraints limit
us to 2 engineers for the next quarter.
```

트래커에 연결된 작업(발견, 분류, 스프린트 계획, 실행)에는 **backlog-manager** 에이전트를 사용하세요.

### 사용자 스토리 코칭

대략적인 아이디어로부터 스토리를 만들려면 **backlog-manager** 에이전트 선택:

```text
I need a user story for adding webhook retry logic to our event
notification service. Deliveries currently fail silently when endpoints
return 5xx errors, and customers are missing critical billing events.
```

모호한 스토리를 정제하려면 **backlog-manager** 에이전트 선택:

```text
Help me refine this story. Title: Improve error handling. Description:
Make error handling better across the API. AC: Errors should be handled
properly. This is too vague and I need testable acceptance criteria
tied to specific API endpoints.
```

### 비즈니스 맥락 리서치

`/rpi-research` 사용:

```text
Research best practices for migrating from manual invoice approval workflows
to automated AP processing. Compare ERP-integrated solutions versus
standalone AP automation platforms across processing volume limits,
three-way matching accuracy, audit trail completeness, and average
reduction in days payable outstanding. Our finance team processes 8,000
invoices per month with a 12% exception rate we need to cut in half.
```

### UX 리서치

**ux-ui-designer** 에이전트 선택:

```text
Create a Jobs-to-be-Done analysis and user journey map for the first-time
developer onboarding flow. Target audience is enterprise developers with
3-5 years experience migrating from a competitor platform. Include
accessibility requirements for WCAG AA compliance and keyboard-only
navigation support.
```

## 주요 에이전트 및 워크플로

| 에이전트 또는 스킬          | 목적                                                   | 문서                                               |
|-------------------------|-----------------------------------------------------------|------------------------------------------------------|
| **brd-builder**         | 비즈니스 요구사항 문서 작성                                   | 에이전트 파일                                         |
| **requirements-author** | BRD 및 PRD 작성 지침                            | 스킬 파일                                         |
| **backlog-manager**     | 작업 항목 생성, 정제, 백로그 코칭      | [Backlog Management](../../agents/backlog/)        |
| **rpi-research**        | 비즈니스 맥락 및 시장 조사                      | [RPI workflow](../../rpi/)                         |
| **ux-ui-designer**      | 비즈니스 지향 산출물을 위한 UX/UI 안내           | 에이전트 파일                                         |
| **dt-coach**            | 사용자 중심 프로그램 설계를 위한 Design Thinking 코칭 | [Design Thinking](../../design-thinking/README.md) |

프로그램 설계에 사용자 중심 검증이 필요할 때 BPM은 **dt-coach**의 도움을 받습니다. Design Thinking의 Scope Conversations(Method 1)와 User Concepts(Method 5)는 공식 BRD 작성 전에 비즈니스 요구사항을 검증된 사용자 니즈에 근거하도록 돕습니다.

횡단적 워크플로를 위해 스킬이 에이전트를 보완합니다:

| 스킬        | 목적                                                       | 호출          |
|--------------|-----------------------------------------------------------------|-----------------|
| git-commit   | 전통적인 메시지 형식으로 변경 사항을 스테이징하고 커밋 | `/git-commit`   |
| pull-request | 구조화된 설명과 함께 풀 리퀘스트 생성             | `/pull-request` |

## 팁

| 할 것                                                               | 하지 말 것                                                    |
|------------------------------------------------------------------|------------------------------------------------------------------|
| 구조화된 요구사항을 위해 **brd-builder** 에이전트로 시작 | BRD 구조 없이 비공식 요구사항 작성       |
| 데이터 기반 의사결정을 위해 `requirements-author` 스킬 사용  | 자문 없이 우선순위 결정     |
| 비즈니스 성과와 이해관계자 정렬에 집중             | 기술 구현 세부 사항에 깊이 들어가기                       |
| 기술적 분해를 위해 TPM과 조율                 | Azure DevOps 또는 GitHub 이슈 관리를 직접 시도 |
| 요구사항 정의 전에 시장 맥락 조사             | 조사 없이 비즈니스 맥락 가정            |

## 관련 역할

* BPM + TPM: BPM은 비즈니스 요구사항과 성과를 정의하고, TPM은 이를 기술 스펙과 작업 항목으로 분해합니다. 이 역할 간의 강력한 협업은 비즈니스 의도가 구현까지 이어지도록 보장합니다. [TPM 가이드](tpm.md)를 참고하세요.
* BPM + Security Architect: 비즈니스 요구사항에는 컴플라이언스와 보안 제약사항이 포함됩니다. 보안 계획은 비즈니스 약속이 기술적으로 실현 가능한지 검증합니다. [Security Architect 가이드](security-architect.md)를 참고하세요.

## 다음 단계

> [!TIP]
> 전체 HVE Core 인벤토리 둘러보기: [HVE Core package](../../plugins/hve-core.md)
> 기술 핸드오프를 위한 TPM 워크플로 이해하기: [TPM 가이드](tpm.md)
> 프로그램 관리가 프로젝트 라이프사이클에 맞는 방식 확인하기: [AI-Assisted Project Lifecycle](../lifecycle/)

---

> [!NOTE]
> 전용 BPM 워크플로 자동화와 비즈니스 성과 추적은 향후 개선 계획입니다.

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
