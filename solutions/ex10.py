# 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from util import prime_sieve


def main():
    return sum(prime_sieve(2_000_000))


if __name__ == "main":
    main()
