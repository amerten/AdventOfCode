from itertools import permutations

m = {}
for line in open(0).readlines():
    e = line.split(' ')
    t1, t2, d = e[0], e[2], int(e[4])
    if t1 not in m:
        m[t1] = {}
    if t2 not in m:
        m[t2] = {}
    m[t1][t2] = d
    m[t2][t1] = d

r = []
for c in permutations(m.keys()):
    r.append(0)
    for i in range(len(c) - 1):
        r[-1] += m[c[i]][c[i + 1]]
print(min(r))
