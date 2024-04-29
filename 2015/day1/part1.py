f = 0
for c in open(0).read().strip():
    f += 1 if c == '(' else -1
print(f)