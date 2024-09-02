t = 0
for line in open(0).read().splitlines():
    a, b, c = map(int, line.split())
    t += (a + b > c and a + c > b and b + c > a)
print(t)