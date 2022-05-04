# 34
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from itertools import count
from math import factorial
from util import digits

# precompute factorials
factorials = {i: factorial(i) for i in range(10)}


def sum_factorial_digits(n):
    return sum([factorials[i] for i in digits(n)])


def len_digits(n):
    return len(str(n))


def find_max_digits():
    for i in count(1):
        max_n = int("".join(["9"] * i))
        max_sf = sum_factorial_digits(max_n)
        if len_digits(max_sf) < len_digits(max_n):
            # largest possible i digit number will never create
            # a sum factorial digit with i digits, so consider
            # all numbers with i - 1 digits
            return i - 1
    else:
        return 0


def main():
    max_digits = find_max_digits()
    max_num = int("".join(["9"] * max_digits))
    reciprocal_factorials = []
    for i in range(10, max_num):
        if sum_factorial_digits(i) == i:
            reciprocal_factorials.append(i)
    return sum(reciprocal_factorials)


if __name__ == "__main__":
    main()
