# 10. 로드맵과 추적

구현 진행은 저장소 루트 [dashboard.html](../../dashboard.html)에서 GitHub Milestone/Issue로 추적한다. 데이터 원본은 [dashboard-data.json](../../dashboard-data.json)(오프라인 기본값)이며, 같은 항목을 `scripts/create-github-backlog.sh` 로 GitHub에 생성할 수 있다.

## 마일스톤

| M | 이름 | 산출물 | 완료 기준 |
|---|---|---|---|
| M1 | 기반과 배포 | Bicep 모듈, Managed App 패키지 | 테스트 구독 배포 성공, 정책 준수 |
| M2 | 신원과 접근 통제 | OBO, ACL 테이블/동기화, 검색 필터 | 교차 계정 테스트 통과 |
| M3 | 수집과 검색 | 4개 소스 수집, 인덱스 | 필수 필드/ACL 100% |
| M4 | AI와 인사이트 | 점수 엔진, 프롬프트, 인용 검증 | 평가 게이트 통과 |
| M5 | 에이전트와 API | OpenAPI, Declarative agent | Copilot 에서 E2E |
| M6 | 감사와 운영 | 로그, KQL, 불변 보존, 알림 | 증거 패키지 생성 |
| M7 | 검증과 출시 | 보안 리뷰, 부하, 문서, Marketplace | 게이트 체크리스트 완료 |

## 이슈 백로그

이슈 정의는 [dashboard-data.json](../../dashboard-data.json)의 `issues` 배열이 기준이다. 라벨: `area:*`, `priority:P0|P1|P2`.
