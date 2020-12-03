from aoc.util import load


def part1(data):
    passwords = [line for line in data.split("\n") if line]
    passwords = [password.split(": ") for password in passwords]

    valid = 0

    for policy, password in passwords:
        range, letter = policy.split(" ")
        lower, upper = range.split("-")
        lower = int(lower)
        upper = int(upper)

        if lower <= password.count(letter) <= upper:
            valid += 1

    return valid


def part2(data):
    passwords = [line for line in data.split("\n") if line]
    passwords = [password.split(": ") for password in passwords]

    valid = 0
    for policy, password in passwords:
        if part2_validator(policy, password):
            valid += 1

    return valid


def part2_validator(policy, password) -> bool:
    range, letter = policy.split(" ")
    left, right = range.split("-")
    left = int(left) - 1
    right = int(right) - 1

    if password[left] == letter and password[right] == letter:
        return False

    if password[left] == letter:
        return True

    if password[right] == letter:
        return True

    return False


if __name__ == '__main__':
    data = load(2)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
