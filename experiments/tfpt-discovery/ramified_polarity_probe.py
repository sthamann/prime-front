#!/usr/bin/env python3
"""Review-Modul 2: PRIME.HECKE.POLARITY.01 -- der Polaritaets-Match.

INZIDENZ-LEMMA UNTER PRUEFUNG (paralleler Worker, woertlich): V = L/(1+i)L
ist symplektisch via der reduzierten hermiteschen Form h-bar, und die 15
Hyperflaechen H_y = y^perp sind die Orthogonal-Raeume.  v738 fand: die
ramifizierte Hecke-Schicht = 15 Hyperebenen von V mit 2:1-Deck.  HIER wird
exakt geprueft, ob die 15 v738-Hecke-Hyperebenen GENAU die h-bar-
Orthogonalraeume {y^perp : y in P} sind, ob die Polaritaets-Identifikation
x |-> x^perp eindeutig ist, und welcher y-Label zu welcher Hecke-Hyperebene
gehoert (Identitaet / kanonische Bijektion?).

KONSTRUKTION (alles modul-intern, exakte Z[i]/F2-Arithmetik, keine
Primtabelle -- AST-erzwungen; Maschinerie read-only aus v738):
  *  L = Z[i]^4 via der v738-HNF-Basis; ambient hermitesche Form
     H(z, z') = sum_c z_c conj(z'_c) auf den gepackten Koordinaten
     (Re H = Standard-Skalarprodukt, J = Multiplikation mit i).
  *  Die KANONISCHE Gitterform: h = H/4 -- gemessen (nicht gesetzt):
     alle H-Gram-Eintraege sind durch 4 teilbar, h ist Z[i]-wertig,
     hermitesch, UNIMODULAR (det Gram = 1) und GERADE (h(x,x) = 2 auf
     den Basisvektoren, Wurzeln h(r,r) = 2).  Das ist die Gaussian-E8-
     Struktur; KEINE Normierungs-Freiheit (H/2 ist noch durchgaengig
     gerade, H/4 ist unimodular -- beides wird gemessen).
  *  h-bar: V x V -> F2 = par(h) (Reduktion mod (1+i), par(a+bi) =
     (a+b) mod 2); wohldefiniert auf Klassen, da h Z[i]-wertig ist.
  *  Die 15 ramifizierten Hecke-Untermoduln aus der v738-Layer-
     Maschinerie ((j0, phi)-Funktionale ueber F2, Hyperebene = ker phi;
     v738 H1.1: Bild von iota-bar = ker phi, 2:1-Deck = ker iota-bar).

PRUEFPUNKTE (alle exakt, keine Stichproben ausser wo vermerkt):
  P1  die Form: Z[i]-wertig/hermitesch/unimodular/gerade; h-bar
      wohldefiniert (konstruktiv: 200 LCG-Repraesentanten-Paare),
      ALTERNIEREND auf allen 16 Klassen, NICHTDEGENERIERT (Rang 4)
      => V ist symplektisch; sigma-bar symplektisch (alle 256 Paare).
  P2  der Match: fuer jede der 15 Hecke-Hyperebenen ker phi gibt es
      GENAU EIN y (unter allen 15 nichttrivialen Klassen) mit
      y^perp = ker phi (Eindeutigkeit exhaustiv, nicht nur via
      Invertierbarkeit); die Zuordnung ist y(phi) = Gbar^{-1} phi --
      eine KANONISCHE LINEARE BIJEKTION, nicht die Identitaet
      (Fixpunkte werden gezaehlt und gedruckt); Absolutpunkt-Eigenschaft
      y(phi) in ker phi (symplektische Polaritaet ist NULL-Polaritaet --
      das ist der Traeger der 7er-Inzidenz); Inzidenz B[x,y] =
      [h-bar(x,y) = 0]: Zeilengrad 7, Diagonale 1, B^2 = 4I + 3J
      (die GQ(2,2)-Numerologie des Stinespring-Workers, hier aus der
      KANONISCHEN Form -- nicht lexikographisch gewaehlt).
  P3  sigma-Funktorialitaet: sigma(y)^perp = sigma(y^perp) fuer alle
      15 y (exhaustiv); die v738-Pushforward-Permutation der 15
      Untermoduln wird intertwined: y(sigma . phi) = sigma-bar(y(phi));
      Orbits 3 fix + 4 x 3 auf den Labels.
  P4  Deck vs. Pruefsummen-Bit: (a) chi_par((1+i)x) = 0 fuer ALLE x
      (Basis + 200 LCG-Vektoren) => das NS/R-Bit steigt auf JEDE
      ramifizierte Faser V(M') ab; (b) konstruktiv ueber alle 15 M',
      alle v in W, beide Deck-Blaetter: chi auf beiden Blaettern gleich
      und == chi_par(v) (Deck und chi KOMMUTIEREN exakt);
      Repraesentanten-Unabhaengigkeit (2 LCG-Shifts pro (M', v)).
  C   Must-fail-Kontrollen: (C1) eine nichtdegenerierte, NICHT
      alternierende Form (Identitaet) zerstoert Null-Polaritaet und
      B^2-Struktur; (C2) ein mutiertes sigma bricht die Invarianz.

KILLS (Review, woertlich, vorregistriert): keine eindeutige
Polaritaets-Identifikation (P1 degeneriert / P2 nicht eindeutig oder
Mengen-Match verletzt); fehlende sigma-Funktorialitaet (P3); Deck nicht
mit dem Pruefsummen-Bit vertraeglich (P4).  Jeder Kill => POLARITY-DEAD.
Verdicts (eingefroren): POLARITY-MATCH / POLARITY-DEAD.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt; kein v563-Fenster-Surface (RESTRICTED-Symbole komplett
verboten, nicht nur declared_-beschraenkt).  Kein Fit, kein freier
Parameter; alle Zahlen exakte Integer/F2.

Vorgaenger (read-only): verification/v738_hecke_mod_ramified.py
(L, V, sigma, die 15 Untermoduln, Deck, chi_par);
experiments/tfpt-discovery/kms_incidence_stinespring_probe.py
(der parallele Worker: waehlte Omega lexikographisch -- hier wird die
kanonische Form aus h hergeleitet und der Anschluss gemessen).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ramified_polarity_probe.py
"""

