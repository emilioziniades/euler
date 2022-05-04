# 41
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations

from util import from_digits, is_prime, is_pandigital


def main():
    # start with largest pandigital numbers, check if prime
    for i in range(9, 0, -1):
        for digits in permutations(range(i, 0, -1), r=i):
            n = from_digits(digits)
            if not is_prime(n):
                continue
            if not is_pandigital(n):
                continue
            return n


if __name__ == "__main__":
    print(main())
