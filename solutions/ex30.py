# 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 44
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from util import digits
from itertools import count, permutations

pow = 5
# precompute powers
powers = {i: i**pow for i in range(0, 10)}


def sum_power_digits(n):
    return sum(map(lambda x: powers[x], digits(n)))


def find_max_digits():
    for i in count(1):
        num = int("9" * i)
        max_sum = sum_power_digits(num)
        if i > len(digits(max_sum)):
            # even with the largest possible sum, i*9^5,
            # we still cannot reach a number with i digits
            # so return i - 1
            return i - 1
    else:
        return 0


def main():
    sum = 0
    max_digits = find_max_digits()
    for i in range(2, max_digits * (9**pow)):
        digits_power = sum_power_digits(i)
        if digits_power == i:
            sum += i
    return sum


if __name__ == "__main__":
    main()
