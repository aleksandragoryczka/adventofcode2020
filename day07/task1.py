import re

with open('../inputs/day07/input.txt') as f:
    lines = f.read().splitlines()

def go_through_bags(inner_color, outer_color):
    if inner_color in bags_dict[outer_color]:
        return True
    return any([go_through_bags(inner_color, b) for b in bags_dict[outer_color]])

bags_dict = {}
for line in lines:
    matches = re.findall(r"\b(\w+\s\w+)\s(?=\w*bag)", line)
    if 'no other' == matches[1]:
        bags_dict[matches[0]] = []
    else:
        bags_dict[matches[0]] = matches[1:]

result = sum([go_through_bags('shiny gold', bag) for bag in bags_dict])
print(result)

