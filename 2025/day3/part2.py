t = 0
for bank in open(0).read().splitlines():
    n = ""
    i = 0
    while len(n) < 12:
        sub_b = list(map(int, bank[i:len(bank) - 11 + len(n)]))
        m = str(max(sub_b))
        i = bank.index(m, i) + 1
        n += m
    t += int(n)
print(t)