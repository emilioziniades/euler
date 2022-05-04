# 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
#
numbers = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def write_number(n):
    digits = list(str(n))
    match len(digits):
        case 1:
            return numbers[n]
        case 2:
            if n in numbers:
                return numbers[n]
            return numbers[int(digits[0]) * 10] + numbers[int(digits[1])]
        case 3:
            if n % 100 == 0:
                return numbers[n / 100] + "hundred"
            return "".join(
                [
                    numbers[int(digits[0])],
                    "hundredand",
                    write_number(int("".join(digits[1:]))),
                ]
            )
        case 4:
            return "onethousand"


def main():
    return sum([len(write_number(i)) for i in range(1, 1001)])


if __name__ == "__main__":
    main()
