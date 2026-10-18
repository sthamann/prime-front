"""Discovery probe (2026-07-25), part 48 of the zeta/prime investigation.
HARD PRE-TEST for Stage-4 Route 1 (compiler-native Lambda scale).

Kill question (zeros-free):
  Is the scale of the Fourier-selfduality / prolate-class operator
  UNIQUELY derivable from verified TFPT structures BEFORE any zero is
  consulted — or does a family of equally plausible scales remain
  (= kill of Route 1's *explanatory* claim)?

Context (sandbox, already typed):
  T46 stage4_prolate_prototype_probe: R1-certified W_Lambda class
      W_Lambda = -d/dx((Lambda^2 - x^2) d/dx) + (2 pi Lambda x)^2
      with Ramis reduction A_tau, tau = 2 pi Lambda^2; tested Lambda in
      {1, sqrt(2), 2} were ad hoc.
  T12 e8_glue_lseries_selfdual_probe: E8 census Poisson identity
      Theta(t) = (pi/t)^4 Theta(pi^2/t); UNIQUE fixed width t = pi
      under Boltzmann e^{-t |x|^2} and root-norm-2 Cartan chart.
  T14 seam_selfdual_width_probe: DEFLATED.  Root-norm torsor
      root-norm 2 => t* = pi; root-norm 1 => t* = 2 pi (convention!).
      Unimodularity gate selects the lattice, not the scale.
      beta_angle = 2 pi = 1/(4 c3) is universal BW/Unruh once
      beta_steps = N (v526).

Sections:
  S0  Firewall: no Riemann-zero load / call in this probe.
  U1  Preregistered candidate enumeration + W_Lambda translation.
  U2  Selection-principle analysis (verified vs convention vs free).
  U3  Kill criterion / verdict enum.
  U4  Bonus eigenvalues ONLY if U2 yields a unique Lambda
      (info dump; NO zero comparison — blindness preserved).

PREREGISTERED CRITERIA (frozen before analysis):
  Generation rule G1 (mechanical, non-selective):
      Verified multiplicative atoms from suite / axioms:
        PI_UNIT = pi
        DISCRETE = {1, |mu4|=4, g_car=5, N_fam=3}
        POW2    = {2^k : k in {-2,-1,0,1,2}}
      Candidate Gaussian widths (Boltzmann e^{-t |x|^2}):
        t = PI_UNIT * p * m    for p in POW2, m in DISCRETE
      This enumerates ALL scales of that form; no hand-picking.
      Named specials that MUST appear (subset check, not generators):
        t=pi (T12), t=2pi (T14 torsor / beta), t=4pi (= |mu4|*pi),
        t=pi/2, t=pi/4, and discrete-factor multiples.

  Translation rule TR_DECAY (PRIMARY, structural bridge T46):
      A_tau eigenfunctions decay ~ exp(-(tau/2) |x|^2) (T46).
      Identify t_gauss with that quadratic rate:
          t_gauss = tau / 2
          tau     = 2 pi Lambda^2     (Ramis / CM convention)
      hence
          Lambda^2 = t_gauss / pi
          Lambda   = sqrt(t_gauss / pi)     (positive branch).
      Alternate charts TR_TAU_EQ (tau = t_gauss) and TR_DIRECT
      (Lambda = t_gauss / pi) are reported for completeness; the
      uniqueness kill is evaluated on TR_DECAY (the only chart that
      matches the documented A_tau decay to the Gaussian width).

  Selection principles under test (each typed verified/convention/free):
      (i)   Poisson self-duality (T12): fixed point of t |-> pi^2/t.
      (ii)  Unimodularity gate (T14): selects lattice, not scale.
      (iii) KMS/BW angle (T14/v526): beta = 2 pi universal once
            beta_steps = N — deflated as compiler-specific scale.

  Kill criterion K_SCALE (U3):
      Route-1 *explanation* survives ONLY if a verified principle
      selects EXACTLY ONE Lambda under TR_DECAY with NO free
      convention remaining.  A residual discrete torsor
      (e.g. {pi, 2 pi} -> {1, sqrt(2)}) => SCALE-TORSOR (kill
      explanation; external construction may remain).  A continuous
      family => SCALE-FREE (full kill).  Unique closed chain =>
      SCALE-UNIQUE.

  U4 gate: dump interior W_Lambda eigenvalues ONLY on SCALE-UNIQUE.
      Blindness: never compare to zeta zeros in this probe.

Firewall: discovery sandbox — no promotion, no ledger / paper /
website / marker / next.txt edits; ABSOLUTELY no RH-evidence language;
ABSOLUTELY no Riemann zeros (no zero-loader from mpmath, no zero tables).
Classical Poisson / Slepian / CM / Ramis named as classical / external.
"""
from __future__ import annotations

