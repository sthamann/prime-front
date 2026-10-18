"""v817 Prime Front scope: prime packet-state finite summability instance.

Scope extraction from original module at ba2f0fc; original ID and
mathematical statements preserved. Original full source is retained
in the extraction provenance; no proof/status promotion.
"""
import math

import time

import numpy as np

N_THETA = 16500

LADDER0 = 256

KP = 6

PRATE_BAR = 0.85

PENV_BASE = 0.75

CTRL_PRIME_BAR = 0.02

CHECKS = []

def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name
          + ("  -- " + detail if detail else ""))
    return ok

def section(title):
    print("\n-- %s --" % title)

def sparse_theta_terms(kind, cap):
    out = []
    if kind in ("th3", "th4"):
        out.append((0, 1))
        n = 1
        while n * n <= cap:
            out.append((n * n, 2 if kind == "th3" else 2 * ((-1) ** n)))
            n += 1
    else:                                   # th2-type: odd squares
        o = 1
        while o * o <= cap:
            out.append((o * o, 2))
            o += 2
    return out

def sparse_mul(dense, terms):
    out = np.zeros_like(dense)
    for e, c in terms:
        if e == 0:
            out += c * dense
        else:
            out[e:] += c * dense[:-e]
    return out

def build_thetas():
    """exact class thetas Th_j, sigma3, f8 coefficients to N_THETA."""
    sig3 = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(1, N_THETA + 1):
        sig3[d::d] += d ** 3
    scap = 2 * N_THETA
    t3 = sparse_theta_terms("th3", scap)
    t4 = sparse_theta_terms("th4", scap)
    one = np.zeros(scap + 1, dtype=np.int64)
    one[0] = 1
    p3 = one.copy()
    p4 = one.copy()
    for _ in range(8):
        p3 = sparse_mul(p3, t3)
        p4 = sparse_mul(p4, t4)
    m53 = one.copy()
    for _ in range(5):
        m53 = sparse_mul(m53, t3)
    for _ in range(3):
        m53 = sparse_mul(m53, t4)
    m35 = one.copy()
    for _ in range(5):
        m35 = sparse_mul(m35, t4)
    for _ in range(3):
        m35 = sparse_mul(m35, t3)
    num0 = p3 + m53 + m35 + p4
    num2 = p3 - m53 - m35 + p4
    ok_div = bool(np.all(num0 % 4 == 0) and np.all(num2 % 4 == 0))
    Th0 = (num0 // 4)[::2][:N_THETA + 1].copy()
    Th2 = (num2 // 4)[::2][:N_THETA + 1].copy()
    tcap = 8 * N_THETA
    t2 = sparse_theta_terms("th2", tcap)
    acc = np.zeros(tcap + 1, dtype=np.int64)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    ok_div &= bool(np.all(acc[::8][:N_THETA + 1] % 4 == 0))
    Th1 = (acc[::8][:N_THETA + 1] // 4).copy()
    # f8 eta recurrence (exact; int64 dot certified by the -8f8 gate)
    tk = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(2, N_THETA + 1, 2):
        tk[d::d] += d * (4 + (4 if d % 4 == 0 else 0))
    g = np.zeros(N_THETA, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_THETA):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        if r != 0:
            return None
        g[n] = q
    a = np.zeros(N_THETA + 1, dtype=np.int64)
    a[1:] = g
    return dict(sig3=sig3, Th_real=(Th0, Th1, Th2, Th1), a=a,
                ok_div=ok_div)

def primes_upto(N):
    s = np.ones(N + 1, bool)
    s[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]

def build_events(cap):
    """prime-power events n <= cap: (n, Lambda(n)/sqrt(n), channel)."""
    ev = []
    for p in primes_upto(cap):
        m, n = 1, int(p)
        while n <= cap:
            if p == 2:
                ch = "ro" if m % 2 == 1 else "re"
            else:
                ch = "sp" if p % 4 == 1 else "in"
            ev.append((n, math.log(p) / math.sqrt(n), ch))
            m += 1
            n *= int(p)
    ev.sort()
    return ev

SECTORS = [(e, v, j) for e in (1, -1) for v in ("v1", "v7")
           for j in (0, 1, 2)]

MULT = np.array([(2 if v == "v1" else 14) * (2 if j == 1 else 1)
                 for e, v, j in SECTORS], float)

def event_profile(n, ch, th, mode="true"):
    """per-event GNS sector values t^2/nu over the 12 classes."""
    sig3, a = th["sig3"], th["a"]
    Th0, Th1, Th2, Th3 = th["Th_real"]
    E = 240.0 * float(sig3[n])
    c2m = float(a[n]) / float(sig3[n])
    if mode == "ep":
        c2m = math.cos(2.0 * math.log(n))
    if mode == "scr" and ch in ("sp", "in") \
            and int(math.log2(n)) % 2 == 1:
        ch = "ro"
    mh = (1.0, (float(Th0[n]) - float(Th2[n])) / E,
          (float(Th0[n]) - float(Th1[n]) + float(Th2[n])
           - float(Th3[n])) / E)
    t = np.empty(12)
    for k, (e, v, j) in enumerate(SECTORS):
        c2f = 1.0 if e == 1 else c2m
        vf = (-1.0 / 7.0) if (ch == "ro" and v == "v7") else 1.0
        t[k] = c2f * vf * mh[j]
    nu = float((t * t) @ MULT) / 128.0
    return (t * t) / nu

def l1_state(qa, qb):
    """state norm on C[G]: l1 over the 128 characters."""
    return float(np.abs(qa - qb) @ MULT) / 128.0

def leg_prime(th):
    section("C: INSTANCE 2 -- prime/packet (ladder N_k = %d * 2^k)"
            % LADDER0)
    t0 = time.time()
    sig3 = th["sig3"]
    Th0, Th1, Th2, Th3 = th["Th_real"]
    a = th["a"]
    heads = (int(Th0[1]), int(Th1[1]), int(Th2[1]), int(Th3[1]))
    tot_ok = bool(np.all((Th0 + Th1 + Th2 + Th3)[1:]
                         == 240 * sig3[1:]))
    f8_ok = bool(np.all((Th0 - Th2 + 8 * a)[1:N_THETA:2] == 0))
    check("C1 packet layer exact: heads %s == (52,64,60,64); glue "
          "identity ALL n <= %d; Th1 == Th3; Th0 - Th2 = -8 f8 on ALL "
          "odd n" % (str(heads), N_THETA),
          th["ok_div"] and heads == (52, 64, 60, 64) and tot_ok
          and f8_ok and bool(np.all(Th1 == Th3)))

    ev = build_events(N_THETA)
    P = np.array([event_profile(n, ch, th) for n, w, ch in ev])
    W = np.array([w for n, w, ch in ev])
    Narr = np.array([n for n, w, ch in ev])
    ladder = [LADDER0 * 2 ** k for k in range(KP + 1)]
    rows, zs = [], []
    for Nk in ladder:
        m = Narr <= Nk
        z = float(W[m].sum())
        zs.append(z)
        rows.append((W[m] @ P[m]) / z)
    wards = [abs(float(r @ MULT) / 128.0 - 1.0) for r in rows]
    ok_pos = bool(np.all(P >= -1e-15)) and \
        all(bool(np.all(r >= -1e-15)) for r in rows)
    check("C2 register states: %d events, all per-event sector values "
          ">= 0; census rows >= 0 at all %d depths; unit ward <= %.0e "
          "(max %.1e)" % (len(ev), len(ladder), 1e-9, max(wards)),
          ok_pos and max(wards) <= 1e-9)

    ok_cvx = True
    for k in range(KP):
        m_new = (Narr > ladder[k]) & (Narr <= ladder[k + 1])
        w_sh = float(W[m_new].sum())
        t = w_sh / zs[k + 1]
        nu_sh = (W[m_new] @ P[m_new]) / w_sh
        ident = np.abs((1 - t) * rows[k] + t * nu_sh
                       - rows[k + 1]).max()
        ok_cvx &= (0.0 < t < 1.0) and ident < 1e-12 \
            and bool(np.all(nu_sh >= -1e-15)) \
            and abs(float(nu_sh @ MULT) / 128.0 - 1.0) <= 1e-9
    check("C3 ladder transitions convex/CP: q_{k+1} = (1-t) q_k + "
          "t nu_shell, t in (0,1), nu_shell a state (identity 1e-12)",
          ok_cvx)

    deltas = [l1_state(rows[k + 1], rows[k]) for k in range(KP)]
    print("   PRIME state defects (l1 over 128 characters):")
    print("   %3s %14s %12s %8s" % ("k", "N -> 2N", "delta_k", "ratio"))
    for k in range(KP):
        r = deltas[k] / deltas[k - 1] if k >= 1 else float("nan")
        print("   %3d %6d->%-6d %12.3e %8.3f"
              % (k, ladder[k], ladder[k + 1], deltas[k], r))
    ok_rate = all(deltas[k] <= PRATE_BAR * deltas[k - 1]
                  for k in range(1, KP))
    Cp = 2 * deltas[0]
    ok_env = all(deltas[k] <= Cp * PENV_BASE ** k + 1e-15
                 for k in range(1, KP))
    rate_fit = (deltas[KP - 1] / deltas[1]) ** (1.0 / (KP - 2))
    check("C4 THE NEW NUMBER -- prime state defects SUMMABLE: ratios "
          "<= %.2f; envelope delta_k <= 2 delta_0 (3/4)^k; fitted "
          "rate %.3f/doubling vs dilution law 2^-1/2 = 0.707; "
          "sum of tail defects = %.3e"
          % (PRATE_BAR, rate_fit, sum(deltas[1:])),
          ok_rate and ok_env)
    c4_ok = ok_rate and ok_env

    ok_tail = True
    for k in range(1, KP + 1):
        lhs = l1_state(rows[KP], rows[k])
        bar = 4 * Cp * PENV_BASE ** k
        ok_tail &= lhs <= bar + 1e-12
    check("C5 Cauchy tail on every rung: ||q_last - q_k||_1 <= "
          "4 C (3/4)^k", ok_tail)
    print("   (6) closure datum: sector-adapted Gamma_R continua live "
          "on the WINDOW face [typed]; the state-face open item is "
          "the SECTOR FLOOR (GL1 sign sector), not summability.")
    print("   (7) Mosco form family [typed, parallel strand]."
          "   (%.1f s)" % (time.time() - t0))
    return dict(deltas=deltas, rate=rate_fit, rows=rows, ev=ev,
                ladder=ladder, c4_ok=c4_ok)

def leg_controls(th, gnet=None):
    ev = build_events(N_THETA)
    W = np.array([w for n, w, ch in ev])
    Narr = np.array([n for n, w, ch in ev])
    ladder = [LADDER0 * 2 ** k for k in range(KP + 1)]
    for mode, name, why in (
            ("scr", "K2", "label scramble (V-frame misassignment, "
             "alternating shells)"),
            ("ep", "K3", "Epstein-type drift c2m -> cos(2 ln n) "
             "(off-line oscillation surrogate)")):
        Pm = np.array([event_profile(n, ch, th, mode) for n, w, ch in ev])
        rows = [(W[Narr <= Nk] @ Pm[Narr <= Nk])
                / float(W[Narr <= Nk].sum()) for Nk in ladder]
        dm = [l1_state(rows[k + 1], rows[k]) for k in range(KP)]
        check("%s fires: prime %s: min(delta_4, delta_5) = %.3e > %.2f"
              " -- summability breaks"
              % (name, why, min(dm[4], dm[5]), CTRL_PRIME_BAR),
              min(dm[4], dm[5]) > CTRL_PRIME_BAR)

def run():
    CHECKS.clear()
    th = build_thetas()
    if th is None:
        return 1
    leg_prime(th)
    leg_controls(th)
    failed = [n for n, ok in CHECKS if not ok]
    print("v817 Prime Front packet scope: %d/%d checks passed; finite hypothesis checks only" % (len(CHECKS)-len(failed),len(CHECKS)))
    return 0 if not failed else 1

if __name__ == "__main__":
    raise SystemExit(run())
