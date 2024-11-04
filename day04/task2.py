with open('../inputs/day04/input.txt') as f:
    lines = f.read().splitlines()

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_passwords = 0

password_set = set()
for line in lines:
    if line != '':
        entries = line.split(' ')
        for entry in entries:
            key, value = entry.split(':')
            match key:
                case 'byr':
                    if 2002 >= int(value) >= 1920:
                        password_set.add(key)
                case 'iyr':
                    if 2020 >= int(value) >= 2010:
                        password_set.add(key)  
                case 'eyr':
                    if 2030 >= int(value) >= 2020:
                        password_set.add(key)
                case 'hgt':
                    if value.endswith('in'):
                        if 76 >= int(value[:-2]) >= 59:
                            password_set.add(key)
                    elif value.endswith('cm'):
                        if 193 >= int(value[:-2]) >= 150:
                            password_set.add(key) 
                case 'hcl':
                    if value.startswith('#'):
                        for ch in value[1:]:
                            if ch not in [range(0,10), 'a', 'b','c','d','e','f']:
                                break
                        password_set.add(key)
                case 'ecl':
                    if value in ['amb','blu','brn','gry','grn','hzl','oth']:
                        password_set.add(key)
                case 'pid':
                    if len(value) == 9 and value.isnumeric():
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
             