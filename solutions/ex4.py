# 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product
from util import is_palindrome


def main():
    palindromes = []
    start = 100
    end = 1000
    for i, j in product(range(start, end), range(start, end)):
        current = i * j
        if is_palindrome(current):
            palindromes.append(current)

    return max(palindromes)


if __name__ == "__main__":
    main()
