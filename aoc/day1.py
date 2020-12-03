import itertools
import math

from aoc.util import load


def part1(report, repeat):
    report = report.split("\n")
    report = [int(entry) for entry in report if entry]

    for thing in itertools.product(report, repeat=repeat):
        if sum(thing) == 2020:
            return math.prod(thing)


if __name__ == '__main__':
    day1_input = load(1)

    print(f"Part 1: {part1(day1_input, 2)}")
    print(f"Part 2: {part1(day1_input, 3)}")
