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

max_seat_id = 0
for line in lines:
    row = find_place_recursively(0, 127, 0, line[:-3])
    column = find_place_recursively(0, 7, 0, line[-3:])
    seat_id = row * 8 + column
    max_seat_id = max(seat_id, max_seat_id)

print(max_seat_id)

