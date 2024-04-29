v = {(0, 0)}
x, y = 0, 0
for c in open(0).read().strip():
    if c == '>': x += 1
    if c == '<': x -= 1
    if c == '^': y += 1
    if c == 'v': y -= 1
    v.add((x, y))
print(len(v))