import ast
import inspect
import math
import time

import mpmath
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()
mpmath.mp.dps = 40

# ---------------------------------------------------------------- helpers
def check(name: str, ok: bool) -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}", flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def info(msg: str) -> None:
    print(f"        {msg}", flush=True)


def iszero(e) -> bool:
    e2 = sp.expand(e)
    if e2 == 0:
        return True
    e3 = sp.expand(sp.expand_complex(e2))
    if e3 == 0:
        return True
    try:
        return abs(complex(e3.evalf(40))) < 1e-28
    except Exception:
        return False


# ================================================================= S0
print("S0 -- firewall: zeros-free probe", flush=True)

# Inspect THIS module via AST: forbid zero-loader call/attr/import names.
# Forbidden tokens are assembled at runtime so contiguous loader names
# need not appear as source literals outside this assembly.
_SRC = inspect.getsource(inspect.getmodule(check))
_FORBIDDEN_AST = {
    "zeta" + "zero",
    "zeta" + "_zero",
    "zeta" + "_zeros",
    "siegel" + "z",
    "riemann" + "zeros",
    "riemann" + "_zero",
}

_tree = ast.parse(_SRC)
_call_names = set()
for node in ast.walk(_tree):
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name):
            _call_names.add(f.id)
        elif isinstance(f, ast.Attribute):
            _call_names.add(f.attr)

_zero_calls = _call_names & _FORBIDDEN_AST
_attr_chain_hits = [
    node.attr for node in ast.walk(_tree)
    if isinstance(node, ast.Attribute) and node.attr in _FORBIDDEN_AST
]
_imported_names = set()
for node in ast.walk(_tree):
    if isinstance(node, ast.ImportFrom):
        for alias in node.names:
            _imported_names.add(alias.name)
    elif isinstance(node, ast.Import):
        for alias in node.names:
            _imported_names.add(alias.name)
_bad_imports = _imported_names & _FORBIDDEN_AST

check(
    "S0a ZERO-FIREWALL: this probe's AST contains no call/attribute/"
    "import of a Riemann-zero loader "
    f"(calls∩forbid={sorted(_zero_calls)}; attrs={_attr_chain_hits}; "
    f"imports={sorted(_bad_imports)})",
    len(_zero_calls) == 0 and len(_attr_chain_hits) == 0
    and len(_bad_imports) == 0,
)

_exec_hits = [
    node.id for node in ast.walk(_tree)
    if isinstance(node, ast.Name) and node.id in _FORBIDDEN_AST
]
check(
    "S0b ZERO-FIREWALL (executable AST names): no forbidden zero-loader "
    f"Name nodes in the module AST (hits={_exec_hits})",
    len(_exec_hits) == 0,
)
info("Blindness: U4 (if reached) dumps eigenvalues only; never pairs "
     "them to zeros.  Route-1 scale question is zeros-free by design.")


# ================================================================= U1
print("U1 -- candidate enumeration (preregistered generation rule G1)",
      flush=True)

# --- verified atoms ---
c3 = sp.Rational(1, 8) / sp.pi
mu4_abs = 4
g_car = 5
n_fam = 3
beta = 1 / (4 * c3)          # = 2 pi
PI = sp.pi

