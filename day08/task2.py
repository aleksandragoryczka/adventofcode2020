with open('../inputs/day08/input.txt') as f:
    lines = f.read().splitlines()

accumulator = 0
indexes_list = set()

def iterate_through_lines(line, idx, lines_copy):
    global accumulator
    if idx in indexes_list:
        return False
    indexes_list.add(idx)
    instruction, value = line.split(" ")
    if instruction == 'acc':
        accumulator += int(value)
        if idx+1 >= len(lines_copy):
            return True
        return iterate_through_lines(lines_copy[idx+1], idx+1, lines_copy)
    elif instruction == 'jmp':
        if int(idx + int(value)) >= len(lines_copy):
            return True
        return iterate_through_lines(lines_copy[int(idx + int(value))], int(idx + int(value)), lines_copy)
    else:
        if idx+1 >= len(lines_copy):
            return True
        return iterate_through_lines(lines_copy[idx+1], idx+1, lines_copy)

for idx, line in enumerate(lines):
    indexes_list = set()
    accumulator = 0
    instruction, value = line.split(" ")
    if instruction == 'acc':
        continue
    elif instruction == 'nop':
        instruction = 'jmp'
    elif instruction == 'jmp':
        instruction = 'nop'
    new_line = instruction + ' ' + value
    lines_copy = lines.copy()
    lines_copy[idx] = new_line
    result = iterate_through_lines(lines_copy[0], 0, lines_copy)
    if result:
        print(accumulator)
        break
        