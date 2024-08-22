def next_state(m, l, c):
    nb_on = 0
    if l in [0, len(m) - 1] and c in [0, len(m) - 1]:
        return '#'
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if 0 <= l + y < len(m) and 0 <= c + x < len(m):
                nb_on += m[l + y][c + x] == '#'
    if m[l][c] == '#':
        return '#' if nb_on in [2, 3] else '.'
    return '#' if nb_on == 3 else '.'


nb_steps = 100

m = open(0).read().splitlines()
for _ in range(nb_steps):
    n = []
    for l in range(len(m)):
        n_line = ""
        for c in range(len(m[l])):
            n_line += next_state(m, l, c)
        n.append(n_line)
    m = n

print(sum(l.count('#') for l in m))
