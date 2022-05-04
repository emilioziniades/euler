from itertools import product


def is_triplet(a, b, c):
    return a**2 + b**2 == c**2


def main():
    for a, b in product(range(1, 1001), range(1, 1001)):
        c = 1000 - a - b
        if c < 1:
            continue
        if is_triplet(a, b, c):
            return a * b * c


if __name__ == "__main__":
    print(main())
    main()
