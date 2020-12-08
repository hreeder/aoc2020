import pytest

from aoc import day7


@pytest.fixture
def parsed(fixtures):
    with open(fixtures / "day7.txt") as df:
        data = df.read()

    return day7.parse_statements(data)


def test_parser_parses_no_contents(parsed):
    assert "dotted black" in parsed
    assert parsed["dotted black"] == set()


def test_parser_parses_contents(parsed):
    assert "bright white" in parsed
    assert (1, "shiny gold") in parsed["bright white"]
    assert "light red" in parsed
    assert (1, "bright white") in parsed["light red"]
    assert (2, "muted yellow") in parsed["light red"]


def test_part1(fixtures):
    with open(fixtures / "day7.txt") as df:
        data = df.read()

    assert day7.part1(data) == 4


def test_part2(fixtures):
    with open(fixtures / "day7.txt") as df:
        first_data = df.read()

    with open(fixtures / "day7_two.txt") as df:
        second_data = df.read()

    assert day7.part2(first_data) == 32
    assert day7.part2(second_data) == 126
