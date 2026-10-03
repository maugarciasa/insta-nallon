#!/usr/bin/env bash
# Copia as skills próprias de .claude/skills (oficiais) para .agents/skills (Codex).
# Rode depois de editar qualquer arquivo delas: bash sincronizar-skills.sh
set -euo pipefail
cd "$(dirname "$0")"
for s in brag-instagram reels-nallon; do
  cp -r ".claude/skills/$s/." ".agents/skills/$s/"
done
sed -i 's#~/\.claude/#~/.Codex/#g' .agents/skills/brag-instagram/SKILL.md
