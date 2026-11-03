---
title: HVE Core 포크하고 확장하기
description: 업스트림 동기화와 Copilot 지원 적용을 통해 완전히 맞춤화된 프롬프트 엔지니어링 프레임워크를 만들기 위한 HVE Core 포크
author: Microsoft
ms.date: 2026-10-31
ms.topic: tutorial
keywords:
  - forking
  - extending
  - upstream sync
  - customization
estimated_reading_time: 10
---

## 언제 포크해야 하는가

포크는 여러분이 완전히 제어하는 HVE Core의 독립적인 사본을 만듭니다. 제자리 커스터마이징
(지침 추가, 패키지 범위 산출물 추가, 검증 확장)으로는 부족할 때 포크를 고려하세요.

### 다음과 같은 경우 포크하세요

* 핵심 워크플로 에이전트를 조직별 버전으로 교체해야 할 때
* 플러그인 멤버십, 확장 패키징, 빌드 시스템을 수정해야 할 때
* 구조적 변경이 필요한 맞춤형 거버넌스 정책을 강제해야 할 때
* 독점 산출물을 가진 비공개 배포 채널을 유지해야 할 때
* 핵심 스크립트 변경이 필요한 내부 시스템과 통합해야 할 때

### 다음과 같은 경우 제자리 커스터마이징을 유지하세요

* 기존 항목을 수정하지 않고 새 에이전트, 프롬프트, 지침을 추가하는 경우
* 자체 패키지 범위 네임스페이스 아래에 조직별 산출물을 추가하는 경우
* 맞춤형 린팅 스크립트로 검증을 확장하는 경우
* 기존 도구를 설정 파일을 통해 구성하는 경우

> [!IMPORTANT]
> 포킹은 지속적인 유지관리 비용을 수반합니다. 모든 업스트림 릴리스는 평가, 병합,
> 잠재적 충돌 해결이 필요합니다. 제자리 커스터마이징으로 목표를 달성할 수 없을 때만
> 포킹을 선택하세요.

## 포크 설정

### 1단계: 포크 생성

GitHub의 포크 메커니즘을 통해 저장소를 포크하세요. 개인 계정 또는 조직으로 포크할지
선택하세요.

```bash
gh repo fork microsoft/hve-core --org your-org --clone
cd hve-core
```

### 2단계: 업스트림 리모트 구성

```bash
git remote add upstream https://github.com/microsoft/hve-core.git
git fetch upstream
```

### 3단계: 의존성 설치

```bash
npm ci
```

