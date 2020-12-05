from aoc import day4


def test_parsing(fixtures):
    with open(fixtures / "day4.txt") as df:
        data = df.read()

    passports = day4.parse(data)

    assert 4 == len(passports)


def test_checking(fixtures):
    with open(fixtures / "day4.txt") as df:
        data = df.read()

    passports = day4.parse(data)
    assert 2 == day4.check_missing(*passports)