# 33
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""
Represent fraction F = (10a + b) / (10c + d)

The only way one can cancel the digits and obtain the same fraction is if 

1) a = d and F = b / c, which implies bd = 10ac - 9bc
2) b = c and F = a / d, which implies bd = 10ab - 9ad
"""

from itertools import product
from fractions import Fraction


def main():
    digits = range(1, 10)
    fraction_product = Fraction(1, 1)
    for a, b, c, d in product(digits, repeat=4):
        if a == b == c == d:
            continue
        F = Fraction((10 * a + b), (10 * c + d))
        if F > 1:
            continue
        bd = b * d
        condition_1 = a == d and bd == 10 * a * c - 9 * b * c
        condition_2 = b == c and bd == 10 * a * b - 9 * a * d
        if condition_1 or condition_2:
            fraction_product *= F

    return fraction_product.denominator


if __name__ == "__main__":
    main()
