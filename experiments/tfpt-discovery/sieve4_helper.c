/* sieve4_helper.c -- PRIME.EULERPICK.N4.SIEVE.01 compiled helper
 *
 * Segmented Eratosthenes sieve over an interval (LO, HI], computing for
 * every PRIME p in the interval (prime powers are handled exactly on the
 * Python side; LO >= 100 so p is odd):
 *
 *   theta   = sum log(p)                          (double-double)
 *   S_j     = sum log(p) * p^(-s_j),  j = 1..4    (double-double each)
 *   s_1 = 5/2,  s_2 = 2,  s_3 = 11/6,  s_4 = 7/4  (s_j = 3/2 + 1/j)
 *
 * SUMMATION-ERROR MODEL (frozen; gated by the Python probe):
 *   p^(-s) is built WITHOUT exp/pow from IEEE-exact primitives:
 *     r  = 1/p          (1 rounding, <= u each, u = 2^-53)
 *     p2 = r*r          -> p^-2      rel err <= 3u
 *     q  = sqrt(p)      -> p^(1/2)   rel err <= u      (IEEE-correct)
 *     q4 = sqrt(q)      -> p^(1/4)   rel err <= 1.5u   (IEEE-correct)
 *     c6 = cbrt(q)      -> p^(1/6)   rel err <= A_CBRT + 0.5u/3
 *     f1 = p2*sqrt(r)   -> p^(-5/2)  rel err <= 5.5u
 *     f2 = p2           -> p^(-2)    rel err <= 3u
 *     f3 = p2*c6        -> p^(-11/6) rel err <= 4u + A_CBRT + u/6
 *     f4 = p2*q4        -> p^(-7/4)  rel err <= 5.5u
 *     l  = log(p)                    rel err <= A_LOG
 *     term_j = l*f_j                 rel err <= A_LOG + err(f_j) + u
 *   ASSUMPTION A (gated pointwise by the probe against mpmath):
 *     libm log and cbrt are <= 2 ulp, i.e. A_LOG, A_CBRT <= 4u.
 *   => per-term relative error <= 13.5u + O(u^2); the probe freezes the
 *   outward bound K_TERM = 32u per term and gates measured deviations at
 *   <= K_TERM/2 (window sums) and <= K_TERM/2 (pointwise samples).
 *   Accumulation is double-double (two_sum + fast_two_sum, Shewchuk/QD):
 *   error <= 4u^2 * |acc| per add, i.e. <= 4*N*u^2*S total -- negligible
 *   (N <= 4e10 => 4Nu^2 < 2e-21).  All terms are positive, so
 *   sum|term| = S and the total enclosure radius used by the probe is
 *     ERR_S(j) = K_TERM*u*S_j + 4*N*u^2*S_j.
 *   theta:  |log^(p) - log p| <= A_LOG*log p <= 4u*log p, summed:
 *     ERR_TH = 4u*theta + 4*N*u^2*theta.
 *   No reassociation: compiled with -O2 (no -ffast-math), FP_CONTRACT OFF.
 *
 * MODES
 *   sieve4_helper sum    LO HI          -> one line:
 *     OK <count> <th_hi> <th_lo> <s1h> <s1l> ... <s4h> <s4l>
 *   sieve4_helper sample LO HI MAXN     -> up to MAXN lines:
 *     P <p> <l> <t1> <t2> <t3> <t4>     (per-prime terms, for the ward)
 *   All numbers printed %.17e (exact double round-trip).
 */

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma STDC FP_CONTRACT OFF

#define SEG_ODDS (1u << 23) /* odds per segment: 8.4M odds = 16.8M span */

typedef struct {
    double hi;
    double lo;
} dd;

/* accumulate double x into dd (Shewchuk two_sum + fast_two_sum) */
static inline void dd_add(dd *a, double x) {
    double s = a->hi + x;
    double b = s - a->hi;
    double e = (a->hi - (s - b)) + (x - b);
    e += a->lo;
    /* fast_two_sum(s, e): |s| >= |e| holds after accumulation */
    double h = s + e;
    a->lo = e - (h - s);
    a->hi = h;
}

