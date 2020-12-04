# Part 2 of this code validates 2 additional passports, return 158 valid
# passports, when the real answer is 156 valid passports, which I
# got by guessing. I'm not finding out why I'm 2 passports off.

import re

VALID_PASSPORT_PROPERTIES = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def validate_byr(year):
    return len(year) == 4 and int(year) >= 1920 and int(year) <= 2002

def validate_iyr(year):
    return len(year) == 4 and int(year) >= 2010 and int(year) <= 2020

def validate_eyr(year):
    return len(year) == 4 and int(year) >= 2020 and int(year) <= 2030

def validate_hgt(height):
    valid_inches = 'in' in height \
        and (int(height.replace('in', '')) >= 150 or int(height.replace('in', '')) <= 193)
    valid_cms = 'cm' in height \
        and (int(height.replace('cm', '')) >= 59 or int(height) <= 76)
    return valid_inches or valid_cms

def validate_hcl(color):
    valid_chars = all(re.compile("[a-f]|[0-9]").match(char) for char in color[1:7])
    return len(color) == 7 and color[0] == "#" and valid_chars

def validate_ecl(color):
    VALID_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return color in VALID_COLORS

def validate_pid(id):
    valid_chars = all(re.compile("[0-9]").match(char) for char in id)
    return valid_chars and len(id) == 9

VALIDATE_PROPERTY = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
    'cid': lambda x: True
}

def create_passports(passport_lines):
    passports = []
    current_passport = []
    for passport_line in passport_lines:
        if passport_line:
            current_passport.append(passport_line)
        else:
            passports.append(current_passport)
            current_passport = []
    passports.append(current_passport)

    return [create_passport(passport) for passport in passports]

def create_passport(passport_lines):
    passport = {}
    for passport_line in passport_lines:
        for property in passport_line.split(' '):
            key, value = property.split(':')
            passport[key] = value
    return passport

def filter_valid_passports(passports):
    valid_passports = []
    for passport in passports:
        if all(property in passport for property in VALID_PASSPORT_PROPERTIES):
            valid_passports.append(passport)
    return valid_passports

def filter_extra_valid_passports(passports):
    valid_passports = []
    for passport in passports:
        if all(VALIDATE_PROPERTY[key](value) for key, value in passport.items()):
            valid_passports.append(passport)
    return valid_passports

def solve_part_1(passport_lines):
    passports = create_passports(passport_lines)
    passports = filter_valid_passports(passports)
    return len(passports)

def solve_part_2(passport_lines):
    passports = create_passports(passport_lines)
    passports = filter_valid_passports(passports)
    passports = filter_extra_valid_passports(passports)
    return len(passports)

with open('./input.txt') as f:
    input = f.read().splitlines()
    print(solve_part_1(input))
    print(solve_part_2(input))
