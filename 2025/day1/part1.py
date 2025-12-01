t = 0
p = 50
input = open(0).read().splitlines()
for rot in input:
    dir, dist = rot[0], int(rot[1:])
    dir = 1 if dir == 'R' else -1
    p = (p + dist * dir) % 100
    t += p == 0
print(t)