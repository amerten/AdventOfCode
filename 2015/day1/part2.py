f = 0
for i, c in enumerate(open(0).read().strip()):
    f += 1 if c == '(' else -1
    if f == -1:
        print(i + 1)
        break