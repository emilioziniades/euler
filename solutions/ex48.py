from util import digits


def sum_self_powers(n):
    return sum(i**i for i in range(1, n + 1))


def main():
    x = sum_self_powers(1000)
    return str(x)[-10:]


if __name__ == "__main__":
    main()
