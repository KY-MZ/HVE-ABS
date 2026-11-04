---
type: publishing
status: draft
evidence: documented
updated: 2026-11-03
---

# 게시 경로 비교

> 정책 매트릭스는 바뀔 수 있다. 문서도 "현재 Microsoft 가이드가 지원되는 경로를 확인할 때까지 모든 상업 경로, 오퍼 유형, 추가 기능 제한을 검증 항목으로 취급"하라고 한다. 수수료, 지급, 적격성은 Partner Center가 권위 소스다.

| 항목 | Azure Managed Application | Microsoft 365 Copilot 에이전트 |
|---|---|---|
| 오퍼 유형 | Azure Application | Apps and agents for Microsoft 365 and Copilot |
| 배포 모델 | 고객 구독에 리소스 배포 | 선언형 또는 커스텀 엔진 에이전트 |
| 패키지 | Bicep→ARM, `mainTemplate.json` + `createUiDefinition.json` → `app.zip` | 매니페스트, 인증된 API 연결 |
| 사전 준비 | Partner Center, 게시자 확인, 법인·세금·지급, 비프로덕션 구독, RP 등록 | Microsoft 365 and Copilot 프로그램 등록 |
| 테스트 | 샌드박스, 보안·RBAC·비용 검토, 비프로덕션 배포·수명주기 | 테스트 테넌트 사이드로드, RAI 검증, 프롬프트 인젝션 시나리오 |
| 심사 | 미리보기→인증 피드백→테스트 구독→승인 후 공개 | 인증 정책, Store 검증 가이드라인 |
| 위험 초점 | RBAC, 비용, 배포 수명주기 | 최소 권한, 동의 경계, 테넌트 관리자 승인, 인용·에스컬레이션 |

## 상업 체크리스트 (Documented)
브랜드·가치 제안, 초기 지역·대상·컴플라이언스, 상용화 계획(가격/청구/비용/세금 가정 일치), Lean Canvas, Partner Center 체크리스트, 에이전트와 백엔드 요금 조정(이중 청구 방지), 담당자 지정(엔지니어링·제품·보안·운영)

## 제출 주제가 닿는 지점 (Inference)
- 안 A(읽기 전용 평가): 에이전트 경로의 최소 권한 요건과 잘 맞음
- 안 B(승인 기반 적용): 두 경로 모두에서 동의·권한·롤백 요건이 큼
- 로컬 Playwright 하네스 그대로는 두 경로 어디에도 직접 대응하지 않음 → 포장 방식 결정이 첫 번째 열린 질문

## 열린 질문
1. 두 경로 중 어느 쪽을 1차 목표로 할 것인가
2. 브라우저 자동화가 서비스 약관·게시 정책상 허용되는가 (미확인)
3. 가격 구조 (공개가/비공개가, 고정/사용자당)

---

## 업데이트 2026-11-03: 범주 확정
Publishing 범주는 **Microsoft 365 Copilot**으로 확정되었다 ([[Decision-001-Publishing-Category]]). 위 비교표의 Azure Managed Application 열은 대안으로만 남긴다. 상세 분석은 [[M365-Copilot-Path-Analysis]].
