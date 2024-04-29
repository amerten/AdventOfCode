from z3 import *

s = Solver()
x, y, z, dx, dy, dz = Int('x'), Int('y'), Int('z'), Int('dx'), Int('dy'), Int('dz')
t1, t2, t3 = Int('t1'), Int('t2'), Int('t3')

c = [x, y, z, dx, dy, dz]
t = [t1, t2, t3]

for i, line in enumerate(open(0).read().splitlines()):
    val = list(map(int, line.replace(' @', ',').split(', ')))
    for j in range(3):
        s.add(val[j] + val[j + 3] * t[i] == c[j] + c[j + 3] * t[i])
    if i == 2:
        break

s.check()
print(s.model()[x].as_long() + s.model()[y].as_long() + s.model()[z].as_long())