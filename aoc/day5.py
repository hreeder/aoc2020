import math
from collections import defaultdict

from aoc.util import load


def part1(boarding_pass):
    row_range = (0, 127)
    col_range = (0, 7)

    for selector in boarding_pass:
        if selector == "F":
            row_range = (row_range[0], math.floor(row_range[1] - ((row_range[1] - row_range[0]) / 2)))
        elif selector == "B":
            row_range = (math.ceil(row_range[0] + ((row_range[1] - row_range[0]) / 2)), row_range[1])
        elif selector == "R":
            col_range = (math.ceil(col_range[0] + ((col_range[1] - col_range[0]) / 2)), col_range[1])
        elif selector == "L":
            col_range = (col_range[0], math.floor(col_range[1] - ((col_range[1] - col_range[0]) / 2)))

    return (row_range[0] * 8) + col_range[0], row_range[0], col_range[0]


if __name__ == '__main__':
    data = load(5)

    highest = 0
    ids = set()
    rows = defaultdict(lambda: [" ", " ", " ", " ", " ", " ", " ", " "])

    for line in data.split("\n"):
        entry = part1(line)
        if entry[0] > highest:
            highest = entry[0]

        rows[entry[1]][entry[2]] = "X"

        ids.add(entry[0])

    print(f"Part 1: {highest}")

    for row_no, row in sorted(rows.items()):
        print(row_no, "".join(row))

    taken = set([id for id in ids if id + 1 in ids and id - 1 in ids])
    not_both_neighbors = (ids - taken)
    gap = list(sorted([id for id in not_both_neighbors if id + 2 in not_both_neighbors or id - 2 in not_both_neighbors]))
    if len(gap) == 2 and gap[1] - gap[0] == 2:
        print(f"Part 2: Seat {gap[1] - 1}")
