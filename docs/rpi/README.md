---
title: RPI 워크플로 이해하기
description: Research, Plan, Implement, Review, Follow-up이 증거 기반 전달을 어떻게 안내하는지 배우기
sidebar_position: 1
sidebar_label: 개요
sidebar_custom_props:
  accessibleName: "개요: RPI 워크플로 이해하기"
pagination_label: RPI 워크플로 이해하기
author: Microsoft
ms.date: 2026-10-31
ms.topic: concept
keywords:
  - rpi workflow
  - rpi agent
  - rpi research
  - rpi plan
  - rpi implement
  - rpi review
  - rpi walkthrough
  - follow-up
  - github copilot
estimated_reading_time: 7
---

RPI(Research, Plan, Implement, Review) 라이프사이클은 복잡한 코딩 작업을 검증된 결과와 명확한 후속 조치로 이끕니다. 모든 실행이 다섯 가지 개념을 전부 수행하도록 요구하지 않으면서도 각 개념을 명확히 구분합니다. 조사 준비 상태 평가부터 시작하세요: 제공되었거나 이미 완료된 증거가 충분하다면 재사용하고, 입증된 격차가 있을 때만 조사를 활성화하세요.

> 작업 맥락과 증거 → 필요시 조사 → 계획 → 구현 → 리뷰 → 후속 조치

## RPI를 사용하는 이유

AI 코딩 어시스턴트는 간단한 작업을 빠르게 완료할 수 있지만, 복잡한 변경에는 그럴듯해 보이는 코드 이상의 것이 필요합니다. 어시스턴트는 기존 패턴을 검증하고, 종속성을 이해하고, 결정을 보존하고, 결과를 명시적인 수용 기준과 비교해야 합니다.

RPI는 반직관적인 통찰로 이 문제를 해결합니다: AI가 구현할 수 없다는 것을 알 때, "그럴듯한 코드"에 대한 최적화를 멈추고 "검증된 진실"에 대한 최적화를 시작합니다. 제약이 목표를 바꾸는 것입니다.

### 핵심 이점

* 조사 단계를 시작하기 전에 증거를 평가하므로, 충분한 조사는 반복되지 않고 재사용됩니다.
* 그럴듯한 패턴을 새로 만드는 대신 검증된 기존 패턴을 사용합니다.
* 결정, 변경, 검증, 리뷰 라우팅을 지속적인 작업 산출물에 보존합니다.

> [!TIP]
> 라이프사이클 이면의 심리, 품질 비교, 진입 경로에 대해서는 [RPI 워크플로가 효과적인 이유](why-rpi)를 참고하세요.

RPI는 자율적인 전문 작업자 체인을 요구하지 않고 라이프사이클 개념을 분리합니다. 사용자가 선택하는 라이프사이클 래퍼로 `RPI Agent`를 사용하거나, 집중된 작업이 필요할 때 단계별 스킬을 직접 사용하세요.

## 라이프사이클 개념

### 🔬 rpi-research로 조사하기

요구사항, 수용 기준, 종속성, 중요한 위험, 복잡도, 불확실성, 또는 의사결정에 중요한 질문에 대해 현재 증거가 충분하지 않을 때만 `/rpi-research`를 사용하세요. 다중 파일 변경, 새로운 패턴, 외부 통합, 아키텍처 결정은 격차를 드러낼 수 있지만, 자동으로 새로운 조사를 요구하지는 않습니다.

조사는 읽기 전용입니다. 워크스페이스와 관련된 외부 소스를 검색하고, 증거를 가정과 구분하고, 대안을 평가하고, 계획 준비 상태를 기록합니다. 조사가 실행되면 지속되는 출력은 다음과 같습니다:

```text
.copilot-tracking/research/{{YYYY-MM-DD}}/{{task_slug}}-research.md
```

제공되었거나 이미 완료된 증거가 충분하다면 재사용하세요. 조사가 왜 재사용되었는지 또는 충족되어 생략되었는지를 기록하여 다음 단계가 조사를 반복하지 않도록 하세요.

### 📋 rpi-plan으로 계획하기

충분한 증거를 소스 파일을 변경하지 않고 순서가 지정된 검증 가능한 구현 전략으로 전환해야 할 때 `/rpi-plan`을 사용하세요. 계획 수립은 소스 파일 변경이 아니라 종속성, 수용 기준, 경계, 안정적인 작업 식별자에 초점을 맞춥니다.

이 스킬은 계획을 생성하거나 수정하며, 비평(critique)을 건너뛰지 않는 한 비평 산출물도 함께 생성합니다:

```text
.copilot-tracking/plans/{{YYYY-MM-DD}}/{{task_slug}}-plan.md
.copilot-tracking/reviews/plans/{{YYYY-MM-DD}}/{{task_slug}}-plan-critique.md
```

