# 28
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#

import numpy as np
from itertools import count
from more_itertools import take


def main():
    grid_size = 1001
    grid = make_spiral_grid(grid_size)
    return sum_diagonals(grid)


def make_spiral_grid(grid_size):
    grid = [[1]]

    for size in range(3, grid_size + 1, 2):

        right_start = (size - 2) ** 2 + 1
        left_start = size**2 - size

        right_vals = take(size - 2, count(right_start, 1))
        left_vals = take(size - 2, count(left_start, -1))
        top_vals = take(size, count(size**2 - size + 1))
        bot_vals = take(size, count(left_vals[-1] - 1, -1))

        # add left and right values
        for i, _ in enumerate(grid):
            grid[i].insert(0, left_vals[i])
            grid[i].append(right_vals[i])

        # add top and bottom values
        grid.insert(0, top_vals)
        grid.append(bot_vals)

    return np.array(grid)


def sum_diagonals(grid):
    main_diagonal = grid.diagonal()
    off_diagonal = np.flip(grid, axis=1).diagonal()
    return sum(main_diagonal) + sum(off_diagonal) - 1


if __name__ == "__main__":
    main()
