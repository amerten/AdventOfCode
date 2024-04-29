def nice(s):
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return 0
    nb_v, duo = 0, False
    for i, c in enumerate(s):
        if not duo and i > 0 and s[i-1] == s[i]:
            duo = True
        nb_v += c in 'aeiou'
    return int(nb_v >= 3 and duo)


print(sum(map(nice, open(0).read().splitlines())))