---
title: Engineer 가이드
description: 기능을 구축하고, 버그를 수정하고, AI 지원 워크플로로 코드를 출시하는 엔지니어를 위한 HVE Core 지원
sidebar_position: 3
author: Microsoft
ms.date: 2026-10-31
ms.topic: how-to
keywords:
  - engineer
  - development
  - RPI
  - coding standards
estimated_reading_time: 10
---

코드를 작성하고, 기능을 구현하고, 버그를 수정하고, 풀 리퀘스트를 리뷰하거나, 프로덕션 시스템을 유지보수하는 분이라면 이 가이드가 적합합니다. 엔지니어는 HVE Core에서 가장 깊은 도구 지원을 받으며, 조사, 계획, 구현, 리뷰, 전달에 걸친 28개 이상의 대상 자산을 사용할 수 있습니다.

## 권장 설치

> [!TIP]
> VS Code 마켓플레이스에서 [HVE Core 확장](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core)을 설치하면 구성 없이 완전한 활성 컴포넌트 세트를 사용할 수 있습니다.
>
> 클론 기반 설정을 하려면, 포함된 `hve-core-installer` 스킬을 사용해 RPI와 언어별 코딩 컴포넌트를 포함하는 전체 매니페스트 또는 맞춤형 선택을 하세요. [설치 가이드](../../getting-started/install.md)를 참고하세요.

