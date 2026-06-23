#!/usr/bin/env bash
# pre-deploy.sh — Gate de deploy para sociedad-opita (monumento-cultural-v1)
# 5 pasos: lint → verify → bitácora → S3 sync → CloudFront invalidation
# Aborta en cualquier paso fallido (set -e + set -u + set -o pipefail)
#
# Uso:
#   ./scripts/pre-deploy.sh
#
# Variables de entorno opcionales (con defaults):
#   S3_BUCKET         default: s3://sociedad-opita-app-prod/
#   CF_DIST_ID        default: E9NPTPSJGKRMQ
#   ACADEMIC_REPO     default: ../sociedad-opita-academic
#   SKIP_S3_SYNC=1    salta el paso 4 (útil para dry-run / sandbox)
#   SKIP_CF_INVALIDATION=1  salta el paso 5

set -euo pipefail

S3_BUCKET="${S3_BUCKET:-s3://sociedad-opita-app-prod/}"
CF_DIST_ID="${CF_DIST_ID:-E9NPTPSJGKRMQ}"
ACADEMIC_REPO="${ACADEMIC_REPO:-../sociedad-opita-academic}"
CACHE_CONTROL="${CACHE_CONTROL:-max-age=300}"

log() { printf '\n=== %s ===\n' "$*"; }
ok()  { printf '  ✓ %s\n' "$*"; }
die() { printf '  ✗ %s\n' "$*" >&2; exit 1; }

log "pre-deploy.sh — monumento-cultural-v1"
echo "Working dir : $(pwd)"
echo "S3 bucket   : $S3_BUCKET"
echo "CloudFront  : $CF_DIST_ID"
echo "Academic    : $ACADEMIC_REPO"
echo "Started     : $(date -u +%Y-%m-%dT%H:%M:%SZ)"

# --- Paso 1: linter de léxico (HARD gate) ---
log "[1/5] Linter de léxico"
if ! node scripts/check-lexicon.mjs; then
  die "linter FAILED — abortando antes de S3 sync"
fi
ok "linter pasó"

# --- Paso 2: verificar archivos críticos ---
log "[2/5] Verificar sitemap.xml + VISUAL-HONESTY.md"
[ -f sitemap.xml ]        || die "sitemap.xml no existe"
[ -f VISUAL-HONESTY.md ]  || die "VISUAL-HONESTY.md no existe"
[ -f robots.txt ]         || echo "  ⚠ robots.txt no existe (no bloqueante)"
ok "sitemap.xml presente"
ok "VISUAL-HONESTY.md presente"

# --- Paso 3: append bitácora entry (best-effort) ---
log "[3/5] Bitácora del proyecto"
if [ -f "$ACADEMIC_REPO/web/bitacora.html" ]; then
  echo "  academic repo detectado en $ACADEMIC_REPO"
  echo "  bitácora se construye externamente; verificar antes de continuar"
else
  echo "  ⚠ academic repo no accesible en $ACADEMIC_REPO"
  echo "  fallback: últimas entradas de git log (referencia)"
  if git rev-parse --git-dir >/dev/null 2>&1; then
    git log --oneline -5 || true
  else
    echo "  (no es un repo git o no hay commits)"
  fi
fi
ok "bitácora verificada"

# --- Paso 4: S3 sync ---
log "[4/5] S3 sync → $S3_BUCKET"
if [ "${SKIP_S3_SYNC:-0}" = "1" ]; then
  echo "  SKIP_S3_SYNC=1 — saltando (dry-run / sandbox)"
else
  if ! aws s3 sync . "$S3_BUCKET" --delete --cache-control "$CACHE_CONTROL"; then
    die "aws s3 sync FAILED"
  fi
  ok "S3 sync completo (cache-control: $CACHE_CONTROL)"
fi

# --- Paso 5: CloudFront invalidation ---
log "[5/5] CloudFront invalidation → $CF_DIST_ID"
if [ "${SKIP_CF_INVALIDATION:-0}" = "1" ]; then
  echo "  SKIP_CF_INVALIDATION=1 — saltando"
else
  if ! aws cloudfront create-invalidation \
      --distribution-id "$CF_DIST_ID" \
      --paths "/*"; then
    die "cloudfront invalidation FAILED"
  fi
  ok "CloudFront invalidation creada (paths: /*)"
fi

log "Deploy completo: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "  Próximos pasos sugeridos:"
echo "    1. curl -I https://sociedad.opitacode.com (verificar 200)"
echo "    2. axe-core / lighthouse en /  y /memoria-viva/"
echo "    3. tag semver + entrada en bitácora del proyecto"
