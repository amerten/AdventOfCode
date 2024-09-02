pad = [[None, None, '1', None, None], [None, '2', '3', '4', None], ['5', '6', '7', '8', '9'], [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
r, c = 1, 1
for line in open(0).read().splitlines():
    for d in line:
        if d == 'L':
            if c - 1 >= 0 and pad[r][c - 1]:
                c -= 1
        elif d == 'R':
            if c + 1 <= 4 and pad[r][c + 1]:
                c += 1
        elif d == 'U':
            if r - 1 >= 0 and pad[r - 1][c]:
                r -= 1
        elif r + 1 <= 4 and pad[r + 1][c]:
            r += 1
    print(end=pad[r][c])