작업 중심 계획은 일치하는 `<!-- rpi:... -->` 마커와 함께 안정적인 `Pxx` 단계 ID와 `Pxx-Txx` 작업 ID를 사용합니다. 계획은 요약(executive summary)과 전체 변경 사항의 Mermaid 다이어그램으로 시작하는 Phase Checklist로 열리며, 각 단계는 자신의 부분이 강조된 해당 다이어그램을 반복합니다.

모든 작업은 레이블이 붙은 `Goals:`, `Requirements:`, `Details:`, `References:`, `Dependencies:` 블록을 포함하며, 코드와 명령은 백틱으로 감싸고 영향을 받는 파일에 대한 마크다운 링크를 포함합니다. `Requirements:` 블록은 작업에 대한 확인 가능한 기록이며, 이를 검증하는 방법은 구현자에게 맡겨집니다.

비평은 기본적으로 실행되며 구현 준비 상태 전에 `Pass`, `Revise`, `Blocked` 중 하나를 기록합니다. `critique=skip`을 전달하거나 생략을 요청하면 계획 수립은 비평이 생략되었음을 기록합니다. 계획의 다른 준비 상태 확인은 여전히 적용됩니다.

### ⚡ rpi-implement로 구현하기

승인된 `Pxx` 또는 `Pxx-Txx` 작업을 실행하려면 `/rpi-implement`를 사용하세요. 실행 범위가 명확할 때는 날짜가 포함된 계획, 비평 결과, 정확한 단계 또는 작업을 제공하세요.

구현은 실질적인 작업과 진실한 검증을 다음에 기록합니다:

```text
.copilot-tracking/changes/{{YYYY-MM-DD}}/{{task_slug}}-changes.md
```

완료 체크박스는 증거가 존재할 때만 변경됩니다. 구현 과정에서 승인된 계획에서 크게 벗어나야 한다면, 변경 기록에 그 발견을 기록하고, 필요한 결정 이후 영향을 받는 계획 작업을 업데이트하며, 계획이 최신 상태가 될 때까지 종속 작업만 일시 중지합니다. 기존 비평은 역사적 증거로 남으며, 후속 비평은 선택사항입니다.

### ✅ rpi-review로 리뷰하기

구현 증거가 수용 리뷰 준비가 되었을 때 `/rpi-review`를 사용하세요. 리뷰는 선택사항이며, 수용 기록이 필요하지 않다면 생략하세요. 리뷰는 검토 대상 소스를 수정하지 않습니다. 요구사항, 수용 기준, 계획 및 작업 완료, 비평 결과, 구현 시점의 계획 업데이트, 변경 사항, 검증 증거를 하나의 기록으로 비교하고, 최종 결과와 라우팅을 기록합니다:

```text
.copilot-tracking/reviews/logs/{{YYYY-MM-DD}}/{{task_slug}}-review.md
```

중대한 발견에는 심각도가 표시된 `RV-xxx` 식별자와 명시적인 목적지가 부여됩니다. 리뷰는 실행 상태(`Complete`, `Partial`, `Blocked`)를 결과(`Conformant`, `Conformant with justified divergence`, `Defects found`, `Residual work`, `Not accepted`)와 별도로 유지합니다. 이 구분은 완료된 실행이 수용된 작업으로 오인되는 것을 방지합니다.

### ➡️ 후속 조치

후속 조치는 다른 라이프사이클 개념의 이름을 바꾸거나 반복하지 않습니다. 결함은 구현으로, 결정 격차는 계획으로, 증거 격차는 조사로, 잔여 작업은 별도의 다음 항목으로 라우팅합니다.

## RPI 진입 경로

다음 작업을 소유하는 가장 작은 진입 경로를 선택하세요:

| 진입 경로      | 사용 시점                                                   | 계약                                                                                            |
|--------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `RPI Agent`        | 사용자가 선택하는 라이프사이클 래퍼를 원할 때                    | 하나의 작업 아이덴티티로 해당 RPI 스킬을 활성화; 기본적으로 수동, 요청 시 Full Auto |
| `/rpi-research`    | 입증된 증거 격차가 신뢰할 수 있는 진행을 가로막을 때          | 계획이나 구현 없이 조사 증거를 생성                                                               |
| `/rpi-plan`        | 충분한 증거가 구현 전략을 필요로 할 때            | 작업 중심 계획과 비평 결과를 생성                                                            |
| `/rpi-implement`   | 승인된 작업이 실행 준비가 되었을 때                             | 소스 변경, 변경 증거, 검증을 생성                                                               |
| `/rpi-review`      | 구현 증거가 조정(reconciliation) 준비가 되었을 때           | 하나의 리뷰 기록을 생성하고 미해결 작업을 라우팅                                                               |
| `/rpi-challenger`  | 행동하기 전에 가정을 드러내고 싶을 때                  | 적응형 회의적 질문을 던지고 미해결 항목을 기록                                              |
| `/rpi-walkthrough` | 변경하기 전에 코드나 산출물을 이해하고 싶을 때 | 한 번에 한 구간씩 설명하고 필요시 요청된 변경 사항을 기록                                                           |