import ast
import os
import sys
import time
from itertools import permutations

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _VERIFY)

import v738_hecke_mod_ramified as ram  # noqa: E402  (read-only machinery)

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "zetas", "mpz_zeta")
FORBIDDEN_SURFACE = ("U_ALL", "MU_ALL", "LAM_TAB", "G_ALL", "NU_MAIN",
                     "ATOM_MAX", "atoms_in", "atom_lags_at", "arch_lags",
                     "frame_a_zones", "build_window", "odd_toeplitz", "_NN")

CHECKS = []
KILL_FLAGS = []


def check(name, ok, detail="", kill=False):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILL_FLAGS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


_LCG = [20260804]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


ALL_V = ram.ALL_V
NZ = [v for v in ALL_V if any(v)]


def vidx(v):
    return ram.vidx(v)


# ------------------------------------------------------------------ G0
def g0_firewall():
    section("G0 -- AST-Firewall + Umgebung")
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    bad, leaks = [], []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [al.name for al in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.append(node.module)
            for m in mods:
                if any(b in m for b in BANNED_IDS):
                    bad.append(m)
            continue
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
        if name in FORBIDDEN_SURFACE:
            leaks.append(name)
    check("G0.1 keine Primtabellen-/Zeta-Symbole", not bad,
          "gefunden %s" % bad if bad else "sauber")
    check("G0.2 kein v563-Fenster-Surface in dieser Datei (komplett "
          "verboten)", not leaks,
          "Leaks: %s" % leaks if leaks else "sauber")
    print("    python %s" % sys.version.split()[0])


# ------------------------------------------------------------------ S1
def s1_setup():
    section("S1 -- L, V, sigma, die ramifizierte Schicht (v738-Frame, "
            "exakt re-verifiziert)")
    L = ram.Lmodule()
    E = [tuple((1 if j == k else 0, 0) for j in range(4)) for k in range(4)]
    Bamb = [L.to_ambient(e) for e in E]
    check("S1.1 Z[i]-HNF-Basis: abelscher Index N(det) = %d = 256"
          % L.index, L.index == 256, kill=True)

    roots = ram.roots_E8()
    census = {}
    for r in roots:
        c = L.class_of_w(r)
        census[c] = census.get(c, 0) + 1
    check("S1.2 Klassen-Zensus: 240 Wurzeln -> 15 x 16, Nullklasse leer",
          len(census) == 15 and (0, 0, 0, 0) not in census
          and sorted(census.values()) == [16] * 15, kill=True)

    S = [L.coords(ram.pack(ram.sig8(ram.unpack(L.to_ambient(E[k])))))
         for k in range(4)]
    S2 = [[ram.par(S[k][j]) for j in range(4)] for k in range(4)]

    def sigbar(v):
        return tuple((sum(v[k] * S2[k][j] for k in range(4))) & 1
                     for j in range(4))

    ok3 = all(sigbar(sigbar(sigbar(v))) == v for v in ALL_V) \
        and any(sigbar(v) != v for v in ALL_V)
    check("S1.3 sigma-bar: F2-linear, sigma^3 = id, nichttrivial", ok3,
          kill=True)

    ly = ram.Layer("(1+i)", (1, 1))
    check("S1.4 ramifizierte Schicht: 15 Untermoduln (= Hyperebenen-"
          "Funktionale ueber F2)", len(ly.subs) == 15, kill=True)
    return dict(L=L, E=E, Bamb=Bamb, S=S, S2=S2, sigbar=sigbar, ly=ly,
                roots=roots)


# ------------------------------------------------------------------ P1
def gconj(z):
    return (z[0], -z[1])


def herm_amb(z, zp):
    s = (0, 0)
    for c in range(4):
        s = ram.gadd(s, ram.gmul(z[c], gconj(zp[c])))
    return s


def zi_det4(G):
    """exakte Determinante einer 4x4-Z[i]-Matrix (Permutations-Summe)."""
    det = (0, 0)
    for p in permutations(range(4)):
        s = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if p[i] > p[j]:
                    s = -s
        t = (1, 0)
        for i in range(4):
            t = ram.gmul(t, G[i][p[i]])
        det = ram.gadd(det, t if s > 0 else (-t[0], -t[1]))
    return det


def p1_form(ctx):
    section("P1 -- die kanonische Form h = H/4 und ihre Reduktion h-bar")
    L, Bamb = ctx["L"], ctx["Bamb"]
    H = [[herm_amb(Bamb[k], Bamb[l]) for l in range(4)] for k in range(4)]
    div4 = all(H[k][l][0] % 4 == 0 and H[k][l][1] % 4 == 0
               for k in range(4) for l in range(4))
    div8 = all(H[k][l][0] % 8 == 0 and H[k][l][1] % 8 == 0
               for k in range(4) for l in range(4))
    G = [[(H[k][l][0] // 4, H[k][l][1] // 4) for l in range(4)]
         for k in range(4)]
    herm_ok = all(G[l][k] == gconj(G[k][l]) for k in range(4)
                  for l in range(4))
    diag = [G[k][k] for k in range(4)]
    det = zi_det4(G)
    check("P1.1 H-Gram durch 4 teilbar (nicht durch 8): h = H/4 ist "
          "Z[i]-wertig, KEINE Normierungs-Freiheit",
          div4 and not div8, "Diagonale h = %s" % (diag,), kill=True)
    check("P1.2 h hermitesch, GERADE (Diagonale = 2), UNIMODULAR "
          "(det Gram = %s, Norm %d)" % (det, ram.gnorm(det)),
          herm_ok and all(d == (2, 0) for d in diag)
          and ram.gnorm(det) == 1, kill=True)

    # Wurzel-Norm-Kontrolle: h(r, r) = 2 auf 40 Wurzeln
    def h_coords(x, y):
        s = (0, 0)
        for k in range(4):
            for l in range(4):
                s = ram.gadd(s, ram.gmul(ram.gmul(x[k], G[k][l]),
                                         gconj(y[l])))
        return s

    okr = all(h_coords(L.w_coords(r), L.w_coords(r)) == (2, 0)
              for r in ctx["roots"][:40])
    check("P1.3 h(r, r) = 2 auf 40 Wurzeln (E8-Normierung |w|^2/4)", okr)

    Gbar = [[ram.par(G[k][l]) for l in range(4)] for k in range(4)]

    def b(x, y):
        return (sum(x[k] * Gbar[k][l] * y[l]
                    for k in range(4) for l in range(4))) & 1

    # Wohldefiniertheit konstruktiv: 200 LCG-Paare mit (1+i)-Shifts
    pool = [tuple((lcg(5) - 2, lcg(5) - 2) for _ in range(4))
            for _ in range(24)]
    ok_wd = True
    for _ in range(200):
        x = pool[lcg(24)]
        y = pool[lcg(24)]
        sx = tuple(ram.gadd(x[c], ram.gmul((1, 1), pool[lcg(24)][c]))
                   for c in range(4))
        sy = tuple(ram.gadd(y[c], ram.gmul((1, 1), pool[lcg(24)][c]))
                   for c in range(4))
        cx = tuple(ram.par(c) for c in x)
        cy = tuple(ram.par(c) for c in y)
        ok_wd &= (ram.par(h_coords(x, y)) == b(cx, cy))
        ok_wd &= (ram.par(h_coords(sx, sy)) == b(cx, cy))
    check("P1.4 h-bar wohldefiniert auf Klassen (200 konstruktive "
          "Repraesentanten-Paare, (1+i)-Shifts)", ok_wd, kill=True)

    alt_ok = all(b(v, v) == 0 for v in ALL_V)
    sym_ok = all(Gbar[k][l] == Gbar[l][k] for k in range(4)
                 for l in range(4))
    cols = [tuple(Gbar[i][j] for i in range(4)) for j in range(4)]
    rk, _ker, inv = ram.f2_rank_ker_inv(cols)
    check("P1.5 h-bar ALTERNIEREND (alle 16 Klassen) + NICHTDEGENERIERT "
          "(Rang %d) => V ist symplektisch" % rk,
          alt_ok and sym_ok and rk == 4 and inv is not None, kill=True)

    sigbar = ctx["sigbar"]
    ok_sig = all(b(sigbar(x), sigbar(y)) == b(x, y)
                 for x in ALL_V for y in ALL_V)
    check("P1.6 sigma-bar ist SYMPLEKTISCH bzgl. h-bar (alle 256 Paare)",
          ok_sig, kill=True)
    print("    Gbar (Zeilen) = %s" % (Gbar,))
    return dict(G=G, Gbar=Gbar, b=b, inv=inv, h_coords=h_coords)


# ------------------------------------------------------------------ P2
def p2_polarity(ctx, form):
    section("P2 -- der Polaritaets-Match: 15 Hecke-Hyperebenen == "
            "{y^perp}")
    ly = ctx["ly"]
    b, inv = form["b"], form["inv"]
    phis = [tuple(phi) for (_j0, phi) in ly.subs]

    def hyp(phi):
        return frozenset(v for v in ALL_V
                         if (sum(phi[j] * v[j] for j in range(4))) & 1 == 0)

    def perp(y):
        return frozenset(v for v in ALL_V if b(v, y) == 0)

    # Eindeutigkeit exhaustiv: pro Hecke-Hyperebene GENAU EIN y
    tab = {}
    ok_unique = True
    for phi in phis:
        Hs = hyp(phi)
        cands = [y for y in NZ if perp(y) == Hs]
        ok_unique &= (len(cands) == 1)
        if cands:
            tab[phi] = cands[0]
    check("P2.1 Mengen-Match + Eindeutigkeit: jede der 15 Hecke-"
          "Hyperebenen ist GENAU EIN y^perp (exhaustiv ueber alle "
          "15 x 15 Kandidaten)", ok_unique and len(tab) == 15, kill=True)

    ok_formula = all(tab[phi] == ram.f2_matvec(inv, phi) for phi in tab)
    ys = sorted(vidx(y) for y in tab.values())
    fix = [phi for phi in tab if tab[phi] == phi]
    check("P2.2 die Zuordnung ist die kanonische lineare Bijektion "
          "y(phi) = Gbar^{-1} phi; Bild = alle 15 nichttrivialen "
          "Klassen", ok_formula and ys == list(range(1, 16)),
          "Fixpunkte der Koordinaten-Identifikation: %d" % len(fix),
          kill=True)

    ok_abs = all(tab[phi] in hyp(phi) for phi in tab)
    check("P2.3 Absolutpunkte: y(phi) liegt AUF seiner eigenen "
          "Hyperebene (Null-Polaritaet, da h-bar alternierend)", ok_abs)

    B = [[1 if b(x, y) == 0 else 0 for y in NZ] for x in NZ]
    row_ok = all(sum(r) == 7 for r in B)
    diag_ok = all(B[i][i] == 1 for i in range(15))
    sym_ok = all(B[i][j] == B[j][i] for i in range(15) for j in range(15))
    B2 = [[sum(B[i][k] * B[k][j] for k in range(15)) for j in range(15)]
          for i in range(15)]
    b2_ok = all(B2[i][j] == (7 if i == j else 3)
                for i in range(15) for j in range(15))
    check("P2.4 Inzidenz B: Zeilengrad 7, Diagonale 1, symmetrisch, "
          "B^2 = 4I + 3J exakt (GQ(2,2) -- die Stinespring-Numerologie "
          "aus der KANONISCHEN Form)",
          row_ok and diag_ok and sym_ok and b2_ok)

    print("    Zuordnungs-Tabelle phi -> y (als Klassen-Indizes 1..15):")
    line = []
    for phi in phis:
        line.append("%d->%d" % (vidx(phi), vidx(tab[phi])))
    print("      " + "  ".join(line))
    return dict(tab=tab, phis=phis, hyp=hyp, perp=perp, B=B)


# ------------------------------------------------------------------ P3
def p3_sigma(ctx, form, pol):
    section("P3 -- sigma-Funktorialitaet der Polaritaet")
    sigbar = ctx["sigbar"]
    perp, tab = pol["perp"], pol["tab"]

    ok_f = all(frozenset(sigbar(v) for v in perp(y)) == perp(sigbar(y))
               for y in NZ)
    check("P3.1 sigma(y)^perp = sigma(y^perp) fuer ALLE 15 y "
          "(exhaustiv)", ok_f, kill=True)

    # v738-Pushforward-Permutation der Schicht + Intertwining
    ly, S, L = ctx["ly"], ctx["S"], ctx["L"]
    F = ly.F
    Sf = [[F["red"](S[k][j]) for j in range(4)] for k in range(4)]
    Sfinv = ram.field_matinv(F, Sf)
    ok_perm = Sfinv is not None
    ok_int = True
    orbit_perm = {}
    for (j0, phi) in ly.subs:
        u = [F["zero"]] * 4
        for i in range(4):
            for j in range(4):
                u[i] = F["add"](u[i], F["mul"](Sfinv[i][j], phi[j]))
        p0 = next((i for i in range(4) if u[i] != F["zero"]), None)
        if p0 is None:
            ok_perm = False
            break
        s = F["inv"](u[p0])
        psi = tuple(F["mul"](s, x) for x in u)
        if (p0, psi) not in ly.key:
            ok_perm = False
            break
        # Membership-Funktorialitaet: sigma-Bilder der M'-Basis in M'_psi
        for r in ly.m_basis(j0, phi):
            img = ram.tuple_sum_mul(r, S)
            if not ly.member(psi, img):
                ok_perm = False
        orbit_perm[tuple(phi)] = tuple(psi)
        ok_int &= (tab[tuple(psi)] == sigbar(tab[tuple(phi)]))
    check("P3.2 v738-Pushforward permutiert die 15 Untermoduln "
          "(Membership verifiziert) UND intertwined die Polaritaet: "
          "y(sigma . phi) = sigma-bar(y(phi)) fuer alle 15",
          ok_perm and ok_int, kill=True)

    seen, sizes = set(), []
    for phi in orbit_perm:
        if phi in seen:
            continue
        o = [phi]
        x = orbit_perm[phi]
        while x != phi:
            o.append(x)
            x = orbit_perm[x]
        seen |= set(o)
        sizes.append(len(o))
    check("P3.3 Label-Orbits: 3 fix + 4 Drei-Zyklen",
          sorted(sizes) == [1, 1, 1, 3, 3, 3, 3],
          "Orbitlaengen %s" % sorted(sizes))


# ------------------------------------------------------------------ P4
def p4_deck_checksum(ctx):
    section("P4 -- 2:1-Deck vs. NS/R-Pruefsummen-Bit chi_par")
    L, E, ly = ctx["L"], ctx["E"], ctx["ly"]

    def chi_amb(x):
        """ambiente Paritaet w1 mod 2 eines Gittervektors in L-Koords."""
        return ram.unpack(L.to_ambient(x))[0] & 1

    a_par = tuple(chi_amb(E[k]) for k in range(4))

    def chi_par(v):
        return (sum(a * c for a, c in zip(a_par, v))) & 1

    # (a) chi_par((1+i)x) = 0 fuer alle x: Basis + 200 LCG-Vektoren
    aprime = tuple(chi_amb(tuple(ram.gmul((1, 1), E[k][c])
                                 for c in range(4))) for k in range(4))
    ok_desc = (aprime == (0, 0, 0, 0))
    for _ in range(200):
        x = tuple((lcg(7) - 3, lcg(7) - 3) for _ in range(4))
        x1i = tuple(ram.gmul((1, 1), c) for c in x)
        ok_desc &= (chi_amb(x1i) == 0)
        ok_desc &= (chi_amb(x) == chi_par(tuple(ram.par(c) for c in x)))
    check("P4.1 chi_par((1+i)L) = 0 (Basis exakt + 200 LCG-Vektoren): "
          "das Pruefsummen-Bit steigt auf JEDE ramifizierte Faser "
          "V(M') ab; chi_amb == <a_par, Klasse> auf ganz L",
          ok_desc, "a_par = %s, a' = %s" % (a_par, aprime), kill=True)

    # (b) konstruktiv: alle 15 M', alle v in W, beide Deck-Blaetter
    ok_deck = True
    ok_rep = True
    n_pairs = 0
    for (j0, phi) in ly.subs:
        cols = ly.iota_cols(j0, phi)
        rk, ker, _inv = ram.f2_rank_ker_inv(cols)
        if rk != 3 or len(ker) != 1:
            ok_deck = False
            continue
        mb = ly.m_basis(j0, phi)
        for v in ALL_V:
            if (sum(phi[j] * v[j] for j in range(4))) & 1:
                continue
            x = ly.representative(j0, phi, v)
            x3 = list(x)
            x3[j0] = ram.gadd(x3[j0], (1, 1))
            x3 = tuple(x3)
            t = tuple(ram.par(c) for c in ly.mprime_coords(j0, phi, x))
            t3 = tuple(ram.par(c) for c in ly.mprime_coords(j0, phi, x3))
            ok_deck &= (t != t3)                       # echtes 2:1-Deck
            ok_deck &= (ram.f2_matvec(cols, t) == v
                        and ram.f2_matvec(cols, t3) == v)
            # das Pruefsummen-Bit auf beiden Blaettern:
            ok_deck &= (chi_amb(x) == chi_amb(x3) == chi_par(v))
            # Repraesentanten-Unabhaengigkeit: 2 LCG-Shifts um (1+i)M'
            for _ in range(2):
                m2 = [(0, 0)] * 4
                for k in range(4):
                    co = (lcg(3) - 1, lcg(3) - 1)
                    for c in range(4):
                        m2[c] = ram.gadd(m2[c], ram.gmul(co, mb[k][c]))
                x2 = tuple(ram.gadd(x[c], ram.gmul((1, 1), m2[c]))
                           for c in range(4))
                ok_rep &= (chi_amb(x2) == chi_amb(x))
            n_pairs += 1
    check("P4.2 Deck-Kommutation KONSTRUKTIV: %d (M', v)-Paare, beide "
          "Blaetter real transportiert -- chi ist auf beiden Blaettern "
          "gleich und == chi_par(v): Deck und Pruefsummen-Bit "
          "KOMMUTIEREN exakt" % n_pairs,
          ok_deck and n_pairs == 15 * 8, kill=True)
    check("P4.3 Repraesentanten-Unabhaengigkeit des Faser-Bits "
          "(2 LCG-(1+i)M'-Shifts pro Paar)", ok_rep, kill=True)


# ------------------------------------------------------------------ C
def c_controls(ctx, form, pol):
    section("C -- Must-fail-Kontrollen")
    sigbar = ctx["sigbar"]

    # C1: nichtdegenerierte, NICHT alternierende Form (Identitaet)
    def b_id(x, y):
        return (sum(x[k] * y[k] for k in range(4))) & 1

    null_fail = any(b_id(v, v) == 1 for v in NZ)
    Bm = [[1 if b_id(x, y) == 0 else 0 for y in NZ] for x in NZ]
    diag_broken = any(Bm[i][i] == 0 for i in range(15))
    check("C1 nicht-alternierende Kontrollform (Identitaet): "
          "Null-Polaritaet VERLETZT, B-Diagonale nicht mehr konstant 1 "
          "(beides muss brechen -- die Alternierung erzwingt 'alle "
          "Punkte absolut', den Traeger von K = (I + A0)/7; B^2 = "
          "4I + 3J selbst ist dimensions-kombinatorisch und gilt fuer "
          "JEDE nichtdegenerierte Form -- ehrlich vermerkt)",
          null_fail and diag_broken)

    # C2: mutiertes sigma (Vertauschung zweier Basis-Bilder)
    def sig_mut(v):
        w = sigbar(v)
        return (w[1], w[0], w[2], w[3])

    b = form["b"]
    mut_fail = any(b(sig_mut(x), sig_mut(y)) != b(x, y)
                   for x in ALL_V for y in ALL_V)
    check("C2 mutiertes sigma bricht die symplektische Invarianz "
          "(muss brechen)", mut_fail)

    # Zensus: wie kanonisch ist die Form? (informativ)
    S2 = ctx["S2"]
    n_alt = n_nd = n_sig = 0
    first_sig = None
    for bits in range(64):
        M = [[0] * 4 for _ in range(4)]
        idx = 0
        for i in range(4):
            for j in range(i + 1, 4):
                M[i][j] = M[j][i] = (bits >> idx) & 1
                idx += 1
        n_alt += 1
        cols = [tuple(M[i][j] for i in range(4)) for j in range(4)]
        rk, _k, _i = ram.f2_rank_ker_inv(cols)
        if rk != 4:
            continue
        n_nd += 1
        inv_ok = True
        for x in NZ:
            sx = tuple((sum(x[k] * S2[k][j] for k in range(4))) & 1
                       for j in range(4))
            for y in NZ:
                sy = tuple((sum(y[k] * S2[k][j] for k in range(4))) & 1
                           for j in range(4))
                bxy = (sum(x[a] * M[a][c] * y[c]
                           for a in range(4) for c in range(4))) & 1
                bsxy = (sum(sx[a] * M[a][c] * sy[c]
                            for a in range(4) for c in range(4))) & 1
                if bxy != bsxy:
                    inv_ok = False
                    break
            if not inv_ok:
                break
        if inv_ok:
            n_sig += 1
            if first_sig is None:
                first_sig = [row[:] for row in M]
    Gbar = form["Gbar"]
    is_first = (first_sig == [list(r) for r in Gbar])
    print("    Zensus: 64 alternierende Formen, %d nichtdegeneriert, "
          "%d davon sigma-invariant" % (n_nd, n_sig))
    print("    h-bar %s die lexikographisch erste sigma-invariante "
          "nichtdegenerierte Form (Worker-Wahl: lexikographisch; hier: "
          "KANONISCH aus h -- die Mehrdeutigkeit der Wahl ist damit "
          "aufgeloest)" % ("IST" if is_first else "ist NICHT"))
    check("C3 Kanonizitaet: h-bar ist sigma-invariant nichtdegeneriert "
          "alternierend; der Worker-Wahlraum hat %d Elemente -- die "
          "hermitesche Herleitung fixiert EINE Form ohne Wahl" % n_sig,
          n_sig >= 1)


# ------------------------------------------------------------------ verdict
def verdict():
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    if KILL_FLAGS:
        v = "POLARITY-DEAD"
        note = ("Kill gefeuert (Review-Kriterium, woertlich): %s"
                % KILL_FLAGS[:3])
    elif n_pass == n_all:
        v = "POLARITY-MATCH"
        note = ("die 15 ramifizierten Hecke-Hyperebenen sind EXAKT die "
                "h-bar-Orthogonalraeume; Polaritaet eindeutig, "
                "kanonisch-linear (nicht Identitaet), sigma-funktoriell; "
                "Deck kommutiert mit dem Pruefsummen-Bit.")
    else:
        v = "POLARITY-MATCH (Konstruktions-Caveats)"
        note = "Nicht-Kill-Checks gescheitert -- siehe FAIL-Zeilen."
    print("%d/%d Checks bestanden" % (n_pass, n_all))
    print("VERDICT: %s" % v)
    print("PRIME.HECKE.POLARITY.01: %s -- %s" % (v, note))
    return n_pass == n_all


def main():
    t0 = time.time()
    print("=" * 74)
    print("PRIME.HECKE.POLARITY.01 -- Review-Modul 2: der "
          "Polaritaets-Match auf V = L/(1+i)L")
    print("=" * 74)
    g0_firewall()
    ctx = s1_setup()
    form = p1_form(ctx)
    pol = p2_polarity(ctx, form)
    p3_sigma(ctx, form, pol)
    p4_deck_checksum(ctx)
    c_controls(ctx, form, pol)
    ok = verdict()
    print("Gesamtlaufzeit %.1f s" % (time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
