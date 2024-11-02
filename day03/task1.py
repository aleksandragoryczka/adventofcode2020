with open('../inputs/day03/input.txt') as f:
    lines = f.read().splitlines()

x = 0
y = 0
trees = 0

while y < len(lines) - 1:
    x = (x + 3) % (len(lines[0]))
    y = y + 1
    
    if lines[y][x] == '#':
        trees = trees + 1

print(trees)