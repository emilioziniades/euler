from math import sqrt

"""
t = n(n+1)/2
2t = n^2 + n
n^2 + n - 2t = 0

if the roots of the above quadratic are integers, i.e. n is an integer, then t is a triangle number 
so we plug into quadratic formula:

n = (-1 ± sqrt(1 + 8t))/2

clearly, the only fractional component could come from sqrt(1 + 8t)
if 1+ 8t is a perfect square, then t is a triangle number
"""


def is_perfect_square(n):
    x = sqrt(n)
    return x == int(x)


def sum_letter_counts(word):
    return sum([ord(i) - 64 for i in word.upper()])


def is_triangle_word(word):
    t = sum_letter_counts(word)
    return is_perfect_square(1 + 8 * t)


def main():
    with open("solutions/ex42_words.txt") as f:
        words = [word.strip('"') for word in f.read().split(",")]
    triangle_words = list(filter(is_triangle_word, words))
    return len(triangle_words)


if __name__ == "__main__":
    main()