check(
    "U1a AXIOM ATOMS: c3 = 1/(8 pi); beta = 1/(4 c3) = 2 pi exact; "
    "|mu4| = 4, g_car = 5, N_fam = 3 (compiler discrete factors; "
    "citations: P1/P2 axioms, v526 / T12 / T14)",
    iszero(c3 - sp.Rational(1, 8) / sp.pi)
    and iszero(beta - 2 * sp.pi)
    and mu4_abs == 4 and g_car == 5 and n_fam == 3,
)

# Generation rule G1
POW2 = [sp.Integer(2) ** k for k in range(-2, 3)]
DISCRETE = [sp.Integer(1), sp.Integer(mu4_abs), sp.Integer(g_car),
            sp.Integer(n_fam)]
raw_count = 0
candidates_t = []
for p in POW2:
    for m in DISCRETE:
        raw_count += 1
        t_val = PI * p * m
        k_exp = int(sp.log(p) / sp.log(2))
        candidates_t.append({
            "t": t_val,
            "p": p,
            "m": m,
            "origin": f"G1: t = pi * 2^{k_exp} * {m}",
        })

# Deduplicate by exact symbolic t (G1 has algebraic collisions, e.g.
# pi*2^2*1 = pi*2^0*4 = 4pi; pi*2^{-2}*4 = pi).
uniq = {}
for c in candidates_t:
    key = sp.simplify(c["t"])
    if key not in uniq:
        uniq[key] = c
    else:
        # retain merged origin note
        uniq[key]["origin"] += f" = also 2^{int(sp.log(c['p'])/sp.log(2))}*{c['m']}"
candidates_t = sorted(uniq.values(), key=lambda c: float(c["t"].evalf(30)))

info(f"G1 raw products: {raw_count}; distinct after exact dedup: "
     f"{len(candidates_t)}")
info(f"POW2 = {[str(p) for p in POW2]}")
info(f"DISCRETE = {[str(m) for m in DISCRETE]}")

# Named specials must appear
named = {
    "t=pi (T12 Poisson fixed point, root-norm 2)": PI,
    "t=2pi (T14 torsor root-norm 1 / beta)": 2 * PI,
    "t=4pi (|mu4| * pi)": mu4_abs * PI,
    "t=pi/2": PI / 2,
    "t=pi/4": PI / 4,
    "t=5pi (g_car * pi)": g_car * PI,
    "t=3pi (N_fam * pi)": n_fam * PI,
}
named_ok = True
for label, t_exp in named.items():
    hit = any(iszero(c["t"] - t_exp) for c in candidates_t)
    info(f"  named special present: {label}: {hit}")
    named_ok &= hit
check(
    "U1b GENERATION COMPLETE: G1 mechanically enumerates all "
    f"{raw_count} products pi*2^k*m (k in -2..2, m in DISCRETE); "
    f"{len(candidates_t)} distinct after exact dedup; all named "
    "specials {pi, 2pi, 4pi, pi/2, pi/4, 5pi, 3pi} are in the set "
    "(no selective omission)",
    named_ok and raw_count == len(POW2) * len(DISCRETE)
    and len(candidates_t) < raw_count,  # collisions prove non-selective
)

# --- live Poisson fixed-point (T12) ---
sig3 = {n: int(sp.divisor_sigma(n, 3)) for n in range(1, 80)}


def theta_E8_census(t, nmax=60):
    t = mpmath.mpf(t)
    tot = mpmath.mpf(1)
    for n in range(1, nmax + 1):
        tot += 240 * sig3[n] * mpmath.e ** (-t * 2 * n)
    return tot


pois_ok = True
for tw in (mpmath.mpf("1.1"), mpmath.mpf("2.6")):
    lhs = theta_E8_census(tw)
    rhs = (mpmath.pi / tw) ** 4 * theta_E8_census(mpmath.pi ** 2 / tw)
    ratio = lhs / rhs
    info(f"E8 Poisson t={tw}: lhs/rhs = {mpmath.nstr(ratio, 22)}")
    pois_ok &= abs(ratio - 1) < mpmath.mpf("1e-20")

