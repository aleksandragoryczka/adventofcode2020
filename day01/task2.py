with open('../inputs/day01/input.txt') as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]

for num, line in enumerate(lines):
    for num2 in range(num + 1, len(lines)):
        for num3 in range(num2 + 1, len(lines)):
            if line + lines[num2] + lines[num3] == 2020:
                print(line * lines[num2] * lines[num3])