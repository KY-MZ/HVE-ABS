---
title: 파트너 워크샵 게시 후속 작업
description: Microsoft Marketplace와 Microsoft 365 Copilot Agent Store를 위한 게시 준비 상태와 제품 가격 책정 구성
sidebar_position: 11
author: Microsoft
ms.date: 2026-11-01
ms.topic: how-to
keywords:
  - Azure Applications
  - Microsoft Marketplace
  - Partner Center
  - Microsoft 365 Copilot
  - Agent Store
  - monetization
  - product pricing
estimated_reading_time: 16
---

## 워크샵 일정

| 단계 | 활동                                                                                       | 시간   |
|------|-------------------------------------------------------------------------------------------|-------|
| 1    | [워크샵 개요](partner-workshop.md)                                                     | 30분 |
| 2    | [로컬 VS Code 설정](partner-workshop-setup.md)                                            | 30분 |
| 3-1    | [역할별 트랙 Part1: 계획/비전/경험](partner-workshop-role-tracks.md)                      | 45분 |
| 3-2    | [역할별 트랙 Part2: 백로그, 아키텍처 설계](partner-workshop-role-tracks-2.md)                 | 45분 |
| 4    | [검증 및 솔루션](partner-workshop-solution.md)                                             | 30분 |
| 5    | [**Microsoft Marketplace 및 Copilot Agent Store 준비**](partner-workshop-publishing.md)       | 60분 |
| 6    | [구현 및 상용화로의 핸드오프](partner-workshop-implementation.md)                            | 30분 |

## 목표

Microsoft Marketplace와 Microsoft 365 Copilot Agent Store를 통한 게시에
적합하고 검토 가능하도록 만드는 데 필요한 최소한의 작업을 파악하세요.

## 권장 워크샵 결과

세션이 끝날 때까지 팀은 다음 질문에 답할 수 있어야 합니다:

* 어떤 게시 경로를 먼저 목표로 하는가?
* 수익성 있는 제품을 뒷받침하는 공개 가격, 프라이빗 오퍼 가격, 비용
  가정은 무엇인가?
* 엔지니어링, 제품, 보안, 운영 중 누가 소유해야 하는가?
* 실제 제출 전에 무엇이 미해결 상태로 남아 있는가?

## 상업적 준비 상태 및 게시 계획

오퍼 패키지를 구축하기 전에 Marketplace와 에이전트 스토어 검토에 영향을
미칠 상업적 및 시장 진출(go-to-market) 컨텍스트를 파악하세요.

1. Azure 오퍼와 Microsoft 365 에이전트 경험 모두에 대한 제품 브랜드,
   메시징, 핵심 가치 제안을 정의하세요.
2. 초기 지리적 범위, 목표 고객 세그먼트, 언어나 지역 컴플라이언스 제약과
   같은 출시 제한 사항을 확인하세요.
