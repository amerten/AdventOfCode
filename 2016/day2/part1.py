pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
r, c = 1, 1
for line in open(0).read().splitlines():
    for d in line:
        if d == 'L':
            c = max(0, c - 1)
        elif d == 'R':
            c = min(2, c + 1)
        elif d == 'U':
            r = max(0, r - 1)
        else:
            r = min(2, r + 1)
    print(end=pad[r][c])
