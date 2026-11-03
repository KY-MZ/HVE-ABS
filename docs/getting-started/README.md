---
title: HVE Core 시작하기
description: 프로젝트에서 HVE Core Copilot 커스터마이징을 사용하기 위한 빠른 설정 가이드
sidebar_position: 1
sidebar_label: 개요
sidebar_custom_props:
  accessibleName: "개요: HVE Core 시작하기"
pagination_label: HVE Core 시작하기
author: Microsoft
ms.date: 2026-10-31
ms.topic: tutorial
keywords:
  - github copilot
  - multi-root workspace
  - setup
  - getting started
estimated_reading_time: 5
---

HVE Core를 설치했습니다. 이제 무엇을 해야 할까요?

솔직한 답변: 에이전트를 바로 사용하기 시작할 수 있고, 일부는 즉시 좋은 결과를 내줄 것입니다. 하지만 HVE Core의 진짜 힘은 AI와 협업하는 방식을 바꾸는 RPI(Research, Plan, Implement, Review) 방법론에 있습니다. AI에게 "코드를 작성해줘"라고 요청하는 대신, 먼저 조사하고, 다음으로 계획을 세우고, 세 번째로 구현하고, 마지막으로 리뷰하도록 요청합니다. 이 제약이 모든 것을 바꿉니다.

이 가이드는 네 단계를 차례로 안내하며, 각 단계는 이전 단계 위에 쌓입니다:

| 단계                                                      | 할 일                                             | 시간    |
|-----------------------------------------------------------|---------------------------------------------------------|---------|
| [첫 상호작용](first-interaction.md)                 | 에이전트와 대화하고 응답을 확인하기                        | 1분   |
| [첫 조사](first-research.md)                       | 자신의 코드베이스에서 /rpi-research 사용하기                  | 5분   |
| [첫 전체 워크플로](first-workflow.md)                  | Research, Plan, Implement 전체 사이클 실행하기          | 15분  |
| [HVE와 함께 성장하기](../hve-guide/roles/new-contributor.md) | 독립적으로 사용할 수 있을 때까지 네 가지 마일스톤 진행하기 | 지속적 |

> [!TIP]
> AI 지원 개발에 이미 익숙하신가요? [첫 전체 워크플로](first-workflow.md)로 바로 건너뛰거나, 조율된 라이프사이클을 위해
> [RPI Agent](https://github.com/microsoft/hve-core/blob/main/.github/CUSTOM-AGENTS.md#rpi-agent)를 선택하거나,
> 단계별 직접 작업을 위해 `/rpi-research`, `/rpi-plan`, `/rpi-implement`, `/rpi-review`를 사용하세요.

설치 도움이 필요하신가요? 모든 방법을 보려면 [설치 가이드](install.md)를 확인하거나,
가장 빠른 경로를 원한다면 [VS Code 확장](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core)을 설치하세요.

소스 채널이나 선택적 클론 방식을 고르려면 [HVE Core 아이덴티티와 채널](packages.md)을 확인하세요.

## 문제 해결

### 설치 관련 문제

#### 에이전트를 사용할 수 없음

* GitHub Copilot 확장이 설치되어 활성화되어 있는지 확인하세요
* VS Code 창을 다시 로드하세요: `Ctrl+Shift+P` → "Developer: Reload Window"
* hve-core에 접근 가능한지 확인하세요(올바르게 클론되었거나 구성되었는지)

#### Copilot이 커스터마이징을 찾지 못함

* Multi-Root의 경우: 폴더가 아니라 `.code-workspace` 파일을 열었는지 확인하세요
* `chat.agentFilesLocations`이 올바른 경로를 가리키는지 확인하세요
* 창 제목에 워크스페이스 이름이 표시되는지 확인하세요

#### Git 또는 클론 오류

* Git이 설치되어 있는지 확인하세요: 터미널에서 `git --version` 실행
* github.com에 대한 네트워크 연결을 확인하세요
* 방법별 문제 해결은 [설치 가이드](install.md)를 참고하세요

## 선택적 스크립트

HVE Core에는 프로젝트에 복사해 사용할 수 있는 유틸리티 스크립트가 포함되어 있습니다:

| 스크립트                                             | 목적                                            |
|----------------------------------------------------|------------------------------------------------------|
| `scripts/linting/Validate-MarkdownFrontmatter.ps1` | JSON 스키마에 대해 마크다운 프런트매터를 검증 |
| `scripts/linting/Invoke-PSScriptAnalyzer.ps1`      | 프로젝트 설정으로 PSScriptAnalyzer 실행         |
| `scripts/security/Test-DependencyPinning.ps1`      | GitHub Actions의 고정된 종속성 확인       |

필요한 스크립트를 프로젝트의 `scripts/` 디렉터리로 복사하고 경로를 적절히 조정하세요.

## 다음 단계

* 여정 시작하기: [첫 상호작용](first-interaction.md)
* 복잡한 작업을 위한 [RPI Workflow](../rpi/) 학습
* 전체 카탈로그는 [사용 가능한 에이전트](https://github.com/microsoft/hve-core/blob/main/.github/CUSTOM-AGENTS.md) 둘러보기

## Design Thinking 경로

구현 전에 사용자 중심 요구사항 발견이 필요한 프로젝트의 경우:

* [Design Thinking 가이드](../design-thinking/README.md): DT 개요를 위해 여기서 시작
* [DT Coach 사용하기](../design-thinking/dt-coach.md): dt-coach 에이전트 사용법 학습
* [DT to RPI Integration](../design-thinking/dt-rpi-integration.md): DT에서 구현으로 전환

## 참고 자료

* [설치 가이드](install.md) - 모든 설치 방법에 대한 전체 의사결정 매트릭스
* [MCP 구성](mcp-configuration.md) - Model Context Protocol 서버 구성
* [역할 가이드](../hve-guide/roles/) - 역할별 가이드 찾기

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->

## 다음 단계
워크샵 개요 페이지에서 워크샵을 시작하세요: [워크샵 개요](../workshop/README.md)