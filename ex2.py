# 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#

from util import FibonacciNumbers


def main():
    fn = FibonacciNumbers()
    return sum([i for i in fn.until(4_000_000) if i % 2 == 0])


if __name__ == "__main__":
    main()