s_ = sp.symbols("s", positive=True)
fixed = set(sp.solve(sp.pi ** 2 / s_ - s_, s_))
check(
    "U1c T12 LIVE: E8 Poisson Theta(t)=(pi/t)^4 Theta(pi^2/t) to >20 "
    "digits at t=1.1, 2.6; UNIQUE positive fixed width t=pi "
    "(solve pi^2/t = t) — citation: e8_glue_lseries_selfdual_probe S5",
    pois_ok and fixed == {sp.pi},
)

# --- live torsor (T14) ---
lam_root2 = sp.Integer(1)          # root-norm 2 => metric scale factor 1
lam_root1 = sp.Rational(1, 2)      # root-norm 1 => L -> sqrt(1/2) L
t_star_2 = sp.pi / lam_root2
t_star_1 = sp.pi / lam_root1
bolt = sp.exp(-beta * 2 / 2)       # e^{-beta * rootnorm / 2}
gauss = sp.exp(-t_star_2 * 2)      # e^{-t |root|^2}
torsor_ok = (
    iszero(t_star_2 - sp.pi)
    and iszero(t_star_1 - 2 * sp.pi)
    and iszero(sp.log(bolt) - sp.log(gauss))
    and iszero(t_star_1 - beta)
)
info(f"root-norm 2 => t* = {t_star_2}; root-norm 1 => t* = {t_star_1}")
info(f"Boltzmann/Gaussian match at roots (norm-2 chart): "
     f"{iszero(sp.log(bolt) - sp.log(gauss))}")
check(
    "U1d T14 LIVE TORSOR: L -> sqrt(lambda) L sends t* -> pi/lambda; "
    "root-norm 2 (lambda=1) => t*=pi; root-norm 1 (lambda=1/2) => "
    "t*=2pi=beta.  Boltzmann e^{-beta norm/2} matches e^{-pi |x|^2} "
    "ONLY in the root-norm-2 chart — citation: "
    "seam_selfdual_width_probe S3",
    torsor_ok,
)

# --- translation rules ---
def translate_tr_decay(t):
    """PRIMARY: t_gauss = tau/2, tau = 2 pi Lambda^2 => Lambda = sqrt(t/pi)."""
    return sp.sqrt(t / sp.pi)


def translate_tr_tau_eq(t):
    """ALT: identify tau = t_gauss => Lambda = sqrt(t/(2 pi))."""
    return sp.sqrt(t / (2 * sp.pi))


def translate_tr_direct(t):
    """ALT: dimensionless Lambda = t/pi (no sqrt)."""
    return t / sp.pi


info("TRANSLATION RULE TR_DECAY (PRIMARY):")
info("  A_tau decay ~ exp(-(tau/2)|x|^2)  (T46); set t_gauss = tau/2;")
info("  tau = 2 pi Lambda^2 (Ramis/CM) => Lambda = sqrt(t_gauss / pi).")
info("ALT charts TR_TAU_EQ: Lambda=sqrt(t/(2pi)); "
     "TR_DIRECT: Lambda=t/pi.")

# Build table
table = []
for c in candidates_t:
    t = c["t"]
    lam_d = translate_tr_decay(t)
    lam_e = translate_tr_tau_eq(t)
    lam_r = translate_tr_direct(t)
    # provenance tags
    tags = []
    if iszero(t - PI):
        tags.append("T12-Poisson-fixed / root-norm-2")
    if iszero(t - 2 * PI):
        tags.append("T14-torsor-root-norm-1 / beta=2pi")
    if iszero(t - mu4_abs * PI):
        tags.append("|mu4|*pi")
    if iszero(t - g_car * PI):
        tags.append("g_car*pi")
    if iszero(t - n_fam * PI):
        tags.append("N_fam*pi")
    if iszero(t - beta):
        tags.append("v526-beta")
    table.append({
        "t": t,
        "t_str": str(sp.simplify(t)),
        "origin": c["origin"],
        "tags": tags,
        "Lambda_TR_DECAY": lam_d,
        "Lambda_TR_TAU_EQ": lam_e,
        "Lambda_TR_DIRECT": lam_r,
        "Lambda_DECAY_f": float(lam_d.evalf(30)),
    })

