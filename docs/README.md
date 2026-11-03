---
title: HVE Core 문서
description: HVE Core 문서 허브 — GitHub Copilot 워크플로에 AI 기반 에이전트, 지침, 스킬을 제공하는 프롬프트 엔지니어링 프레임워크
sidebar_position: 1
author: Microsoft
ms.date: 2026-10-31
ms.topic: overview
keywords:
  - hve core
  - documentation
  - copilot customizations
  - agents
  - prompt engineering
estimated_reading_time: 3
---

HVE Core는 팀에게 GitHub Copilot을 위한 프로덕션 수준의 에이전트, 코딩 지침, 실행 가능한
스킬을 제공합니다. 구조화된 워크플로(Research → Plan → Implement), 스키마로 강제되는
품질 게이트, 10개 엔지니어링 분야에 걸친 역할별 도구를 얻을 수 있습니다. VS Code 마켓플레이스에서
설치하고 몇 분 안에 AI 지원 엔지니어링을 시작하세요.

## 설치 방식 선택

| 옵션         | HVE Core 확장                                                                                       | 선택적 클론                                                                |
|--------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| 받는 것   | 배포 가능한 모든 에이전트, 지침, 스킬                                                               | 완전한 또는 맞춤형 에이전트, 지침, 배포 가능한 스킬                       |
| 적합한 대상     | 관리형 업데이트와 전체 콘텐츠 세트를 원하는 팀                                                   | 저장소가 소유하고 검토 가능한 컴포넌트 선택을 원하는 팀                  |
| 시작        | [HVE Core 설치](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core) | 고정되거나 복제된 소스와 함께 포함된 `hve-core-installer` 스킬 사용 |

> 어떤 것을 선택해야 할지 확실하지 않으신가요? 자세한 분석은
> [설치 방식 비교](getting-started/methods/comparison.md)를 참조하세요.

