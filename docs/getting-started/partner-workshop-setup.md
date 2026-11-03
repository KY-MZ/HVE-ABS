---
title: 파트너 워크샵 설정
description: HVE 파트너 워크샵을 위한 로컬 VS Code 설정 안내
sidebar_position: 8
author: Microsoft
ms.date: 2026-11-01
ms.topic: tutorial
keywords:
  - GitHub Codespaces
  - Visual Studio Code
  - macOS
  - HVE Core All
  - workshop setup
estimated_reading_time: 8
---

## 워크샵 일정

| 단계 | 활동                                                                                       | 시간   |
|------|-------------------------------------------------------------------------------------------|-------|
| 1    | [워크샵 개요](partner-workshop.md)                                                     | 30분 |
| 2    | [**워크샵 환경 설정(로컬 VS Code)**](partner-workshop-setup.md)                                            | 30분 |
| 3-1    | [역할별 트랙 Part1: 계획/비전/경험](partner-workshop-role-tracks.md)                      | 45분 |
| 3-2    | [역할별 트랙 Part2: 아키텍처 설계, 백로그](partner-workshop-role-tracks-2.md)                 | 45분 |
| 4    | [검증 및 솔루션](partner-workshop-solution.md)                                             | 30분 |
| 5    | [Microsoft Marketplace 및 Copilot Agent Store 준비](partner-workshop-publishing.md)       | 60분 |
| 6    | [구현 및 상용화로의 핸드오프](partner-workshop-implementation.md)                            | 30분 |

## 설정 경로 선택

이번 워크샵에서는 Windows 또는 macOS에서 VS Code를 로컬로 실행하는 옵션으로 진행합니다. 원문에서는 GitHub Codespaces를 사용하는 옵션도 제공하고 있으니, Codespaces를 사용하고자 하는 경우 참고하시기 바랍니다.

## 공통 사전 요구사항

시작하기 전에 다음 단계를 완료하세요:

1. GitHub Copilot 접근 권한이 있는 GitHub 계정으로 로그인하세요.
2. 조직이 GitHub Copilot Chat을 허용하는지 확인하세요.


## Windows 또는 macOS의 로컬 VS Code 설정