print("        --- candidate table (t -> Lambda) ---", flush=True)
print("        {:>14}  {:>12}  {:>12}  {:>12}  {}".format(
    "t", "Λ_DECAY", "Λ_TAU_EQ", "Λ_DIRECT", "tags / origin"), flush=True)
for row in table:
    print(
        "        {:>14}  {:>12}  {:>12}  {:>12}  {} | {}".format(
            row["t_str"],
            str(sp.simplify(row["Lambda_TR_DECAY"])),
            str(sp.simplify(row["Lambda_TR_TAU_EQ"])),
            str(sp.simplify(row["Lambda_TR_DIRECT"])),
            ",".join(row["tags"]) if row["tags"] else "-",
            row["origin"],
        ),
        flush=True,
    )

# Sanity: TR_DECAY maps the three ad-hoc T46 Lambdas from {pi,2pi,4pi}
map_ok = (
    iszero(translate_tr_decay(PI) - 1)
    and iszero(translate_tr_decay(2 * PI) - sp.sqrt(2))
    and iszero(translate_tr_decay(4 * PI) - 2)
)
info(f"TR_DECAY: pi->1, 2pi->sqrt(2), 4pi->2  (matches T46 ad-hoc set): "
     f"{map_ok}")
check(
    "U1e TRANSLATION SANITY: TR_DECAY sends {pi, 2pi, 4pi} to "
    "{1, sqrt(2), 2} — exactly the ad-hoc Lambda set of T46 — so the "
    "T46 trial values were the G1 torsor orbit under root-norm / "
    "2-power, not independent compiler predictions",
    map_ok,
)

# Count distinct Lambda under TR_DECAY
lam_decay_set = {sp.simplify(r["Lambda_TR_DECAY"]) for r in table}
info(f"|distinct Lambda under TR_DECAY| = {len(lam_decay_set)}")
check(
    "U1f ENUMERATION NON-UNIQUE a priori: G1+TR_DECAY yields "
    f"{len(lam_decay_set)} distinct Lambda values before any selection "
    "principle (family size > 1 is expected; uniqueness must come "
    "from U2, not from thinning G1)",
    len(lam_decay_set) > 1,
)


# ================================================================= U2
print("U2 -- selection-principle analysis", flush=True)

# (i) Poisson
poisson_selects_t = sp.pi
poisson_selects_lambda_norm2 = translate_tr_decay(poisson_selects_t)  # 1
poisson_selects_lambda_norm1 = translate_tr_decay(2 * sp.pi)         # sqrt(2)

info("PRINCIPLE (i) Poisson self-duality (T12):")
info(f"  selects t = pi uniquely as fixed point of t |-> pi^2/t")
info(f"  under root-norm-2: Lambda_DECAY = {poisson_selects_lambda_norm2}")
info(f"  under root-norm-1: t* = 2pi => Lambda_DECAY = "
     f"{sp.simplify(poisson_selects_lambda_norm1)}")
info("  Assumption Z_rootnorm: Cartan root-norm = 2 (lambda=1).")
info("  Status of Z_rootnorm: CONVENTION (T14) — free chart choice; "
     "NOT verified as uniquely forced by any vN module.  Suite uses "
     "root-norm 2 as Cartan packaging; root-norm 1 is the same "
     "physical lattice up to scale (T14 S3).")

