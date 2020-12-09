from copy import deepcopy
from dataclasses import dataclass, field

from aoc.util import load


@dataclass
class Machine:
    program: list

    accumulator: int = 0
    visited: list = field(default_factory=lambda: [])
    position: int = 0
    complete: bool = False

    @staticmethod
    def from_data(data):
        program = []
        for num, line in enumerate(data.strip().split("\n")):
            line = line.split()
            program.append((num, line[0], line[1]))

        return Machine(program=program)

    def step(self):
        if self.position >= len(self.program):
            self.complete = True
            return

        line, command, value = self.program[self.position]

        if command == "nop":
            self.position += 1
        elif command == "acc":
            self.accumulator += int(value)
            self.position += 1
        elif command == "jmp":
            self.position += int(value)

        self.visited.append(line)

    def run(self):
        while (not self.complete) and (self.position not in self.visited):
            self.step()


def part1(data):
    machine = Machine.from_data(data)
    while machine.position not in machine.visited:
        machine.step()
    return machine.accumulator


def part2(data):
    parsed = Machine.from_data(data)
    for line in parsed.program:
        line, command, value = line
        if command == "acc":
            continue

        program = deepcopy(parsed.program)
        program[line] = (line, "nop" if command == "jmp" else "jmp", value)

        machine = Machine(program=program)
        machine.run()

        if machine.complete:
            return machine.accumulator


if __name__ == '__main__':
    data = load(8)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
