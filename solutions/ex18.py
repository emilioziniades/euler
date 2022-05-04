# 18
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum current_total from top to bottom is 23.

example = """
3
7 4
2 4 6
8 5 9 3
"""

# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum current_total from top to bottom of the triangle below:

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

from collections import deque, namedtuple
from typing import List

Position = namedtuple("Position", "row col")


def neighbours(curr: Position) -> List[Position]:
    return [Position(curr.row + 1, curr.col), Position(curr.row + 1, curr.col + 1)]


def to_grid(input: str) -> List[List[int]]:
    return [
        [int(i) for i in j]
        for j in [k.split(" ") for k in input.strip("\n").split("\n")]
    ]


def find_max_total(input: str) -> int:
    numbers = to_grid(input)
    height = len(numbers)
    start = Position(0, 0)
    start_value = numbers[start.row][start.col]
    q = deque([(start, start_value)])
    max_total = 0

    while q:
        current, current_total = q.pop()
        if current_total > max_total:
            max_total = current_total
        left, right = neighbours(current)
        if left.row < height:
            q.appendleft((left, current_total + numbers[left.row][left.col]))
        if right.row < height:
            q.appendleft((right, current_total + numbers[right.row][right.col]))

    return max_total


def main():
    return find_max_total(triangle)


if __name__ == "__main__":
    main()
