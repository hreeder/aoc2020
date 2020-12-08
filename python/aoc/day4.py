from aoc.util import load

def parse(data) -> list:
    passports = []

    current_passport = {}

    data = data.split("\n")
    for line in data:
        line = line.strip()
        # If this is a blank line, we've got a filled out passport
        if line == "" and current_passport:
            passports.append(current_passport)
            current_passport = {}
            continue

        pairs = line.split(" ")
        for pair in pairs:
            key, val = pair.split(":")
            current_passport[key] = val


    return passports


def check_missing(*passports: list) -> int:
    valid = 0
    for passport in passports:
        required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        if required <= set(passport.keys()):
            valid += 1

    return valid


def validate_fields(*passports: list) -> int:
    valid = 0

    for passport in passports:
        if check_missing(passport) != 1:
            continue

        byr = int(passport['byr'])
        if not 1920 <= byr <= 2002:
            continue

        iyr = int(passport['iyr'])
        if not 2010 <= iyr <= 2020:
            continue

        eyr = int(passport['eyr'])
        if not 2020 <= eyr <= 2030:
            continue

        hgt = passport['hgt']
        if "cm" in hgt and not 150 <= int(hgt[:-2]) <= 193:
            continue
        elif "in" in hgt and not 59 <= int(hgt[:-2]) <= 76:
            continue
        elif "cm" not in hgt and "in" not in hgt:
            continue

        hcl = passport['hcl']
        if hcl[0] != "#":
            continue

        try:
            int(hcl[1:], 16)
        except ValueError:
            continue

        ecl = passport['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue

        pid = passport['pid']
        if len(pid) != 9:
            continue

        try:
            int(pid)
        except ValueError:
            continue

        valid += 1

    return valid


if __name__ == '__main__':
    data = load(4)
    passports = parse(data)

    print(f"Part 1: {check_missing(*passports)}")
    print(f"Part 2: {validate_fields(*passports)}")
