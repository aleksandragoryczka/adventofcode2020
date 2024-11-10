import re

with open('../inputs/day07/input.txt') as f:
    lines = f.read().splitlines()

bags_dict = {}

def go_through_bags(outer_color, quantity):
    result = 0
    for inner_bag in bags_dict[outer_color]:
        result += int(inner_bag[0]) + int(inner_bag[0]) * go_through_bags(inner_bag[1], int(inner_bag[0]))
    return result

for line in lines:
    matches = re.findall(r"(?:^|(\d+)\s)?(\w+\s\w+)\s(?=\w*bag)", line)
    if 'no other' == matches[1][1]:
        bags_dict[matches[0][1]] = []
    else:
        bags_dict[matches[0][1]] = matches[1:]

result = go_through_bags('shiny gold', 1)
print(result)
