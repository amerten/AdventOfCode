v = {(0, 0)}
p = [[0, 0], [0, 0]]
santa = True
for c in open(0).read().strip():
    i = int(santa)
    if c == '>': p[i][0] += 1
    if c == '<': p[i][0] -= 1
    if c == '^': p[i][1] += 1
    if c == 'v': p[i][1] -= 1
    v.add(tuple(p[i]))
    santa = not santa
print(len(v))
