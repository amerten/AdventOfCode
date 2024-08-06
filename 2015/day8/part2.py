t = 0
for line in open(0).read().splitlines():
    t += 4
    i = 0
    s = line[1:-1]
    while i < len(s):
        if s[i] == "\\":
            if s[i + 1] == "x":
                t += 1
                i += 2
            else:
                t += 2
                i += 1
        i += 1
print(t)
