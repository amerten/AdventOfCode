import re

p = "([ \w]+) (\d+),(\d+) through (\d+),(\d+)"
lights = {}
for line in open(0).read().splitlines():
    m = re.match(p, line)
    ins, x1, y1, x2, y2 = m[1], int(m[2]), int(m[3]), int(m[4]), int(m[5])
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x, y) not in lights:
                lights[x, y] = 0
            if ins == "turn on":
                lights[x, y] += 1
            elif ins == "turn off":
                lights[x, y] = max(0, lights[x, y] - 1)
            else:
                lights[x, y] += 2
print(sum(lights.values()))