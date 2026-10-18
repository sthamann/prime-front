"""discipline_audit_probe -- sandbox probe for META.DISCIPLINE.01: the
suite audits ITSELF.

The suspicion to be defused is "numerology / AI slop": a large corpus of
machine-checked claims could in principle be a confirmation-bias
generator (only positives promoted, nothing preregistered, nothing
reproducible, no external anchor).  This probe MEASURES the scientific
process discipline of the verification suite -- from the suite's own
files, machine-readable, no self-praise:

  D1  LEDGER CENSUS: rows / active rows / display-class distribution of
      verification/status_ledger.csv, plus the census of documented
      honest negatives, kills and retypes (keyword census over the
      claim + canonical_status columns).
  D2  MUST-FAIL CENSUS: all verification/v*.py -- module count, static
      check() call sites, static keyword census of must-fail /
      must-break / kill / scramble / negative-control semantics, and
      the [C]-vs-[E] typing marks in module sources.
  D3  PREREGISTRATION CENSUS: research contracts in
      tfpt_research_contracts.tex + ledger, kill criteria named BEFORE
      execution, and two named executed examples verified in the ledger
      (FTR.PGL2.01: preregistered v533 -> executed v632;
      PRIME.WEIL.OPERATOR.01: kill tests K1-K3 named 2026-08-02 ->
      W1 theorem-closed v643) + the frozen prediction registry
      (REG.FREEZE.01 / predictions_frozen.json).
  D4  REPRODUCIBILITY: a declared 12-module sample across the number
      range (incl. v634, v643, v648) is executed TWICE in fresh
      subprocesses; outputs must be identical up to timing lines
      (deterministic-replay test); plus corpus counts of explicit
      seeds and sympy-exact arithmetic.
  D5  EXTERNAL ANCHORS: five classical results recomputed here against
      the literature values the suite quotes (Jacobi four squares /
      Hecke-Eisenstein layer of v625; Construction A E8 of v626;
      Shephard-Todd G31 degrees of v634; Suzuki archimedean constants
      of v630/v631/v643; the completed-zeta functional equation
      underlying the v563 Weil frame) + corpus citation census.
  D6  LEAN LAYER: committed formal proof modules in
      experiments/lean4-carrier-rigidity/TfptCarrier/ (git ls-files;
      the uncommitted sandbox WIP of parallel workers is EXCLUDED),
      build artefacts present; `lake build` is NOT re-run here (honest:
      runtime + a parallel sandbox owns uncommitted .lean WIP today).
  D7  THE LIMIT, honest: what this audit does NOT show.

FIREWALL: read-only.  This probe writes nothing, moves no marker,
changes no status.  It measures process discipline, not physics truth.
Verdict enums: DISCIPLINE-MEASURED (all censuses complete, replay
deterministic 12/12), REPLAY-BROKEN (any sample module
non-deterministic), CENSUS-INCOMPLETE (a source file unreadable).
"""
import csv
import os
import re
import subprocess
import sys
import time

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "verification", "run_all.py")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root with verification/run_all.py not found")


ROOT = find_root()
VERIF = os.path.join(ROOT, "verification")
LEAN_DIR = os.path.join(ROOT, "experiments", "lean4-carrier-rigidity")

# ---------------------------------------------------------------- D1 census
# Display-class mapping mirrors the public four-class scheme
# (make_changelog_web.MARKERS): fine types I/L/F/N/M render as [E],
# P/B/R as [C], A as [O].
E_TAGS = {"E", "I", "L", "F", "N", "M"}
C_TAGS = {"C", "P", "B", "R"}
O_TAGS = {"O", "A"}
X_TAGS = {"X"}
E_WORDS = ("identity", "formal", "lattice", "numerical", "measured",
           "exact", "red-team")
C_WORDS = ("physical", "branch policy", "geometric premise", "conjecture",
           "reduction")
KILL_RE = re.compile(
    r"kill|ill-posed|honest negative|no-independent|must-fail|must fail"
    r"|must-break|retyped|superseded|\bdead\b|bingo|numerolog", re.I)