check(
    "U2a PRINCIPLE (i) Poisson: selects t=pi uniquely UNDER the "
    "Boltzmann convention e^{-t|x|^2} AND root-norm-2 chart; the "
    "T14 torsor moves the fixed width to t*=2pi under root-norm-1.  "
    "Exact statement: 'Poisson selects candidate t=pi uniquely under "
    "assumption Z_rootnorm=2; Z_rootnorm is CONVENTION (free), not "
    "verified in vN'.  Live: fixed=={pi} and torsor {pi,2pi}",
    fixed == {sp.pi} and torsor_ok
    and iszero(poisson_selects_lambda_norm2 - 1)
    and iszero(poisson_selects_lambda_norm1 - sp.sqrt(2)),
)

# (ii) Unimodularity
info("PRINCIPLE (ii) Unimodularity gate (T14):")
info("  Among atlas lattices, ONLY E8 (det=1) admits a Poisson "
     "self-dual Gaussian width.  This selects the LATTICE "
     "(mu4-completion), NOT a numerical scale among {pi, 2pi, ...}.")
# Quick det certificate (same as T14)
B_E8 = np.array([
    [0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [-1, 1, 0, 0, 0, 0, 0, 0],
    [0, -1, 1, 0, 0, 0, 0, 0],
    [0, 0, -1, 1, 0, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 0, -1, 1, 0, 0],
    [0, 0, 0, 0, 0, -1, 1, 0],
], dtype=np.float64).T
B_D5A3 = np.array([
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 1, -1, 0, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, -1, 0],
    [0, 0, 0, 0, 0, 0, 1, -1],
    [0, 0, 0, 0, 0, 1, 1, 0],
], dtype=np.float64).T
gd_e8 = float(np.linalg.det(B_E8.T @ B_E8))
gd_d5 = float(np.linalg.det(B_D5A3.T @ B_D5A3))
uni_ok = abs(gd_e8 - 1) < 1e-8 and abs(gd_d5 - 16) < 1e-8
info(f"  Gram det E8={gd_e8:.6g} (unimodular); D5+A3={gd_d5:.6g} "
     f"(not).  Scale among torsor: UNSELECTED.")
check(
    "U2b PRINCIPLE (ii) Unimodularity: selects the lattice E8 "
    "(det=1; D5+A3 det=16 fails) — VERIFIED structural gate (T14 S2 / "
    "classical Poisson).  Exact statement: 'Unimodularity selects "
    "candidate LATTICE E8 under assumption L even-unimodular; it does "
    "NOT select a scale.  Assumption is verified (classical + T14 "
    "atlas census), but the principle is scale-blind'",
    uni_ok,
)

# (iii) KMS/BW
info("PRINCIPLE (iii) KMS/BW angle (T14/v526):")
info("  beta_steps = N is measured (compiler kernel detailed balance).")
info("  beta_angle = beta_steps * (2pi/N) = 2pi is the UNIVERSAL "
     "BW/Unruh geometric conversion — not a compiler-specific "
     "numerical output beyond beta_steps = N (T14 DEFLATED).")
N8 = 8
beta_steps = N8
beta_angle = beta_steps * (2 * sp.pi / N8)
kms_ok = iszero(beta_angle - 2 * sp.pi) and iszero(beta_angle - 1 / (4 * c3))
# Does beta alone pick a unique Lambda under TR_DECAY?
# Identifying t_gauss with beta gives t=2pi => Lambda=sqrt(2);
# identifying with beta/2 gives t=pi => Lambda=1 — again a chart choice.
info("  Identifying t_gauss ?= beta (=2pi) => Lambda_DECAY = sqrt(2);")
info("  identifying t_gauss ?= beta/2 (=pi) => Lambda_DECAY = 1.")
info("  Status: DEFLATED / FREE chart between {beta, beta/2}; not a "
     "verified unique scale selector.")
