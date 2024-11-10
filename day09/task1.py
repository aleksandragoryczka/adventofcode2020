with open('../inputs/day09/input.txt') as f:
    lines = f.read().splitlines()

def find_sum(preamble, value):
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            if int(preamble[i]) + int(preamble[j]) == value:
                return
    return value

for i in range(25, len(lines)):
    preamble = lines[i-25:i]
    result = find_sum(preamble, int(lines[i]))
    if result:
        print(result)
        break