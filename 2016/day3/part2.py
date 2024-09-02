input = [list(map(int, l.split())) for l in open(0).read().splitlines()]
t = 0
for r in range(0, len(input), 3):
    for c in range(3):
        x, y, z = input[r][c], input[r + 1][c], input[r + 2][c]
        t += (x + y > z and x + z > y and y + z > x)
print(t)