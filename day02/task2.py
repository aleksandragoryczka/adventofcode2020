with open('../inputs/day02/input.txt') as f:
    lines = f.readlines()

lines_num = 0
for line in lines:
    index1 = line.split('-')[0]
    index2 = line.split('-')[1].split(' ')[0]
    letter = line.split('-')[1].split(' ')[1].split(':')[0]
    letters_chain = line.split(': ')[1]

    if letters_chain[int(index1) - 1] == letter and letters_chain[int(index2) - 1] != letter:
        lines_num += 1
    elif letters_chain[int(index1) - 1] != letter and letters_chain[int(index2) - 1] == letter:
        lines_num += 1

print(lines_num)