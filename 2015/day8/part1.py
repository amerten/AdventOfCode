t = 0
for line in open(0).read().splitlines():
    t += len(line)
    s = line[1:-1]
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            if s[i + 1] == 'x':
                i += 2
            i += 1
        i += 1
        t -= 1

print(t)
