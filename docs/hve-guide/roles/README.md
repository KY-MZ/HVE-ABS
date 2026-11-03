---
title: 역할 가이드
description: HVE Core 도구를 활용한 AI 지원 엔지니어링을 위한 역할별 가이드 찾기
sidebar_position: 1
author: Microsoft
ms.date: 2026-10-31
ms.topic: concept
keywords:
  - roles
  - guides
  - AI-assisted engineering
  - capabilities
estimated_reading_time: 5
---

HVE Core는 전체 배포 아이덴티티의 에이전트, 지침(instructions), 스킬을 통해 역할별 기능을 제공합니다. 각 역할 가이드는 작업 방식에 맞춰 권장 기능, 단계별 안내, 시작 프롬프트, 협업 패턴을 다룹니다.

## 역할 개요

| 역할                     | 전용 자산 수 | 전체 대상 자산 수 | 주요 단계                              | 가이드                                                   |
|--------------------------|------------------|--------------------|-----------------------------------------------|-----------------------------------------------------------|
| Engineer                 | 26               | 28+                | Stage 2, Stage 3, Stage 6, Stage 7, Stage 8 | [Engineer](engineer.md)                                 |
| TPM                      | 24               | 32+                | Stage 2, Stage 3, Stage 4, Stage 5, Stage 8 | [TPM](tpm.md)                                           |
| Tech Lead / Architect    | 19               | 23+                | Stage 2, Stage 3, Stage 6, Stage 7, Stage 9 | [Tech Lead](tech-lead.md)                               |
| Security Architect       | 3                | 9                  | Stage 2, Stage 3, Stage 7, Stage 9          | [Security Architect](security-architect.md)             |
| Data Scientist           | 6                | 13                 | Stage 2, Stage 3, Stage 6, Stage 7, Stage 8 | [Data Scientist](data-scientist.md)                     |
| UX Designer              | 58               | 63+                | Stage 2, Stage 3, Stage 6, Stage 7, Stage 9 | [UX Designer](ux-designer.md)                           |
| SRE / Operations         | 8                | 13+                | Stage 1, Stage 3, Stage 6, Stage 8, Stage 9 | [SRE / Operations](sre-operations.md)                   |
| Business Program Manager | N/A              | N/A                | Stage 2, Stage 3, Stage 4, Stage 5          | [Business Program Manager](business-program-manager.md) |
| New Contributor          | 2                | 10                 | Stage 1, Stage 2, Stage 6, Stage 7          | [New Contributor](new-contributor.md)                   |
| Utility                  | N/A              | 13                 | All                                         | [Utility](utility.md)                                   |

> **전용 자산**은 특정 역할의 주요 워크플로를 위해 만들어진 에이전트, 지침, 스킬의 수를 셉니다. **전체 대상 자산**에는 횡단적 도구(Git 스킬, 자동 활성화 지침, 공유 스킬)가 더해집니다. **+** 접미사는 개별적으로 나열되지 않은 추가 자동 활성화 자산을 나타냅니다. 숫자는 근사치입니다.

## 역할 찾기

| 하고 싶은 일                                                  | 추천 역할 가이드                                  |
|---------------------------------------------------------------|-----------------------------------------------------------|
| 코드 작성, 기능 구현, 버그 수정                   | [Engineer](engineer.md)                                 |
| 프로젝트 계획, 요구사항 관리, 작업 추적             | [TPM](tpm.md)                                           |
| 아키텍처 설계, 코드 리뷰, 표준 수립            | [Tech Lead](tech-lead.md)                               |
| 보안 평가, 보안 모델 작성, 컴플라이언스 검토 | [Security Architect](security-architect.md)             |
| 데이터 분석, 노트북 구축, 대시보드 생성           | [Data Scientist](data-scientist.md)                     |
| DT 워크샵 진행, 사용자 경험 설계, 프로토타입 테스트 | [UX Designer](ux-designer.md)                           |
| 인프라 관리, 인시던트 처리, 배포            | [SRE / Operations](sre-operations.md)                   |
| 비즈니스 성과 정의 또는 이해관계자 정렬 관리      | [Business Program Manager](business-program-manager.md) |
| 프로젝트 기여 시작하기                       | [New Contributor](new-contributor.md)                   |
| 횡단적 유틸리티 사용(워크플로 상태, 문서, 미디어)     | [Utility](utility.md)                                   |