def ledger_rows():
    with open(os.path.join(VERIF, "status_ledger.csv"), newline="",
              encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def row_class(status):
    low = status.lower()
    tags = set()
    for grp in re.findall(r"\[([A-Za-z/+, ]+)\]", status):
        for t in re.split(r"[/+, ]+", grp):
            t = t.strip().upper()
            if t:
                tags.add(t)
    if low.startswith("axiom"):
        return "AXIOM"
    if tags & X_TAGS:
        return "X"
    if tags & O_TAGS or low.startswith("open") or "contract" in low:
        return "O"
    if tags & C_TAGS:
        return "C"
    if tags & E_TAGS:
        return "E"
    if any(low.startswith(w) for w in E_WORDS):
        return "E"
    if any(low.startswith(w) for w in C_WORDS):
        return "C"
    return "OTHER"


def ledger_census(rows):
    dist = {"E": 0, "C": 0, "O": 0, "X": 0, "AXIOM": 0, "OTHER": 0}
    for r in rows:
        dist[row_class(r["status"])] += 1
    kill_ids = sorted({r["claim_id"] for r in rows if KILL_RE.search(
        (r.get("claim") or "") + " " + (r.get("canonical_status") or ""))})
    return dict(
        rows=len(rows),
        active=sum(1 for r in rows
                   if (r.get("active") or "").strip().lower() == "true"),
        retired=sum(1 for r in rows
                    if (r.get("active") or "").strip().lower() != "true"),
        dist=dist,
        kill_ids=kill_ids,
    )


# ---------------------------------------------------------------- D2 census
MF_RE = re.compile(r"must-fail|must fail|must-break|must break"
                   r"|negative control|negative-control|\bkill"
                   r"|scramble", re.I)
SEED_RE = re.compile(r"np\.random\.seed|random\.seed\(|default_rng\("
                     r"|RandomState\(|\bseed\s*=")


def module_files():
    return sorted(f for f in os.listdir(VERIF)
                  if re.match(r"v\d+_.+\.py$", f))


def suite_census():
    files = module_files()
    out = dict(modules=len(files), sites=0, no_check=[], mf_occ=0,
               mf_mods=0, c_marks=0, e_marks=0, seed_mods=0,
               sympy_mods=0, exact_occ=0)
    for f in files:
        with open(os.path.join(VERIF, f), encoding="utf-8",
                  errors="replace") as fh:
            src = fh.read()
        sites = (len(re.findall(r"\bcheck\(", src))
                 - len(re.findall(r"def\s+check\(", src)))
        out["sites"] += sites
        if sites == 0:
            out["no_check"].append(f)
        n_mf = len(MF_RE.findall(src))
        out["mf_occ"] += n_mf
        out["mf_mods"] += 1 if n_mf else 0
        out["c_marks"] += src.count("[C]")
        out["e_marks"] += src.count("[E]")
        out["seed_mods"] += 1 if SEED_RE.search(src) else 0
        out["sympy_mods"] += 1 if re.search(r"^\s*(import|from)\s+sympy",
                                            src, re.M) else 0
        out["exact_occ"] += len(re.findall(r"exact", src, re.I))
    return out


# ---------------------------------------------------------------- D3 census
def contracts_census(rows):
    with open(os.path.join(ROOT, "tfpt_research_contracts.tex"),
              encoding="utf-8") as fh:
        tex = fh.read()
    tex_mentions = len(re.findall(r"research contract", tex, re.I))
    prereg = [r for r in rows if re.search(
        r"preregist|research contract", (r.get("claim") or "")
        + " " + (r.get("status") or ""), re.I)]
    prereg_kill = [r for r in prereg if re.search(
        r"kill", (r.get("claim") or ""), re.I)]
    by_id = {r["claim_id"]: r for r in rows}
    ftr = by_id.get("FTR.PGL2.01", {})
    weil = by_id.get("PRIME.WEIL.OPERATOR.01", {})
    reg = by_id.get("REG.FREEZE.01", {})
    ex_ftr = ("v632" in (ftr.get("script") or "")
              and re.search(r"preregist", ftr.get("claim") or "", re.I)
              is not None)
    ex_weil = (re.search(r"KILL TESTS|kill test", weil.get("claim") or "",
                         re.I) is not None
               and "W1 THEOREM-closed (v643"
               in (weil.get("canonical_status") or ""))
    ex_reg = (bool(reg) and os.path.exists(
        os.path.join(VERIF, "predictions_frozen.json")))
    return dict(tex_mentions=tex_mentions, prereg=len(prereg),
                prereg_ids=sorted(r["claim_id"] for r in prereg),
                prereg_kill=len(prereg_kill),
                ex_ftr=ex_ftr, ex_weil=ex_weil, ex_reg=ex_reg)


# ------------------------------------------------------------- D4 replay
REPRO_SAMPLE = [
    "v55_coxeter_cycle", "v91_spine_tetrahedron", "v108_pascal_ladder",
    "v205_xi_threequarter", "v305_witness_independence",
    "v405_seam_equiv_omega", "v505_celestial_wp5e_beta_equivariant_ledger",
    "v555_pareto_tv_identities", "v600_joint_embedding",
    "v634_st31_structure", "v643_w1_theorem", "v648_sign_uncertainty",
]
TIME_LINE_RE = re.compile(
    r"elapsed|\(\s*\d+(?:\.\d+)?\s*s\s*\)|\b\d+(?:\.\d+)?\s*s\b", re.I)


def canon_output(out):
    kept, dropped = [], 0
    for line in out.splitlines():
        if TIME_LINE_RE.search(line):
            dropped += 1
            continue
        kept.append(line)
    return "\n".join(kept), dropped


def run_module_once(name):
    p = subprocess.run([sys.executable, name + ".py"], cwd=VERIF,
                       capture_output=True, text=True, timeout=900)
    return p.returncode, p.stdout


def replay_sample():
    results = []
    for name in REPRO_SAMPLE:
        rc1, out1 = run_module_once(name)
        rc2, out2 = run_module_once(name)
        c1, d1 = canon_output(out1)
        c2, d2 = canon_output(out2)
        same = (rc1 == 0 and rc2 == 0 and c1 == c2 and d1 == d2)
        results.append((name, rc1, rc2, same, d1, len(c1.splitlines())))
        print("      %-45s rc=%d/%d deterministic=%s "
              "(%d lines compared, %d timing lines filtered)"
              % (name, rc1, rc2, same, len(c1.splitlines()), d1))
    return results


# ------------------------------------------------------------- D5 anchors
def sigma(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


def anchor_jacobi():
    """Jacobi 1834: r_4(n) = 8 sum_{d | n, 4 !| d} d (four-square counts;
    the classical layer under v625's theta = Eisenstein identity)."""
    worst = None
    for n in range(1, 41):
        brute = 0
        m = int(n ** 0.5) + 1
        for a in range(-m, m + 1):
            for b in range(-m, m + 1):
                for c in range(-m, m + 1):
                    r = n - a * a - b * b - c * c
                    if r < 0:
                        continue
                    d = int(round(r ** 0.5))
                    if d * d == r:
                        brute += 2 if d else 1
        jac = 8 * sum(d for d in range(1, n + 1)
                      if n % d == 0 and d % 4 != 0)
        if brute != jac:
            worst = n
    return worst is None, "r_4(n) = 8 sigma'(n) exact for n = 1..40"


def hamming_codewords():
    G = [(1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
         (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0)]
    words = set()
    for m in range(16):
        w = [0] * 8
        for i in range(4):
            if (m >> i) & 1:
                w = [(a + b) % 2 for a, b in zip(w, G[i])]
        words.add(tuple(w))
    return words


def anchor_construction_a():
    """Construction A (Leech/Sloane classic; v626): the extended Hamming
    [8,4,4] code lifts to the even unimodular rank-8 lattice with 240
    minimal vectors."""
    words = hamming_codewords()
    wts = {}
    for w in words:
        wts[sum(w)] = wts.get(sum(w), 0) + 1
    selfdual = all(sum(a * b for a, b in zip(u, v)) % 2 == 0
                   for u in words for v in words)
    n_min = 0
    from itertools import product as iproduct
    for x in iproduct((-2, -1, 0, 1, 2), repeat=8):
        if sum(v * v for v in x) != 4:
            continue
        if tuple(v % 2 for v in x) in words:
            n_min += 1
    ok = (wts == {0: 1, 4: 14, 8: 1} and selfdual and n_min == 240)
    return ok, ("weights {0:1, 4:14, 8:1}, self-dual, 240 minimal "
                "vectors (= 16 + 14*16)")


def anchor_st31():
    """Shephard-Todd 1954 / Springer: G31 degrees (8, 12, 20, 24) --
    product = group order 46080 = |W(D5)|*|W(A3)|, reflections
    60 = sum (d_i - 1) (the literature side of v634)."""
    degs = (8, 12, 20, 24)
    prod = 1
    for d in degs:
        prod *= d
    w_d5 = 2 ** 4 * 120          # |W(D5)| = 2^(5-1) * 5!
    w_a3 = 24                    # |W(A3)| = S4
    ok = (prod == 46080 and prod == w_d5 * w_a3
          and sum(d - 1 for d in degs) == 60)
    return ok, "8*12*20*24 = 46080 = 1920*24, sum(d_i - 1) = 60"


def anchor_suzuki(mp):
    """Suzuki arXiv:2606.09096 (v630/v631/v643): the archimedean
    constants -- psi(1/4) = -gamma - 3 log 2 - pi/2 (25 digits, two
    routes), the delta_0 weight L = log pi - psi(1/4), and the printed
    origin constant A = (1/2)(log 2 pi - psi(2)) = 0.70754637."""
    mp.mp.dps = 40
    psi_q = mp.digamma(mp.mpf(1) / 4)
    closed = -mp.euler - 3 * mp.log(2) - mp.pi / 2
    dev1 = abs(psi_q - closed)
    a_const = (mp.log(2 * mp.pi) - mp.digamma(2)) / 2
    dev2 = abs(a_const - mp.mpf("0.70754637"))
    l_const = mp.log(mp.pi) - psi_q
    ok = (dev1 < mp.mpf(10) ** -25 and dev2 < mp.mpf(10) ** -8
          and abs(l_const - mp.mpf("5.372184")) < mp.mpf(10) ** -6)
    return ok, ("psi(1/4) closed form dev %s; A dev %s; L = %s"
                % (mp.nstr(dev1, 3), mp.nstr(dev2, 3),
                   mp.nstr(l_const, 8)))


def anchor_xi(mp):
    """Riemann 1859 / Weil 1952 frame (v563): the completed zeta
    xi(s) = (1/2) s (s-1) pi^(-s/2) Gamma(s/2) zeta(s) satisfies
    xi(s) = xi(1-s) -- the functional-equation engine of the explicit
    formula, recomputed at three strip points to 20+ digits."""
    mp.mp.dps = 30

    def xi(s):
        return (s * (s - 1) / 2 * mp.pi ** (-s / 2)
                * mp.gamma(s / 2) * mp.zeta(s))

    devs = [abs(xi(s) - xi(1 - s)) / abs(xi(s)) for s in
            (mp.mpf(3) / 10 + mp.mpf(7) / 10 * 1j, mp.mpf(1) / 5,
             mp.mpf(4) / 5 - mp.mpf(2) / 5 * 1j)]
    return max(devs) < mp.mpf(10) ** -20, ("worst rel dev %s"
                                           % mp.nstr(max(devs), 3))


ANCHOR_CITES = ["Jacobi", "Hecke", "Construction A", "Suzuki", "Weil",
                "Eisenstein"]


def citation_census():
    counts = {k: 0 for k in ANCHOR_CITES}
    arxiv = 0
    for f in module_files():
        with open(os.path.join(VERIF, f), encoding="utf-8",
                  errors="replace") as fh:
            src = fh.read()
        for k in ANCHOR_CITES:
            if k in src:
                counts[k] += 1
        arxiv += 1 if "arXiv:" in src else 0
    return counts, arxiv


# ------------------------------------------------------------- D6 lean
def lean_census():
    method = "git"
    try:
        p = subprocess.run(
            ["git", "-C", ROOT, "ls-files",
             "experiments/lean4-carrier-rigidity/TfptCarrier/"],
            capture_output=True, text=True, timeout=60)
        names = [ln for ln in p.stdout.splitlines()
                 if ln.endswith(".lean")]
        if p.returncode != 0:
            raise RuntimeError
    except Exception:
        method = "fs-fallback (git unavailable -- counts may include "\
                 "uncommitted files)"
        d = os.path.join(LEAN_DIR, "TfptCarrier")
        names = sorted(f for f in os.listdir(d) if f.endswith(".lean"))
    artefacts = {a: os.path.exists(os.path.join(LEAN_DIR, a))
                 for a in ("lakefile.lean", "lake-manifest.json",
                           "lean-toolchain",
                           os.path.join(".lake", "build"))}
    return dict(n=len(names), method=method, artefacts=artefacts)


# ---------------------------------------------------------------- runner
def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("DISCIPLINE AUDIT PROBE -- the suite measures its own process "
          "discipline")
    print("=" * 78)

    rows = ledger_rows()

    # ------------------------------------------------------------- D1
    print("\nD1 -- ledger census (verification/status_ledger.csv)")
    lc = ledger_census(rows)
    print("      rows = %d, active = %d, retired = %d" %
          (lc["rows"], lc["active"], lc["retired"]))
    print("      display-class distribution: %s" % lc["dist"])
    print("      kill/negative keyword rows: %d" % len(lc["kill_ids"]))
    print("      sample ids: %s ..." % ", ".join(lc["kill_ids"][:12]))
    check("D1.1 [E] ledger census: %d rows, %d active, class "
          "distribution E/C/O/X/AXIOM/OTHER = %d/%d/%d/%d/%d/%d"
          % (lc["rows"], lc["active"], lc["dist"]["E"], lc["dist"]["C"],
             lc["dist"]["O"], lc["dist"]["X"], lc["dist"]["AXIOM"],
             lc["dist"]["OTHER"]),
          lc["rows"] >= 700 and lc["active"] >= 700)
    check("D1.2 [E] documented kills / honest negatives / retypes: "
          "%d ledger rows carry negative-evidence keywords"
          % len(lc["kill_ids"]), len(lc["kill_ids"]) >= 50)

    # ------------------------------------------------------------- D2
    print("\nD2 -- must-fail census (static, over verification/v*.py)")
    sc = suite_census()
    print("      modules = %d, static check() call sites = %d"
          % (sc["modules"], sc["sites"]))
    print("      modules without check( sites: %s" % (sc["no_check"] or
                                                      "none"))
    print("      must-fail/kill/scramble keyword occurrences = %d in %d "
          "modules" % (sc["mf_occ"], sc["mf_mods"]))
    print("      typing marks in sources: [E] x %d vs [C] x %d"
          % (sc["e_marks"], sc["c_marks"]))
    print("      seeded modules = %d, sympy modules = %d, 'exact' "
          "occurrences = %d" % (sc["seed_mods"], sc["sympy_mods"],
                                sc["exact_occ"]))
    check("D2.1 [E] module census: %d modules, all with check sites"
          % sc["modules"],
          sc["modules"] >= 642 and not sc["no_check"])
    check("D2.2 [E] static check-call census: %d call sites"
          % sc["sites"], sc["sites"] >= 4000)
    check("D2.3 [E] negative-control semantics: %d keyword occurrences "
          "across %d modules" % (sc["mf_occ"], sc["mf_mods"]),
          sc["mf_occ"] >= 500 and sc["mf_mods"] >= 200)

    # ------------------------------------------------------------- D3
    print("\nD3 -- preregistration census")
    cc = contracts_census(rows)
    print("      'research contract' mentions in "
          "tfpt_research_contracts.tex = %d" % cc["tex_mentions"])
    print("      preregistered/contract ledger rows = %d (%s)"
          % (cc["prereg"], ", ".join(cc["prereg_ids"][:10])))
    print("      of which naming kill criteria in the claim = %d"
          % cc["prereg_kill"])
    check("D3.1 [E] contracts exist with named kill criteria: %d "
          "contract/preregistration rows, %d naming kill criteria"
          % (cc["prereg"], cc["prereg_kill"]),
          cc["tex_mentions"] >= 10 and cc["prereg"] >= 5
          and cc["prereg_kill"] >= 3)
    check("D3.2 [E] executed-contract examples verified in the ledger: "
          "FTR.PGL2.01 (prereg v533 -> executed v632) = %s; "
          "PRIME.WEIL.OPERATOR.01 (kill tests K1-K3 -> W1 theorem "
          "v643) = %s; REG.FREEZE.01 + predictions_frozen.json = %s"
          % (cc["ex_ftr"], cc["ex_weil"], cc["ex_reg"]),
          cc["ex_ftr"] and cc["ex_weil"] and cc["ex_reg"])

    # ------------------------------------------------------------- D4
    print("\nD4 -- reproducibility replay (12-module sample, 2 runs "
          "each)")
    rr = replay_sample()
    n_det = sum(1 for r in rr if r[3])
    check("D4.1 [E] deterministic replay: %d/12 sample modules produce "
          "identical output on two fresh runs (timing lines filtered)"
          % n_det, n_det == 12)
    check("D4.2 [E] exactness census: %d modules import sympy, %d "
          "modules carry explicit seeds"
          % (sc["sympy_mods"], sc["seed_mods"]),
          sc["sympy_mods"] >= 50 and sc["seed_mods"] >= 30)

    # ------------------------------------------------------------- D5
    print("\nD5 -- external classical anchors (recomputed against the "
          "literature)")
    import mpmath as mp
    anchors = [
        ("Jacobi 1834 four-square counts (v625 layer)",) + anchor_jacobi(),
        ("Construction A -> E8 from [8,4,4] (v626)",)
        + anchor_construction_a(),
        ("Shephard-Todd G31 degrees (v634)",) + anchor_st31(),
        ("Suzuki archimedean constants (v630/v631/v643)",)
        + anchor_suzuki(mp),
        ("completed-zeta functional equation (v563 frame)",)
        + anchor_xi(mp),
    ]
    n_ok = 0
    for name, ok, detail in anchors:
        n_ok += 1 if ok else 0
        check("D5.%d [E] anchor recompute: %s" % (n_ok, name), ok, detail)
    cites, arxiv = citation_census()
    print("      citation census over module sources: %s; arXiv-citing "
          "modules = %d" % (cites, arxiv))
    check("D5.6 [E] >= 5 independent classical anchors recomputed and "
          "each cited in the corpus (%s)"
          % ", ".join("%s x %d" % kv for kv in cites.items()),
          n_ok >= 5 and all(v >= 1 for v in cites.values()))

    # ------------------------------------------------------------- D6
    print("\nD6 -- the Lean layer (committed formal proof modules)")
    lz = lean_census()
    print("      committed TfptCarrier/*.lean modules = %d (method: %s)"
          % (lz["n"], lz["method"]))
    print("      build artefacts: %s" % lz["artefacts"])
    print("      HONEST: `lake build` is NOT re-run by this probe "
          "(runtime; a parallel sandbox owns uncommitted .lean WIP "
          "today); the last green build (3380 jobs, no sorry) is "
          "quoted from changelog 2026-08-02 (XLIII).")
    check("D6.1 [E] >= 5 formal proof modules committed: %d" % lz["n"],
          lz["n"] >= 5 and all(lz["artefacts"].values()))

    # ------------------------------------------------------------- D7
    print("\nD7 -- the limit, honest")
    open_ids = sorted(r["claim_id"] for r in rows
                      if (r.get("active") or "").strip().lower() == "true"
                      and row_class(r["status"]) == "O")
    print("      open/contract rows (display class O): %d" % len(open_ids))
    print("      majors: %s" % ", ".join(
        i for i in open_ids if i.startswith(("GATE.", "SEAM.THEOREM",
                                             "PRIME.WEIL.OPERATOR",
                                             "QGEO."))))
    named = {"SEAM.THEOREM.01", "PRIME.WEIL.OPERATOR.01"}
    check("D7.1 [C] the limit, typed: this audit measures PROCESS "
          "discipline (censuses, replay, anchors), NOT the truth of "
          "the physics; typed [C] observations stay observations; the "
          "open gates stay open (%d class-O rows incl. %s); a "
          "discipline certificate is a necessary, not a sufficient, "
          "condition against numerology"
          % (len(open_ids), ", ".join(sorted(named))),
          named.issubset(set(open_ids)))

    # ---------------------------------------------------------- summary
    verdict = "DISCIPLINE-MEASURED"
    if any(not r[3] for r in rr):
        verdict = "REPLAY-BROKEN"
    if FAILS:
        verdict = "CENSUS-INCOMPLETE"
    print("\nVERDICT: %s" % verdict)
    print("\nPROPOSED FREEZE VALUES for v649 (measured today):")
    print("  ledger rows/active     : %d / %d" % (lc["rows"], lc["active"]))
    print("  kill/negative rows     : %d" % len(lc["kill_ids"]))
    print("  modules / check sites  : %d / %d" % (sc["modules"],
                                                  sc["sites"]))
    print("  must-fail occ / mods   : %d / %d" % (sc["mf_occ"],
                                                  sc["mf_mods"]))
    print("  [E] / [C] marks        : %d / %d" % (sc["e_marks"],
                                                  sc["c_marks"]))
    print("  seeded / sympy modules : %d / %d" % (sc["seed_mods"],
                                                  sc["sympy_mods"]))
    print("  contract rows / kill   : %d / %d" % (cc["prereg"],
                                                  cc["prereg_kill"]))
    print("  lean modules committed : %d" % lz["n"])
    print("  open class-O rows      : %d" % len(open_ids))

    print("\nchecks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                             FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
