ranges, ids = open(0).read().split('\n\n')
t = 0
for id in ids.split():
    id = int(id)
    for range in ranges.split():
        r1, r2 = map(int, range.split('-'))
        if r1 <= id <= r2:
            t += 1
            break
print(t)