사용자가 선택하는 라이프사이클 래퍼를 원할 때는 이 동일한 스킬을 활성화하는 `RPI Agent`를 선택하세요. 자동 세션을 확인할 때까지 수동 모드로 실행되며, 확인 후 Review까지 나머지 단계를 완료하고 우선순위가 지정된 후속 작업을 제안합니다. `RPI Agent`는 전문 작업자의 자율적인 디스패처가 아니라 진입 경로입니다. 모드 세부 사항은 [RPI를 함께 사용하기](using-together#manual-and-automatic-mode-in-rpi-agent)를 참고하세요.

## 라이프사이클 개념 간 맥락 관리

긴 라이프사이클에 맥락이 누적되었거나, 개념을 전환하거나, 대화가 더 이상 작업에 도움이 되지 않을 때 `/clear` 또는 새 채팅을 사용하세요. 맥락 재설정은 조사를 반복하거나 라이프사이클을 다시 시작해야 하는 요구사항이 아니라 명확성을 위한 도구입니다.

지속되는 산출물이 필요한 맥락을 전달합니다:

```text
research, when it runs → task-centered plan → changes → review and routed follow-up
```

동일한 안정적인 작업 ID로 재개하고 관련된 날짜가 포함된 산출물을 열거나 참조하세요. `Pxx`, `Pxx-Txx`, 헤딩, `<!-- rpi:... -->` 마커로 계획 섹션을 탐색하세요.

이것이 중요한 이유에 대한 기술적 설명은 [Context Engineering](context-engineering)을 참고하세요.

## RPI를 사용해야 할 때

| RPI 산출물을 사용할 때...                                 | 더 작은 직접 편집을 사용할 때...               |
|-----------------------------------------------------------|---------------------------------------------------|
| 작업에 증거, 계획, 리뷰 라우팅이 필요할 때      | 변경이 명확하고 독립적일 때                |
| 종속성, 위험, 불확실성에 명시적 처리가 필요할 때 | 기존 증거와 수용 기준이 충분할 때 |
| 핸드오프에 지속적인 작업 증거가 필요할 때              | 지속적인 라이프사이클 증거가 필요하지 않을 때        |

준비 상태 평가에서 격차가 식별되면 조사를 사용하세요. 그렇지 않으면 작업에 신뢰할 수 있는 증거와 명확한 소유자를 부여하는 가장 작은 라이프사이클 행동을 선택하세요.

## 빠른 시작

1. 요구사항, 수용 기준, 결정, 종속성, 사용 가능한 증거로 작업을 정의하세요.
2. 조사 준비 상태를 평가하고, 입증된 격차가 남아 있을 때만 `/rpi-research`를 사용하세요.
3. 지속적인 계획 수립이 필요할 때 `/rpi-plan`으로 계획하세요.
4. `/rpi-implement`로 승인된 작업을 구현하세요.
5. `/rpi-review`로 리뷰한 다음, 결함, 결정, 증거 격차, 잔여 작업을 Follow-up을 통해 라우팅하세요.

> [!TIP]
> 라이프사이클 진입 경로를 원할 때는 `RPI Agent`를 선택하세요. 필요한 다음 작업이 이미 명확할 때는 단계별 스킬을 직접 사용하세요.

## 다음 단계

* [RPI 워크플로가 효과적인 이유](why-rpi) - 단계 분리가 증거와 추적성을 어떻게 향상시키는지 이해하기
* [RPI를 함께 사용하기](using-together) - 전체 워크플로 예제 따라가기
* [Context Engineering](context-engineering) - 맥락 관리가 중요한 이유
* [RPI Walkthrough](rpi-walkthrough) - 가이드가 포함된 설명으로 코드나 산출물 탐색하기
* [Agents Reference](../reference/agents/) - 사용 가능한 모든 에이전트
* [Agent Systems Catalog](../agents/) - RPI를 넘어선 모든 에이전트 패밀리 둘러보기

## 참고 자료

* [Engineer Guide](../hve-guide/roles/engineer.md) - RPI를 사용하는 엔지니어를 위한 역할별 가이드
* [Tech Lead Guide](../hve-guide/roles/tech-lead.md) - 아키텍처 리뷰와 프롬프트 엔지니어링 워크플로
* [Stage 6: Implementation](../hve-guide/lifecycle/implementation.md) - RPI가 프로젝트 라이프사이클에 맞는 위치

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
