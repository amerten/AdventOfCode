t = 0
for r in open(0).read().split(','):
    r1, r2 = map(int, r.split('-'))
    for i in range(r1, r2 + 1):
        s = str(i)
        l = len(s)
        for j in range(1, l//2 + 1):
            if "".join(s[:j] * (l // j)) == s:
                t += i
                break
print(t)