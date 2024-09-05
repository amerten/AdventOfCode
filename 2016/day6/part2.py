data = []
init = False
for word in open(0).read().splitlines():
    for i, c in enumerate(word):
        if not init:
            data.append({})
        if c not in data[i]:
            data[i][c] = 0
        data[i][c] += 1
    init = True
for d in data:
    print(end=[c for c in d if d[c] == min(d.values())][0])