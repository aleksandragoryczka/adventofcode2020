with open('../inputs/day06/input.txt') as f:
    lines = f.read().splitlines()

group_answers_dict = dict()
lines_number = 0
counts_sum = 0
for line in lines:
    if line != '':
        lines_number += 1
        for l in list(line):
            if l in group_answers_dict.keys():
                group_answers_dict[l] = group_answers_dict[l] + 1
            else:
                group_answers_dict[l] = 1
    else:
        for key, value in group_answers_dict.items():
            if value == lines_number:
                counts_sum += 1
        lines_number = 0
        group_answers_dict = dict()

for key, value in group_answers_dict.items():
    if value == lines_number:
        counts_sum += 1
print(counts_sum)
