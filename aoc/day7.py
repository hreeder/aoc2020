from aoc.util import load


def parse_statements(data):
    statements = {}

    for line in data.strip().split("\n"):
        colour, contents = line.split(" bags contain ")
        statements[colour] = set()

        if contents == "no other bags.":
            continue

        parts = contents[:-1].split(", ")
        for part in parts:
            part = part.split()
            quantity = int(part[0])
            part_colour = " ".join(part[1:3])
            statements[colour].add((quantity, part_colour))

    return statements


def search(target, collection, node):
    output = []
    for item in collection[node]:
        if item[1] == target:
            return True
        else:
            output.append(search(target, collection, item[1]))

    return any(output)


def part1(data) -> int:
    statements = parse_statements(data)
    count = 0
    for key in statements.keys():
        result = search("shiny gold", statements, key)
        if result:
            count += 1

    return count


def search_contains(collection, current):
    return 1 + sum([item[0] * search_contains(collection, item[1]) for item in collection[current]])


def part2(data) -> int:
    count = 0
    statements = parse_statements(data)
    for item in statements['shiny gold']:
        count += item[0] * search_contains(statements, item[1])
    return count


if __name__ == '__main__':
    data = load(7)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
