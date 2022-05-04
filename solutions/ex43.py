# 43
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-n divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

from util import from_digits


def is_substring_divisible(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for prime, start in zip(primes, range(1, 8)):
        if prime == 2 or prime == 5:
            # d2-d4 divisible by 2 and d4-d6 divisible by 5 true by construction
            continue
        substring = str(n)[start : start + 3]
        if int(substring) % prime != 0:
            return False
    return True


def main():
    substring_divisibles = list()

    d4_possible = [0, 2, 4, 6, 8]
    for d4 in d4_possible:
        d6_possible = set([0, 5])
        d6_possible.discard(d4)
        for d6 in d6_possible:
            d_possible = set(range(10)) - set([d4, d6])
            for digits in permutations(d_possible, r=8):
                (d1, d2, d3, d5, d7, d8, d9, d10) = digits
                number = from_digits((d1, d2, d3, d4, d5, d6, d7, d8, d9, d10))
                if is_substring_divisible(number):
                    substring_divisibles.append(number)

    return sum(substring_divisibles)


if __name__ == "__main__":
    main()
