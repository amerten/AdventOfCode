t = 0
for line in open(0).read().splitlines():
    room, cs = line.split('[')
    m = {}
    for c in room:
        if not c.isalpha():
            continue
        if c not in m:
            m[c] = 0
        m[c] += 1
    if ''.join([j[0] for j in sorted(m.items(), key=lambda item: (-item[1], ord(item[0])))])[:5] == cs[:-1]:
        t += int(room[-3:])
print(t)
