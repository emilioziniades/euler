# 37
#
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from util import infinite_prime_sieve

primes = set()


def is_truncatable_prime(n, left=True):
    if n < 10:
        return False
    while True:
        if n not in primes:
            return False
        if len(str(n)) == 1:
            break
        n = int(str(n)[1:]) if left else int(str(n)[:-1])

    return True


def main():
    truncatable_primes = []
    for p in infinite_prime_sieve():
        primes.add(p)
        if len(truncatable_primes) == 11:
            break
        if is_truncatable_prime(p, left=True) and is_truncatable_prime(p, left=False):
            truncatable_primes.append(p)

    return sum(truncatable_primes)


if __name__ == "__main__":
    main()
