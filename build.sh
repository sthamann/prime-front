#!/usr/bin/env bash
# Independent Prime Front sources, documents and public mirrors.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
PYTHON="${PRIME_FRONT_PYTHON:-python3}"
NOTES=(tfpt_prime_front note_hilbert_polya_truncations note_w1_suzuki_identification note_w3_detector_structure parity_toeplitz_classification multilevel_toeplitz_lowerbound extracted_tfpt_1_architecture_e8 extracted_tfpt_2_standard_model extracted_tfpt_3_e8_audit_bootstrap extracted_tfpt_research_contracts extracted_tfpt_4_frontier extracted_introduction extracted_changelog)
gen() {
  "$PYTHON" verification/make_script_index.py
  "$PYTHON" rh/catalog/build_catalog.py --check
}
notes() {
  for name in "${NOTES[@]}"; do
    [ -f "$name.tex" ] || continue
    pdflatex -cnf-line=extra_mem_top=20000000 -cnf-line=extra_mem_bot=20000000 -interaction=nonstopmode -halt-on-error "$name.tex" > /dev/null
    pdflatex -cnf-line=extra_mem_top=20000000 -cnf-line=extra_mem_bot=20000000 -interaction=nonstopmode -halt-on-error "$name.tex" > /dev/null
    echo "Built $name.pdf"
  done
}
website() {
  mkdir -p website/public/papers website/public/verification
  for name in "${NOTES[@]}"; do
    [ ! -f "$name.pdf" ] || cp "$name.pdf" website/public/papers/
  done
  "$PYTHON" - <<'PY'
import csv, shutil
from pathlib import Path
source=Path('verification'); target=Path('website/public/verification')
for path in target.glob('*.py'): path.unlink()
# Include dependencies and source data so downloaded verification files remain reproducible.
for path in source.iterdir():
    if path.is_file() and path.suffix in {'.py','.json','.csv'}:
        shutil.copy2(path,target/path.name)
PY
}
audit() {
  "$PYTHON" verification/audit_sync.py
  "$PYTHON" rh/catalog/build_catalog.py --check
  "$PYTHON" scripts/check_migration.py
}
case "${1:-audit}" in
  gen) gen ;;
  notes) gen; notes ;;
  website) website ;;
  audit) audit ;;
  verify) "$PYTHON" verification/run_all.py ;;
  release) gen; notes; website; audit; (cd website && npm run build) ;;
  *) echo 'Usage: bash build.sh {gen|notes|website|audit|verify|release}' >&2; exit 2 ;;
esac
