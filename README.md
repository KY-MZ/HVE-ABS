## Hypervelocity Innovation
### 혁신에서 마켓플레이스까지, 가속화된 여정

Hypervelocity Innovation은 팀이 리서치와 발견을 가치 있는 솔루션, 마켓플레이스 및 Copilot 에이전틱 IP 수익화, 그리고 속도·품질·보안을 갖춘 게시로 전환하도록 돕는 엔드투엔드 작업 방식입니다.

Design Thinking은 실제 사용자의 니즈를 발견하고, 의미 있는 문제를 재구성하며, 익숙한 답을 넘어선 가능성을 탐색할 공간을 만들어 혁신을 가능하게 합니다. 사용자와 함께 솔루션을 구체화하고 테스트함으로써 통찰을 바람직하고(desirable), 실현 가능하며(feasible), 가치 있는(valuable) 결과로 전환합니다. Hypervelocity Engineering(HVE)은 발견(discovery)을 요구사항, 계획, 구현, 리뷰로 연결하여 증거와 의도를 잃지 않으면서 이 작업을 가속화합니다.

제품 사고, 디자인 씽킹, 엔지니어링 실행, AI 지원 전달부터 Microsoft Marketplace 또는 Copilot Agent Store에서의 혁신 수익화까지, 반복 가능한 혁신 사이클을 운영하고 싶을 때 이 저장소를 사용하세요.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/b3827389-459e-477b-a6bc-15cf6d7053d0" />

> [!TIP]
> 이 가이드와 저장소가 도움이 되었다면, GitHub에서 **이 저장소에 star(즐겨찾기)를 눌러주세요**! Star는 커뮤니티를 성장시키고 연결을 유지하며, 도구·에이전트·워크샵 자료에 대한 지속적인 업데이트를 제공하는 데 도움이 됩니다.

## RM Intelligence Experience 아키텍처

* 단계별 아키텍처 가이드: [docs/Step-by-Step/00-Overview.md](docs/Step-by-Step/00-Overview.md)
* 구현 대시보드(Issue/Milestone 추적): [dashboard.html](dashboard.html), 데이터는 [dashboard-data.json](dashboard-data.json)
* 백로그 생성: `scripts/create-github-backlog.sh [--dry-run]`

## HVE가 혁신을 가속화하는 방법

HVE는 Hypervelocity Innovation 내부의 가속화 레이어입니다. 팀이 빠르게 움직이면서도 사람들이 사용할 수 있고, 조직이 운영할 수 있으며, 책임감 있게 게시하거나 수익화할 수 있는 솔루션을 구축하는 데 필요한 품질을 유지하도록 돕습니다.

다음을 연결합니다:

* 리서치 중심의 의사결정 품질
* 실제 사용자 니즈를 중심으로 한 AI Discovery 및 Design Thinking
* 구조화된 요구사항(BRD 및 PRD)
* 마일스톤 계획 및 백로그 작성
* 반복적인 구현 및 리뷰 루프
* 솔루션의 게시 준비(Publication readiness)

HVE Core는 이 혁신 사이클을 일관되게 실행할 수 있는 도구, 프롬프트, 에이전트, 검증 규칙을 제공합니다.

팀이 핸드오프 손실과 의사결정 모호성을 줄이면서 사용자와 성과를 중심에 두면 혁신은 가속화됩니다.

HVE는 다음을 통해 통찰에서 임팩트로 가는 경로를 단축합니다:

* 발견(discovery) 결과물을 구현 준비가 된 산출물로 전환
* RPI(Research, Plan, Implement, Review)를 통해 모든 마일스톤을 증거에 기반하도록 유지
* 제품, 디자인, 아키텍처, 엔지니어링을 동일한 산출물 흐름(artifact trail)으로 정렬
* 매번 프로세스를 다시 만드는 대신 검증된 템플릿과 자동화를 재사용

## Hypervelocity Innovation 시작하기

[Hypervelocity Innovation 파트너 워크샵](docs/getting-started/partner-workshop.md)은 팀을 공유된 문제에서 요구사항, 백로그, 아키텍처, 구현, 게시 산출물이 연결된 상태로 안내합니다.

1. 개요
  * 성과, 샘플 시나리오 또는 고객 문제, 팀 역할, 팀이 만들 산출물에 대해 합의합니다.
2. 공유 설정
  * [파트너 워크샵 설정](docs/getting-started/partner-workshop-setup.md)을 완료하여 팀이 HVE Core와 GitHub Copilot으로 하나의 프로젝트에서 작업할 수 있도록 합니다.
3. 역할별 트랙: 리서치, 계획, 구상, 경험, 아키텍처 설계, 백로그
  * 리서치와 도메인 맥락부터 시작한 다음, 기회와 원하는 성과를 구체화합니다.
  * AI Discovery Cards 활동을 포함한 디자인 씽킹과 사용자 리서치를 활용해 니즈를 이해하고 경험을 구체화합니다.
  * BRD 및 PRD 방향을 작성하고, 수용 기준(acceptance criteria)을 식별하며, 솔루션을 우선순위가 지정된 백로그로 전환합니다.
  * 제품 방향이 구체화되는 동안 기술 아키텍처와 게시 관련 고려사항을 병행하여 개발합니다.
  * [파트너 워크샵 역할 트랙](docs/getting-started/partner-workshop-role-tracks.md)을 따르고, [DT to RPI Integration](docs/design-thinking/dt-rpi-integration.md)을 통해 디자인 산출물을 엔지니어링과 연결합니다.
