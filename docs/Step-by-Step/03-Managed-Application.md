# 03. Azure Managed Application 패키징과 배포

## 1. 목표

고객이 Marketplace(또는 서비스 카탈로그)에서 한 번 배포하면 고객 구독에 전체 스택이 생성되고, 퍼블리셔는 **관리 리소스 그룹**만 운영한다.

## 2. 패키지 구성

```text
managed-app/
  mainTemplate.bicep        # 진입점 (ARM으로 컴파일해 mainTemplate.json 생성)
  createUiDefinition.json   # 배포 마법사
  modules/
    network.bicep           # VNet, Private Endpoint, Private DNS
    data.bicep              # SQL, Storage(ADLS), AI Search
    ai.bicep                # Azure OpenAI 배포
    compute.bicep           # Container Apps Environment, APIM
    security.bicep          # Key Vault, Managed Identity, 역할 할당
    monitor.bicep           # Log Analytics, App Insights, 진단 설정, 불변 Storage
  viewDefinition.json       # (선택) 고객 포털 뷰
```

빌드: `bicep build mainTemplate.bicep --outfile mainTemplate.json` 후 `createUiDefinition.json`과 함께 zip.

## 3. mainTemplate.bicep 뼈대

```bicep
targetScope = 'resourceGroup'

@description('고객 구분용 짧은 이름')
@minLength(3)
@maxLength(8)
param customerCode string
param location string = resourceGroup().location
@description('Entra 앱(클라이언트) ID: 관리자 동의 후 입력')
param apiClientId string

var suffix = uniqueString(resourceGroup().id)

module network 'modules/network.bicep' = {
  name: 'network'
  params: { location: location, customerCode: customerCode }
}

module security 'modules/security.bicep' = {
  name: 'security'
  params: { location: location, suffix: suffix, subnetId: network.outputs.privateEndpointSubnetId }
}

module data 'modules/data.bicep' = {
  name: 'data'
  params: {
    location: location
    suffix: suffix
    subnetId: network.outputs.privateEndpointSubnetId
    identityPrincipalId: security.outputs.apiIdentityPrincipalId
  }
}

module ai 'modules/ai.bicep' = {
  name: 'ai'
  params: {
    location: location
    suffix: suffix
    subnetId: network.outputs.privateEndpointSubnetId
    identityPrincipalId: security.outputs.apiIdentityPrincipalId
  }
}

module monitor 'modules/monitor.bicep' = {
  name: 'monitor'
  params: { location: location, suffix: suffix }
}

module compute 'modules/compute.bicep' = {
  name: 'compute'
  params: {
    location: location
    suffix: suffix
    apiClientId: apiClientId
    identityId: security.outputs.apiIdentityId
    logAnalyticsId: monitor.outputs.workspaceId
    keyVaultUri: security.outputs.keyVaultUri
    searchEndpoint: data.outputs.searchEndpoint
    openAiEndpoint: ai.outputs.endpoint
  }
}

output apiUrl string = compute.outputs.apiUrl
```

## 4. 핵심 모듈 규칙

### 4.1 data.bicep (필수 설정)

```bicep
resource search 'Microsoft.Search/searchServices@2024-06-01-preview' = {
  name: 'srch-${suffix}'
  location: location
  sku: { name: 'standard' }
  properties: {
    publicNetworkAccess: 'disabled'
    disableLocalAuth: true            // 키 인증 금지, RBAC만
    authOptions: null
    replicaCount: 2
  }
}

resource sql 'Microsoft.Sql/servers@2023-08-01-preview' = {
  name: 'sql-${suffix}'
  location: location
  properties: {
    publicNetworkAccess: 'Disabled'
    minimalTlsVersion: '1.2'
    administrators: { azureADOnlyAuthentication: true, administratorType: 'ActiveDirectory' }
  }
}
```

### 4.2 ai.bicep (학습 미사용 통제)

```bicep
resource aoai 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: 'aoai-${suffix}'
  location: location
  kind: 'OpenAI'
  sku: { name: 'S0' }
  properties: {
    customSubDomainName: 'aoai-${suffix}'
    publicNetworkAccess: 'Disabled'
    disableLocalAuth: true
  }
}
```

* Azure OpenAI는 고객 프롬프트와 완성을 모델 학습에 사용하지 않는다(서비스 약정). 추가로 **파인튜닝 배포를 하지 않으며** Azure Policy로 `fineTuning` 사용을 거부한다. 남용 모니터링(abuse monitoring) 데이터 저장 옵트아웃은 고객 요청 승인 절차가 필요하므로 [06](06-AI-Safeguards.md)에 기록한다.

### 4.3 security.bicep

* 사용자 할당 Managed Identity 1개(API용), 수집용 1개 분리(최소 권한).
* Key Vault: RBAC 모델, 퍼지 보호, soft delete, Private Endpoint.
* 역할 할당: API → Search Index Data Reader, SQL(Entra 사용자로 생성), Cognitive Services OpenAI User. 수집 → Search Index Data Contributor.

## 5. 퍼블리셔/고객 경계

| 항목 | 설정 |
|---|---|
| 잠금 수준 | `ReadOnly` 거부 할당으로 관리 RG 보호 |
| 퍼블리셔 권한 | 관리 RG 에 `Contributor`만. 고객 RG 데이터 평면 권한 없음 |
| 지원 접근 | Azure Lighthouse 또는 JIT, 고객 승인, 세션 로그 |
| 업데이트 | Managed App 새 버전 게시, 고객이 승인 후 적용 |

## 6. createUiDefinition.json 입력 항목

고객 코드, 리전(허용 리전 제한), 네트워크 주소 공간, Entra 앱 클라이언트 ID(동의 완료), 로그 보존 일수, 알림 이메일.

## 7. 구현 체크리스트

- [ ] `bicep build`, `bicep lint` 오류 0
- [ ] `az deployment group what-if` 로 사전 확인
- [ ] 서비스 카탈로그 Managed App 으로 테스트 구독 배포 성공
- [ ] 공용 네트워크 접근이 모두 비활성 (Azure Policy 준수 확인)
- [ ] 퍼블리셔 계정으로 고객 RG 데이터 접근 시도가 거부됨

## 8. 리뷰 포인트

| 질문 | 기대 |
|---|---|
| 데이터가 퍼블리셔 테넌트로 나가는 경로가 있는가 | 없어야 함(텔레메트리는 비식별 운영 지표만) |
| 키/비밀이 템플릿 출력에 노출되는가 | 아니오 (`@secure()` 사용, Key Vault 참조) |
| 리전 고정이 가능한가 | `allowedValues` 로 제한 |
