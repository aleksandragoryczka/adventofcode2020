with open('../inputs/day04/input.txt') as f:
    lines = f.read().splitlines()

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_passwords = 0

password_set = set()
for line in lines:
    if line != '':
        entries = line.split(' ')
        for entry in entries:
            key = entry.split(':')[0]
            password_set.add(key)
    else:
        remaining_fields = required_fields - password_set
        if len(remaining_fields) == 0:
            valid_passwords += 1
        password_set = set()

remaining_fields = required_fields - password_set
if len(remaining_fields) == 0:
    valid_passwords += 1

print(valid_passwords)
             