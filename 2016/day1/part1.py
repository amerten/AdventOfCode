x, y, dx, dy = 0, 0, 0, -1
for c in open(0).read().split(', '):
    d, l = c[0], int(c[1:])
    if d == 'L':
        dx, dy = dy, -dx
    else:
        dx, dy = -dy, dx
    x += dx * l
    y += dy * l
print(abs(x) + abs(y))