4. 검증 및 솔루션 통합
  * [파트너 워크샵 솔루션](docs/getting-started/partner-workshop-solution.md)에서 역할별 산출물을 통합하고, 모순을 해결하며, 추적성(traceability)을 검토하고, 위험을 식별하며, 첫 구현 범위에 합의합니다.
5. 마켓플레이스 및 Copilot Agent Store 준비
  * [파트너 워크샵 게시](docs/getting-started/partner-workshop-publishing.md)에서 제품, 소유권, 통합 계약, 상업적 경로, 미해결 게이트를 정의합니다.
6. 구현 및 상업화
  * [파트너 워크샵 구현](docs/getting-started/partner-workshop-implementation.md)에서 승인된 워크샵 산출물을 증거 기반 전달 계획으로 전환하고, RPI로 실행하며, 구현 및 IP 수익화 경로를 준비합니다.

워크샵은 더 넓은 운영 모델로 들어가는 입구입니다. 세션 이후에는 [RPI Workflow](docs/rpi/README.md)를 사용하여 남은 격차를 조사하고, 좁은 마일스톤을 계획하며, 구현하고, 범위를 확장하기 전에 증거를 검토하세요.

## 새로운 업무 방식

Hypervelocity Innovation을 도입하는 팀이라면 역할의 명확성과 빠른 피드백 사이클부터 시작하세요.

* [HVE Guide Roles](docs/hve-guide/roles/README.md)의 역할 트랙을 중심으로 팀을 구성하세요.
* [Business Program Manager](docs/hve-guide/roles/business-program-manager.md)에서 비즈니스 및 전달 소유권부터 시작하세요.
* [Engineer Guide](docs/hve-guide/roles/engineer.md)로 구현 소유권을 고정하세요.
* [Team Adoption Guide](docs/customization/team-adoption.md)를 사용하여 온보딩 및 실행 기대치를 표준화하세요.

## 팀 준비 상태 및 변화 관리

Hypervelocity Innovation은 팀이 의사결정을 내리고, 맥락을 기록하고, 아이디어에서 전달까지 나아가는 방식을 바꿉니다. 도입을 단순한 도구 적용이 아니라 변화 관리(change-management) 노력으로 다루세요.

### HVE 도입 고려사항

* **가시적인 스폰서십:** 책임 있는 스폰서가 시간을 보호하고, 우선순위 충돌을 해결하며, 첫 마일스톤을 승인하여 워크샵이 실제 전달로 이어지도록 합니다.
* **완전한 관점:** 비즈니스 오너, 주제 전문가(SME), 디자이너, 기술 오너를 포함하여 팀이 함께 충분한 정보를 바탕으로 의사결정할 수 있도록 합니다.
* **명확한 의사결정 권한:** 문제 정의, 요구사항, 아키텍처 방향, 백로그 우선순위, 게시 경로를 누가 승인하는지 명시합니다.
* **하나의 저장소, 다양한 대상:** 읽기 쉬운 워크샵 산출물과 구현 코드를 분리하고, 폴더와 템플릿을 명확히 하며, 리뷰 권한에 합의하면 비기술 참여자와 기술 참여자가 같은 저장소에서 작업할 수 있습니다. Markdown 문서, 다이어그램, 요구사항, 백로그 계획은 모든 참여자가 접근하기 쉬워야 하며, 소스 코드와 배포 변경은 일반적인 엔지니어링 리뷰 게이트를 사용해야 합니다.
* **집중된 엔지니어링 참여:** 핵심 워크샵 그룹은 작게 유지하면서, 솔루션이 명확해짐에 따라 추가 엔지니어와 전문가를 타깃 리뷰에 참여시키세요. 조율, 상충되는 접근 방식, 커뮤니케이션 격차가 전달되는 작업보다 커지면 엔지니어를 늘리는 것이 오히려 속도를 떨어뜨릴 수 있습니다. 명확한 소유권, 작은 작업 그룹, 공유된 의사결정, 짧은 피드백 루프, 합의된 충돌 해결 경로로 추진력을 유지하세요.
* **소유된 후속 조치:** 모든 미해결 가정, 의사결정, 게시 게이트, 백로그 항목에 담당자와 다음 검토일을 지정합니다.

### 권장 팀 구성

워크샵과 첫 솔루션 범위에는 **핵심 인원 4~6명**으로 시작하세요. 소규모 팀에서는 한 사람이 둘 이상의 역할을 맡을 수 있지만, 각 책임은 여전히 명시적이어야 합니다.