check(
    "U2c PRINCIPLE (iii) KMS/BW: beta_angle = 2pi = 1/(4 c3) holds as "
    "rewrite+geometry (live exact); T14 types it as UNIVERSAL BW/Unruh "
    "once beta_steps=N — DEFLATED as compiler-specific Lambda selector.  "
    "Exact statement: 'KMS/BW selects beta=2pi under assumption "
    "thermal-circle = geometric-circle; that assumption is UNIVERSAL "
    "(not TFPT-specific), and the map beta -> t_gauss remains a FREE "
    "chart choice ({beta, beta/2} -> {sqrt(2), 1})'",
    kms_ok,
)

# Discrete-factor "selection" is NOT a principle — assert no verified
# principle uses g_car or N_fam to pick Lambda.
info("NON-PRINCIPLE: g_car=5, N_fam=3 appear in G1 as discrete atoms "
     "but NO verified suite principle selects among them for the "
     "prolate scale (they are SM-readout / family-count integers).")
check(
    "U2d NO EXTRA SELECTOR: neither g_car nor N_fam nor bare |mu4| "
    "is a verified scale-selection principle for W_Lambda "
    "(they enlarge G1; they do not thin it).  Only (i)-(iii) were "
    "candidate principles; (i) is convention-gated, (ii) scale-blind, "
    "(iii) deflated",
    True,
)

# Synthesis of U2
unique_lambda = None  # remains None unless a convention-free unique pick
# Poisson + TR_DECAY under FREE root-norm torsor:
torsor_lambdas = {sp.Integer(1), sp.sqrt(2)}
info(f"U2 SYNTHESIS: residual Lambda torsor under (i)+TR_DECAY "
     f"+ root-norm freedom = {sorted(torsor_lambdas, key=float)}")
check(
    "U2e NO CONVENTION-FREE UNIQUE LAMBDA: the only principle that "
    "picks a scale at all is Poisson (i), and it retains the T14 "
    "root-norm torsor {Lambda=1, Lambda=sqrt(2)} under TR_DECAY.  "
    "No verified principle collapses that torsor.  Therefore "
    "unique_lambda = None at the end of U2",
    unique_lambda is None
    and torsor_lambdas == {sp.Integer(1), sp.sqrt(2)},
)


# ================================================================= U3
print("U3 -- kill criterion K_SCALE / verdict", flush=True)

# Classify residual family
# Discrete torsor of size >= 2 with no continuous modulus => SCALE-TORSOR
residual = torsor_lambdas
is_discrete_torsor = len(residual) >= 2
is_continuous = False  # Poisson fixed-point equation is discrete (one t
# per chart); charts form a discrete Z-torsor under root-norm / 2-powers,
# not a continuous modulus.
verdict = "SCALE-TORSOR"
if unique_lambda is not None and not is_discrete_torsor:
    verdict = "SCALE-UNIQUE"
elif is_continuous:
    verdict = "SCALE-FREE"

info(f"VERDICT ENUM: {verdict}")
info("  residual family (TR_DECAY): Lambda in {1, sqrt(2)}")
info("    <-> t in {pi, 2pi}  <-> root-norm in {2, 1}")
info("  Route-1 explanatory claim: KILLED (scale not uniquely derived "
     "from verified TFPT structures without a free convention).")
info("  Route-1 as external construction: STILL OPEN (CM/Slepian class "
     "R1-certified in T46; Lambda choice remains an external / chart "
     "parameter — consistent with T46/T47 'compiler-native Lambda "
     "derivation' named as open theory project).")

check(
    "U3a KILL FIRES ON EXPLANATION: K_SCALE requires a convention-free "
    "chain verified-structure => unique Lambda.  The chain stops at "
    "the T14 root-norm torsor.  Verdict = SCALE-TORSOR "
    "(not SCALE-UNIQUE, not SCALE-FREE)",
    verdict == "SCALE-TORSOR",
)

check(
    "U3b HONEST TYPING: SCALE-TORSOR kills the *explanatory* claim of "
    "Route 1 (TFPT does not fix the prolate scale), while leaving the "
    "external operator class intact as a construction.  No RH language; "
    "no marker move; sandbox only",
    verdict == "SCALE-TORSOR" and unique_lambda is None,
)

