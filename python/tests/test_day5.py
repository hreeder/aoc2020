from aoc import day5

def test_part_1():
    assert 357 == day5.part1("FBFBBFFRLR")[0]
    assert 567 == day5.part1("BFFFBBFRRR")[0]
    assert 119 == day5.part1("FFFBBBFRRR")[0]
    assert 820 == day5.part1("BBFFBBFRLL")[0]
