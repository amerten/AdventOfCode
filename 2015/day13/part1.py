from itertools import permutations


d = {}
for line in open(0).readlines():
    e = line.split()
    p1, p2, h = e[0], e[10][:-1], int(e[3])
    if p1 not in d:
        d[p1] = {}
    d[p1][p2] = h * [1, -1][e[2] == "lose"]

b = 0
for c in permutations(d.keys()):
    t = 0
    for i, p in enumerate(c):
        il, ir = (i - 1) % len(c), (i + 1) % len(c)
        t += (d[p][c[il]] + d[p][c[ir]])
    if t > b:
        b = t
        table = c
print(b)
