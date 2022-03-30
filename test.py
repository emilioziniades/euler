import unittest
import time

import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12, ex13, ex14, ex15, ex16, ex17, ex18, ex19, ex20, ex21, ex22, ex23, ex24, ex25, ex26


class TestEulerSolutions(unittest.TestCase):
    def test_exercises(self):
        exercises = [
            (ex1, 233168),
            (ex2, 4613732),
            (ex3, 6857),
            (ex4, 906609),
            (ex5, 232792560),
            (ex6, 25164150),
            (ex7, 104743),
            (ex8, 23514624000),
            (ex9, 31875000),
            (ex10, 142913828922),
            (ex11, 70600674),
            (ex12, 76576500),
            (ex13, 5537376230),
            (ex14, 837799),
            (ex15, 137846528820),
            (ex16, 1366),
            (ex17, 21124),
            (ex18, 1074),
            (ex19, 171),
            (ex20, 648),
            (ex21, 31626),
            (ex22, 871198282),
            (ex23, 4179871),
            (ex24, 2783915460),
            (ex25, 4782),
            (ex26, 983),
        ]
        for ex, want in exercises:
            with self.subTest(i=ex):
                started = time.time()
                got = ex.main()
                self.assertEqual(got, want)
                elapsed = time.time() - started
                print(f"{ex.__name__} - {elapsed:.2f}s")


if __name__ == "__main__":
    unittest.main()
