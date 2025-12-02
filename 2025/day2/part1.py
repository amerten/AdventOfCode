t = 0
for r in open(0).read().split(','):
    r1, r2 = map(int, r.split('-'))
    for i in range(r1, r2 + 1):
        s = str(i)
        l = len(s)
        if l % 2 == 0 and s[:l//2] == s[l//2:]:
            t += i
print(t)