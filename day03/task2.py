with open('../inputs/day03/input.txt') as f:
    lines = f.read().splitlines()

width = len(lines[0])

x1, x2, x3, x4 = 0, 0, 0, 0
y = 0
trees1, trees2, trees3, trees4 = 0, 0, 0, 0
while y < len(lines) - 1:
    x1 = (x1 + 1) % width
    x2 = (x2 + 3) % width
    x3 = (x3 + 5) % width
    x4 = (x4 + 7) % width
    y += 1

    if lines[y][x1] == '#':
        trees1 += 1
    if lines[y][x2] == '#':
        trees2 += 1
    if lines[y][x3] == '#':
        trees3 += 1
    if lines[y][x4] == '#':
        trees4 += 1

result = trees1 * trees2 * trees3 * trees4

x = 0
y = 0
trees = 0
while y < len(lines) - 2:
    x = (x + 1) % width
    y += 2
    
    if lines[y][x] == '#':
        trees += 1
result *= trees

print(result)
