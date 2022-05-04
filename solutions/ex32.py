# 32
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


from itertools import permutations


def main():
    # can show that it is either 2-digit * 3-digit or 1-digit * 4-digit
    return sum([sum_pandigital_products(i, j) for i, j in [(2, 3), (1, 4)]])


def sum_pandigital_products(multiplier_digits, multiplicand_digits):
    all_digits = set(range(1, 10))
    pandigital_products = set()

    for i in permutations(all_digits, multiplier_digits):
        remaining_digits = all_digits.difference(i)
        for j in permutations(remaining_digits, multiplicand_digits):
            product_digits_should = remaining_digits.difference(j)
            multiplicand = join_digits(i)
            multiplier = join_digits(j)
            product = multiplicand * multiplier
            product_digits = split_digits(product)
            if len(product_digits) != len(set(product_digits)):
                # some digits repeat in product
                continue
            if set(product_digits) == product_digits_should:
                pandigital_products.add(product)

    return sum(pandigital_products)


def join_digits(digits):
    return int("".join([str(n) for n in digits]))


def split_digits(n):
    return [int(i) for i in str(n)]


if __name__ == "__main__":
    # main()
    print(main())
