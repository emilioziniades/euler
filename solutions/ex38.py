# 38
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
from itertools import permutations, count

from util import is_pandigital


def concat_product(n, limit):
    return "".join([str(n * i) for i in range(1, 1 + limit)])


def main():
    digits = "".join([str(i) for i in range(9, 0, -1)])
    pandigitals = ["".join(i) for i in permutations(digits, 9)]  # highest to lowest
    for pd in pandigitals:
        for i, _ in enumerate(pd):  # try 9, 98, 987, etc...
            n = int(pd[: i + 1])
            for j in count(2):  # try i = 1, i = 2 to concatenate product of n
                x = concat_product(n, j)
                pandigital = is_pandigital(x)
                if len(x) > 9:
                    break
                if not pandigital:
                    break
                if pandigital and len(x) == 9:
                    return int(x)


if __name__ == "__main__":
    # main()
    print(main())
