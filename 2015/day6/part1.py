import re

p = "([ \w]+) (\d+),(\d+) through (\d+),(\d+)"
lights = {}
for line in open(0).read().splitlines():
    m = re.match(p, line)
    ins, x1, y1, x2, y2 = m[1], int(m[2]), int(m[3]), int(m[4]), int(m[5])
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if ins == "turn on":
                lights[x, y] = True
            elif ins == "turn off":
                lights[x, y] = False
            else:
                if (x, y) not in lights:
                    lights[x, y] = False
                lights[x, y] = not lights[x, y]
print(sum(lights.values()))