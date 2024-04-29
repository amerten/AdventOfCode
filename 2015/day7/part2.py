c = {}
for line in open(0).read().splitlines():
    e = line.split(' -> ')
    c[e[1]] = e[0]


memory = {}


def val(x):
    if x.isnumeric():
        return int(x)
    if x in memory:
        return memory[x]
    if x in c:
        memory[x] = val(c[x])
        return memory[x]
    e = x.split()
    if e[1] == 'AND':
        return val(e[0]) & val(e[2])
    elif e[1] == 'OR':
        return val(e[0]) | val(e[2])
    elif e[0] == 'NOT':
        return 65535 - val(e[1])
    elif e[1] == 'RSHIFT':
        return val(e[0]) >> val(e[2])
    elif e[1] == 'LSHIFT':
        return val(e[0]) << val(e[2])
    else:
        raise Exception("Unknown instruction: " + x)


c['b'] = str(val('a'))
memory = {}
print(val('a'))
