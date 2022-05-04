# 39
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?


from collections import defaultdict
from itertools import count


def pythagorean_triplets(limit):
    c, m = 0, 2
    while c < limit:
        for n in range(1, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            if c > limit:
                break
            yield a, b, c
        m += 1


def main():
    limit = 1000
    triplets = set()
    for a, b, c in pythagorean_triplets(limit):
        for n in count(1):
            na, nb, nc = n * a, n * b, n * c
            if na + nb + nc > limit:
                break
            triplets.add((na, nb, nc))

    perimeters: dict = defaultdict(lambda: 0)
    for a, b, c in triplets:
        perimeters[a + b + c] += 1

    return max(perimeters, key=perimeters.get)


if __name__ == "__main__":
    main()
