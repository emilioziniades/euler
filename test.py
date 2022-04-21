import unittest
import time

import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12, ex13, ex14, ex15, ex16, ex17, ex18, ex19, ex20, ex21, ex22, ex23, ex24, ex25, ex26, ex27, ex28, ex29, ex30, ex31, ex32, ex33, ex34, ex35, ex36, ex37, ex38, ex39, ex40, ex41, ex42, ex43


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
            (ex27, -59231),
            (ex28, 669171001),
            (ex29, 9183),
            (ex30, 443839),
            (ex31, 73682),
            (ex32, 45228),
            (ex33, 100),
            (ex34, 40730),
            (ex35, 55),
            (ex36, 872187),
            (ex37, 748317),
            (ex38, 932718654),
            (ex39, 840),
            (ex40, 210),
            (ex41, 7652413),
            (ex42, 162),
            (ex43, 16695334890),
        ]
        for ex, want in exercises:
            with self.subTest(i=ex):
                started = time.perf_counter()
                got = ex.main()
                self.assertEqual(got, want)
                elapsed = time.perf_counter() - started
                print(f"{ex.__name__} - {elapsed:.3f}s")


if __name__ == "__main__":
    unittest.main()
