# 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from util import infinite_prime_sieve
from itertools import islice


def main():
    target = 10_001
    primes = infinite_prime_sieve()
    elem = list(islice(primes, target - 1, target))[0]
    return elem


if __name__ == "__main__":
    main()