3. 가격, 청구, 비용, 세금 가정이 일치하도록
   [제품 매니저 상용화 계획](#제품-매니저-상용화-계획)을 두 게시 트랙
   모두에 대해 완료하세요.
4. 고객 세그먼트, 문제, 솔루션, 채널, 수익, 비용, 파트너, 차별화
   요소를 포함한 간단한 Lean Business Canvas 요약을 작성하세요.
5. Marketplace의 Azure IP Co-sell을 위해, 게시자 설정, 법인 및 세금
   준비, 오퍼 메타데이터, 지원 연락처, 가격 플랜, 기술 패키지 검증을
   다루는 Partner Center Admin 체크리스트를 완료하세요.
6. Copilot Agent Store 추가 기능을 위해, 지원되는 에이전트 유형,
   패키징 경로, 테넌트 관리자 승인, 동의 경계, 에이전트를 독립 오퍼로
   등록할지 Azure 오퍼의 추가 기능으로 등록할지를 확인하세요.

> [!NOTE]
> 현재 Microsoft 가이드가 지원되는 경로를 확인할 때까지, 모든 상업적
> 경로, 오퍼 유형, 추가 기능 제한을 검증 항목으로 취급하세요. 정책
> 매트릭스는 에이전트 유형과 배포 경로에 따라 변경될 수 있습니다.

## Marketplace FastTrack 코칭
### Microsoft Marketplace 및 Copilot Agent Store 게시로의 안내 경로

이 세션을 지원하는 저장소 내 두 개의 코칭 에이전트가 있습니다.

| 에이전트                        | 사용 용도                                                                                                | 기반 스킬                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------|
| **Microsoft Marketplace Coach** | Azure 측면: SaaS, Managed Application, Container App, Azure VM 오퍼, 가격 책정, Partner Center 구성, Azure IP Co-sell 적격성 | `ms-marketplace-publish`      |
| **Copilot Agent Store Coach**   | Microsoft 365 측면: 에이전트 유형 선택, 패키징, Agent Store 제출, 수익화, 테넌트 롤아웃, Agent 365 거버넌스 | `copilot-agent-store-publish` |

Copilot Chat의 에이전트 선택기에서 에이전트를 선택한 후 아래 프롬프트
중 하나를 붙여넣으세요.

> [!TIP]
> 두 코치 모두 현재 상태를 솔직하게 알려줄 때 가장 잘 작동합니다.
> "프로토타입은 있지만 Partner Center 계정이 없습니다"가 "게시할 준비가
> 되어 있습니다"보다 훨씬 유용한 계획을 만들어 냅니다.

### 코치가 최신 Microsoft 가이드에 근거하도록 유지하기

Marketplace 프로그램, 오퍼 유형, 수수료 비율, Copilot 게시 매트릭스는
자주 변경됩니다. 두 코치 모두 변동성이 큰 사실은 기억이 아니라 Microsoft
Learn 문서를 통해 조회하고, 소스 URL과 조회 날짜를 인용하도록
구성되어 있습니다.

**다음은 항상 검증해야 하며 기억에 의존해서는 안 됩니다:**

| 주제                                                    | 변경되는 이유                                            |
|----------------------------------------------------------|-----------------------------------------------------------|
| Marketplace 수수료 비율 및 수익 공유                      | 오퍼 유형, 프로그램, 파트너 상태에 따라 다름              |
| 어떤 오퍼 유형이 거래 가능하거나 공동 판매 적격인지        | 적격성 규칙이 정기적으로 개정됨                           |
| Copilot 에이전트 게시 매트릭스                            | 가장 변동성이 큰 항목이며 에이전트 유형과 경로에 따라 변경 |
| 매니페스트 및 패키지 스키마 버전                          | 버전이 관리되며 오래된 버전은 더 이상 사용되지 않음        |
| 인증 및 Store 검증 정책                                  | 사전 공지 없이 업데이트됨                                 |
| 지급 시기, 원천징수, 세금 서식                            | 시장에 따라 다르며 정책과 함께 변경됨                     |

> [!WARNING]
> 수수료율, 지급 일정, 프로그램 등록, 오퍼 적격성과 같은 계정별 사항은
> Partner Center가 권위 있는 소스입니다. 고객이나 비즈니스 케이스에
> 숫자를 확정하기 전에 반드시 검토하세요.

### Microsoft Marketplace 트랙

**Microsoft Marketplace Coach**를 선택하고 현재 제품 상태를 하나의
프롬프트로 제공하세요:

```text
Read available BRD, PRD, architecture, and Marketplace planning artifacts in
.copilot-tracking/ folder. We are building product for customers and need to
reach Azure IP Co-sell eligibility in 2 weeks.

Recommend:
1. SaaS, Managed Application, or Azure Container
2. The deployment and publisher-access model
3. The pricing and transaction approach, using the shared product manager
   monetization plan: fixed, hybrid, or consumption; separate public and
   private prices; SMC/SMB self-service checkout; costs, profit, fees, and tax
4. The shortest credible readiness path

State the trade-offs and blockers, then ask me to confirm all decisions
together.
Record confirmed decisions, owners, evidence, and next actions in the canonical
Marketplace plan under .copilot-tracking/details/.
```

Microsoft Marketplace 프롬프트 한글 버전

```text
.copilot-tracking/ 폴더에 있는 BRD, PRD, 아키텍처 및 마켓플레이스 계획 관련 자료를 읽고, 이 애플리케이션/에이전트를 Marketplace 에 Transactable offer 로 등록할 수 있게 가이드 해 주세요.

권장 사항:
1. SaaS, Managed Application 또는 Azure Container
2. 오퍼 배포 및 게시자 액세스 모델
3. 가격 및 거래 방법
    - 수익화 계획 (고정, 하이브리드, 사용량 기반)
    - 가격 : 공개(Public), 비공개(Private)
    - SMC/SMB 셀프 서비스 : 결제, 비용, 수익, 수수료, 세금
4. 가장 빠르고 신뢰할 수 있는 준비 경로

절충 사항과 장애물을 명시한 후, 모든 결정을 함께 확정하도록 요청하세요.
확정된 결정, 담당자, 근거 및 다음 조치를 .copilot-tracking/details/ 폴더의 공식 마켓플레이스 계획에 기록하세요.
```

### Microsoft 365 Copilot 에이전트 트랙

**Copilot Agent Store Coach**를 선택하고 현재 에이전트 상태를 하나의
프롬프트로 제공하세요:

```text
Read our available BRD, PRD, architecture, and Marketplace planning artifacts in
.copilot-tracking/ folder.
We are building copilot agent experience for customers and need to reach
publication in 2 weeks.

Recommend:
1. Declarative agent, custom engine agent, or another supported agent type
2. The backend binding and authentication model
3. The licensing, entitlement, and tenant rollout approach, reconciled with the
   shared monetization plan and Marketplace pricing so agent and backend
   charges are clear and included usage is not billed twice
4. The shortest credible validation and submission path

State the trade-offs and blockers, then ask me to confirm all decisions
together.
Record confirmed decisions, owners, evidence, and next actions in the canonical
agent-store plan under .copilot-tracking/details/.
```

Marketplace - Copilot Agent Store 프롬프트 한글 버전

```text
.copilot-tracking/ 폴더에 있는 BRD, PRD, 아키텍처 및 마켓플레이스 계획 관련 자료를 읽고, 이 애플리케이션/에이전트를 Marketplace 에 Transactable offer 로 등록할 수 있게 가이드 해 주세요.

권장 사항:
1. 에이전트 유형 : Declarative agent, Custom engine agent, 그 외 지원되는 agent type
2. 백엔드 바인딩, 인증 모델
3. 라이선스, 권한 부여, 테넌트 배포 방식 (공유 수익 창출 계획 및 마켓플레이스 가격 책정과 연계하여 에이전트 및 백엔드 요금이 명확하고 포함된 사용량에 대한 이중 청구가 발생하지 않도록 함)
4. 가장 빠르고 신뢰할 수 있는 준비 경로

절충 사항과 장애 요인을 명시한 다음, 모든 결정을 함께 확정하도록 요청하십시오.
확정된 결정, 담당자, 근거 및 다음 조치를 .copilot-tracking/details/ 폴더의 공식 에이전트 저장소 계획에 기록하십시오.
```

> [!IMPORTANT]
> 두 코치 모두 세무, 법률, 재무 조언을 제공하지 않습니다. Microsoft가
> 문서화한 내용을 설명하며, 답변이 귀하의 법인, 관할권, 계약에 따라
> 달라지는 지점에서 멈춥니다. 그러한 질문은 자격을 갖춘 전문가에게
> 전달하고 그 의뢰를 워크샵 작업 항목으로 기록하세요.

## 제품 매니저 상용화 계획

제품 매니저는 재무, 엔지니어링, 파트너 영업, 두 게시 트랙 담당자와
함께 가격 책정을 소유합니다. Marketplace 스킬은 재사용 가능한 비용
체크리스트, 가격 비교, 프라이빗 서비스 범위, 승인 검사를 제공합니다.

하나의 출시 패키지, 사용 가능한 시장 참고 자료를 활용한 제안 가격 범위,
공개 대 비공개 가격, 고정 패키지 대 사용자당 청구(월별 및 연간
조건)를 포함한 MVP 가격 권장안을 준비하려면 다음 프롬프트를
사용하세요.

Marketplace 오퍼를 구성하기 전에 이 단계를 완료하여 제품 매니저가
고객이 무엇을 구매하는지, 무엇을 별도로 지불하는지, 제안된 가격이
비용과 시장 증거로 뒷받침되는지 검토할 수 있도록 하세요. 누락된 비용,
라이선스 요구사항, 승인 사항은 계속 보이도록 유지됩니다. 결과는 승인된
가격표가 아니라 검토를 위한 권장안입니다.

**Microsoft Marketplace Coach**를 선택하고 다음을 붙여넣으세요:

```text
/Microsoft-Marketplace-Publishing 
'MVP commercialization decision mode'를 활용하여, BRD, PRD, 아키텍처 및 게시 관련 결정 사항을 기반으로 공용 솔루션 수익화 계획을 수립하거나 업데이트하십시오.
제품 관리자(PM)가 검토하기 좋도록 간결하게 작성하고, 마켓플레이스 핸드오프(handoff) 단계에서 해당 계획으로 연결되는 링크를 포함하십시오.
계획 수립 단계이며, 실제 게시(publish)는 하지 마십시오.
```

### 에이전트 수익화 조정

에이전트 수익화 조정이란 컴패니언 에이전트의 청구, 라이선스, 유료 접근
규칙을 백엔드 가격 플랜과 비교하여 확인하는 것을 의미합니다. 목표는
하나의 일관된 고객 패키지입니다. 즉, 컴패니언 접근이 포함되어 있는지
아니면 별도로 청구되는지, 고객이 별도로 구매해야 하는 것은 무엇인지,
백엔드 자격이 어떻게 검증되는지를 설명합니다.

이 단계를 사용하여 백엔드 사용량이나 포함된 지원에 대한 이중 청구와
두 게시 트랙 간 상충되는 가격을 방지하세요. 이 프롬프트는 기존 공유
계획을 업데이트하고 미해결 비용, 라이선스 결정, 승인 사항을 식별합니다.
또 다른 가격표를 만들거나 판매 가격을 승인하지는 않습니다.

**Copilot Agent Store Coach**를 선택하고 다음을 붙여넣으세요:

```text
/copilot-agent-store-publish
'Monetization reconciliation workflow'를 사용하여 기존 공유 솔루션 수익화 계획을 업데이트합니다.
에이전트/백엔드 요금 내역 및 승인 차이를 검토를 위해 제시하고 에이전트 스토어 인계에서 링크합니다.
계획 수립 전용이며 게시하지 마십시오.
```

조정 후, 제품 매니저는
`.\.copilot-tracking\details\YYYY-MM-DD\solution-monetization-plan.md`에서
공유 계획을 검토할 수 있습니다. 기존 계획의 날짜 폴더를 사용하거나,
다르다면 코치가 보고한 실제 저장 경로를 사용하고, 그 경로를 검토
요청에 포함하세요. 상업적 구현을 승인하기 전에 패키지, 공개/비공개
가격, 별도 고객 청구, 미해결 승인 공백을 검토하세요.

## 게시 준비 참고 자료

Marketplace FastTrack 코칭 세션을 지원할 참고 가이드는 다음과
같습니다. 솔루션 제출을 성공적으로 완료하기 위해 무엇을 준비해야
하는지에 대한 참고 자료 역할을 합니다. 다음 단계에서는 구현을 위해
상용화 구현 계획을 RPI Agent에 핸드오프합니다.

## Azure Managed Application 경로

### 1단계: 게시자 준비 상태 확인

1. Partner Center에서 게시자 계정을 확인하거나 만드세요.
2. 게시자 확인과 Marketplace 등록을 완료하세요.
3. 법인, 세금, 지급, 지원, 등록 담당자를 확인하세요.
4. 비프로덕션 Azure 구독에 대한 접근 권한을 확인하세요.
5. 필요한 리소스 공급자를 등록하세요.
6. Managed Application 권한 시나리오를 선택하세요.
7. 게시자 아이덴티티와 고객 작업에 최소 권한을 적용하세요.
8. 공유 수익화 워크시트, 공개 및 비공개 가격, 계량형 청구가
   필요한지를 확인하세요.

### 2단계: 패키지 구축 및 검증

1. 패키지를 위한 간단한 작업 폴더를 만들고 시작 전에 파일을
   정리하세요.
2. 앱 서비스, 스토리지 계정, Key Vault, 또는 시나리오에 필요한 기타
   리소스와 같은 최소한의 Azure 리소스를 먼저 정의하세요.
3. 가능하면 원시 ARM JSON보다 읽고 유지보수하기 쉬운 Bicep으로 배포를
   구현하세요.
4. 사용 가능한 Azure 도구로 Bicep을 로컬에서 검증하고, 패키징 전에
   구문 또는 매개변수 문제를 수정하세요.
5. 검증된 Bicep을 Managed Application 패키지를 위한 ARM 템플릿
   JSON으로 내보내거나 변환하세요.
6. 배포 템플릿의 이름을 `mainTemplate.json`으로 지정하고 지원되는 ARM
   템플릿 언어 버전 1.0을 유지하세요.
7. 포털에서 배포 값을 입력하기 위한 안내 경험을 제공하도록
   `createUiDefinition.json`을 만드세요.
8. `createUiDefinition.json`의 모든 UI 필드를 `mainTemplate.json`의
   매개변수에 매핑하여 포털과 템플릿이 동기화되도록 하세요.
9. 패키지 구조를 손상시킬 수 있는 추가 중첩 없이 두 파일을 모두
   `app.zip`의 루트에 배치하세요.
10. 아무것도 업로드하기 전에 ARM 템플릿과 패키지 구조를 검증하세요.
11. CreateUiDefinition 샌드박스에서 샘플 값으로 포털 경험을 테스트하여
    UI가 올바르게 동작하는지 확인하세요.
12. 비밀 정보, 취약점, RBAC, 네트워크 노출, 데이터 처리, 진단, 할당량,
    비용을 검토하세요.
13. 패키지를 비프로덕션 구독에 배포하고 배포가 성공하는지
    확인하세요.
14. 고객 경험 관점에서 생성, 업데이트, 장애 복구, 지원 접근, 삭제를
    테스트하세요.
15. 검증 중 발견된 문제를 기록하고 오퍼 제출 전에 수정하세요.

### 3단계: Marketplace 오퍼 생성

1. [Partner Center](https://partner.microsoft.com/dashboard/home)에
   로그인하세요.
2. **Marketplace offers**를 여세요.
3. **New offer**를 선택한 후 **Azure Application**을 선택하세요.
4. 영구적이고 고유한 오퍼 ID를 입력하세요.
5. 확인된 게시자 계정을 선택하세요.
6. 오퍼 설정, 속성, 카테고리, 법적 조건, 계약을 완료하세요.
7. 리스팅 콘텐츠, 검색어, 이미지, 지원, 개인정보 보호, 문서 링크를
   완료하세요.
8. 통제된 테스트 계정을 사용하여 미리보기 대상을 추가하세요.
9. 플랜을 만들고 적절한 Azure Application 플랜 유형을 선택하세요.
10. 검증된 Managed Application 패키지를 업로드하세요.
11. 초안을 저장하고 검증 오류를 해결하세요.

### 4단계: 미리보기, 인증, 출시

1. 오퍼를 미리보기에 제출하세요.
2. 검증 및 인증 피드백을 해결하세요.
3. 미리보기 사용자에게 깨끗한 테스트 구독에 오퍼를 배포하도록
   요청하세요.
4. 고객 관점에서 배포, 청구, 아이덴티티, 텔레메트리, 지원, 업그레이드,
   삭제를 검증하세요.
5. 보안, 개인정보 보호, 접근성, 법무, 지원, 비즈니스 담당자의 승인을
   받으세요.
6. 인증이 완료되면 오퍼를 공개하세요.

## Microsoft 365 Copilot 에이전트 경로

### 1단계: 오퍼 상용화

1. Microsoft Marketplace를 대상으로 할 수 있는 패키징된 선언적
   에이전트 또는 커스텀 엔진 에이전트를 위해 **Microsoft 365 Agents
   Toolkit**을 선택하세요.
2. 유료 백엔드 접근, 별도 라이선스 전제 조건, 공개 또는 비공개 구매
   경로를 포함하여 공유 수익화 워크시트를 Marketplace 트랙과
   조정하세요.

> [!NOTE]
> 지원 여부는 에이전트 유형과 경로에 따라 다르므로, 구현 전에 현재
> [Microsoft 365 Copilot 게시 매트릭스](https://learn.microsoft.com/microsoft-365-copilot/extensibility/publish)를
> 확인하세요.

### 2단계: 에이전트 구축 및 테스트

1. 선택한 도구에서 에이전트를 만드세요.
2. 검토된 이름, 설명, 지침, 대화 시작 문구, 승인된 지식 소스를
   추가하세요.
3. 인증된 API 또는 지원되는 작업을 통해 Azure 애플리케이션을
   연결하세요.
4. 최소 권한 원칙에 따라 위임된 또는 애플리케이션 권한을
   적용하세요.
5. 에이전트 프롬프트뿐만 아니라 Azure 서비스에서도 권한 부여 검사를
   추가하세요.
6. 인용, 불확실성 동작, 피드백, 사람의 개입(에스컬레이션)을
   추가하세요.
7. Agents Toolkit을 사용할 때 Microsoft 365 앱 패키지, 매니페스트,
   아이콘, 필수 파일을 준비하세요.
8. 매니페스트와 책임 있는 AI 검증을 실행하세요.
9. 관리자 승인을 받아 테스트 테넌트에 사이드로드하세요.
10. 예상된 프롬프트, 금지된 프롬프트, 무단 접근, 누락된 콘텐츠, 종속성
    장애, 프롬프트 인젝션, 유해한 출력 처리를 테스트하세요.
11. 보안, 개인정보 보호, 접근성, 책임 있는 AI, 지원 검토를
    완료하세요.

### 3단계: Microsoft Marketplace를 통한 게시

1. 에이전트 유형이 상업적 마켓플레이스 제출을 지원하는지
   확인하세요.
2. 확인된 Partner Center 게시자를 **Microsoft 365 and Copilot** 프로그램에
   등록하세요.
3. Microsoft Commercial Marketplace 인증 정책을 검토하세요.
4. 에이전트를 위한 Microsoft 365 Store 검증 가이드라인을
   검토하세요.
5. 책임 있는 AI 검증 검사를 완료하세요.
6. 고객 대상 설명, 아이콘, 개인정보 보호 정책, 약관, 지원, 설정 지침,
   필요시 테스트 자격 증명을 준비하세요.
7. Partner Center에서 **Apps and agents for Microsoft 365 and Copilot**
   오퍼 유형을 만드세요.
8. 검증된 Microsoft 365 앱 패키지를 업로드하세요.
9. 오퍼를 검증에 제출하고 인증 발견 사항을 해결하세요.

## 다음 단계
[**구현 및 상용화로의 핸드오프**](partner-workshop-implementation.md)를 진행하세요.

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
