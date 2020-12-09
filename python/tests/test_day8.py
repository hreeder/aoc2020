from aoc import day8

def test_part1(fixtures):
    with open(fixtures / "day8.txt") as df:
        data = df.read()

    assert day8.part1(data) == 5


def test_part2(fixtures):
    with open(fixtures / "day8.txt") as df:
        data = df.read()

    assert day8.part2(data) == 8
