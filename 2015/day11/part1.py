def valid(p):
    j, k, rk = 0, 0, True
    pc = '?'
    for c in p:
        if c in "iol":
            return False
        if j < 2:
            if ord(c) - ord(pc) == 1:
                j += 1
            else:
                j = 0
        if c == pc:
            if rk:
                k += 1
                rk = False
        else:
            rk = True
        pc = c
    return j == 2 and k >= 2


def next(p):
    i = len(p) - 1
    while True:
        c = p[i]
        if c == 'z':
            p[i] = 'a'
            i -= 1
        else:
            p[i] = chr(ord(p[i]) + 1)
            break


p = list(open(0).read().strip())
while not valid(p):
    next(p)
print(''.join(p))
