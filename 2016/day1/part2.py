BONUS = False


def get_orientation(dx, dy):
    if dx == 0:
        return '^' if dy < 0 else 'v'
    return '>' if dx > 0 else '<'

x, y, dx, dy = 0, 0, 0, -1
visited = {(x, y)}
path = {(x, y): 'S'}
x_min, x_max, y_min, y_max = 0, 0, 0, 0
for c in open(0).read().split(', '):
    found = False
    d, l = c[0], int(c[1:])
    if d == 'L':
        dx, dy = dy, -dx
    else:
        dx, dy = -dy, dx
    for _ in range(l):
        x += dx
        y += dy
        path[(x, y)] = get_orientation(dx, dy)
        x_min, x_max, y_min, y_max = min(x, x_min), max(x, x_max), min(y, y_min), max(y, y_max)
        if (x, y) in visited:
            print(abs(x) + abs(y))
            if not BONUS:
                quit()
            found = True
            break
        visited.add((x, y))
    if found:
        break

for r in range(y_min, y_max + 1):
    for c in range(x_min, x_max + 1):
        print(path[(c, r)] if (c, r) in visited else ' ', end='')
    print()
