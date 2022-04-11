# 31
#
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?


def main():
    global coins, count
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    count = 0
    make_from_change(200, coins[0])
    return count


def make_from_change(amount, current_coin):
    global count
    current_coin_index = coins.index(current_coin)
    max_coins = amount // current_coin
    for i in range(max_coins + 1):
        amount_left = amount - i * current_coin
        if amount_left > 0 and current_coin_index < len(coins) - 1:
            next_coin = coins[current_coin_index + 1]
            make_from_change(amount_left, next_coin)
        elif amount_left == 0:
            count += 1
            continue


if __name__ == "__main__":
    main()