네트워크가 공개 패키지 레지스트리를 차단하는 경우,
[제한된 네트워크에서 설치하기](../contributing/validation#install-behind-a-restricted-network)를
참조하세요. 포크 파일이 아닌 환경에서 레지스트리 재정의를 설정하여, 포크를 복제하는
모든 사람에게 복원 가능하게 유지하세요.

### 4단계: 초기 구성 변경

다음 파일을 업데이트하여 조직을 반영하세요:

* `package.json`: `name`, `description`, `repository` 필드를 변경하세요
* `README.md`: 브랜딩, 설치 지침, 지원 링크를 업데이트하세요
* `CONTRIBUTING.md`: 팀에 맞게 기여 가이드라인을 조정하세요
* `SECURITY.md`: 조직의 보안 신고 프로세스를 가리키도록 하세요

### 5단계: 빌드 검증

```bash
npm run validate:local
npm run plugin:sync
npm run plugin:validate
```

## 7가지 커스터마이징 영역

포크 후, 다음 영역들이 가장 높은 가치의 커스터마이징 기회를 제공합니다.

### 1. VS Code 확장

`extension/` 디렉터리는 HVE Core 컴포넌트 세트를 하나의 VS Code 확장으로 배포하기 위한
패키징 구성을 포함합니다. 확장 매니페스트, README, 마켓플레이스 프레젠테이션을
커스터마이징하려면 `extension/templates/`를 수정하세요. 확장 패키징 세부 정보는
[VS Code Extension API](https://code.visualstudio.com/api)를 참조하세요.

### 2. Copilot 경로

에이전트와 프롬프트 파일은 `.github/agents/`와 `.github/prompts/` 아래에 있습니다.
조직의 팀 토폴로지나 도메인 경계에 맞게 이 디렉터리들을 재구성하세요. 루트
`plugin.json`에 적합한 `.github` 경로를 반영하려면 `npm run plugin:sync`를 실행하세요.

### 3. MCP 서버

워크플로가 MCP(Model Context Protocol) 서버에 의존하는 경우, `.vscode/mcp.json`
또는 워크스페이스 설정에서 서버 정의를 구성하세요. 포크 수준의 변경을 통해 모든
관련 에이전트와 스킬이 참조할 수 있는 조직별 MCP 서버를 추가할 수 있습니다.

### 4. npm 스크립트

빌드와 검증 요구사항에 맞게 `package.json`에서 npm 스크립트를 추가, 수정, 제거하세요.
일반적인 추가 사항으로는 조직별 린팅 규칙, 맞춤형 배포 스크립트, 통합 테스트
러너가 있습니다.

### 5. Markdownlint 규칙

조직의 문서화 표준을 강제하려면 `.markdownlint.json`을 커스터마이징하세요. 기존
스타일 가이드에 맞게 맞춤형 규칙을 추가하거나 제한(예: 줄 길이)을 조정하세요.

### 6. 릴리스 구성

릴리스 주기와 변경 로그 형식에 맞추려면 `release-please-config.json`을 수정하세요.
워크플로에 맞게 버전 증가 전략과 변경 로그 섹션을 조정하세요.

### 7. 워크플로 권한

`.github/workflows/`의 GitHub Actions 워크플로는 CI/CD 동작을 정의합니다. 워크플로
권한을 조정하거나, 조직별 검증 작업을 추가하거나, 내부 CI 시스템과 통합하세요.

## 업스트림 동기화 워크플로

새로운 기능, 버그 수정, 보안 패치를 받으려면 주기적으로 업스트림 변경 사항을
가져오세요.

### 업스트림 변경 사항 가져오기 및 검토

```bash
git fetch upstream
git log --oneline upstream/main..HEAD
git log --oneline HEAD..upstream/main
```

### 업스트림 변경 사항 병합

```bash
git checkout main
git merge upstream/main
```

### 충돌 해결

충돌은 일반적으로 커스터마이징한 파일에서 발생합니다. 일반적인 충돌 지점:

* `package.json` (스크립트 수정 사항)
* `.markdownlint.json` (규칙 조정 사항)
* 산출물이 추가되거나 제거된 후의 루트 `plugin.json` 멤버십
* 워크플로 파일 (권한 또는 작업 변경 사항)

각 충돌에 대해 여러분의 변경을 유지할지, 업스트림 변경을 수락할지, 또는 둘을
결합할지 평가하세요. 해결 후 검증하세요:

```bash
npm run validate:local
npm run plugin:sync
npm run plugin:validate
```

### 동기화할 파일 vs. 건너뛸 파일

| 동기화 (업스트림 수락)                      | 건너뛰기 (버전 유지)                  |
|--------------------------------------------|---------------------------------------|
| `scripts/`의 핵심 스크립트                 | `package.json` (맞춤 필드)            |
| `scripts/linting/schemas/`의 스키마 파일   | `README.md` (브랜딩)                  |
| 에이전트와 프롬프트 템플릿                 | `.github/workflows/` (CI 구성)        |
| 공유 지침                                  | `CONTRIBUTING.md` (가이드라인)        |
| `docs/`의 문서                             | 맞춤형 플러그인 멤버십 및 브랜딩      |

## Copilot 지원 적용

Copilot을 사용하여 업스트림 통합과 포크 유지관리를 가속화하세요. 다음 프롬프트는
변경 사항을 효율적으로 분석하고 적용하는 데 도움이 됩니다.

### 업스트림 차이 분석

```text
Analyze the upstream changes between our fork and upstream/main.
Summarize what changed, identify which files conflict with our
customizations, and recommend a merge strategy for each conflict.
```

### 새 지침을 조직 맥락에 맞게 적용

```text
Review the new instruction files added in the upstream merge.
Adapt them to use our organization's terminology, coding standards,
and tool chain. Preserve the original intent while aligning with
our conventions in .github/instructions/.
```

### 포크 상태 검증

```text
Compare our fork against upstream/main. Identify files that have
diverged significantly, check for deprecated patterns we still use,
and list any new upstream features we have not adopted. Produce a
prioritized maintenance backlog.
```

## 포크 유지관리

포크를 건강하게 유지하기 위해 정기적인 유지관리 주기를 수립하세요.

### 동기화 빈도

최소한 릴리스 주기당 한 번은 업스트림과 동기화하세요. 더 빈번한 동기화(매주 또는
격주)는 각 병합의 규모를 줄이고 충돌 위험을 낮춥니다.

### 버전 관리 전략

릴리스 주기를 반영하는 자체 버전 체계를 `package.json`에서 유지하세요. 마지막으로
동기화한 업스트림 버전을 주석이나 별도의 추적 파일에 기록하여 각 동기화 시 차이를
식별할 수 있도록 하세요.

### 폐기 처리

업스트림이 산출물을 폐기할 때, 다음 중 평가하세요:

* 즉시 포크에서 제거
* 문서화된 전환 기간 동안 `.github/deprecated/` 아래로 이동
* 조직별 대안으로 교체

### 상태 점검

모든 동기화 후 전체 검증 스위트를 실행하세요:

```bash
npm run validate:local
npm run plugin:sync
npm run plugin:validate
```

## 역할 시나리오

**Fabrikam의 플랫폼 팀**은 조직 전체의 Copilot 거버넌스를 수립하기 위해 HVE Core를
포크합니다. 그들은 기본 RPI 워크플로 에이전트를 Fabrikam의 코드 리뷰 정책을 강제하는
버전으로 교체하고, 내부 API를 위한 맞춤형 MCP 서버 구성을 추가하며, 모든 엔지니어링
팀에게 비공개 VS Code 확장으로 포크를 배포합니다. 격주 업스트림 동기화를 통해
커스터마이징을 방해받지 않으면서 새로운 스킬과 보안 패치를 받습니다.

**Woodgrove Bank의 컴플라이언스 팀**은 금융 규제 지침과 감사 추적 요구사항을
추가하기 위해 HVE Core를 포크합니다. 그들은 모든 에이전트와 프롬프트에 필요한
면책 조항 섹션이 있는지 확인하는 컴플라이언스 검증 스크립트를 포함하도록 빌드
시스템을 커스터마이징합니다. 컴플라이언스 팀은 병합 전에 각 업스트림 변경 사항을
규제 요구사항에 비추어 검토하면서 엄격한 월간 동기화 주기를 유지합니다.

## 추가 읽을거리

* 확장 패키징 및 배포를 위한 [VS Code Extension API](https://code.visualstudio.com/api)
* 산출물 구문 및 기여 가이드라인을 위한 [docs/contributing/](../contributing/)
* 로컬 안전 기본값과 별도의 CI 레인을 위한 [검증 명령과 CI 전용 레인](../contributing/validation)

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
