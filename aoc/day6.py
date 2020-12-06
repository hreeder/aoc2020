from aoc.util import load


def part1(data):
    groups = data.split("\n\n")

    count = 0

    for group in groups:
        group = group.replace("\n", "")
        group = set([question for question in group])
        count += len(group)

    return count


def part2(data):
    count = 0

    for group in data.split("\n\n"):
        sets = [{question for question in person} for person in group.split()]

        result = None
        for item in sets:
            if result is None:
                result = item
            elif result.isdisjoint(item):
                result = set()
            else:
                result = result & item

        count += len(result)

    return count


if __name__ == '__main__':
    data = load(6)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
