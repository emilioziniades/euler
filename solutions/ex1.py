# 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

from util import multiples


def main():
    limit = 1000
    mul_35 = set()
    mul_35.update(multiples(3, limit))
    mul_35.update(multiples(5, limit))
    return sum(mul_35)


if __name__ == "__main__":
    main()
