import unittest
import time

import ex2, ex10, ex11, ex12, ex13, ex14, ex15, ex16, ex17, ex18, ex19


class TestEulerSolutions(unittest.TestCase):
    def test_exercises(self):
        exercises = [
            (ex2, 4613732),
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
