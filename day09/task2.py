with open('../inputs/day09/input.txt') as f:
    lines = f.read().splitlines()

def find_sum(preamble, value):
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            if int(preamble[i]) + int(preamble[j]) == value:
                return
    return value

result = 0
for i in range(25, len(lines)):
    preamble = lines[i-25:i]
    result = find_sum(preamble, int(lines[i]))
    if result:
        break

def find_contiguos_sum(sum_value):
    for i in range(len(lines)):
        values_list = [int(lines[i])]
        for j in range(i+1, len(lines)):
            values_list.append(int(lines[j]))
            if sum(values_list) > sum_value:
                break
            elif sum(values_list) < sum_value:
                continue
            return min(values_list)+ max(values_list)
        
print(find_contiguos_sum(result))