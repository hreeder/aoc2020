from aoc import day6


def test_part1(fixtures):
    with open(fixtures / "day6.txt") as df:
        data = df.read()

    assert 11 == day6.part1(data)


def test_part2(fixtures):
    with open(fixtures / "day6_two.txt") as df:
        data = df.read()

    assert 6 == day6.part2(data)
