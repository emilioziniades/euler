# 19
#
# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def is_leapyear(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


def main():
    day = 0
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            # day at beginning of month
            if day == 0:
                count += 1
            match month:
                case 2 if not is_leapyear(year):
                    n_days = 28
                case 2 if is_leapyear(year):
                    n_days = 29
                case 4 | 6 | 9 | 11:
                    n_days = 30
                case _:
                    n_days = 31
            # day at beginning of next month
            day = ((n_days + day) % 7 - 1) + 1
    return count


if __name__ == "__main__":
    main()
