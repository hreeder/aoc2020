from dataclasses import dataclass

from aoc.util import load


@dataclass
class Slope:
    lines: list = None

    pos: tuple = (0, 0)

    pattern: tuple = (1, 3)

    @staticmethod
    def from_string(data, **kwargs):
        return Slope(
            lines=[line for line in data.split("\n") if line],
            **kwargs
        )

    @property
    def tree(self) -> bool:
        return self.lines[self.pos[0]][self.pos[1]] == "#"

    def next(self):
        self.pos = (self.pos[0] + self.pattern[0], self.pos[1] + self.pattern[1])

        if self.pos[1] >= len(self.lines[0]):
            new_right = self.pos[1] - len(self.lines[0])
            self.pos = (self.pos[0], new_right)

    @property
    def has_next(self) -> bool:
        return self.pos[0] + self.pattern[0] < len(self.lines)

    def result(self) -> int:
        trees = 0
        trees += 1 if self.tree else 0

        while self.has_next:
            self.next()
            trees += 1 if self.tree else 0

        return trees


if __name__ == '__main__':
    day3_input = load(3)

    slope_1 = Slope.from_string(day3_input, pattern=(1, 1))
    slope_2 = Slope.from_string(day3_input)
    slope_3 = Slope.from_string(day3_input, pattern=(1, 5))
    slope_4 = Slope.from_string(day3_input, pattern=(1, 7))
    slope_5 = Slope.from_string(day3_input, pattern=(2, 1))

    slope_2_result = slope_2.result()
    print(f"Part 1: {slope_2_result}")

    overall = slope_1.result() * slope_2_result * slope_3.result() * slope_4.result() * slope_5.result()
    print(f"Part 2: {overall}")