## 협업 패턴

역할은 워크플로 전반에서 자주 협업합니다. 다음 시나리오는 일반적인 다중 역할 상호작용을 보여줍니다:

* 엔지니어와 테크 리드는 아키텍처 리뷰, 코딩 표준 준수, 구현 안내를 포함해 기능 개발에서 협업합니다. [Engineer](engineer.md)와 [Tech Lead](tech-lead.md) 가이드를 참고하세요.
* TPM과 Security Architect는 요구사항 수집, 보안 모델 분석, 컴플라이언스 검증을 결합해 안전한 제품 출시를 조율합니다. [TPM](tpm.md)과 [Security Architect](security-architect.md) 가이드를 참고하세요.
* 데이터 과학자와 엔지니어는 데이터 스펙, 노트북 프로토타이핑, 프로덕션 통합으로 분석 파이프라인 개발을 연결합니다. [Data Scientist](data-scientist.md)와 [Engineer](engineer.md) 가이드를 참고하세요.
* 신규 기여자는 가이드 워크플로에서 완전한 자율적 엔지니어링까지 온보딩을 거쳐 엔지니어로 성장합니다. [New Contributor](new-contributor.md)와 [Engineer](engineer.md) 가이드를 참고하세요.
* UX 디자이너와 엔지니어는 검증된 Design Thinking 컨셉을 RPI 구현 워크플로에 연결하여 사용자 리서치를 엔지니어링 스프린트와 잇습니다. [UX Designer](ux-designer.md)와 [Engineer](engineer.md) 가이드를 참고하세요.

## 커버리지 참고 사항

각 역할은 9개의 라이프사이클 단계와 교차하여 81개의 역할-단계 쌍을 만듭니다. 해당 쌍 전체의 커버리지 수준은 다음과 같습니다:

| 수준    | 역할-단계 쌍 | 비율 |
|----------|-----------------:|--------:|
| Strong   |               13 |     16% |
| Moderate |               18 |     22% |
| Thin     |               18 |     22% |
| None     |               32 |     40% |

가장 강한 커버리지: Stage 6-7(구현 및 리뷰)의 Engineer, Stage 2-5(요구사항부터 스프린트 계획)의 TPM, Stage 9(운영)의 SRE, Design Thinking을 통한 Stage 2-3(발견 및 설계)의 UX Designer.

가장 얇은 역할: Security Architect(전용 자산 3개, 9개 단계 중 6개가 None 또는 Thin)와 Business Program Manager(베타, 모든 도구를 공유 기능에서 차용).

가장 커버리지가 적은 단계: Stage 4 Decomposition — 9개 역할 중 8개가 전용 도구가 없음. TPM만 이 단계에서 강한 커버리지를 가짐.

> [!NOTE]
> 격차는 기여 기회를 나타냅니다. 단계별 세부 사항은 [라이프사이클 단계 가이드](../lifecycle/)를, 새로운 에이전트·프롬프트·지침 작성 안내는 [Contributing](../../contributing/)을 참고하세요.

## 다음 단계

> [!TIP]
> 단계가 역할 전반에서 어떻게 연결되는지 이해하려면 [AI-Assisted Project Lifecycle](../lifecycle/)에서 전체 프로젝트 라이프사이클을 확인하세요. 각 단계 가이드는 해당 작업 단계에 대해 사용 가능한 HVE Core 도구와 역할별 안내를 매핑합니다.

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
