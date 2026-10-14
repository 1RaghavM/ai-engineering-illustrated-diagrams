#!/usr/bin/env bash
# Copy *-final.png diagrams from the newsletter workspace into images/<issue-slug>/
# and regenerate README.md. Usage: ./update.sh [newsletter_dir]
set -euo pipefail
SRC="${1:-/workspace/newsletter}"
cd "$(dirname "$0")"
declare -A SLUG=( [001]=code-sandboxes [002]=model-context-protocol [003]=llm-inference-serving [004]=computer-use-agents [005]=agent-harness [006]=tokenizers [007]=cursor-multi-agent )
for d in "$SRC"/issue-*/; do
  n=$(basename "$d"); n=${n#issue-}
  slug=${SLUG[$n]:-issue-$n}   # add new issues to SLUG above
  for f in "$d"*-final.png; do
    [ -e "$f" ] || continue
    name=$(basename "$f" -final.png); name=${name#fig[0-9]-}; name=${name#fig[0-9][0-9]-}
    mkdir -p "images/$slug"
    cp -u "$f" "images/$slug/$name.png"
  done
done
python3 gen_readme.py "$SRC"
echo "Updated. Review with: git status"
