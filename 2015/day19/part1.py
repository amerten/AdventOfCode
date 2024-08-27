data = open(0).read().splitlines()
r = {}
for line in data[:-2]:
    e = line.split(' => ')
    if e[0] not in r:
        r[e[0]] = []
    r[e[0]].append(e[1])
m = data[-1]

dm = set()
for i in range(len(m)):
    for j in [0, 1]:
        if i + j < len(m) and m[i: i + j + 1] in r:
            for val in r[m[i: i + j + 1]]:
                dm.add(m[:i] + val + m[i + j + 1:])
print(len(dm))