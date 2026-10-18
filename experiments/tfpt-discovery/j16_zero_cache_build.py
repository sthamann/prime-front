#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""j16_zero_cache_build -- one-time builder of the verified-zero cache
consumed by j16_verified_zero_supply_probe.py (EXPLORATION ONLY,
experiments/).

Computes the ordinates gamma_1..gamma_N of the first N = 7000
nontrivial zeta zeros with mpmath.zetazero at dps 15 and stores them
as float64 in verified_zeros_n7000.npy (+ meta json).  PEDIGREE: every
ordinate lies far below T0 = 3e12, hence ON the critical line
unconditionally by Platt-Trudgian 2021 (Bull. LMS 53); mpmath computes
the ordinate of the n-th zero via Riemann-Siegel + root refinement to
working precision (~1e-11 absolute at these heights).  The consuming
probe wards the cache (Rosser corridor per index, spacing, gamma_1,
independent |zeta(1/2 + i gamma)| spot checks) and carries an explicit
ordinate-perturbation pad in every bound, so the cache is DATA with a
declared error budget, not an oracle.

Run:  python j16_zero_cache_build.py     (~5 min on 8 cores)
"""
import json
import multiprocessing as mp_proc
import os
import time

import numpy as np

N_Z = 7000
DPS = 15
_HERE = os.path.dirname(os.path.abspath(__file__))
OUT_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
OUT_META = os.path.join(_HERE, "verified_zeros_n7000_meta.json")


def worker(args):
    lo, hi = args
    from mpmath import mp, zetazero
    mp.dps = DPS
    return [(n, float(zetazero(n).imag)) for n in range(lo, hi)]


def main():
    t0 = time.time()
    nproc = max(1, os.cpu_count() - 1)
    chunk = 50
    jobs = [(lo, min(lo + chunk, N_Z + 1))
            for lo in range(1, N_Z + 1, chunk)]
    out = np.zeros(N_Z)
    done = 0
    with mp_proc.Pool(nproc) as pool:
        for res in pool.imap_unordered(worker, jobs):
            for n, g in res:
                out[n - 1] = g
            done += len(res)
            if done % 1000 < chunk:
                print("  %d/%d zeros  [%.0f s]"
                      % (done, N_Z, time.time() - t0), flush=True)
    assert np.all(out > 0.0) and np.all(np.diff(out) > 0.0)
    np.save(OUT_NPY, out)
    with open(OUT_META, "w") as fh:
        json.dump(dict(n_zeros=N_Z, dps=DPS,
                       generator="mpmath.zetazero",
                       gamma_1=out[0], gamma_N=out[-1],
                       built_s=round(time.time() - t0, 1)), fh)
    print("wrote %s  (gamma_1 %.9f, gamma_N %.4f)  [%.0f s]"
          % (OUT_NPY, out[0], out[-1], time.time() - t0))


if __name__ == "__main__":
    main()