static uint64_t isqrt_u64(uint64_t n) {
    uint64_t r = (uint64_t)sqrt((double)n);
    while (r * r > n) r--;
    while ((r + 1) * (r + 1) <= n) r++;
    return r;
}

int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, "usage: %s sum|sample LO HI [MAXN]\n", argv[0]);
        return 2;
    }
    int sample_mode = strcmp(argv[1], "sample") == 0;
    uint64_t LO = strtoull(argv[2], NULL, 10);
    uint64_t HI = strtoull(argv[3], NULL, 10);
    uint64_t maxn = sample_mode ? strtoull(argv[4], NULL, 10) : 0;
    if (LO < 100 || HI <= LO || HI > (1ULL << 52)) {
        fprintf(stderr, "range error\n");
        return 2;
    }

    /* base primes to sqrt(HI) */
    uint64_t R = isqrt_u64(HI);
    uint8_t *base = calloc(R + 1, 1);
    if (!base) return 3;
    uint32_t nbase = 0;
    for (uint64_t i = 3; i * i <= R; i += 2)
        if (!base[i])
            for (uint64_t k = i * i; k <= R; k += 2 * i) base[k] = 1;
    for (uint64_t i = 3; i <= R; i += 2)
        if (!base[i]) nbase++;
    uint64_t *bp = malloc((nbase ? nbase : 1) * sizeof(uint64_t));
    if (!bp) return 3;
    uint32_t nb = 0;
    for (uint64_t i = 3; i <= R; i += 2)
        if (!base[i]) bp[nb++] = i;
    free(base);

    uint8_t *seg = malloc(SEG_ODDS);
    if (!seg) return 3;

    dd th = {0, 0}, S[4] = {{0, 0}, {0, 0}, {0, 0}, {0, 0}};
    uint64_t count = 0, printed = 0;

    uint64_t first = (LO + 1) | 1; /* first odd candidate > LO */
    for (uint64_t seg_lo = first; seg_lo <= HI; seg_lo += 2ULL * SEG_ODDS) {
        uint64_t seg_hi = seg_lo + 2ULL * (SEG_ODDS - 1);
        if (seg_hi > HI) seg_hi = HI;
        uint64_t nodds = (seg_hi - seg_lo) / 2 + 1;
        memset(seg, 0, nodds);
        for (uint32_t bi = 0; bi < nb; bi++) {
            uint64_t q = bp[bi];
            if (q * q > seg_hi) break;
            uint64_t m = (seg_lo + q - 1) / q * q;
            if (m < q * q) m = q * q;
            if (!(m & 1)) m += q;
            for (uint64_t idx = (m - seg_lo) >> 1; idx < nodds; idx += q)
                seg[idx] = 1;
        }
        for (uint64_t i = 0; i < nodds; i++) {
            if (seg[i]) continue;
            uint64_t p = seg_lo + 2 * i;
            double pd = (double)p; /* exact: p < 2^52 */
            double l = log(pd);
            double r = 1.0 / pd;
            double p2 = r * r;
            double q = sqrt(pd);
            double f1 = p2 * sqrt(r);
            double f2 = p2;
            double f3 = p2 * cbrt(q);
            double f4 = p2 * sqrt(q);
            double t1 = l * f1, t2 = l * f2, t3 = l * f3, t4 = l * f4;
            if (sample_mode) {
                printf("P %llu %.17e %.17e %.17e %.17e %.17e\n",
                       (unsigned long long)p, l, t1, t2, t3, t4);
                if (++printed >= maxn) goto done;
                continue;
            }
            count++;
            dd_add(&th, l);
            dd_add(&S[0], t1);
            dd_add(&S[1], t2);
            dd_add(&S[2], t3);
            dd_add(&S[3], t4);
        }
    }
done:
    if (!sample_mode) {
        printf("OK %llu %.17e %.17e", (unsigned long long)count, th.hi,
               th.lo);
        for (int j = 0; j < 4; j++)
            printf(" %.17e %.17e", S[j].hi, S[j].lo);
        printf("\n");
    }
    free(bp);
    free(seg);
    return 0;
}
