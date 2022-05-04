"""
Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for
the consecutive integer values 0 <= n <= 39
. However, when n = 40, the quadratic is divisible by 41, and
certainly when n = 41, the quadratic  is clearly divisible by 41.

The incredible formula
n^2 -79n + 1601
was discovered, which produces 80 primes for the consecutive values 0<=n<=79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b

, where abs(a) < 1000 and abs(b) <= 1000

where abs(n) is the modulus/absolute value of n
e.g. abs(11) = 11 and abs(-4) = 4

Find the product of the coefficients a and b, for the quadratic expression
that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""

from util import is_prime, prime_sieve
from itertools import product


def quad(a, b, n):
    return n**2 + a * n + b


def n_primes(a, b):
    n = 0
    q_n = quad(a, b, n)
    while is_prime(q_n):
        n += 1
        q_n = quad(a, b, n)
    return n


def main():
    a_s = range(-1000, 1000)
    # time-saving skip: b must be prime, otherwise n = 0  yields a composite number
    b_s = list(prime_sieve(1000))
    b_s.extend([-1 * i for i in b_s])

    max_primes = 0
    coeff_prod = 0
    for a, b in product(a_s, b_s):
        n = n_primes(a, b)
        if n > max_primes:
            max_primes = n
            coeff_prod = a * b

    return coeff_prod


if __name__ == "__main__":
    main()
