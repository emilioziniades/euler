# 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from util import FibonacciNumbers

fn = FibonacciNumbers()

target = 10_001
for i, n in enumerate(fn, 1):
    if i == target:
        print(n)
        break
