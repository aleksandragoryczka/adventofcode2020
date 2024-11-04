with open('../inputs/day05/input.txt') as f:
    lines = f.read().splitlines()

def find_place_recursively(start_index, end_index, letter_index, word):
    if end_index - start_index == 1:
        if word[letter_index] in ['F', 'L']:
            return start_index
        return end_index
    if word[letter_index] in ['F', 'L']:
        return find_place_recursively(start_index, start_index + (end_index - start_index)//2, letter_index+1, word)
    if word[letter_index] in ['B', 'R']:
        return find_place_recursively(start_index + (end_index - start_index)//2 + 1, end_index, letter_index+1, word)

seats_dict = dict()
for line in lines:
    row = find_place_recursively(0, 127, 0, line[:-3])
    column = find_place_recursively(0, 7, 0, line[-3:])
    if row not in seats_dict.keys():
        seats_dict[row] = [column]
    else:
        seats_dict[row].append(column)
        
for row, columns in seats_dict.items():
    if len(columns) != 8:
        missing_column = list({0,1,2,3,4,5,6,7} - set(columns))
        print(row * 8 + missing_column[0])
