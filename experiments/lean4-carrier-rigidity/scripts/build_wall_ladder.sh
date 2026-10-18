#!/usr/bin/env bash
#
# TFPT Carrier Rigidity — serialised WallLadder rung builder
# =========================================================
#
# The generated `TfptCarrier/WallLadder/RungKz*.lean` certificates each drive a
# single kernel `decide` over a packed Cholesky witness and peak in the tens of
# GB of RSS.  `lakefile.lean` therefore pins the default per-process ceiling
# (`leanMemoryMb`) low enough that an uncapped 32-way `lake build` fan-out stays
# inside physical RAM — at the price of failing the rung modules, which this
# script builds with a raised ceiling and a bounded number of concurrent jobs.
#
# Lake 5 has no `-j` flag, so concurrency is bounded by handing `lake build` only
# BATCH targets per invocation: everything else in the library is already built,
# so the number of runnable heavy jobs equals the number of targets passed.
#
# `--reconfigure` is mandatory, not cosmetic: Lake caches the *elaborated*
# lakefile, so `-K leanMemoryMb=...` is silently ignored while a stale package
# configuration is reused — a run can then fail at a ceiling it never asked for.
# The effective `-M` of every invocation is echoed below so the ceiling is
# verified from the build trace rather than assumed.
#
# Usage:
#   ./scripts/build_wall_ladder.sh                 # all missing rungs, defaults
#   BATCH=1 MEM_MB=327680 ./scripts/build_wall_ladder.sh
#   ./scripts/build_wall_ladder.sh RungKz9 RungKz12
#
# Env:
#   BATCH      concurrent rung builds per lake invocation (default 2)
#   MEM_MB     per-process Lean memory ceiling in MB      (default 163840)
#   ONLY_MISSING  1 = skip rungs whose .olean already exists (default 1)
#
# Ceiling sizing is measured, not guessed: RungKz12/13 (~0.1 MB source) build in
# 189 s / 260 s, while RungKz14 (~0.2 MB) exceeded a 48 GB ceiling after 987 s
# with "(kernel) excessive memory consumption detected".  The default ceiling is
# therefore generous and BATCH small; on a 512 GB machine BATCH=2 at 160 GB
# bounds the worst case at 320 GB.
#
# Prints, per batch, wall time and the peak summed RSS of all `lean` processes
# observed while the batch ran, so the cost of the audit is measured, not
# guessed.  Exit code 0 iff every requested rung built.

set -uo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

export PATH="$HOME/.elan/bin:$PATH"

BATCH="${BATCH:-2}"
MEM_MB="${MEM_MB:-163840}"
ONLY_MISSING="${ONLY_MISSING:-1}"
OLEAN_DIR=".lake/build/lib/lean/TfptCarrier/WallLadder"

if [[ "$#" -gt 0 ]]; then
    RUNGS=("$@")
else
    RUNGS=()
    for f in TfptCarrier/WallLadder/RungKz*.lean; do
        RUNGS+=("$(basename "$f" .lean)")
    done
fi

PENDING=()
for r in "${RUNGS[@]}"; do
    if [[ "$ONLY_MISSING" == "1" && -f "$OLEAN_DIR/$r.olean" ]]; then
        echo "[skip] $r (.olean present)"
        continue
    fi
    PENDING+=("$r")
done

if [[ "${#PENDING[@]}" == "0" ]]; then
    echo "[done] every requested rung already has its .olean"
    exit 0
fi

echo "[plan] ${#PENDING[@]} rung(s) to build, batch=$BATCH, ceiling=${MEM_MB}MB"

# Peak-RSS sampler: sums the RSS of every live `lean` process every 5 s and
# keeps the maximum in a file, so a batch's true memory cost is reported.
sample_peak() {
    local out="$1" peak=0 cur
    while :; do
        cur=$(ps -Ao rss=,comm= 2>/dev/null | awk '$2 ~ /(^|\/)lean$/ {s+=$1} END {print s+0}')
        if [[ -n "$cur" && "$cur" -gt "$peak" ]]; then
            peak="$cur"
            printf '%s\n' "$peak" > "$out"
        fi
        sleep 5
    done
}

FAILED=()
BUILT=0
i=0
total="${#PENDING[@]}"
while [[ "$i" -lt "$total" ]]; do
    targets=()
    names=()
    for ((k = 0; k < BATCH && i + k < total; k++)); do
        names+=("${PENDING[i + k]}")
        targets+=("TfptCarrier.WallLadder.${PENDING[i + k]}")
    done
    i=$((i + ${#names[@]}))

    peak_file="$(mktemp)"
    log_file="$(mktemp)"
    printf '0\n' > "$peak_file"
    sample_peak "$peak_file" &
    sampler=$!

    echo "[batch] $(date +%H:%M:%S) building: ${names[*]}"
    start=$(date +%s)
    lake build --reconfigure -K "leanMemoryMb=$MEM_MB" --verbose "${targets[@]}" \
        2>&1 | tee "$log_file"
    rc="${PIPESTATUS[0]}"
    end=$(date +%s)

    effective_m=$(grep -oE -- '-M [0-9]+' "$log_file" | head -1)
    if [[ -n "$effective_m" && "$effective_m" != "-M $MEM_MB" ]]; then
        echo "[batch] WARNING: lean ran with '$effective_m', not '-M $MEM_MB'" >&2
    elif [[ -n "$effective_m" ]]; then
        echo "[batch] ceiling verified from trace: $effective_m"
    fi

    kill "$sampler" 2>/dev/null
    wait "$sampler" 2>/dev/null
    peak_kb=$(cat "$peak_file" 2>/dev/null || echo 0)
    rm -f "$peak_file" "$log_file"

    peak_gb=$(awk -v k="$peak_kb" 'BEGIN {printf "%.1f", k/1048576}')
    echo "[batch] rc=$rc  wall=$((end - start))s  peak lean RSS=${peak_gb}GB"

    for r in "${names[@]}"; do
        if [[ -f "$OLEAN_DIR/$r.olean" ]]; then
            BUILT=$((BUILT + 1))
        else
            FAILED+=("$r")
        fi
    done
done

echo "[summary] built=$BUILT failed=${#FAILED[@]}"
if [[ "${#FAILED[@]}" != "0" ]]; then
    echo "[summary] missing after build: ${FAILED[*]}" >&2
    exit 1
fi
exit 0
