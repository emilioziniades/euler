# 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#
from collections import deque, namedtuple
from math import comb

Point = namedtuple("Point", "x y")
size = 20


def main():
    start = Point(0, 0)
    end = Point(size, size)
    q = deque([start])
    route_count = {}

    while q:
        curr = q.pop()
        if end in route_count:  # finished
            break
        if curr in route_count:  # visited already
            continue
        if curr.x is start.x or curr.y is start.y:  # on edge
            route_count[curr] = 1
        else:  # not on edge
            route_count[curr] = sum([route_count[pt] for pt in neighbours(curr, -1)])
        q.extendleft(neighbours(curr, 1))

    return route_count[end]


def neighbours(point, diff):
    return [
        Point(x, y)
        for x, y in [(point.x + diff, point.y), (point.x, point.y + diff)]
        if 0 <= x <= size and 0 <= y <= size
    ]


def easier_solution(grid_size):
    return comb(grid_size * 2, grid_size)


if __name__ == "__main__":
    main()
