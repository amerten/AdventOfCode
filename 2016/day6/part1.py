data = {}
for word in open(0).read().splitlines():
    for i, c in enumerate(word):
        if i not in data:
            data[i] = ["", "", 0]
        data[i][0] += c
        n = data[i][0].count(c)
        if n > data[i][2]:
            data[i][1] = c
            data[i][2] = n
for _, d in sorted(data.items()):
    print(end=d[1])