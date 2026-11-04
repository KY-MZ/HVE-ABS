#!/usr/bin/env bash
# dashboard-data.json 의 마일스톤과 이슈를 GitHub 에 생성한다. 이미 있는 제목은 건너뛴다.
# 사용: scripts/create-github-backlog.sh [--dry-run]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/dashboard-data.json"
DRY="${1:-}"
REPO="$(jq -r .repo "$DATA")"

run() { if [[ "$DRY" == "--dry-run" ]]; then echo "[dry-run] $*"; else "$@"; fi; }

existing_ms="$(gh api "repos/$REPO/milestones?state=all&per_page=100" --jq '.[].title')"
while IFS= read -r row; do
  title="$(jq -r .title <<<"$row")"
  desc="$(jq -r .description <<<"$row")"
  grep -qxF "$title" <<<"$existing_ms" || run gh api "repos/$REPO/milestones" -f title="$title" -f description="$desc" >/dev/null
done < <(jq -c '.milestones[]' "$DATA")

existing_issues="$(gh issue list -R "$REPO" --state all --limit 500 --json title --jq '.[].title')"
while IFS= read -r row; do
  title="$(jq -r .title <<<"$row")"
  grep -qxF "$title" <<<"$existing_issues" && continue
  mid="$(jq -r .milestone <<<"$row")"
  ms="$(jq -r --arg id "$mid" '.milestones[] | select(.id==$id) | .title' "$DATA")"
  doc="$(jq -r .doc <<<"$row")"
  args=()
  while IFS= read -r l; do
    run gh label create "$l" -R "$REPO" --force >/dev/null 2>&1 || true
    args+=(--label "$l")
  done < <(jq -r '.labels[]' <<<"$row")
  run gh issue create -R "$REPO" --title "$title" --milestone "$ms" "${args[@]}" \
    --body "설계 문서: docs/Step-by-Step/ 의 ${doc}번 문서를 따른다. 완료 기준은 해당 문서의 체크리스트와 리뷰 포인트."
done < <(jq -c '.issues[]' "$DATA")
