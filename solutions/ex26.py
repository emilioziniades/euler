# 26
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from itertools import cycle, islice
from decimal import getcontext, Decimal

getcontext().prec = 2_500


def cycle_length(numerator, denominator):
    f = Decimal(numerator) / Decimal(denominator)
    decimals = list(str(f).removeprefix("0."))
    limit = len(decimals) / 2
    for i, _ in enumerate(decimals):
        if i == 0 or i > limit:
            continue
        possible_cycle = list(islice(cycle(decimals[:i]), 0, len(decimals)))
        if possible_cycle == decimals:
            return i
    else:
        return 0


def main():
    cycle_count = {}
    for i in range(2, 1001):
        cycle_count[i] = cycle_length(1, i)

    c = max(cycle_count.items(), key=lambda x: x[1])
    return c[0]


if __name__ == "__main__":
    main()