1. [Git](https://git-scm.com/downloads)과
   [Visual Studio Code](https://code.visualstudio.com/Download)를
   설치하세요.
2. Node.js, mermaid-cli 를 설치하세요. (윈도우 명령 프롬프트를 열고 아래 명령을 통해서 설치하세요)
        
     winget install OpenJS.NodeJS.LTS     
     npm install –g @mermaid-js/mermaid-cli
4. VS Code를 열고 확장 보기를 열어 **GitHub Copilot**과 **GitHub Copilot Chat**을 설치하세요.
5. Copilot 접근 권한이 있는 GitHub 계정으로 로그인하세요.
6. [HVE Core All](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)을
   설치하세요.
7. 명령 팔레트를 열고 [https://github.com/jeongaelee/hve-innovation-kr](https://github.com/jeongaelee/hve-innovation-kr)에 대해 **Git: Clone**을 실행한 후 여세요.
8. 클론이 끝나면 **Open**을 선택하고, 저장소와 퍼실리테이터를 알고 있는 경우에만 **Trust**를 선택하세요.
9. 파일 편집을 시작하기 전에 기술 리드가 워크샵 활동용 브랜치를 만들 수 있습니다. `workshop/<team-name>`과 같은 이름을 사용하세요.

환경에서 Foundry 로컬 모델을 사용할 수 있다면 로컬 추론에 이를 선택할 수 있습니다. 그렇지 않다면 비용 효율적인 옵션으로 GitHub Copilot Chat에서 `MAI-Code-1-Flash`를 선택하세요. Microsoft Foundry Toolkit을 사용한 로컬 모델 설정 방법은
[https://devblogs.microsoft.com/foundry/ai-assisted-development-powered-by-local-models/](https://devblogs.microsoft.com/foundry/ai-assisted-development-powered-by-local-models/)를 참고하세요.

macOS에서는 동일한 메뉴와 버튼을 사용하세요. Windows에서 `Ctrl`을 사용하는 키보드 단축키는 macOS에서 `Command`를 사용하는 경우가 많으므로, 이 워크샵은 메뉴 탐색을 우선합니다.

## 환경 검증

다음 단계를 완료하세요:

1. 작업 표시줄에서 Copilot Chat을 여세요.
2. Chat 보기에서 에이전트 선택기를 여세요.
3. **RPI Agent**, **BRD Builder**, **UX UI Designer**, **System Architecture Reviewer**와 같은 에이전트가 보이는지 확인하세요.
4. Chat에 `/`를 입력하세요.
5. RPI 프롬프트가 나타나는지 확인하세요. **RPI Agent**를 선택하세요.
6. 다음 프롬프트를 입력하세요:

```text
Review the repository and identify the most relevant HVE Core assets for a partner workshop scenario. Summarize the likely workflow, likely agents, and any prerequisites before the team begins the role exercises.
```
한글 프롬프트:
```text
Repository를 검토하고, partner workshop 시나리오에 가장 적합한 "HVE Core assets"를 식별하세요.
팀이 역할 실습(role exercises)을 시작하기 전에, 예상되는 워크플로우, 활용할 가능성이 높은 에이전트, 그리고 필요한 사전 요구사항을 요약하세요.
```

예상한 에이전트가 보이지 않으면:

1. 확장 보기를 여세요.
2. 두 확장이 모두 설치되어 있다면 **HVE Installer**를 비활성화하세요.
3. 명령 팔레트에서 **Developer: Reload Window**를 실행하세요.
4. Copilot Chat을 다시 열고 에이전트 선택기를 다시 확인하세요.
5. 문제가 계속되면 [문제 해결 가이드](troubleshooting.md)를 사용하세요.

## 워크샵 작업 공간 준비

기술 리드에게 다음 수동 단계를 완료하도록 요청하세요:

* 팀이 워크샵 브랜치에서 작업하고 있는지 확인하세요.
* 첫 번째 역할 실습을 위해 팀원 역할, 알려진 사실, 제약, 승인된 소스
  자료를 준비하세요.
* 이후 어떤 에이전트가 작업하기 전에 세션 컨텍스트 아티팩트 경로를
  제공하고 에이전트에게 해당 파일에서 주제를 읽도록 요청하세요. 이후
  프롬프트에서 주제를 반복하거나 다시 정의하지 마세요.
* 워크샵용 사례의 경우, 합성 데이터 또는 공개 소스 자료를 수동으로 관리하는
  `.copilot-tracking/research/workshop-input/` 폴더에 두세요. 정책, SOP,
  다이어그램, 지원 파일을 파일 유형별로 그곳에 보관하세요.
* 실제 프로덕션 사례의 경우, 민감한 증거는 승인된 소스 시스템 또는 보안
  증거 작업 공간에 보관하세요. 저장소에 파일을 복사하는 대신 신뢰할 수 있는
  경로 또는 통제된 링크를 리서치에 사용하세요.
* 에이전트를 선택하기 전에 세션 주제를 설정한 후
  `.copilot-tracking/research/` 아래에 세션 컨텍스트 아티팩트를 만드세요.
  이 아티팩트를 주제, 증거 위치, 프로덕션 출력 루트에 대한 신뢰할 수 있는
  소스로 취급하세요.

다음 프롬프트를 사용하여 공유 세션 컨텍스트를 만드세요:

```text
Select the /RPI Agent. Create a session-context artifact before starting
research or drafting requirements.

Session name: [short name for this workshop]
Topic: [topic or use case]
Evidence location: [approved path, controlled link, or source system]
Date: [YYYY-MM-DD]

Create the artifact at
`.copilot-tracking/research/[YYYY-MM-DD]/[session-name]-session-context.md`.
Record the session name, topic, evidence location, date, evidence boundary,
and production output roots. Make this artifact the required context for
every later agent. Mark it as draft for human review. Do not start research,
create a BRD or PRD, create backlog items, or copy sensitive evidence into
the repository.
```

예시:

```text
Select the /RPI Agent. Create the session context only.

Session name: relationship-manager-fsi
Topic: Relationship Manager Intelligence Assistant for FSI
Evidence location: ./copilot-tracking/research/workshop-input
Date: 2026-11-04
```

한글 프롬프트 예시:

```text
/RPI Agent를 선택하세요. session context만 생성하세요.
Session name: relationship-manager-fsi
Topic: FSI를 위한 Relationship Manager Intelligence Assistant
Evidence location: ./copilot-tracking/research/workshop-input
Date: 2026-11-04
```

* 첫 번째 역할 실습을 위해 팀원 역할, 알려진 사실, 제약, 승인된 소스 자료를 준비하세요.
* 이후 어떤 에이전트가 작업하기 전에 세션 컨텍스트 아티팩트 경로를 제공하고 에이전트에게 해당 파일에서 주제(Topic)를 읽도록 요청하세요. 이후 프롬프트에서 주제를 반복하거나 다시 정의하지 마세요.
* 워크숍에서 사용할 증빙 자료는 합성 데이터 또는 공개된 자료를 활용하여, 매뉴얼하게 관리하는 `workshop-input/` 폴더에 두세요. 정책, SOP, 다이어그램, 지원 자료 파일을 유형별로 이 폴더에 보관하세요.
* 실제 프로덕션 사례의 경우, 민감한 증거는 승인된 소스 시스템 또는 보안 증거 작업 공간에 보관하세요. 저장소에 파일을 복사하는 대신 신뢰할 수 있는 경로 또는 통제된 링크를 리서치에 사용하세요.
* 승인된 환경이 해당 증거와 접근 통제를 명시적으로 허용하고 이를 확인하지 않는 한, 자격 증명, 개인 데이터, 고객 비밀, 프로덕션 콘텐츠를 프롬프트와 파일에서 제외하세요.
* 검토된 워크샵 출력만 팀 브랜치에 커밋하세요.

> [!TIP]
> 에이전트는 워크플로우가 실행될 때 `.copilot-tracking/`과 `docs/planning/adrs/` 아래에 워크플로우 아티팩트를 만듭니다. 책임 있는 사람이 검토할 때까지 생성된 콘텐츠를 초안으로 표시해 두세요.

## 상호작용 패턴 알아보기

다음 단계에서는 모든 역할 실습에 동일한 패턴을 사용합니다:

1. 지정된 에이전트를 선택하거나 지정된 스킬을 호출하세요.
2. 시나리오, 알려진 사실, 제약, 요청된 출력 경로를 제공하세요.
3. 초안을 요청하세요.
4. 결과를 검토하고 수정하세요.
5. 검토된 결과를 프로덕션 아티팩트 디렉터리에 저장하세요.
6. 아티팩트를 다음 역할에 전달하세요.

## 다음 단계
[**역할별 트랙 Part1: 계획/비전/경험**](partner-workshop-role-tracks.md)을 진행하세요.

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