| 역할 | 주요 책임 |
|------|------------------------|
| 스폰서 또는 책임 있는 제품 오너 | 성과를 설정하고, 역량(capacity)을 보호하며, 우선순위 충돌을 해결하고, 첫 마일스톤을 승인 |
| 퍼실리테이터 또는 프로젝트 매니저 | 워크샵 순서를 운영하고, 의사결정을 유지하며, 백로그를 조율하고, 후속 조치를 추적 |
| 주제 전문가(SME) | 도메인 사실, 사용자 맥락, 제약사항, 용어, 증거를 제공 |
| 디자이너 또는 리서처 | 사용자 리서치, 디자인 씽킹, AI Discovery Cards, 여정(journey), 접근성, 경험 관련 의사결정을 주도 |
| 테크니컬 리드 또는 아키텍트 | 솔루션, 아키텍처, 보안, 통합, 운영 제약사항을 구체화 |
| 엔지니어 또는 포워드 디플로이드 빌더 | 실현 가능성을 테스트하고, 첫 구현 슬라이스의 규모를 산정하며, 승인된 계획을 동작하는 소프트웨어로 전환 |

소규모 아이디어 팀이라면 스폰서와 프로젝트 매니저를 결합하거나, 테크니컬 리드와 엔지니어를 결합하세요. 의사결정에 필요할 때는 보안, 개인정보보호, 데이터, 플랫폼, 재무, 법무, 또는 상업화 전문가를 **파트타임 리뷰어**로 추가하세요. 모든 전문가를 상시 워크샵 참여자로 만들 필요는 없습니다.

목표는 문제와 전달 환경을 대표할 만큼 충분히 크면서도, 현장에서 의사결정을 내릴 수 있을 만큼 작은 팀을 구성하는 것입니다. 세션 전에 소유권을 배정하려면 [파트너 워크샵 역할 트랙](docs/getting-started/partner-workshop-role-tracks.md)을, 구현 전에 격차를 확인하려면 [파트너 워크샵 솔루션](docs/getting-started/partner-workshop-solution.md)을 사용하세요.

## 빠르고 반복적인 솔루션 전달

예상되는 운영 패턴은 빠른 마일스톤 기반 전달입니다:

* 불확실성을 줄이기 위한 리서치
* 각 마일스톤을 위한 좁은 범위 계획
* 명확한 품질 게이트를 갖춘 구현
* 리뷰 및 후속 조치 라우팅

[RPI Workflow](docs/rpi/README.md)로 이 과정을 반복적으로 실행하고, [파트너 워크샵 솔루션](docs/getting-started/partner-workshop-solution.md)을 사용하여 확장하세요.

## 자체 IP 게시 및 수익화

이 프레임워크는 재사용 가능한 IP와 기능을 수익화하고 게시하려는 팀을 지원합니다.

* [파트너 워크샵 게시](docs/getting-started/partner-workshop-publishing.md)를 사용하여 게시 준비(publication readiness)를 준비하세요.

## 책임감 있는 AI(Responsible AI)

Microsoft는 고객이 AI 지원 시스템을 개발할 때 윤리적이고 안전하며 포용적인 AI 관행을 보장하기 위해 Responsible AI Standard를 검토할 것을 권장합니다. 자세한 내용은 [Microsoft's Responsible AI](https://www.microsoft.com/ai/responsible-ai)에서 확인하세요.

> [!CAUTION]
> HVE Core는 매우 주관적이고 빠르게 진화하는 에이전틱 SDLC 프레임워크입니다. 안정적인 플랫폼, 기반, 또는 프로덕션 의존성이 아니라 패턴과 학습의 원천으로 다루는 것이 가장 좋습니다.
> 기술 환경이 진화함에 따라 워크플로, 인터페이스, 아키텍처, 권장 관행은 하위 호환되지 않는 방식을 포함하여 크게 변경될 수 있습니다. 모든 자료를 자신의 요구사항과 위험 허용 범위에 맞춰 평가하세요.
> HVE Builder 스킬(`/hve-builder`로 사용)과 GitHub Copilot은 여러분이 독립적으로 소유하고 유지하는 에이전틱 SDLC에 관련 패턴을 적용하거나 복사하는 데 도움을 줄 수 있습니다.
> 독립적인 구현을 만들려면 [Forking and Extending HVE Core](docs/customization/forking.md)부터 시작하고, 어떤 구성 요소든 도입하기 전에 [HVE Core documentation](docs/README.md)을 검토하세요.

## 법적 고지

이 프로젝트는 [MIT License](./LICENSE)에 따라 라이선스가 부여됩니다.

## 상표 고지

> 이 프로젝트에는 프로젝트, 제품 또는 서비스에 대한 상표나 로고가 포함될 수 있습니다. Microsoft 상표 또는 로고의 승인된 사용은
> Microsoft의 상표 및 브랜드 가이드라인을 따라야 합니다. 이 프로젝트의 수정된 버전에서 Microsoft 상표 또는 로고를 사용할 때는
> 혼동을 일으키거나 Microsoft의 후원을 암시해서는 안 됩니다. 타사 상표나 로고의 사용은 해당 타사의 정책을 따릅니다.

---

## 워크샵 시작
[Hypervelocity Innovation 파트너 워크샵](docs/getting-started/partner-workshop.md)

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
