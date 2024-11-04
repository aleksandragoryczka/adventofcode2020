with open('../inputs/day06/input.txt') as f:
    lines = f.read().splitlines()

group_answers_set = set()
counts_sum = 0
for line in lines:
    if line != '':
       [group_answers_set.add(answer) for answer in list(line)]
    else:
        counts_sum += len(group_answers_set)
        group_answers_set = set()
counts_sum += len(group_answers_set)

print(counts_sum)