1. 코드를 작성하기 전에 코드베이스 패턴, 외부 API, 아키텍처를 조사합니다
2. 단계별 작업 분해를 포함한 구조화된 구현 계획을 작성합니다
3. 단계 기반 실행과 진행 상황 추적으로 계획에 따라 기능을 구현합니다
4. 표준, 패턴, 아키텍처 지침에 따라 코드 변경을 리뷰합니다
5. 전통적인 커밋 메시지와 풀 리퀘스트 설명을 생성합니다
6. 파일 유형에 따라 언어별 코딩 표준을 자동으로 활성화합니다(C#, Python, Bash, Bicep, Terraform, GitHub Actions)
7. 병합, 리베이스, 충돌 해결을 포함한 Git 워크플로를 관리합니다

## 당신의 라이프사이클 단계

> [!NOTE]
> 엔지니어는 주로 다음 라이프사이클 단계에서 활동합니다:
>
> [Stage 2: Discovery](../lifecycle/discovery.md): 요구사항 조사, 코드베이스 탐구, 맥락 수집
> [Stage 3: Product Definition](../lifecycle/product-definition.md): 조사를 구조화된 구현 계획으로 전환
> [Stage 6: Implementation](../lifecycle/implementation.md): 기능 구축, 코드 작성, 계획 실행
> [Stage 7: Review](../lifecycle/review.md): 코드 리뷰, 변경 검증, 품질 보장
> [Stage 8: Delivery](../lifecycle/delivery.md): 커밋, PR 생성, 변경 병합

## 단계별 안내

1. Stage 2: Discovery. `/rpi-research`를 사용하여 요구사항을 조사하고, 코드베이스 패턴을 탐구하고, 접근 방식에 대한 증거를 수집하세요.
2. Stage 3: Product Definition. `/rpi-plan`을 사용하여 충분한 증거를 단계, 작업, 성공 기준을 갖춘 구조화된 구현 계획으로 전환하세요.
3. Stage 6: Implementation. `/rpi-implement`로 승인된 계획을 실행하거나, 전체 라이프사이클 조율을 원한다면 `RPI Agent`를 선택하세요.
4. Stage 7: Review. `/rpi-review`를 실행하여 계획 대비 구현을 검증하고, 코딩 표준을 확인하고, 아키텍처 준수를 보장하세요.
5. Stage 8: Delivery. 전통적인 커밋 메시지는 `/git-commit`, PR 생성은 `/pull-request`, 병합 워크플로는 `/git-merge`를 사용하세요.

## 시작 프롬프트

전체 라이프사이클 조율을 위해 **RPI Agent** 선택:

```text
Implement the user notification preferences API endpoint from work
item #4523. Follow the REST conventions in src/api/handlers/ and add
integration tests covering email, SMS, and push notification channels.
```

`/rpi-research` 사용:

```text
Research the best approach for implementing a rate limiter in the API
gateway. Compare token bucket vs sliding window algorithms, evaluate
Redis vs in-memory storage for distributed deployments, and review
existing patterns in src/middleware/.
```

`/rpi-plan`을 사용하고 조사 산출물을 참조:

```text
Create an implementation plan for the webhook delivery system. Include
phases for the event dispatcher, retry queue, and dead-letter handling.
Reference patterns in src/services/.
```

`/rpi-implement`를 사용하고 승인된 계획 산출물을 참조:

```text
Implement the webhook delivery system following the attached plan. Start
with the event dispatcher phase and execute the retry queue phase
second.
```

`/rpi-review`를 사용하고 변경 기록을 참조:

```text
Review my webhook delivery system implementation. Check for error
handling gaps, verify retry logic correctness, and validate compliance
with coding standards.
```

```text
/git-commit Commit changes with a conventional message
```

```text
/pull-request Create a PR for the current changes
```

## 주요 에이전트 및 워크플로

| 에이전트 또는 스킬    | 목적                                        | 문서                       |
|-------------------|------------------------------------------------|-----------------------------|
| **rpi-research**  | 심층 코드베이스 및 API 조사                 | [RPI Overview](../../rpi/) |
| **rpi-plan**      | 구조화된 구현 계획 수립                     | [RPI Overview](../../rpi/) |
| **rpi-implement** | 승인된 계획의 증거 기반 구현  | [RPI Overview](../../rpi/) |
| **rpi-review**    | 구현 리뷰 및 결과 라우팅      | [RPI Overview](../../rpi/) |
| **RPI Agent**     | 전체 RPI 라이프사이클 조율                | [RPI Overview](../../rpi/) |
| **code-review**   | 풀 리퀘스트 리뷰 자동화                 | 에이전트 파일                 |
| **hve-builder**   | 프롬프트 엔지니어링 산출물 생성 및 정제 | 스킬 파일                 |

자동 활성화 지침은 파일 유형에 따라 코딩 표준을 적용합니다: C#(`*.cs`), Python(`*.py`), Bash(`*.sh`), Bicep(`bicep/**`), Terraform(`*.tf`), GitHub Actions 워크플로(`*.yml`).

## 팁

| 할 것                                                         | 하지 말 것                                                            |
|------------------------------------------------------------|--------------------------------------------------------------------|
| 다중 파일 변경을 구현하기 전에 조사            | 복잡한 기능을 바로 코딩하기 시작하기                         |
| 계획된 다단계 작업에 `RPI Agent` 사용               | 조사, 계획, 구현을 수동으로 조율하기           |
| 파일 유형에 따라 코딩 표준이 자동 활성화되도록 두기            | 언어별 지침을 재정의하거나 건너뛰기                  |
| 계획 단계를 시작하기 전에 조사 문서 리뷰하기 | 낯선 코드베이스나 API에 대한 조사 건너뛰기                   |
| `/clear`로 RPI 단계 간 맥락 정리                | 조사, 계획, 구현, 리뷰 사이에 오래된 맥락 전달하기 |

## 관련 역할

* Engineer + Tech Lead: 기능 개발은 아키텍처 리뷰와 표준 강제에서 이점을 얻습니다. Tech Lead가 설계 결정을 검증하는 동안 Engineer가 구현합니다. [Tech Lead 가이드](tech-lead.md)를 참고하세요.
* Engineer + Data Scientist: 분석 파이프라인 개발은 데이터 스펙과 노트북 프로토타이핑을 프로덕션급 통합과 짝지웁니다. [Data Scientist 가이드](data-scientist.md)를 참고하세요.
* New Contributor to Engineer: 기여자는 가이드 모드에서 자율적 엔지니어링으로 성장합니다. [New Contributor 가이드](new-contributor.md)를 참고하세요.

## 다음 단계

> [!TIP]
> 첫 RPI 워크플로 실행하기: [첫 워크플로 가이드](../../getting-started/first-workflow.md)
> 전체 RPI 방법론 둘러보기: [RPI 문서](../../rpi/)
> 단계가 어떻게 연결되는지 확인하기: [AI-Assisted Project Lifecycle](../lifecycle/)

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
