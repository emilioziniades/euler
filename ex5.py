# 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#


def main():
    current = 1
    step = 1
    multiple = 1

    while multiple <= 20:
        if current % multiple == 0:
            step = current
            multiple += 1
            continue
        current += step

    return current


if __name__ == "__main__":
    main()
