def nice(s):
    ok1 = False
    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            subs = chr(a) + chr(b)
            if s.count(subs) > 1:
                ok1 = True
                break
        if ok1:
            break

    ok2 = False
    for i in range(len(s) - 2):
        subs = s[i:i+3]
        if subs[0] == subs[-1]:
            ok2 = True
            break

    return int(ok1 and ok2)


print(sum(map(nice, open(0).read().splitlines())))