from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLVER_PATH = ROOT / "seam_geodesic_factor.py"


def load_solver():
    spec = importlib.util.spec_from_file_location("seam_geodesic_factor", SOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load seam_geodesic_factor.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SeamGeodesicFactorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solver = load_solver()

    def test_deterministic_miller_rabin_boundary_cases(self) -> None:
        prime = 2_305_843_009_213_693_951
        strong_pseudoprime = 341_550_071_728_321
        self.assertTrue(self.solver.is_probable_prime(prime))
        self.assertFalse(self.solver.is_probable_prime(strong_pseudoprime))

    def test_multiplier_schedule_repairs_multiplier_one_failures(self) -> None:
        cases = {
            31_613: (101, 313),
            34_037: (101, 337),
            45_349: (101, 449),
            62_317: (101, 617),
            67_973: (101, 673),
            78_073: (101, 773),
            19_879: (103, 193),
            28_943: (103, 281),
            46_247: (103, 449),
            58_607: (103, 569),
            59_431: (103, 577),
            78_383: (103, 761),
        }
        for n, expected in cases.items():
            with self.subTest(n=n):
                split = self.solver.geodesic_squfof_split(n, max_iterations=5_000)
                self.assertIsNotNone(split)
                assert split is not None
                self.assertIn(split.factor, expected)
                self.assertEqual(split.factor * split.cofactor, n)
                self.assertGreater(split.multiplier, 1)

    def test_complete_factorization_handles_sign_powers_and_repeated_primes(self) -> None:
        n = -(2**10) * (3**3) * (101**2) * 313
        result = self.solver.factor_integer(n)
        self.assertEqual(result.sign, -1)
        self.assertEqual(result.factor_powers, {2: 10, 3: 3, 101: 2, 313: 1})
        self.assertTrue(result.verified)

    def test_square_and_prime_inputs(self) -> None:
        square = self.solver.factor_integer(1009**4)
        prime = self.solver.factor_integer(2_305_843_009_213_693_951)
        self.assertEqual(square.factor_powers, {1009: 4})
        self.assertEqual(prime.factor_powers, {2_305_843_009_213_693_951: 1})
        self.assertTrue(square.verified)
        self.assertTrue(prime.verified)

    def test_pollard_brent_fallback_is_a_real_alternate_path(self) -> None:
        n = 1_000_003 * 1_000_033
        result = self.solver.factor_integer(n, method="rho", seed=642)
        self.assertEqual(result.factor_powers, {1_000_003: 1, 1_000_033: 1})
        self.assertTrue(any(event.method == "pollard-brent" for event in result.events))

    def test_auto_uses_fallback_above_the_squfof_bit_limit(self) -> None:
        n = 32_416_187_567 * 32_416_190_071
        result = self.solver.factor_integer(n, seed=642)
        self.assertEqual(result.factor_powers, {32_416_187_567: 1, 32_416_190_071: 1})
        self.assertTrue(result.verified)
        self.assertTrue(any(event.method == "pollard-brent" for event in result.events))

    def test_cli_json_is_machine_readable_and_exactly_verified(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SOLVER_PATH), "31613", "633003781", "--json"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload[0]["factor_powers"], {"101": 1, "313": 1})
        self.assertEqual(payload[1]["factor_powers"], {"8821": 1, "71761": 1})
        self.assertTrue(all(row["verified"] for row in payload))

    def test_zero_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "zero"):
            self.solver.factor_integer(0)


if __name__ == "__main__":
    unittest.main()
