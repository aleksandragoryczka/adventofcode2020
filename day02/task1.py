with open('../inputs/day02/input.txt') as f:
    lines = f.readlines()

lines_num = 0
for line in lines:
    minimum = line.split('-')[0]
    maximum = line.split('-')[1].split(' ')[0]
    letter = line.split('-')[1].split(' ')[1].split(':')[0]
    letters_chain = line.split(': ')[1]

    if int(maximum) >= letters_chain.count(letter) >= int(minimum):
        lines_num += 1

print(lines_num)