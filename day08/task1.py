with open('../inputs/day08/input.txt') as f:
    lines = f.read().splitlines()

accumulator = 0
indexes_list = set()

def iterate_through_lines(line, idx):
    global accumulator
    if idx in indexes_list:
        return
    indexes_list.add(idx)
    instruction, value = line.split(" ")
    if instruction == 'acc':
        accumulator += int(value)
        iterate_through_lines(lines[idx+1], idx+1)
    elif instruction == 'jmp':
        iterate_through_lines(lines[int(idx + int(value))], int(idx + int(value)))
    else:
        iterate_through_lines(lines[idx+1], idx+1)

iterate_through_lines(lines[0], 0)
print(accumulator)
        