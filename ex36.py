# 36

# The decimal number 585 = 1001001001 (binary) is palindromic in both bases
# Find the total of all numbers, less than one million, which are palindromic in base 10 and base 2
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from util import is_palindrome


def main():
    total = 0
    for n in range(1_000_000):
        if not is_palindrome(n):
            continue
        n_2 = f"{n:b}"
        if not is_palindrome(n_2):
            continue
        total += n
    print(total)
    return total


if __name__ == "__main__":
    main()
