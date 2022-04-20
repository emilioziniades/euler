# 40
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

from itertools import count

from more_itertools import nth

from util import digits, product


def champernowne():
    yield from range(1, 10)
    for i in count(1):
        for j in range(10):
            yield from digits(i)
            yield j


def main():
    result = [nth(champernowne(), 1 * 10**i - 1) for i in range(7)]
    return product(result)


if __name__ == "__main__":
    main()