HVE Core는 더 이상 프롬프트 파일을 제공하지 않습니다. `/rpi`나 `/security-review`와 같은
이전 프롬프트 명령을 사용했다면, [폐기된 프롬프트 명령](getting-started/package-migration.md#retired-prompt-commands)에서
각 명령을 대체 항목에 매핑합니다.

## 여러분의 경로를 찾으세요

### HVE Core가 처음이신가요?

설치, 구성, 첫 AI 지원 워크플로로 시작하여 실행해 보세요.

* [HVE Core 설치](getting-started/install.md)는 마켓플레이스 확장부터 개발자 클론까지
  세 가지 설정 경로를 다룹니다
* [첫 워크플로 실행하기](getting-started/first-workflow.md)는 엔드투엔드 RPI 예제를
  안내합니다
* [HVE Core 정체성 이해하기](getting-started/packages.md)에서 채널과 릴리스 보증을
  비교하세요

### 팀을 이끌고 계신가요?

거버넌스, 선택적 도입, 커스터마이징 옵션으로 팀을 위해 HVE Core를 설정하세요.

* [팀 도입 가이드](customization/team-adoption.md)는 거버넌스, 네이밍 규칙, 온보딩을
  다룹니다
* [HVE Core 정체성과 채널](getting-started/packages.md)은 산출물이 번들링되고
  배포되는 방식을 설명합니다
* [커스터마이징 가이드](customization/README.md)는 가벼운 지침부터 포크 및 확장까지
  전체 스펙트럼을 다룹니다

### HVE Core에 기여하고 계신가요?

프레임워크를 위한 에이전트, 프롬프트, 지침, 스킬을 만들고 유지관리하세요.

* [기여 가이드](contributing/)는 산출물 작성 표준을 설명합니다
* [템플릿](templates/)은 ADR, BRD, 보안 계획을 위한 시작점을 제공합니다
* [아키텍처 개요](architecture/)는 시스템 설계, 컴포넌트, 빌드 파이프라인을
  문서화합니다

### 더 깊이 탐구하고 계신가요?

Design Thinking 코칭, 보안 계획, 방법론 참조를 포함한 고급 기능을 탐색하세요.

* [Design Thinking](design-thinking/README.md)은 세 가지 공간에 걸친 9가지 방법으로
  팀을 안내합니다
* [프로젝트 계획](agents/project-planning/)은 ADR 생성, BRD/PRD 구축, 아키텍처
  다이어그램, 보안 계획 생성을 다룹니다
* [보안 문서](security/README.md)는 위협 모델링과 보안 계획을 다룹니다
* [RPI 방법론](rpi/)은 Research, Plan, Implement, Review, Follow-up 워크플로를
  설명합니다

## 역할

HVE Core는 10개의 엔지니어링 역할 각각에 맞춤화된 에이전트, 스킬, 시작 워크플로를
제공합니다. [역할 가이드](hve-guide/roles/) 페이지에서 여러분의 역할 가이드를
찾아보세요.

## AI 지원 프로젝트 라이프사이클

HVE Core는 초기 설정부터 지속적인 운영까지 9단계 라이프사이클을 지원합니다. 각
단계는 특정 에이전트, 스킬, 역할별 안내에 매핑됩니다.

* [단계 개요](hve-guide/lifecycle/)는 전체 라이프사이클 맵을 제공합니다
* [구현(6단계)](hve-guide/lifecycle/implementation.md)은 30개 이상의 자산을 가진
  가장 밀도 높은 단계입니다
* [발견(2단계)](hve-guide/lifecycle/discovery.md)는 조사, 요구사항, BRD 생성을
  다룹니다

**[전체 라이프사이클 탐색하기 →](hve-guide/lifecycle/)**

## 에이전트 시스템

전문화된 에이전트는 에이전트, 스킬, 지침 파일을 일관된 워크플로로 결합하는 기능별
그룹으로 구성됩니다.

* [RPI 오케스트레이션](rpi/)은 복잡한 작업을 조사, 계획, 구현, 검토 단계로 분리합니다
* [프로젝트 계획](agents/project-planning/)은 안내된 AI 워크플로를 통해 ADR, BRD,
  PRD, 아키텍처 다이어그램, 보안 계획을 생성합니다
* [백로그 관리](agents/backlog/)는 Azure DevOps, GitHub, Jira 전반에 걸쳐 작업 발견,
  분류, 스프린트 계획, 실행을 자동화합니다
* 추가 시스템은 [에이전트 카탈로그](agents/)에 문서화되어 있습니다

**[에이전트 카탈로그 둘러보기 →](agents/)**

## RPI 방법론

Research, Plan, Implement, Review(RPI)는 복잡한 엔지니어링 작업을 RPI Agent가
조율하거나 직접 호출되는 단계별 스킬로 분해합니다.

* [왜 RPI인가?](rpi/why-rpi.md)는 문제 정의와 설계 근거를 설명합니다
* [RPI 개요](rpi/)는 RPI Agent와 직접 호출 가능한 `rpi-*` 단계 스킬을 소개합니다
* [함께 사용하기](rpi/using-together.md)는 단계 조율과 지속적인 핸드오프를
  설명합니다

**[RPI 문서 →](rpi/)**

## Design Thinking

dt-coach 에이전트는 문제 공간, 솔루션 공간, 검증에 걸친 9가지 Design Thinking
방법으로 팀을 안내합니다.

* [Design Thinking 가이드](design-thinking/README.md)는 개요와 방법 카탈로그를
  제공합니다
* [왜 Design Thinking인가?](design-thinking/why-design-thinking.md)는 DT를 사용해야
  할 때를 설명합니다
* [DT Coach 사용하기](design-thinking/dt-coach.md)는 에이전트 사용법을 다룹니다

**[모든 Design Thinking 문서 둘러보기 →](design-thinking/)**

## 프롬프트 엔지니어링

HVE Core는 프로토콜 패턴, 입력 변수, 증거 기반 품질 게이트로 AI 산출물을 구조화합니다.

* `hve-builder` 스킬은 하나의 라이프사이클을 통해 AI 산출물을 생성, 개선, 리팩터링,
  교체, 리뷰, 검증합니다
* [AI 산출물 개요](contributing/ai-artifacts-common.md)는 산출물 유형 전반의 공통
  패턴을 다룹니다
* [활성화 맥락](architecture/ai-artifacts.md#activation-context)은 워크플로 내에서
  산출물이 활성화되는 시점을 설명합니다

## 빠른 링크

| 리소스                                                                                | 설명                        |
|-----------------------------------------------------------------------------------------|------------------------------------|
| [커스터마이징 가이드](customization/)                                                   | 워크플로에 맞게 HVE Core 조정    |
| [CHANGELOG](https://github.com/microsoft/hve-core/blob/main/CHANGELOG.md)               | 릴리스 이력과 버전 노트  |
| [CONTRIBUTING](https://github.com/microsoft/hve-core/blob/main/CONTRIBUTING.md)         | 저장소 기여 가이드라인 |
| [Scripts README](https://github.com/microsoft/hve-core/blob/main/scripts/README.md)     | 자동화 스크립트 참조    |
| [Extension README](https://github.com/microsoft/hve-core/blob/main/extension/README.md) | VS Code 확장 문서    |

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
