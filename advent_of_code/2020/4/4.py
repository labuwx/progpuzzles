#!/usr/bin/env python3

import re

allowed_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}


def check1(passport):
    return passport.keys() ^ allowed_fields <= {'cid'}


def check2(passport):
    if not check1(passport):
        return False

    isvalid = (
        bool(re.match(r'^\d{4}$', passport['byr']))
        and (1920 <= int(passport['byr']) <= 2002)
        and bool(re.match(r'^\d{4}$', passport['iyr']))
        and (2010 <= int(passport['iyr']) <= 2020)
        and bool(re.match(r'^\d{4}$', passport['eyr']))
        and (2020 <= int(passport['eyr']) <= 2030)
        and bool(hgt_m := re.match(r'^(?P<value>\d+)(?P<unit>in|cm)$', passport['hgt']))
        and (
            150 <= int(hgt_m['value']) <= 193
            if hgt_m['unit'] == 'cm'
            else 59 <= int(hgt_m['value']) <= 76
        )
        and bool(re.match(r'^#[0-9a-f]{6}$', passport['hcl']))
        and bool(re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']))
        and bool(re.match(r'^\d{9}$', passport['pid']))
    )

    return isvalid


def main():
    input = open('input').read().strip()
    passports = [
        {field[0]: field[1] for f in record.split() for field in [f.split(':')]}
        for record in input.split('\n\n')
    ]

    s1 = sum(check1(passport) for passport in passports)
    s2 = sum(check2(passport) for passport in passports)

    print(s1)
    print(s2)


main()