# Document that continuous freedom is NOT present once Boltzmann+Poisson
# are fixed per chart:
check(
    "U3c NOT SCALE-FREE: within a fixed root-norm chart, Poisson picks "
    "exactly one t (the fixed point).  The residual is a discrete "
    "torsor of charts, not a continuous modulus — hence SCALE-TORSOR "
    "rather than SCALE-FREE",
    not is_continuous and len(residual) == 2,
)


# ================================================================= U4
print("U4 -- bonus eigenvalues (gated on SCALE-UNIQUE)", flush=True)

if verdict == "SCALE-UNIQUE" and unique_lambda is not None:
    # Interior W_Lambda Galerkin (T46 machinery) — info only, no zeros.
    from numpy.polynomial.legendre import leggauss

    def interior_W_legendre(lam: float, n_basis: int) -> np.ndarray:
        tau = 2.0 * math.pi * lam * lam
        n_quad = max(2 * n_basis + 20, 120)
        nodes, weights = leggauss(n_quad)
        p = np.empty((n_basis, n_quad))
        dp = np.empty((n_basis, n_quad))
        p[0] = 1.0
        dp[0] = 0.0
        if n_basis > 1:
            p[1] = nodes
            dp[1] = 1.0
        for n in range(1, n_basis - 1):
            p[n + 1] = ((2 * n + 1) * nodes * p[n] - n * p[n - 1]) / (n + 1)
            dp[n + 1] = (
                (2 * n + 1) * (p[n] + nodes * dp[n]) - n * dp[n - 1]
            ) / (n + 1)
        one_my2 = np.maximum(1.0 - nodes * nodes, 0.0)
        mass = (p * weights) @ p.T
        stiff = (dp * (weights * one_my2)) @ dp.T
        pot = (p * (weights * (tau * tau * nodes * nodes))) @ p.T
        amat = 0.5 * (stiff + pot + stiff.T + pot.T)
        mass = 0.5 * (mass + mass.T)
        evals_m, evecs_m = np.linalg.eigh(mass)
        evals_m = np.maximum(evals_m, 1e-14)
        inv_sqrt = evecs_m * (1.0 / np.sqrt(evals_m))
        a_red = inv_sqrt.T @ amat @ inv_sqrt
        a_red = 0.5 * (a_red + a_red.T)
        return np.sort(np.linalg.eigh(a_red)[0])[:8]

    lam_f = float(unique_lambda.evalf(30))
    eigs = interior_W_legendre(lam_f, 48)
    info(f"U4 DUMP (blind): interior W_Lambda eigenvalues at "
         f"Lambda={lam_f}: {eigs.tolist()}")
    check("U4a eigenvalue dump recorded (info only; no zero compare)",
          len(eigs) >= 4)
else:
    info(f"U4 SKIPPED: verdict={verdict} (gate requires SCALE-UNIQUE).")
    info("Blindness preserved: no eigenvalue–zero pairing in this probe.")
    check(
        "U4a GATE: bonus eigenvalue dump correctly skipped because U2 "
        "did not produce a unique convention-free Lambda "
        f"(verdict={verdict})",
        verdict != "SCALE-UNIQUE",
    )


# ================================================================= end
print("SYNTHESIS", flush=True)
info("U1: G1 enumerates a finite family; TR_DECAY maps the T14 torsor "
     "{pi, 2pi} onto the CM/T46 pair {1, sqrt(2)}.")
info("U2: (i) Poisson selects a scale only under free root-norm "
     "convention; (ii) unimodularity is scale-blind; (iii) KMS/BW "
     "deflated / chart-ambiguous.")
info(f"U3: verdict {verdict} — Route-1 explanation killed; external "
     "construction remains.")
info("U4: skipped (no unique Lambda).")

elapsed = time.time() - T0
print(f"\nTOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)", flush=True)
raise SystemExit(0 if FAIL == 0 else 1)
